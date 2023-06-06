

# multi-gpu ffmpeg transcode
```bash
# iGfx: 1 or 2 segment
python run.py -i ..\bbb_sunflower_2160p_60fps_normal.mp4 -s 1 -gpu 1
python run.py -i ..\bbb_sunflower_2160p_60fps_normal.mp4 -s 2 -gpu 1 1

# A380: 1 or 2 segment
python run.py -i ..\bbb_sunflower_2160p_60fps_normal.mp4 -s 1 -gpu 0
python run.py -i ..\bbb_sunflower_2160p_60fps_normal.mp4 -s 2 -gpu 0 0

# A380 + A380: 2 or 4 segment
python run.py -i ..\bbb_sunflower_2160p_60fps_normal.mp4 -s 2 -gpu 0 2
python run.py -i ..\bbb_sunflower_2160p_60fps_normal.mp4 -s 4 -gpu 0 0 2 2

# A380 + A380 + iGfx: 3 or 6 segment
python run.py -i ..\bbb_sunflower_2160p_60fps_normal.mp4 -s 3 -gpu 0 2 1
python run.py -i ..\bbb_sunflower_2160p_60fps_normal.mp4 -s 6 -gpu 0 0 2 2 1 1
```

## ffmpeg split video file
```
ffmpeg -i bbb.mp4 -acodec copy -f segment -vcodec copy -reset_timestamps 1 -map 0 out-%03d.mp4
ffmpeg -i bbb.mp4 -acodec copy -f segment -vcodec copy -reset_timestamps 1 -map 0 -segment_list_type csv -segment_list tmp.txt out-%03d.mp4
ffmpeg -i bbb_full.mp4 -acodec copy -f segment -vcodec copy -reset_timestamps 1 -segment_time 158 -map 0 -segment_list_type csv -segment_list split.txt out-%03d.mp4
```

## ffmpeg transcode segment
```
ffmpeg -ss 0.000000   -to 160.400000 -hwaccel qsv -i bbb_full.mp4 -low_power 1 -c:v hevc_qsv -b:v 10M out.0.mp4
ffmpeg -ss 160.400000 -to 316.900000 -hwaccel qsv -i bbb_full.mp4 -low_power 1 -c:v hevc_qsv -b:v 10M out.1.mp4
ffmpeg -ss 316.900000 -to 475.183333 -hwaccel qsv -i bbb_full.mp4 -low_power 1 -c:v hevc_qsv -b:v 10M out.2.mp4
ffmpeg -ss 475.183333 -to 634.566667 -hwaccel qsv -i bbb_full.mp4 -low_power 1 -c:v hevc_qsv -b:v 10M out.3.mp4
```
