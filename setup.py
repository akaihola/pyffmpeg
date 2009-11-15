# -*- coding: utf-8 -*-
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from os.path import join as path_join
from sys import platform
import numpy.distutils.misc_util as nd

if platform == 'win32':
    ffmpegpath = r'c:\ffmpeg-static'
else:
    ffmpegpath = '/opt/ffmpeg'

# static dependencies resolution by looking into pkgconfig files
def static_resolver(libs):
    deps = []

    for lib in libs:
        try:
            pc = open(path_join(ffmpegpath, 'lib', 'pkgconfig', 'lib' + lib + '.pc')).readlines()
        except IOError:
            continue

        # we only need line starting with 'Libs:'
        l = filter(lambda x: x.startswith('Libs:'), pc).pop().strip()

        # we only need after '-lmylib' and one entry for library
        d = l.split(lib, 1).pop().split()

        # remove '-l'
        d = map(lambda x: x[2:], d)

        # empty list means no deps
        if len(d): deps += d

    # Unique list
    result = list(libs)
    map(lambda x: x not in result and result.append(x), deps)
    return result

#./configure --enable-shared --enable-swscale --enable-gpl --enable-memalign-hack #--enable-nonfree
#print dir(nd)
#url="http://ffmpeg.arrozcru.org/builds/bin/ffmpeg-latest-gpl-shared-dev.tar.bz2"
#url7zip="http://downloads.sourceforge.net/sevenzip/7za465.zip"
#urlffmpeg="http://ffmpeg.arrozcru.org/autobuilds/ffmpeg/mingw32/shared/fmpeg-latest-gpl-shared-dev.7z"
#"""
#wget -nd  url7zip
#unzip 7za.zip
#"""

libs = ('avformat', 'avcodec', 'swscale')
incdir = [ path_join(ffmpegpath, 'include') ] + nd.get_numpy_include_dirs()
libinc = [ path_join(ffmpegpath, 'lib') ]

if platform == 'win32':
    libs = static_resolver(libs + ('avutil',))
    libinc += [ r'/mingw/lib' ] # why my mingw is unable to find libz2?

setup(
    name = 'pyffmpegb',
    cmdclass = {'build_ext': build_ext},
    ext_modules = [
                   Extension('pyffmpegb', [ 'pyffmpegb.pyx' ],
                    include_dirs = incdir,
                    library_dirs = libinc,
                    libraries = libs)
                ]
)
