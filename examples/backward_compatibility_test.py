# -*- coding: utf-8 -*-
import sys
import pyffmpegb as pyffmpeg

stream = pyffmpeg.VideoStream()
stream.open(sys.argv[1])
image = stream.GetFrameNo(0)
image.save('firstframe.png')