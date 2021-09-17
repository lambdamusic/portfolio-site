---
title: "Installing PIL on Djangostack 1.1.1/1.2/1.3"
date: "2011-02-08"
categories: 
  - "techlife"
  - "tips-and-tricks"
tags: 
  - "image"
  - "pil"
  - "python"
  - "tutorial"
---

The popular [Python Imaging Library](http://www.pythonware.com/products/pil/) (PIL) adds image processing capabilities to your Python interpreter. This library supports many file formats and provides powerful image processing and graphics capabilities. I normally use [Bitnami Djangostack](http://bitnami.org/stack/djangostack) for most of my Django development, which doesn't come with PIL installed by default so in this post I'm summing up what steps I've taken to get that up and running.

This is the **preamble**: I recently got a new desktop machine (an iMac Intel core i3) with the latest OS installed (10.6.4), so I had to re-install a whole bunch of stuff. In order to set up the new mac I used [Migration Assistant](http://support.apple.com/kb/HT4413). This neat piece of software cloned almost all I had on the previous machine onto the new one, and that worked just wonderfully. However I was expecting some troubles with low-level libraries.. and that just happened with PIL this morning. It costed a 2-3 hours headache but the web eventually stirred me in the right direction... in this post I'm just summarising how I got around the problem.

### The problem: missing gcc compiler

Yeah, first of all, let's make it clear what the problem was: I usually run my django projects using [Bitnami Djangostack](http://bitnami.org/stack/djangostack) (a closed environment that includes ready-to-run versions of Apache, MySQL, PostgreSQL, SQLite, Python and Django and required dependencies). Today I needed to use PIL in a project of mine, so was trying to install it using [easy\_install](http://www.michelepasin.org/blog/2009/01/27/python-easyinstall-the-peak-developers-center/) within the stack:

bash-3.2$ easy\_install PIL
Searching for PIL
Reading [http://pypi.python.org/simple/PIL/](http://pypi.python.org/simple/PIL/)
Reading [http://www.pythonware.com/products/pil](http://www.pythonware.com/products/pil)
Reading [http://effbot.org/zone/pil-changes-115.htm](http://effbot.org/zone/pil-changes-115.htm)
Reading [http://effbot.org/downloads/](http://effbot.org/downloads/)#Imaging
Best match: PIL 1.1.7
Downloading [http://effbot.org/media/downloads/PIL-1.1.7.tar.gz](http://effbot.org/media/downloads/PIL-1.1.7.tar.gz)
Processing PIL-1.1.7.tar.gz
Running PIL-1.1.7/setup.py \-q bdist\_egg \--dist-dir /var/folders/kd/kdz+WPeYFKik+eU2zVQ+tE+++TI/-Tmp-/easy\_install-R5yISp/PIL-1.1.7/egg-dist-tmp-crzD37
WARNING: '' not a valid package name**;** please use only.-separated package names in setup.py
\--- using frameworks at /System/Library/Frameworks
unable to execute gcc: No such file or directory
error: Setup script exited with error: command 'gcc' failed with exit status 1

Apparently the key error there is "_unable to execute gcc: No such file or directory_". The **installer can't find the C compiler**. Pretty weird cause I had already installed Xcode and all the rest (I ran the iPhone simulator a couple of days ago). I thought that **maybe cloning the disk caused some unwanted file-renaming** and so on... so I reinstalled [Apple's Developer Tools](http://developer.apple.com/tools/) using the OS installation CD that came with the computer. After 10 minutes of low screeches and CD-ROM loading, the installation was over and I had another go:

\[mac\]@macs-iMac:/Applications/djangostack-1.1.1-0/projects/ltb\_project/src/ltb**\>**usemydjangostack
bash-3.2$ easy\_install PIL
Searching for PIL
Reading [http://pypi.python.org/simple/PIL/](http://pypi.python.org/simple/PIL/)
Reading [http://www.pythonware.com/products/pil](http://www.pythonware.com/products/pil)
Reading [http://effbot.org/zone/pil-changes-115.htm](http://effbot.org/zone/pil-changes-115.htm)
Reading [http://effbot.org/downloads/](http://effbot.org/downloads/)#Imaging
Best match: PIL 1.1.7
Downloading [http://effbot.org/media/downloads/PIL-1.1.7.tar.gz](http://effbot.org/media/downloads/PIL-1.1.7.tar.gz)
Processing PIL-1.1.7.tar.gz
Running PIL-1.1.7/setup.py \-q bdist\_egg \--dist-dir /var/folders/kd/kdz+WPeYFKik+eU2zVQ+tE+++TI/-Tmp-/easy\_install-oET2AJ/PIL-1.1.7/egg-dist-tmp-Ptx6Q-
WARNING: '' not a valid package name**;** please use only.-separated package names in setup.py
\--- using frameworks at /System/Library/Frameworks
cc1: error: unrecognized command line option "-Wno-long-double"
error: Setup script exited with error: command 'gcc' failed with exit status 1
bash-3.2$

Looked like I made some progress, as **the error now seemed more specific**: "_cc1: error: unrecognized command line option "-Wno-long-double_"". The reason why this is happening goes beyond my knowledge, so in desperate need of a quick fix I started a long google-journey. Luckily I soon ran into this post on stackOverflow "[Xcode gcc exit status 1](http://stackoverflow.com/questions/1832665/xcode-gcc-exit-status-1)". Essentially, it suggests to run _setup.py_ **using to an older gcc version** (gcc-4.0). Tried that and it worked just fine!

> Following some blog posts, on a hunch, I ran setup.py pointing to an older gcc version (gcc-4.0).
> 
> CC='/usr/bin/gcc-4.0' python setup.py build

### The fix

After downloading the PIL library from [here](http://www.pythonware.com/products/pil/), I **built** it:

bash-3.2$ CC='/usr/bin/gcc-4.0' python setup.py build
running build
running build\_py
running build\_ext
\--- using frameworks at /System/Library/Frameworks
building '\_imaging' extension
/usr/bin/gcc-4.0 \-fno-strict-aliasing \-Wno-long-double \-no-cpp-precomp \-mno-fused-madd \-DNDEBUG \-g \-fwrapv \-O3 \-Wall \-Wstrict-prototypes \-DHAVE\_LIBJPEG \-DHAVE\_LIBZ \-I/System/Library/Frameworks/Tcl.framework/Headers \-I/System/Library/Frameworks/Tk.framework/Headers \-IlibImaging \-I/Applications/djangostack-1.1.1-0/python/include \-I/usr/local/include \-I/usr/include \-I/Applications/djangostack-1.1.1-0/python/include/python2.5 \-c \_imaging.c \-o build/temp.macosx-10.4-i386-2.5/\_imaging.o
\_imaging.c:3017: warning: initialization from incompatible pointer type
\_imaging.c:3077: warning: initialization from incompatible pointer type
/usr/bin/gcc-4.0 \-fno-strict-aliasing \-Wno-long-double \-no-cpp-precomp \-mno-fused-madd \-DNDEBUG \-g \-fwrapv \-O3 \-Wall \-Wstrict-prototypes \-DHAVE\_LIBJPEG \-DHAVE\_LIBZ \-I/System/Library/Frameworks/Tcl.framework/Headers \-I/System/Library/Frameworks/Tk.framework/Headers \-IlibImaging \-I/Applications/djangostack-1.1.1-0/python/include \-I/usr/local/include \-I/usr/include \-I/Applications/djangostack-1.1.1-0/python/include/python2.5 \-c decode.c \-o build/temp.macosx-10.4-i386-2.5/decode.o
/usr/bin/gcc-4.0 \-fno-strict-aliasing \-Wno-long-double \-no-cpp-precomp \-mno-fused-madd \-DNDEBUG \-g \-fwrapv \-O3 \-Wall \-Wstrict-prototypes \-DHAVE\_LIBJPEG \-DHAVE\_LIBZ \-I/System/Library/Frameworks/Tcl.framework/Headers \-
\[......various other warnings........**\]**

gcc \-L/Applications/djangostack-1.1.1-0/common/lib \-bundle \-undefined dynamic\_lookup build/temp.macosx-10.4-i386-2.5/\_imaging.o build/temp.macosx-10.4-i386-2.5/decode.o build/temp.macosx-10.4-i386-2.5/encode.o build/temp.macosx-10.4-i386-2.5/map.o build/temp.macosx-10.4-i386-2.5/display.o build/temp.macosx-10.4-i386-2.5/outline.o build/temp.macosx-10.4-i386-2.5/path.o build/temp.macosx-10.4-i386-2.5/libImaging/Access.o build/temp.macosx-10.4-i386-2.5/libImaging/Antialias.o build/temp.macosx-10.4-i386-2.5/libImaging/Bands.o build/temp.macosx-10.4-i386-2.5/libImaging/BitDecode.o build/temp.macosx-10.4-i386-2.5/libImaging/Blend.o build/temp.macosx-10.4-i386-2.5/libImaging/Chops.o build/temp.macosx-10.4-i386-2.5/libImaging/Convert.o build/temp.macosx-10.4-i386-2.5/libImaging/ConvertYCbCr.o build/temp.macosx-10.4-i386-2.5/libImaging/Copy.o build/temp.macosx-10.4-i386-2.5/libImaging/Crc32.o build/temp.macosx-10.4-i386-2.5/libImaging/Crop.o build/temp.macosx-10.4-i386-2.5/libImaging/Dib.o build/temp.macosx-10.4-i386-2.5/libImaging/Draw.o build/temp.macosx-10.4-i386-2.5/libImaging/Effects.o build/temp.macosx-10.4-i386-2.5/libImaging/EpsEncode.o build/temp.macosx-10.4-i386-2.5/libImaging/File.o build/temp.macosx-10.4-i386-2.5/libImaging/Fill.o build/temp.macosx-10.4-i386-2.5/libImaging/Filter.o build/temp.macosx-10.4-i386-2.5/libImaging/FliDecode.o build/temp.macosx-10.4-i386-2.5/libImaging/Geometry.o build/temp.macosx-10.4-i386-2.5/libImaging/GetBBox.o build/temp.macosx-10.4-i386-2.5/libImaging/GifDecode.o build/temp.macosx-10.4-i386-2.5/libImaging/GifEncode.o build/temp.macosx-10.4-i386-2.5/libImaging/HexDecode.o build/temp.macosx-10.4-i386-2.5/libImaging/Histo.o build/temp.macosx-10.4-i386-2.5/libImaging/JpegDecode.o build/temp.macosx-10.4-i386-2.5/libImaging/JpegEncode.o build/temp.macosx-10.4-i386-2.5/libImaging/LzwDecode.o build/temp.macosx-10.4-i386-2.5/libImaging/Matrix.o build/temp.macosx-10.4-i386-2.5/libImaging/ModeFilter.o build/temp.macosx-10.4-i386-2.5/libImaging/MspDecode.o build/temp.macosx-10.4-i386-2.5/libImaging/Negative.o build/temp.macosx-10.4-i386-2.5/libImaging/Offset.o build/temp.macosx-10.4-i386-2.5/libImaging/Pack.o build/temp.macosx-10.4-i386-2.5/libImaging/PackDecode.o build/temp.macosx-10.4-i386-2.5/libImaging/Palette.o build/temp.macosx-10.4-i386-2.5/libImaging/Paste.o build/temp.macosx-10.4-i386-2.5/libImaging/Quant.o build/temp.macosx-10.4-i386-2.5/libImaging/QuantHash.o build/temp.macosx-10.4-i386-2.5/libImaging/QuantHeap.o build/temp.macosx-10.4-i386-2.5/libImaging/PcdDecode.o build/temp.macosx-10.4-i386-2.5/libImaging/PcxDecode.o build/temp.macosx-10.4-i386-2.5/libImaging/PcxEncode.o build/temp.macosx-10.4-i386-2.5/libImaging/Point.o build/temp.macosx-10.4-i386-2.5/libImaging/RankFilter.o build/temp.macosx-10.4-i386-2.5/libImaging/RawDecode.o build/temp.macosx-10.4-i386-2.5/libImaging/RawEncode.o build/temp.macosx-10.4-i386-2.5/libImaging/Storage.o build/temp.macosx-10.4-i386-2.5/libImaging/SunRleDecode.o build/temp.macosx-10.4-i386-2.5/libImaging/TgaRleDecode.o build/temp.macosx-10.4-i386-2.5/libImaging/Unpack.o build/temp.macosx-10.4-i386-2.5/libImaging/UnpackYCC.o build/temp.macosx-10.4-i386-2.5/libImaging/UnsharpMask.o build/temp.macosx-10.4-i386-2.5/libImaging/XbmDecode.o build/temp.macosx-10.4-i386-2.5/libImaging/XbmEncode.o build/temp.macosx-10.4-i386-2.5/libImaging/ZipDecode.o build/temp.macosx-10.4-i386-2.5/libImaging/ZipEncode.o -L/usr/local/lib -L/Applications/djangostack-1.1.1-0/python/lib -L/usr/lib -ljpeg -lz -o build/lib.macosx-10.4-i386-2.5/\_imaging.so
ld: warning: in build/temp.macosx-10.4-i386-2.5/\_imaging.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/decode.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/encode.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/map.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/display.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/outline.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/path.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/libImaging/Access.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/libImaging/Antialias.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/libImaging/Bands.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/libImaging/BitDecode.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/libImaging/Blend.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/libImaging/Chops.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/libImaging/Convert.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/libImaging/ConvertYCbCr.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/libImaging/Copy.o, file was built for i386 which is not the architecture being linked (x86\_64)
\[...various other warnings....**\]**

building '\_imagingtk' extension
creating build/temp.macosx-10.4-i386-2.5/Tk
/usr/bin/gcc-4.0 \-fno-strict-aliasing \-Wno-long-double \-no-cpp-precomp \-mno-fused-madd \-DNDEBUG \-g \-fwrapv \-O3 \-Wall \-Wstrict-prototypes \-I/System/Library/Frameworks/Tcl.framework/Headers \-I/System/Library/Frameworks/Tk.framework/Headers \-IlibImaging \-I/Applications/djangostack-1.1.1-0/python/include \-I/usr/local/include \-I/usr/include \-I/Applications/djangostack-1.1.1-0/python/include/python2.5 \-c \_imagingtk.c \-o build/temp.macosx-10.4-i386-2.5/\_imagingtk.o \-framework Tcl \-framework Tk
In file included from /System/Library/Frameworks/Tk.framework/Headers/tk.h:78,
                 from \_imagingtk.c:19:
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:131: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:334: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:453: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:471: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:496: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:497: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:509: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:522: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:1056: warning: function declaration isn~Rt a prototype
i686-apple-darwin10-gcc-4.0.1: \-framework: linker input file unused because linking not done
i686-apple-darwin10-gcc-4.0.1: Tcl: linker input file unused because linking not done
i686-apple-darwin10-gcc-4.0.1: \-framework: linker input file unused because linking not done
i686-apple-darwin10-gcc-4.0.1: Tk: linker input file unused because linking not done
/usr/bin/gcc-4.0 \-fno-strict-aliasing \-Wno-long-double \-no-cpp-precomp \-mno-fused-madd \-DNDEBUG \-g \-fwrapv \-O3 \-Wall \-Wstrict-prototypes \-I/System/Library/Frameworks/Tcl.framework/Headers \-I/System/Library/Frameworks/Tk.framework/Headers \-IlibImaging \-I/Applications/djangostack-1.1.1-0/python/include \-I/usr/local/include \-I/usr/include \-I/Applications/djangostack-1.1.1-0/python/include/python2.5 \-c Tk/tkImaging.c \-o build/temp.macosx-10.4-i386-2.5/Tk/tkImaging.o \-framework Tcl \-framework Tk
In file included from /System/Library/Frameworks/Tk.framework/Headers/tk.h:78,
                 from Tk/tkImaging.c:51:
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:131: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:334: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:453: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:471: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:496: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:497: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:509: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:522: warning: function declaration isn~Rt a prototype
/System/Library/Frameworks/Tk.framework/Headers/X11/Xlib.h:1056: warning: function declaration isn~Rt a prototype
i686-apple-darwin10-gcc-4.0.1: \-framework: linker input file unused because linking not done
i686-apple-darwin10-gcc-4.0.1: Tcl: linker input file unused because linking not done
i686-apple-darwin10-gcc-4.0.1: \-framework: linker input file unused because linking not done
i686-apple-darwin10-gcc-4.0.1: Tk: linker input file unused because linking not done
gcc \-L/Applications/djangostack-1.1.1-0/common/lib \-bundle \-undefined dynamic\_lookup build/temp.macosx-10.4-i386-2.5/\_imagingtk.o build/temp.macosx-10.4-i386-2.5/Tk/tkImaging.o \-L/usr/local/lib \-L/Applications/djangostack-1.1.1-0/python/lib \-L/usr/lib \-o build/lib.macosx-10.4-i386-2.5/\_imagingtk.so \-framework Tcl \-framework Tk
ld: warning: in build/temp.macosx-10.4-i386-2.5/\_imagingtk.o, file was built for i386 which is not the architecture being linked (x86\_64)
ld: warning: in build/temp.macosx-10.4-i386-2.5/Tk/tkImaging.o, file was built for i386 which is not the architecture being linked (x86\_64)
building '\_imagingmath' extension
/usr/bin/gcc-4.0 \-fno-strict-aliasing \-Wno-long-double \-no-cpp-precomp \-mno-fused-madd \-DNDEBUG \-g \-fwrapv \-O3 \-Wall \-Wstrict-prototypes \-I/System/Library/Frameworks/Tcl.framework/Headers \-I/System/Library/Frameworks/Tk.framework/Headers \-IlibImaging \-I/Applications/djangostack-1.1.1-0/python/include \-I/usr/local/include \-I/usr/include \-I/Applications/djangostack-1.1.1-0/python/include/python2.5 \-c \_imagingmath.c \-o build/temp.macosx-10.4-i386-2.5/\_imagingmath.o
gcc \-L/Applications/djangostack-1.1.1-0/common/lib \-bundle \-undefined dynamic\_lookup build/temp.macosx-10.4-i386-2.5/\_imagingmath.o \-L/usr/local/lib \-L/Applications/djangostack-1.1.1-0/python/lib \-L/usr/lib \-o build/lib.macosx-10.4-i386-2.5/\_imagingmath.so
ld: warning: in build/temp.macosx-10.4-i386-2.5/\_imagingmath.o, file was built for i386 which is not the architecture being linked (x86\_64)
\--------------------------------------------------------------------
PIL 1.1.7 SETUP SUMMARY
\--------------------------------------------------------------------
version       1.1.7
platform      darwin 2.5.4 (r254:67916, Nov 24 2009, 10:46:19)
              \[GCC 4.0.1 (Apple Computer, Inc. build 5250)**\]**
\--------------------------------------------------------------------
\--- TKINTER support available
\--- JPEG support available
\--- ZLIB (PNG/ZIP) support available
\*\*\* FREETYPE2 support not available
\*\*\* LITTLECMS support not available
\--------------------------------------------------------------------
To add a missing option, make sure you have the required
library, and set the corresponding ROOT variable in the
setup.py script.

To check the build, run the selftest.py script.
running build\_scripts
creating build/scripts-2.5
copying and adjusting Scripts/pilconvert.py \-**\>** build/scripts-2.5
copying and adjusting Scripts/pildriver.py \-**\>** build/scripts-2.5
copying and adjusting Scripts/pilfile.py \-**\>** build/scripts-2.5
copying Scripts/pilfont.py \-**\>** build/scripts-2.5
copying and adjusting Scripts/pilprint.py \-**\>** build/scripts-2.5
changing mode of build/scripts-2.5/pilconvert.py from 644 to 755
changing mode of build/scripts-2.5/pildriver.py from 644 to 755
changing mode of build/scripts-2.5/pilfile.py from 644 to 755
changing mode of build/scripts-2.5/pilfont.py from 644 to 755
changing mode of build/scripts-2.5/pilprint.py from 644 to 755

Then I **installed** it:

bash-3.2$ CC='/usr/bin/gcc-4.0' python setup.py install
running install
running build
running build\_py
running build\_ext
\--- using frameworks at /System/Library/Frameworks
\--------------------------------------------------------------------
PIL 1.1.7 SETUP SUMMARY
\--------------------------------------------------------------------
version       1.1.7
platform      darwin 2.5.4 (r254:67916, Nov 24 2009, 10:46:19)
              \[GCC 4.0.1 (Apple Computer, Inc. build 5250)**\]**
\--------------------------------------------------------------------
\--- TKINTER support available
\--- JPEG support available
\--- ZLIB (PNG/ZIP) support available
\*\*\* FREETYPE2 support not available
\*\*\* LITTLECMS support not available
\--------------------------------------------------------------------
To add a missing option, make sure you have the required
library, and set the corresponding ROOT variable in the
setup.py script.

To check the build, run the selftest.py script.
running build\_scripts
running install\_lib
creating /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/\_\_init\_\_.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/\_imaging.so \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/\_imagingmath.so \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/\_imagingtk.so \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ArgImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/BdfFontFile.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/BmpImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/BufrStubImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ContainerIO.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/CurImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/DcxImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/EpsImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ExifTags.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/FitsStubImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/FliImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/FontFile.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/FpxImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/GbrImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/GdImageFile.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/GifImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/GimpGradientFile.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/GimpPaletteFile.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/GribStubImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/Hdf5StubImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/IcnsImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/IcoImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/Image.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageChops.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageCms.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageColor.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageDraw.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageDraw2.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageEnhance.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageFile.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageFileIO.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageFilter.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageFont.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageGL.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageGrab.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageMath.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageMode.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageOps.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImagePalette.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImagePath.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageQt.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageSequence.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageShow.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageStat.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageTk.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageTransform.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImageWin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/ImtImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/IptcImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/JpegImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/McIdasImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/MicImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/MpegImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/MspImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/OleFileIO.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/PaletteFile.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/PalmImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/PcdImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/PcfFontFile.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/PcxImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/PdfImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/PixarImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/PngImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/PpmImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/PsdImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/PSDraw.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/SgiImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/SpiderImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/SunImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/TarIO.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/TgaImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/TiffImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/TiffTags.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/WalImageFile.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/WmfImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/XbmImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/XpmImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
copying build/lib.macosx-10.4-i386-2.5/XVThumbImagePlugin.py \-**\>** /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/\_\_init\_\_.py to \_\_init\_\_.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ArgImagePlugin.py to ArgImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/BdfFontFile.py to BdfFontFile.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/BmpImagePlugin.py to BmpImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/BufrStubImagePlugin.py to BufrStubImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ContainerIO.py to ContainerIO.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/CurImagePlugin.py to CurImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/DcxImagePlugin.py to DcxImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/EpsImagePlugin.py to EpsImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ExifTags.py to ExifTags.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/FitsStubImagePlugin.py to FitsStubImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/FliImagePlugin.py to FliImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/FontFile.py to FontFile.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/FpxImagePlugin.py to FpxImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/GbrImagePlugin.py to GbrImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/GdImageFile.py to GdImageFile.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/GifImagePlugin.py to GifImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/GimpGradientFile.py to GimpGradientFile.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/GimpPaletteFile.py to GimpPaletteFile.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/GribStubImagePlugin.py to GribStubImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/Hdf5StubImagePlugin.py to Hdf5StubImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/IcnsImagePlugin.py to IcnsImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/IcoImagePlugin.py to IcoImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/Image.py to Image.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageChops.py to ImageChops.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageCms.py to ImageCms.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageColor.py to ImageColor.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageDraw.py to ImageDraw.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageDraw2.py to ImageDraw2.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageEnhance.py to ImageEnhance.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageFile.py to ImageFile.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageFileIO.py to ImageFileIO.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageFilter.py to ImageFilter.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageFont.py to ImageFont.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageGL.py to ImageGL.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageGrab.py to ImageGrab.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageMath.py to ImageMath.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageMode.py to ImageMode.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageOps.py to ImageOps.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImagePalette.py to ImagePalette.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImagePath.py to ImagePath.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageQt.py to ImageQt.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageSequence.py to ImageSequence.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageShow.py to ImageShow.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageStat.py to ImageStat.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageTk.py to ImageTk.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageTransform.py to ImageTransform.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImageWin.py to ImageWin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImImagePlugin.py to ImImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/ImtImagePlugin.py to ImtImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/IptcImagePlugin.py to IptcImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/JpegImagePlugin.py to JpegImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/McIdasImagePlugin.py to McIdasImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/MicImagePlugin.py to MicImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/MpegImagePlugin.py to MpegImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/MspImagePlugin.py to MspImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/OleFileIO.py to OleFileIO.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/PaletteFile.py to PaletteFile.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/PalmImagePlugin.py to PalmImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/PcdImagePlugin.py to PcdImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/PcfFontFile.py to PcfFontFile.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/PcxImagePlugin.py to PcxImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/PdfImagePlugin.py to PdfImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/PixarImagePlugin.py to PixarImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/PngImagePlugin.py to PngImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/PpmImagePlugin.py to PpmImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/PsdImagePlugin.py to PsdImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/PSDraw.py to PSDraw.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/SgiImagePlugin.py to SgiImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/SpiderImagePlugin.py to SpiderImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/SunImagePlugin.py to SunImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/TarIO.py to TarIO.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/TgaImagePlugin.py to TgaImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/TiffImagePlugin.py to TiffImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/TiffTags.py to TiffTags.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/WalImageFile.py to WalImageFile.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/WmfImagePlugin.py to WmfImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/XbmImagePlugin.py to XbmImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/XpmImagePlugin.py to XpmImagePlugin.pyc
byte-compiling /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/XVThumbImagePlugin.py to XVThumbImagePlugin.pyc
running install\_scripts
copying build/scripts-2.5/pilconvert.py \-**\>** /Applications/djangostack-1.1.1-0/python/bin
copying build/scripts-2.5/pildriver.py \-**\>** /Applications/djangostack-1.1.1-0/python/bin
copying build/scripts-2.5/pilfile.py \-**\>** /Applications/djangostack-1.1.1-0/python/bin
copying build/scripts-2.5/pilfont.py \-**\>** /Applications/djangostack-1.1.1-0/python/bin
copying build/scripts-2.5/pilprint.py \-**\>** /Applications/djangostack-1.1.1-0/python/bin
changing mode of /Applications/djangostack-1.1.1-0/python/bin/pilconvert.py to 755
changing mode of /Applications/djangostack-1.1.1-0/python/bin/pildriver.py to 755
changing mode of /Applications/djangostack-1.1.1-0/python/bin/pilfile.py to 755
changing mode of /Applications/djangostack-1.1.1-0/python/bin/pilfont.py to 755
changing mode of /Applications/djangostack-1.1.1-0/python/bin/pilprint.py to 755
running install\_egg\_info
Writing /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL/PIL-1.1.7-py2.5.egg-info
creating /Applications/djangostack-1.1.1-0/python/lib/python2.5/site-packages/PIL.pth

And **that was it**: djangostack's python now has PIL available too:

bash-3.2$ python
Python 2.5.4 (r254:67916, Nov 24 2009, 10:46:19)
\[GCC 4.0.1 (Apple Computer, Inc. build 5250)\] on darwin
Type "help", "copyright", "credits" **or** "license" **for** more information.
>>> import Image
>>> dir(Image)
\['ADAPTIVE', 'AFFINE', 'ANTIALIAS', 'BICUBIC', 'BILINEAR', 'CONTAINER', 'CUBIC', 'DEBUG', 'EXTENSION', 'EXTENT', 'FLIP\_LEFT\_RIGHT', 'FLIP\_TOP\_BOTTOM', 'FLOYDSTEINBERG', 'ID', 'Image', 'ImageMode', 'ImagePalette', 'ImagePointHandler', 'ImageTransformHandler', 'IntType', 'LINEAR', 'MESH', 'MIME', 'MODES', 'NEAREST', 'NONE', 'NORMAL', 'OPEN', 'ORDERED', 'PERSPECTIVE', 'QUAD', 'RASTERIZE', 'ROTATE\_180', 'ROTATE\_270', 'ROTATE\_90', 'SAVE', 'SEQUENCE', 'StringType', 'TupleType', 'UnicodeStringType', 'VERSION', 'WEB', '\_E', '\_ENDIAN', '\_ImageCrop', '\_MAPMODES', '\_MODEINFO', '\_MODE\_CONV', '\_\_builtins\_\_', '\_\_doc\_\_', '\_\_file\_\_', '\_\_name\_\_', '\_conv\_type\_shape', '\_fromarray\_typemap', '\_getdecoder', '\_getencoder', '\_getscaleoffset', '\_imaging\_not\_installed', '\_initialized', '\_show', '\_showxv', '\_wedge', 'blend', 'byteorder', 'composite', 'core', 'eval', 'fromarray', 'frombuffer', 'fromstring', 'getmodebandnames', 'getmodebands', 'getmodebase', 'getmodetype', 'init', 'isDirectory', 'isImageType', 'isNumberType', 'isSequenceType', 'isStringType', 'isTupleType', 'merge', 'new', 'open', 'os', 'preinit', 'register\_extension', 'register\_mime', 'register\_open', 'register\_save', 'string', 'sys', 'v', 'warnings'\]
>>>

### Update 14/11/11: If you're on 10.7 (Lion)

This recipy won't work anymore on Lion because of the reasons pointed out in this [stack-overflow article](http://stackoverflow.com/questions/6906385/mac-osx-lion-virtualenv-pil-install-gcc-error):

> Xcode 4.1 on OS X Lion 10.7 no longer includes gcc-4.0 as it did in earlier versions of OS X. When you install a Python package like PIL that includes a C extension module, Python's Distutils will attempt to use the same version of the C compiler that that Python itself was build with.

Too bad. It's very easy to circumvent the problem.. just download PIL, start the stack as you would normally (./use\_djangostack) and manually install the PIL package with python setup.py install.

**Warning**: this will work, but you'll be able to use only _some_ of the functionalities PIL offers. E.g.:

\>>> import Image
# works just fine
>>> import \_imaging
dlopen("/Applications/djangostack-1.3-0/python/lib/python2.6/site-packages/PIL/\_imaging.so", 2);
Traceback (most recent call last):
  File "", line 1, in ImportError: dlopen(/Applications/djangostack-1.3-0/python/lib/python2.6/site-packages/PIL/\_imaging.so, 2): no suitable image found.  Did find:
	/Applications/djangostack-1.3-0/python/lib/python2.6/site-packages/PIL/\_imaging.so: mach-o, but wrong architecture

I order to understand what's going on, you should remember that the PIL library consists of two main parts: a number of Python modules, usually stored in a PIL subdirectory, and a binary extension module called \_imaging. Depending on platform and version, the latter is stored in a file named \_imaging.pyd, \_imaging.dll or \_imaging.so (more info on all of this can be found [here](http://effbot.org/zone/pil-imaging-not-installed.htm)).

The error we got ("\_imaging C module is not installed") is caused by the fact that Lion uses a different C compiler than the one used for building the python libraries in your Djangostack. That had a cascade effect on the C-imaging libraries installed by PIL (for the reason mentioned above), which, as a result, can't be run by Lion, and thus need to be updated.

The quick and dirty fix I used is this one: I installed again PIL **outside** the djangostack, and then copied over the newly generate C files back inside the stack. In other words, I installed again PIL using the latest C compiler that comes by default with Lion, and copied over only what I needed (the C libraries) into the stack.

That is: install PIL system-wide via the usual easy\_install PIL. This will install the package in /Library/Python/2.7/site-packages/PIL-1.1.7-py2.7-macosx-10.7-intel.egg/. Then grab the files you need from there (e.g. \_imaging.so, \_imagingmath.so, \_imagingtk.so) and put them into the djangostack python folder, which will be something like this: /Applications/djangostack-1.3-0/python/lib/python2.6/site-packages/PIL (obviously this location varies depending on where you originally installed djangostack).

That's the end. It's a dirty trick, but it worked for me!

### References:

- [Installing the Python Imaging Library on Mac OS X Leopard](http://passingcuriosity.com/2009/installing-pil-on-mac-os-x-leopard/)
- [Installing PIL on Mac OS X Leopard virtualenv with easy\_install](http://nathanvangheem.com/news/installing-pil-on-mac-os-x-leopard-virtualenv-with-easy_install)
- [The GNU compiler collection on mac osX](http://developer.apple.com/tools/gcc_overview.html)
- [\-Wno-long-double discussion on google groups](http://groups.google.com/group/pygraphviz-discuss/browse_thread/thread/63d366af8fd7323b?pli=1)
- [MAC OSX Python build issues /w PIL (Imaging-1.1.7)](http://vonluck.wordpress.com/2010/05/22/mac-osx-python-build-issues-w-pil-imaging-1-1-7/)
- [libjpeg and Python Imaging (PIL) on Snow Leopard](http://jetfar.com/libjpeg-and-python-imaging-pil-on-snow-leopard/)
- [Xcode gcc exit status 1](http://stackoverflow.com/questions/1832665/xcode-gcc-exit-status-1)
