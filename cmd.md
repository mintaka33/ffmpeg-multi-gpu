
ffmpeg -i bbb.mp4 -acodec copy -f segment -vcodec copy -reset_timestamps 1 -map 0 out-%03d.mp4
ffmpeg -i bbb.mp4 -acodec copy -f segment -vcodec copy -reset_timestamps 1 -map 0 -segment_list_type csv -segment_list tmp.txt out-%03d.mp4
ffmpeg -i bbb_full.mp4 -acodec copy -f segment -vcodec copy -reset_timestamps 1 -segment_time 158 -map 0 -segment_list_type csv -segment_list split.txt out-%03d.mp4

ffmpeg -ss 0.000000   -to 160.400000 -hwaccel qsv -i bbb_full.mp4 -low_power 1 -c:v hevc_qsv -b:v 10M out.0.mp4
ffmpeg -ss 160.400000 -to 316.900000 -hwaccel qsv -i bbb_full.mp4 -low_power 1 -c:v hevc_qsv -b:v 10M out.1.mp4
ffmpeg -ss 316.900000 -to 475.183333 -hwaccel qsv -i bbb_full.mp4 -low_power 1 -c:v hevc_qsv -b:v 10M out.2.mp4
ffmpeg -ss 475.183333 -to 634.566667 -hwaccel qsv -i bbb_full.mp4 -low_power 1 -c:v hevc_qsv -b:v 10M out.3.mp4

