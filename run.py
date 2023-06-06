import os, time
import subprocess
import argparse

split_file, concat_file = 'split.txt', 'concat.txt'
input_video = '..\\bbb_sunflower_2160p_60fps_normal.mp4'

def get_duration(videofile):
    dur_sec = 0
    cmd = 'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 %s' % (videofile)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    for line in proc.stdout:
        dur_sec = float(line.strip()) #if line.isnumeric() else 0.1
        print(dur_sec, line)
        break
    return dur_sec

def run_prepare(args):
    # get input video duration
    dur_sec = get_duration(args.input_video)
    if dur_sec <= 0:
        print('ERROR: invalid input video duration %f, exit' % (dur_sec))
        exit(-1)

    cmd_list = []
    if args.segment > 1:
        # segment video based on segment number
        seg_dur = dur_sec / args.segment
        seg_cmd = 'ffmpeg -i %s -acodec copy -f segment -vcodec copy -reset_timestamps 1 -segment_time %d -map 0 \
                    -segment_list_type csv -segment_list %s tmp.%s%s.mp4' % (args.input_video, seg_dur, split_file, '%', 'd')
        os.system(seg_cmd)
        # construct ffmpeg transcode command line for each segment
        with open(split_file, 'rt') as f:
            for i, line in enumerate(f.readlines()):
                if i >= args.segment:
                    break
                name, s, e = line.strip('\n').split(',')
                cmd_list.append('ffmpeg -ss %s -to %s -qsv_device %s -hwaccel qsv -i %s -low_power 1 \
                                -preset %d -c:v %s_qsv -b:v %dM -y out_enc.%03d.mp4' %  (s, e, args.gpu_list[i],
                                args.input_video, args.preset, args.codec_format, args.bitrate ,i))
    else:
        cmd_list.append('ffmpeg -qsv_device %d -hwaccel qsv -i %s -low_power 1 -preset %d -c:v %s_qsv \
                        -b:v %dM -y out_enc.mp4' %  (args.gpu_list[0], args.input_video, args.preset, 
                                                          args.codec_format, args.bitrate))
    trans_cmd = [" ".join(cmd.split()) for cmd in cmd_list]
    return trans_cmd

def run_ffmpeg(trans_cmd):
    print('\n'.join(trans_cmd))
    proc_list = []
    for cmd in trans_cmd:
        print(cmd)
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        proc_list.append(proc)

    while True:
        lineout, total_fps = [], 0
        for i, proc in enumerate(proc_list):
            for line in proc.stdout:
                # print(line.strip())
                if 'frame=' in line and 'fps=' in line and 'q=' in line:
                    stats = line.split('q=')[0]
                    frame, fps_num = stats.split('fps=')
                    frame_num = frame.split('frame=')[1]
                    frame_num, fps_num = frame_num.strip(), fps_num.strip()
                    lineout.append('proc=%d, frame=%s, FPS=%s' % (i, frame_num, fps_num))
                    fps = int(fps_num) if fps_num.isnumeric() else 0
                    total_fps += fps
                    break
                elif '[out#' in line:
                    print('proc %d finished'%i)
                    proc_list.remove(proc)
        if len(proc_list) == 0:
            break
        print('total_fps = %d'%total_fps, lineout)

def run_concat(args):
    lines = []
    for i in range(args.segment):
        lines.append('file out_enc.%03d.mp4\n' % i)
    with open(concat_file, 'wt') as f:
        f.writelines(lines)
    cmdline = 'ffmpeg -f concat -safe 0 -i %s -c copy -y out_all.mp4' % (concat_file)
    print(cmdline)
    os.system(cmdline)

def cleanup():
    os.system('del /Q /F tmp.*.mp4')
    os.system('del /Q /F out_enc.*.mp4')
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input_video", type=str, help="input video file")
    parser.add_argument("-p", "--preset", type=int, choices=[1, 4, 7], default=4, help="encode preset 1/4/7")
    parser.add_argument("-b", "--bitrate", type=int, default=10, help="encode bitrate (Mbps)")
    parser.add_argument("-frame", "--vframes", type=int, default=1000, help="encoding frame number")
    parser.add_argument("-codec", "--codec_format", type=str, choices=['h264', 'hevc', 'av1'], default='hevc', help="encoding video codec format")
    parser.add_argument("-s", "--segment", type=int, choices=[1, 2, 3, 4, 5, 6, 7, 8], default=1, help="number of transcode segment")
    parser.add_argument("-gpu", "--gpu_list", type=int, nargs="*", default=[0], help="list of gpu index")
    
    args = parser.parse_args()
    parser.print_help()

    print('\ncurrent command line arguments:')
    print('-'*64)
    print('--input_video = %s' % args.input_video)
    print('--preset = %s' % args.preset)
    print('--bitrate = %sMbps' % args.bitrate)
    print('--vframes = %s' % args.vframes)
    print('--codec_format = %s' % args.codec_format)
    print('--segment = %s' % args.segment)
    print('--gpu_list = %s' % args.gpu_list)
    print('-'*64, '\n')
    
    trans_cmd = run_prepare(args)
    run_ffmpeg(trans_cmd)
    run_concat(args)
    cleanup()

    print('done')