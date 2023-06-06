import os, time
import subprocess

segment_num, split_file, concat_file = 0, 'split.txt', 'concat.txt'
input_video = 'bbb_sunflower_2160p_60fps_normal.mp4'
cmd_list = []

def run_prepare():
    global segment_num
    with open(split_file, 'rt') as f:
        for i, line in enumerate(f.readlines()):
            name, s, e = line.strip('\n').split(',')
            cmd_list.append('ffmpeg -ss %s -to %s -qsv_device %d -hwaccel qsv -i %s -low_power 1 -preset 7 -c:v hevc_qsv -b:v 10M -y out_enc.%03d.mp4' % (s, e, (i//2)*2, input_video, i))
            segment_num += 1
    # print('\n'.join(cmd_list))
    pass

def run_ffmpeg():
    proc_list = []
    for cmd in cmd_list:
        print(cmd)
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        # proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
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

def run_concat():
    lines = []
    for i in range(segment_num):
        lines.append('file out_enc.%03d.mp4\n' % i)
    with open(concat_file, 'wt') as f:
        f.writelines(lines)
    cmdline = 'ffmpeg -f concat -safe 0 -i %s -c copy -y out_all.mp4' % (concat_file)
    print(cmdline)
    os.system(cmdline)

run_prepare()
run_ffmpeg()
run_concat()

print('done')