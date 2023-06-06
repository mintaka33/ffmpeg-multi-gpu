# ffmpeg-multi-gpu

## example command

```bash
# A380 + A380 + iGfx: 2 segments per GPU, total 6 segment
python run.py -i ..\bbb_sunflower_2160p_60fps_normal.mp4 --preset 4 -b 10 -codec hevc -s 6 -gpu 0 0 2 2 1 1
```

```
total_fps = 427 ['proc=0, frame=3808, FPS=91', 'proc=1, frame=3786, FPS=90', 'proc=2, frame=3814, FPS=91', 'proc=3, frame=3731, FPS=89', 'proc=4, frame=1462, FPS=33', 'proc=5, frame=1446, FPS=33']
total_fps = 427 ['proc=0, frame=3852, FPS=91', 'proc=1, frame=3832, FPS=90', 'proc=2, frame=3866, FPS=91', 'proc=3, frame=3771, FPS=89', 'proc=4, frame=1480, FPS=33', 'proc=5, frame=1464, FPS=33']
total_fps = 428 ['proc=0, frame=3898, FPS=91', 'proc=1, frame=3877, FPS=90', 'proc=2, frame=3907, FPS=91', 'proc=3, frame=3820, FPS=89', 'proc=4, frame=1498, FPS=34', 'proc=5, frame=1481, FPS=33']
total_fps = 428 ['proc=0, frame=3949, FPS=91', 'proc=1, frame=3920, FPS=90', 'proc=2, frame=3949, FPS=91', 'proc=3, frame=3869, FPS=89', 'proc=4, frame=1515, FPS=34', 'proc=5, frame=1498, FPS=33']
total_fps = 428 ['proc=0, frame=3996, FPS=91', 'proc=1, frame=3967, FPS=90', 'proc=2, frame=3990, FPS=91', 'proc=3, frame=3922, FPS=89', 'proc=4, frame=1533, FPS=34', 'proc=5, frame=1516, FPS=33']
total_fps = 428 ['proc=0, frame=4046, FPS=91', 'proc=1, frame=4008, FPS=90', 'proc=2, frame=4032, FPS=91', 'proc=3, frame=3971, FPS=89', 'proc=4, frame=1552, FPS=34', 'proc=5, frame=1534, FPS=33']
total_fps = 428 ['proc=0, frame=4091, FPS=91', 'proc=1, frame=4055, FPS=90', 'proc=2, frame=4077, FPS=91', 'proc=3, frame=4021, FPS=89', 'proc=4, frame=1569, FPS=34', 'proc=5, frame=1552, FPS=33']
total_fps = 429 ['proc=0, frame=4139, FPS=91', 'proc=1, frame=4098, FPS=90', 'proc=2, frame=4120, FPS=91', 'proc=3, frame=4069, FPS=90', 'proc=4, frame=1587, FPS=34', 'proc=5, frame=1569, FPS=33']
total_fps = 428 ['proc=0, frame=4185, FPS=91', 'proc=1, frame=4143, FPS=90', 'proc=2, frame=4166, FPS=91', 'proc=3, frame=4115, FPS=90', 'proc=4, frame=1602, FPS=33', 'proc=5, frame=1587, FPS=33']
total_fps = 429 ['proc=0, frame=4232, FPS=91', 'proc=1, frame=4191, FPS=90', 'proc=2, frame=4209, FPS=91', 'proc=3, frame=4165, FPS=90', 'proc=4, frame=1620, FPS=34', 'proc=5, frame=1604, FPS=33']
total_fps = 429 ['proc=0, frame=4276, FPS=91', 'proc=1, frame=4238, FPS=90', 'proc=2, frame=4251, FPS=91', 'proc=3, frame=4214, FPS=90', 'proc=4, frame=1639, FPS=34', 'proc=5, frame=1622, FPS=33']
total_fps = 428 ['proc=0, frame=4319, FPS=91', 'proc=1, frame=4288, FPS=90', 'proc=2, frame=4291, FPS=90', 'proc=3, frame=4266, FPS=90', 'proc=4, frame=1655, FPS=34', 'proc=5, frame=1640, FPS=33']
total_fps = 428 ['proc=0, frame=4368, FPS=91', 'proc=1, frame=4333, FPS=90', 'proc=2, frame=4327, FPS=90', 'proc=3, frame=4321, FPS=90', 'proc=4, frame=1674, FPS=34', 'proc=5, frame=1658, FPS=33']
total_fps = 428 ['proc=0, frame=4414, FPS=91', 'proc=1, frame=4375, FPS=90', 'proc=2, frame=4369, FPS=90', 'proc=3, frame=4372, FPS=90', 'proc=4, frame=1691, FPS=34', 'proc=5, frame=1676, FPS=33']
total_fps = 428 ['proc=0, frame=4460, FPS=91', 'proc=1, frame=4423, FPS=90', 'proc=2, frame=4415, FPS=90', 'proc=3, frame=4416, FPS=90', 'proc=4, frame=1709, FPS=34', 'proc=5, frame=1695, FPS=33']
total_fps = 428 ['proc=0, frame=4512, FPS=91', 'proc=1, frame=4462, FPS=90', 'proc=2, frame=4459, FPS=90', 'proc=3, frame=4466, FPS=90', 'proc=4, frame=1727, FPS=34', 'proc=5, frame=1714, FPS=33']
total_fps = 428 ['proc=0, frame=4560, FPS=91', 'proc=1, frame=4505, FPS=90', 'proc=2, frame=4508, FPS=90', 'proc=3, frame=4510, FPS=90', 'proc=4, frame=1744, FPS=34', 'proc=5, frame=1732, FPS=33']
total_fps = 428 ['proc=0, frame=4614, FPS=91', 'proc=1, frame=4546, FPS=90', 'proc=2, frame=4550, FPS=90', 'proc=3, frame=4560, FPS=90', 'proc=4, frame=1761, FPS=34', 'proc=5, frame=1749, FPS=33']
```