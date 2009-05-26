from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [ 
                   Extension("pyffmpegb", ["pyffmpegb.pyx"], include_dirs=["/usr/include/ffmpeg", "/usr/include/libavcodec","/usr/include/libavutil", "/usr/include/libavformat", "/usr/include/libswscale"],libraries = ["avformat","avcodec","swscale"]),
                 ]
)


