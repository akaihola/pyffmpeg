# -*- coding: utf-8 -*-
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy.distutils.misc_util as nd

# linux
pythonpath="/usr/lib/python2.5"
pythonpathlib="/usr/lib/python2.5"
# windows
pythonpath="c:/python25"
pythonpathlib="c:/python25/lib"

ffmpegpath="../ffmpeg"

#./configure --enable-shared --enable-swscale --enable-gpl --enable-memalign-hack #--enable-nonfree 
#print dir(nd)


url="http://ffmpeg.arrozcru.org/builds/bin/ffmpeg-latest-gpl-shared-dev.tar.bz2"

url7zip="http://downloads.sourceforge.net/sevenzip/7za465.zip"
urlffmpeg="http://ffmpeg.arrozcru.org/autobuilds/ffmpeg/mingw32/shared/fmpeg-latest-gpl-shared-dev.7z"
"""
wget -nd  url7zip
unzip 7za.zip
"""

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [ 
                   Extension("pyffmpegb", ["pyffmpegb.pyx"], include_dirs=[
                      "/usr/include",
                      "/MinGW/include",
                      pythonpath,
                      ffmpegpath,
                      ffmpegpath+"/include",
                      ffmpegpath+"/include/libavcodec",
                      ffmpegpath+"/include/libavutil",
                      ffmpegpath+"/include/libavformat",
                      ffmpegpath+"/include/libswscale",
                      ffmpegpath+"/libavcodec",
                      ffmpegpath+"/libavutil",
                      ffmpegpath+"/libavformat",
                      ffmpegpath+"/libswscale",
                      "/usr/local/include/ffmpeg",
                      "/usr/local/include/libavcodec",
                      "/usr/local/include/libavutil",
                      "/usr/local/include/libavformat",
                      "/usr/local/include/libswscale",
                      "/usr/include/ffmpeg",
                      "/usr/include/libavcodec",
                      "/usr/include/libavutil",
                      "/usr/include/libavformat",
                      "/usr/include/libswscale",
                       ]+
                      nd.get_numpy_include_dirs(),
                      #language="c++",
                      library_dirs=["."],
                      libraries = ["avformat","avcodec","swscale","avutil", "wsock32"]),
                 ]
)


