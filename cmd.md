

ffmpeg -i bbb.mp4 -acodec copy -f segment -vcodec copy -reset_timestamps 1 -map 0 out-%03d.mp4

ffmpeg -i bbb_full.mp4 -acodec copy -f segment -vcodec copy -reset_timestamps 1 -segment_time 100 -map 0 out-%03d.mp4
