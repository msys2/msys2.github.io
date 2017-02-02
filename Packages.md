This is a dump from `pacman` of all the packages we provide as of 18th April 2015. The commands used to generate this list are:

    pacman -Ss | grep '^mingw64/' -A 1 | sed -r -e 's/\[installed.*\]//' -e 's#^mingw64/([^ ]+)#<br/>mingw/<b>\1</b>#' -e 's/-x86_64//'
    pacman -Ss | grep '^msys/' -A 1 | sed -r -e 's/\[installed.*\]//' -e 's#^msys/([^ ]+)#<br/>msys/<b>\1</b>#'

<br/>mingw/<b>mingw-w64-FreeImage</b> 3.16.0-6
    Library project for developers who would like to support popular graphics image formats (mingw-w64).
<br/>mingw/<b>mingw-w64-GtkAda-svn</b> 3.8_r229123P-1 (mingw-w64-x86_64)
    GtkAda is a Gtk2+ binding for Ada using the OOP and other features of this programming language
<br/>mingw/<b>mingw-w64-LibRaw</b> 0.16.0-2 
    Library for reading RAW files obtained from digital photo cameras (mingw-w64)
<br/>mingw/<b>mingw-w64-OpenSceneGraph</b> 3.3.6-1
    Open source high performance 3D graphics toolkit (mingw-w64)
<br/>mingw/<b>mingw-w64-OpenSceneGraph-debug</b> 3.3.6-1
    Open source high performance 3D graphics toolkit (debug) (mingw-w64)
<br/>mingw/<b>mingw-w64-OpenSceneGraph-debug-git</b> r13068.2bdb951-2
    Open source high performance 3D graphics toolkit (mingw-w64)
<br/>mingw/<b>mingw-w64-OpenSceneGraph-git</b> r13068.2bdb951-2
    Open source high performance 3D graphics toolkit (mingw-w64)
<br/>mingw/<b>mingw-w64-ResIL</b> 1.7.9-4
    Library for reading several different image formats (mingw-w64)
<br/>mingw/<b>mingw-w64-SDL</b> 1.2.15-5 
    A library for portable low-level access to a video framebuffer, audio output, mouse, and keyboard (mingw-w64)
<br/>mingw/<b>mingw-w64-SDL2</b> 2.0.3-2
    A library for portable low-level access to a video framebuffer, audio output, mouse, and keyboard (Version 2) (mingw-w64)
<br/>mingw/<b>mingw-w64-SDL2_image</b> 2.0.0-2
    A simple library to load images of various formats as SDL surfaces (Version 2)
<br/>mingw/<b>mingw-w64-SDL2_mixer</b> 2.0.0-4
    A simple multi-channel audio mixer (Version 2) (mingw-w64)
<br/>mingw/<b>mingw-w64-SDL2_net</b> 2.0.0-2
    A small sample cross-platform networking library (Version 2) (mingw-w64)
<br/>mingw/<b>mingw-w64-SDL2_sound-hg</b> r596.719dade41745-1
    A library to decode several popular sound file formats, patched for SDL2 (dev version)
<br/>mingw/<b>mingw-w64-SDL2_ttf</b> 2.0.12-1
    A library that allows you to use TrueType fonts in your SDL applications (Version 2)
<br/>mingw/<b>mingw-w64-SDL_gfx</b> 2.0.25-1
    SDL Graphic Primitives (mingw-w64)
<br/>mingw/<b>mingw-w64-SDL_image</b> 1.2.12-2
    A simple library to load images of various formats as SDL surfaces (mingw-w64)
<br/>mingw/<b>mingw-w64-SDL_ttf</b> 2.0.11-1
    A library that allows you to use TrueType fonts in your SDL applications (mingw-w64)
<br/>mingw/<b>mingw-w64-SnoreGrowl</b> 0.4.0-1
    A C and C++ library providing an api to use Growl notifications, based on the GNTP protocol. (mingw-w64)
<br/>mingw/<b>mingw-w64-Snorenotify</b> 0.5.2-1
    Snorenotify is a multi platform Qt notification framework. Using a plugin system it is possible to create notifications with many different notification systems on Windows, Mac OS and Unix. (mingw-w64)
<br/>mingw/<b>mingw-w64-a52dec</b> 0.7.4-1 
    A free library for decoding ATSC A/52 streams
<br/>mingw/<b>mingw-w64-adwaita-icon-theme</b> 3.16.0-1 (mingw-w64-x86_64-gnome) 
    GNOME icon theme (mingw-w64)
<br/>mingw/<b>mingw-w64-ag</b> 0.29.1.r1497.773e96a-1 
    The Silver Searcher: An attempt to make something better than ack, which itself is better than grep (mingw-w64)
<br/>mingw/<b>mingw-w64-allegro</b> 5.0.11-1
    Portable library mainly aimed at video game and multimedia programming (mingw-w64)
<br/>mingw/<b>mingw-w64-angleproject-git</b> 2.1.r3427-1 (mingw-w64) 
    Angle project built from git source (mingw-w64)
<br/>mingw/<b>mingw-w64-aria2</b> 1.18.10-1 
    A multi-protocol & multi-source, cross platform download utility (mingw-w64)
<br/>mingw/<b>mingw-w64-aribb24</b> 1.0.3-1 
    A library for ARIB STD-B24, decoding JIS 8 bit characters and parsing MPEG-TS stream (mingw-w64)
<br/>mingw/<b>mingw-w64-aspell</b> 0.60.7.20131207-1 
    A spell checker designed to eventually replace Ispell (mingw-w64)
<br/>mingw/<b>mingw-w64-assimp</b> 3.1.1-1
    Portable Open Source library to import various well-known 3D model formats in an uniform manner (mingw-w64)
<br/>mingw/<b>mingw-w64-assimp-git</b> r2029.bd0c283-1
    Portable Open Source library to import various well-known 3D model formats in an uniform manner (mingw-w64)
<br/>mingw/<b>mingw-w64-astyle</b> 2.05.1-1 
    A free, fast and small automatic formatter for C, C++, C#, and Java source code (mingw-w64)
<br/>mingw/<b>mingw-w64-atk</b> 2.16.0-1 
    A library providing a set of interfaces for accessibility (mingw-w64)
<br/>mingw/<b>mingw-w64-atkmm</b> 2.22.7-2 
    C++ bindings for atk (mingw-w64)
<br/>mingw/<b>mingw-w64-babl-git</b> r768.c9690f8-1 
    Dynamic Pixel Format Translation Library (mingw-w64)
<br/>mingw/<b>mingw-w64-badvpn</b> 1.999.129-1
    NCD scripting language, tun2socks proxifier, P2P VPN (mingw-w64)
<br/>mingw/<b>mingw-w64-bc</b> 1.06-2
    bc is an arbitrary precision numeric processing language (mingw-w64)
<br/>mingw/<b>mingw-w64-binutils</b> 2.25-3 (mingw-w64-x86_64-toolchain)
    A set of programs to assemble and manipulate binary and object files
<br/>mingw/<b>mingw-w64-binutils-git</b> 2.25.r81716.c8daf7d-1 
    A set of programs to assemble and manipulate binary and object files
<br/>mingw/<b>mingw-w64-bison</b> 3.0.4-2
    The GNU general-purpose parser generator
<br/>mingw/<b>mingw-w64-blender</b> 2.74-1 
    A fully integrated 3D graphics creation suite (mingw-w64)
<br/>mingw/<b>mingw-w64-blender-git</b> r58316.c32ded3-1
    A fully integrated 3D graphics creation suite (mingw-w64)
<br/>mingw/<b>mingw-w64-boost</b> 1.57.0-2 
    Free peer-reviewed portable C++ source libraries (mingw-w64)
<br/>mingw/<b>mingw-w64-box2d</b> 2.3.0-1 
    2D rigid body simulation library for games (mingw-w64)
<br/>mingw/<b>mingw-w64-breakpad-svn</b> r1413-1
    An open-source multi-platform crash reporting system (mingw-w64)
<br/>mingw/<b>mingw-w64-btyacc</b> 3.0-1
    BackTracking Yacc (mingw-w64)
<br/>mingw/<b>mingw-w64-bullet</b> 2.83-2
    A 3D Collision Detection and Rigid Body Dynamics Library for games and animation (mingw-w64)
<br/>mingw/<b>mingw-w64-bullet-debug</b> 2.83-2
    A 3D Collision Detection and Rigid Body Dynamics Library for games and animation (mingw-w64)
<br/>mingw/<b>mingw-w64-bwidget</b> 1.9.7-1
    A companion to Tcllib, for Tk related packages.
<br/>mingw/<b>mingw-w64-bzip2</b> 1.0.6-3 
    A high-quality data compression program (mingw-w64)
<br/>mingw/<b>mingw-w64-c-ares</b> 1.10.0-1 
    C library that performs DNS requests and name resolves asynchronously (mingw-w64)
<br/>mingw/<b>mingw-w64-ca-certificates</b> 20141019-1 
    Common CA certificates (mingw-w64)
<br/>mingw/<b>mingw-w64-cairo</b> 1.14.2-1 
    Cairo vector graphics library (mingw-w64)
<br/>mingw/<b>mingw-w64-cairomm</b> 1.11.2-1 
    C++ bindings to Cairo vector graphics library (mingw-w64)
<br/>mingw/<b>mingw-w64-ccache-git</b> r1359.c5533d6-1 
    A compiler cache (mingw-w64).
<br/>mingw/<b>mingw-w64-cegui</b> 0.8.3-2
    A free library providing windowing and widgets for graphics APIs/engines (mingw-w64)
<br/>mingw/<b>mingw-w64-celt</b> 0.11.3-2 
    Low-latency audio communication codec (mingw-w64)
<br/>mingw/<b>mingw-w64-cfitsio</b> 3.370-1 
    A library of C and Fortran subroutines for reading and writing data files in FITS (Flexible Image Transport System) data format (mingw-w64)
<br/>mingw/<b>mingw-w64-cgal</b> 4.5.1-2
    Computational Geometry Algorithms Library (mingw-w64)
<br/>mingw/<b>mingw-w64-check</b> 0.9.14-1
    A unit testing framework for C (mingw-w64)
<br/>mingw/<b>mingw-w64-chipmunk</b> 7.0.0-1 
    A high-performance 2D rigid body physics library (mingw-w64)
<br/>mingw/<b>mingw-w64-chromaprint</b> 1.2-1 
    Library that implements a custom algorithm for extracting fingerprints from any audio source (mingw-w64)
<br/>mingw/<b>mingw-w64-clang</b> 3.5.1-1 
    C language family frontend for LLVM
<br/>mingw/<b>mingw-w64-clang-analyzer</b> 3.5.1-1 
    A source code analysis framework
<br/>mingw/<b>mingw-w64-clang-analyzer-cern-git</b> r52924-1
    A source code analysis framework
<br/>mingw/<b>mingw-w64-clang-analyzer-svn</b> r217857-1
    A source code analysis framework
<br/>mingw/<b>mingw-w64-clang-cern-git</b> r52924-1
    C language family frontend for LLVM
<br/>mingw/<b>mingw-w64-clang-svn</b> r217857-1
    C language family frontend for LLVM
<br/>mingw/<b>mingw-w64-clang-tools-extra</b> 3.5.1-1 
    Extra tools built using Clang's tooling APIs
<br/>mingw/<b>mingw-w64-clang-tools-extra-svn</b> r217768-1
    Extra tools built using Clang's tooling APIs
<br/>mingw/<b>mingw-w64-cling-cern-git</b> r2453-1
    C language family frontend for LLVM
<br/>mingw/<b>mingw-w64-cloog</b> 0.18.1-3 (mingw-w64-x86_64) 
    Library that generates loops for scanning polyhedra
<br/>mingw/<b>mingw-w64-clutter</b> 1.22.0-1
    A GObject based library for creating fast, visually rich graphical user interfaces. (mingw-w64)
<br/>mingw/<b>mingw-w64-clutter-gst</b> 2.0.12-1
    A GStreamer integration library for Clutter. (mingw-w64)
<br/>mingw/<b>mingw-w64-clutter-gtk</b> 1.6.0-1
    Clutter integration with GTK+. (mingw-w64)
<br/>mingw/<b>mingw-w64-cmake</b> 3.2.1-2 
    A cross-platform open-source make system (mingw-w64).
<br/>mingw/<b>mingw-w64-cmake-git</b> r25180.3bbdb23-1
    A cross-platform open-source make system (mingw-w64).
<br/>mingw/<b>mingw-w64-cocos2d-x-console-git</b> r492.cc6097d-1
    cocos2d command line tool (mingw-w64)
<br/>mingw/<b>mingw-w64-cocos2d-x-git</b> r25639.c9d0b0f-1 
    Open source game framework written in C++ (mingw-w64).
<br/>mingw/<b>mingw-w64-codelite-git</b> 7.0.157.ga86ea67-1 
    Open-source, cross platform IDE for the C/C++ programming languages (mingw-w64)
<br/>mingw/<b>mingw-w64-cogl</b> 1.20.0-1
    An object oriented GL/GLES Abstraction/Utility Layer (mingw-w64)
<br/>mingw/<b>mingw-w64-coin3d-hg</b> r11404.a9b4869bdc0e-1
    High-level, retained-mode toolkit for effective 3D graphics development (mingw-w64)
<br/>mingw/<b>mingw-w64-collada-dom-svn</b> 2.4.1.r889-3
    API that provides a C++ object representation of a COLLADA XML instance document (mingw-w64)
<br/>mingw/<b>mingw-w64-conemu-git</b> r1093.261fe53-2 
    Customizable Windows console emulator with tabs.
<br/>mingw/<b>mingw-w64-cppunit</b> 1.13.2-3 
    A C++ unit testing framework (mingw-w64)
<br/>mingw/<b>mingw-w64-crt-git</b> 5.0.0.4485.c881cc7-1 (mingw-w64-x86_64-toolchain mingw-w64-x86_64) 
    MinGW-w64 CRT for Windows
<br/>mingw/<b>mingw-w64-crypto++</b> 5.6.2-2
    Crypto++ Library is a free C++ class library of cryptographic schemes.
<br/>mingw/<b>mingw-w64-ctags</b> 5.8-1 
    A multilanguage implementation of Ctags (mingw-w64)
<br/>mingw/<b>mingw-w64-ctpl-git</b> 0.3.3.382.8aea180-1
    C Template (Parser) Library (mingw-w64)
<br/>mingw/<b>mingw-w64-curl</b> 7.41.0-1 
    An URL retrival utility and library. (mingw-w64)
<br/>mingw/<b>mingw-w64-cyrus-sasl</b> 2.1.26-4 
    Cyrus Simple Authentication Service Layer (SASL) library
<br/>mingw/<b>mingw-w64-cython</b> 0.22-1 (mingw-w64-x86_64) 
    C-Extensions for Python (mingw-w64)
<br/>mingw/<b>mingw-w64-cython2</b> 0.22-1 (mingw-w64-x86_64) 
    C-Extensions for Python (mingw-w64)
<br/>mingw/<b>mingw-w64-d-feet</b> 0.3.9-1
    D-Bus debugger for GNOME (mingw-w64)
<br/>mingw/<b>mingw-w64-daala-git</b> r1109.07ba88c-1
    Daala is next-next-gen video compression technology from Xiph.org, Mozilla and others.
<br/>mingw/<b>mingw-w64-db</b> 6.0.19-2 (mingw-w64-x86_64) 
    The Berkeley DB embedded database system (mingw-w64)
<br/>mingw/<b>mingw-w64-dbus</b> 1.9.10-1 
    Freedesktop.org message bus system (mingw-w64)
<br/>mingw/<b>mingw-w64-dbus-glib</b> 0.102-1 
    D-Bus Message Bus System (mingw-w64)
<br/>mingw/<b>mingw-w64-devhelp</b> 3.8.2-1
    Remote desktop client for the GNOME Desktop (mingw-w64)
<br/>mingw/<b>mingw-w64-dime-hg</b> r189.7d019eb887bd-1
    A library for reading, constructing, manipulating, and writing DXF files (mingw-w64)
<br/>mingw/<b>mingw-w64-discount</b> 2.1.8-1
    A Markdown implementation written in C (mingw-w64)
<br/>mingw/<b>mingw-w64-djvulibre</b> 3.5.25.3-1 
    Suite to create, manipulate and view DjVu (mingw-w64)
<br/>mingw/<b>mingw-w64-dlfcn</b> r19-1
    A wrapper for dlfcn to the Win32 API (mingw-w64)
<br/>mingw/<b>mingw-w64-dlfcn-svn</b> r37-1
    A wrapper for dlfcn to the Win32 API (mingw-w64)
<br/>mingw/<b>mingw-w64-dmake</b> 4.12.2-5 (mingw-w64-x86_64) 
    Dmake is a make utility similar to GNU make or the Workshop dmake (mingw-w64)
<br/>mingw/<b>mingw-w64-dnscrypt-proxy</b> 1.4.2-1
    A tool for securing communications between a client and a DNS resolver (mingw-w64)
<br/>mingw/<b>mingw-w64-dnssec-anchors</b> 20141229-1
    DNSSEC trust anchors for the root zone (mingw-w64)
<br/>mingw/<b>mingw-w64-docbook-xml</b> 4.5-4 
    A widely used XML scheme for writing documentation and help
<br/>mingw/<b>mingw-w64-docbook-xsl</b> 1.78.1-4 
    XML stylesheets for Docbook-xml transformations (mingw-w64)
<br/>mingw/<b>mingw-w64-doxygen</b> 1.8.9.1-1
    A documentation system for C++, C, Java, IDL and PHP (mingw-w64)
<br/>mingw/<b>mingw-w64-drmingw</b> 0.6.6-1
    Just-in-Time (JIT) debugger (mingw-w64)
<br/>mingw/<b>mingw-w64-drmingw-git</b> r182.867ab17-1
    Just-in-Time (JIT) debugger (mingw-w64)
<br/>mingw/<b>mingw-w64-dumb</b> 0.9.3-3
    IT, XM, S3M and MOD player library (mingw-w64)
<br/>mingw/<b>mingw-w64-eigen3</b> 3.2.4-1 
    Lightweight C++ template library for vector and matrix math (mingw-w64)
<br/>mingw/<b>mingw-w64-emacs</b> 24.5-1
    The extensible, customizable, self-documenting, real-time display editor.
<br/>mingw/<b>mingw-w64-emacs-git</b> r121030.a2940cd-1
    The extensible, customizable, self-documenting, real-time display editor (mingw-w64)
<br/>mingw/<b>mingw-w64-enca</b> 1.16-1 
    Charset analyser and converter (mingw-w64)
<br/>mingw/<b>mingw-w64-enchant</b> 1.6.0-7 
    Enchanting Spell Checking Library (mingw-w64)
<br/>mingw/<b>mingw-w64-eog</b> 3.16.0-1
    Eye of GNOME graphics viewer program (mingw-w64)
<br/>mingw/<b>mingw-w64-eog-plugins</b> 3.16.0-1
    Eye of GNOME graphics viewer program - plugins (mingw-w64)
<br/>mingw/<b>mingw-w64-evince</b> 3.16.0-1
    Document (PostScript, PDF) viewer (mingw-w64)
<br/>mingw/<b>mingw-w64-exiv2</b> 0.24-4 
    Exif and Iptc metadata manipulation library and tools (mingw-w64)
<br/>mingw/<b>mingw-w64-expat</b> 2.1.0-5 
    An XML parser library (mingw-w64)
<br/>mingw/<b>mingw-w64-extra-cmake-modules</b> 1.5.0-1 
    Extra CMake modules (mingw-w64)
<br/>mingw/<b>mingw-w64-faac</b> 1.28-1 (mingw-w64-x86_64)
    FAAC is an AAC audio encoder (mingw-w64)
<br/>mingw/<b>mingw-w64-faad2</b> 2.7-1 (mingw-w64-x86_64) 
    ISO AAC audio decoder (mingw-w64)
<br/>mingw/<b>mingw-w64-farstream</b> 0.2.7-1 (mingw-w64-x86_64) 
    Farstream (formerly Farsight) - Audio/Video Communications Framework
<br/>mingw/<b>mingw-w64-ffmpeg</b> 2.6.2-1 (mingw-w64-x86_64) 
    Complete and free Internet live audio and video broadcasting solution (mingw-w64)
<br/>mingw/<b>mingw-w64-fftw</b> 3.3.4-3 
    A library for computing the discrete Fourier transform (DFT) (mingw-w64)
<br/>mingw/<b>mingw-w64-field3d</b> 1.4.3-2 
    Open source library for storing voxel data (mingw-w64)
<br/>mingw/<b>mingw-w64-firebird-git</b> 3.0.0.31514.b244095-1 
    Cross-platform relational database offering many ANSI SQL standard features (mingw-w64)
<br/>mingw/<b>mingw-w64-flac</b> 1.3.1-1 
    Free Lossless Audio Codec (mingw-w64)
<br/>mingw/<b>mingw-w64-flexdll</b> 0.34-1
    An implementation of a dlopen-like API for Windows (mingw-w64)
<br/>mingw/<b>mingw-w64-fltk</b> 1.3.3-1 (mingw-w64-x86_64) 
    C++ user interface toolkit (mingw-w64)
<br/>mingw/<b>mingw-w64-fluidsynth</b> 1.1.6-2 
    A real-time software synthesizer based on the SoundFont 2 specifications (mingw-w64)
<br/>mingw/<b>mingw-w64-fontconfig</b> 2.11.1-3 
    A library for configuring and customizing font access (mingw-w64)
<br/>mingw/<b>mingw-w64-fossil</b> 1.32-1
    Simple, high-reliability, distributed software configuration management (mingw-w64)
<br/>mingw/<b>mingw-w64-freeglut</b> 3.0.0-1
    Freeglut allows the user to create and manage windows containing OpenGL contexts (mingw32-w64)
<br/>mingw/<b>mingw-w64-freetype</b> 2.5.5-3 
    TrueType font rendering library (mingw-w64)
<br/>mingw/<b>mingw-w64-fribidi</b> 0.19.6-3 
    A Free Implementation of the Unicode Bidirectional Algorithm (mingw-w64)
<br/>mingw/<b>mingw-w64-ftgl</b> 2.1.3rc5-1
    OpenGL library to use arbitrary fonts (mingw-w64)
<br/>mingw/<b>mingw-w64-gc</b> 7.4.2-1 
    A garbage collector for C and C++ (mingw-w64)
<br/>mingw/<b>mingw-w64-gcc</b> 4.9.2-5 (mingw-w64-x86_64-toolchain mingw-w64-x86_64) 
    GNU Compiler Collection (C,C++,OpenMP) for MinGW-w64
<br/>mingw/<b>mingw-w64-gcc-ada</b> 4.9.2-5 (mingw-w64-x86_64-toolchain mingw-w64-x86_64) 
    GNU Compiler Collection (Ada) for MinGW-w64
<br/>mingw/<b>mingw-w64-gcc-ada-debug</b> 4.9.1-3
    Detached debugging symbols for mingw-w64-gcc-ada
<br/>mingw/<b>mingw-w64-gcc-debug</b> 4.9.1-3
    Detached debugging symbols for mingw-w64-gcc
<br/>mingw/<b>mingw-w64-gcc-fortran</b> 4.9.2-5 (mingw-w64-x86_64-toolchain mingw-w64-x86_64) 
    GNU Compiler Collection (Fortran) for MinGW-w64
<br/>mingw/<b>mingw-w64-gcc-fortran-debug</b> 4.9.1-3
    Detached debugging symbols for mingw-w64-gcc-fortran
<br/>mingw/<b>mingw-w64-gcc-libgfortran</b> 4.9.2-5 (mingw-w64-x86_64-toolchain mingw-w64-x86_64) 
    GNU Compiler Collection (libgfortran) for MinGW-w64
<br/>mingw/<b>mingw-w64-gcc-libgfortran-debug</b> 4.9.1-3
    Detached debugging symbols for mingw-w64-gcc-libgfortran
<br/>mingw/<b>mingw-w64-gcc-libs</b> 4.9.2-5 (mingw-w64-x86_64-toolchain mingw-w64-x86_64) 
    GNU Compiler Collection (libraries) for MinGW-w64
<br/>mingw/<b>mingw-w64-gcc-libs-debug</b> 4.9.1-3
    Detached debugging symbols for mingw-w64-gcc-libs
<br/>mingw/<b>mingw-w64-gcc-objc</b> 4.9.2-5 (mingw-w64-x86_64-toolchain mingw-w64-x86_64) 
    GNU Compiler Collection (ObjC,Obj-C++) for MinGW-w64
<br/>mingw/<b>mingw-w64-gcc-objc-debug</b> 4.9.1-3
    Detached debugging symbols for mingw-w64-gcc-objc
<br/>mingw/<b>mingw-w64-gd</b> 2.1.0-2
    Library for the dynamic creation of images by programmers (mingw-w64)
<br/>mingw/<b>mingw-w64-gdal</b> 1.11.2-1
    A translator library for raster geospatial data formats (mingw-w64)
<br/>mingw/<b>mingw-w64-gdb</b> 7.6.2-2 (mingw-w64-x86_64-toolchain) 
    GNU Debugger (mingw-w64)
<br/>mingw/<b>mingw-w64-gdbm</b> 1.11-1 
    GNU database library (mingw-w64)
<br/>mingw/<b>mingw-w64-gdk-pixbuf2</b> 2.31.1-3 
    An image loading library (mingw-w64)
<br/>mingw/<b>mingw-w64-gdl</b> 3.16.0-1 
    GNOME Docking Library (mingw-w64)
<br/>mingw/<b>mingw-w64-geany</b> 1.24.1-1 
    Fast and lightweight IDE (mingw-w64)
<br/>mingw/<b>mingw-w64-gedit</b> 3.16.0-1 
    A text editor for GNOME (mingw-w64)
<br/>mingw/<b>mingw-w64-gedit-plugins</b> 3.16.0-1 
    Collection of plugins for the gedit Text Editor (mingw-w64)
<br/>mingw/<b>mingw-w64-gegl-git</b> r6521.06aea8e-1 
    Generic Graphics Library (mingw-w64)
<br/>mingw/<b>mingw-w64-geoclue</b> 0.12.99-2 
    Modular Geoinformation Service (mingw-w64)
<br/>mingw/<b>mingw-w64-geocode-glib</b> 3.16.0-1
    geocoding and reverse geocoding GLib library using Yahoo! Place Finder (mingw-w64)
<br/>mingw/<b>mingw-w64-geoip2-database</b> 20150102-1
    GeoLite country geolocation database compiled by MaxMind (mingw-w64)
<br/>mingw/<b>mingw-w64-geos</b> 3.4.2-3
    C++ port of the Java Topology Suite (mingw-w64)
<br/>mingw/<b>mingw-w64-gettext</b> 0.19.4-2 (mingw-w64-x86_64) 
    GNU internationalization library (mingw-w64)
<br/>mingw/<b>mingw-w64-gexiv2</b> 0.10.3-1
    GObject-based wrapper around the Exiv2 library (mingw-w64)
<br/>mingw/<b>mingw-w64-ghex</b> 3.10.1-2
    GNOME Hex editor for files (mingw-w64)
<br/>mingw/<b>mingw-w64-ghostscript</b> 9.15-2 (mingw-w64-x86_64) 
    An interpreter for the PostScript language (mingw-w64)
<br/>mingw/<b>mingw-w64-giflib</b> 5.1.1-1 
    A library for reading and writing gif images (mingw-w64)
<br/>mingw/<b>mingw-w64-gimp</b> 2.8.14-3 (mingw-w64-x86_64) 
    GNU Image Manipulation Program (mingw-w64)
<br/>mingw/<b>mingw-w64-gimp-ufraw</b> 0.19.2-1 (mingw-w64-x86_64-gimp-plugins) 
    Converter for raw files; utility and GIMP plugin (mingw-w64)
<br/>mingw/<b>mingw-w64-gl2ps</b> 1.3.8-3 
    an OpenGL to PostScript printing library (mingw-w64)
<br/>mingw/<b>mingw-w64-glade</b> 3.18.3-3
    User interface builder for GTK+ and GNOME (mingw-w64)
<br/>mingw/<b>mingw-w64-glew</b> 1.12.0-1 (mingw-w64-x86_64) 
    GLEW, The OpenGL Extension Wrangler Library (mingw-w64)
<br/>mingw/<b>mingw-w64-glfw</b> 3.1-1 
    A free, open source, portable framework for OpenGL application development. (mingw-w64)
<br/>mingw/<b>mingw-w64-glib-networking</b> 2.44.0-2 
    Network-related GIO modules for glib (mingw-w64)
<br/>mingw/<b>mingw-w64-glib2</b> 2.44.0-1 
    Common C routines used by GTK+ 2.4 and other libs (mingw-w64)
<br/>mingw/<b>mingw-w64-glibmm</b> 2.44.0-1 
    Glib-- (glibmm) is a C++ interface for glib (mingw-w64)
<br/>mingw/<b>mingw-w64-glm</b> 0.9.6.3-1
    C++ mathematics library for 3D software based on the OpenGL Shading Language (GLSL) specification (mingw-w64)
<br/>mingw/<b>mingw-w64-glpk</b> 4.55-2 
    GNU Linear Programming Kit: solve LP, MIP and other problems (mingw-w64)
<br/>mingw/<b>mingw-w64-glsl-optimizer-git</b> r60842.9b2a2d2-1
    C++ library that takes GLSL shaders, does some GPU-independent optimizations on them and outputs GLSL back (mingw-w64)
<br/>mingw/<b>mingw-w64-gmime</b> 2.6.20-1
    Glorious MIME Utility Library (mingw-w64)
<br/>mingw/<b>mingw-w64-gmp</b> 6.0.0-2 (mingw-w64-x86_64) 
    A free library for arbitrary precision arithmetic
<br/>mingw/<b>mingw-w64-gnome-calculator</b> 3.16.0-1
    GNOME desktop calculator (mingw-w64)
<br/>mingw/<b>mingw-w64-gnome-common</b> 3.14.0-1 (mingw-w64-x86_64-gnome) 
    Common development macros for GNOME (mingw-w64)
<br/>mingw/<b>mingw-w64-gnome-doc-utils</b> 0.20.10-1 
    A Collection of Documentation Utilities for GNOME (mingw-w64)
<br/>mingw/<b>mingw-w64-gnome-icon-theme-symbolic</b> 3.12.0-1 (mingw-w64-x86_64-gnome)
    GNOME icon theme, symbolic icons (mingw-w64)
<br/>mingw/<b>mingw-w64-gnome-js-common</b> 0.1.2-1 (mingw-w64-x86_64)
    GNOME JavaScript common modules (mingw-w64)
<br/>mingw/<b>mingw-w64-gnonlin-git</b> 1.3.0.1.733.c91c4e4-1
    GStreamer Non-Linear plugins (mingw-w64)
<br/>mingw/<b>mingw-w64-gnu-cobol-svn</b> r275-1 (mingw-w64-x86_64)
    GNU Cobol is a free, modern COBOL compiler
<br/>mingw/<b>mingw-w64-gnupg</b> 1.4.18-1 (mingw-w64-x86_64)
    GNU Privacy Guard - a PGP replacement tool (mingw-w64)
<br/>mingw/<b>mingw-w64-gnutls</b> 3.4.0-2 
    A library which provides a secure layer over a reliable transport layer (mingw-w64)
<br/>mingw/<b>mingw-w64-go</b> 1.3-1 (mingw-w64-x86_64) 
    Go Lang
<br/>mingw/<b>mingw-w64-gobject-introspection</b> 1.44.0-3 
    GObject Introspection can scan C header and source files in order to generate introspection typelib files (mingw-w64)
<br/>mingw/<b>mingw-w64-goocanvas</b> 2.0.2-1
    Canvas widget for GTK+ that uses the Cairo 2D library (mingw-w64)
<br/>mingw/<b>mingw-w64-gperf</b> 3.0.4-2
    Perfect hash function generator (mingw-w64)
<br/>mingw/<b>mingw-w64-gpgme</b> 1.5.3-1
    A C wrapper library for GnuPG
<br/>mingw/<b>mingw-w64-gprbuild-gpl</b> 2013-1 (mingw-w64-x86_64)
    Software tool designed to help automate the construction of multi-language systems
<br/>mingw/<b>mingw-w64-graphicsmagick</b> 1.3.21-1 
    An image viewing/manipulation program (mingw-w64)
<br/>mingw/<b>mingw-w64-grep</b> 2.21-2 (mingw-w64-x86_64)
    Grep searches one or more input files for lines containing a match to a specified pattern (mingw-w64)
<br/>mingw/<b>mingw-w64-gsasl</b> 1.8.0-2 
    Simple Authentication and Security Layer framework and a few common SASL mechanisms (mingw-w64)
<br/>mingw/<b>mingw-w64-gsettings-desktop-schemas</b> 3.16.0-1 
    Shared GSettings schemas for the desktop (mingw-w64)
<br/>mingw/<b>mingw-w64-gsl</b> 1.16-2 
    The GNU Scientific Library (GSL) is a modern numerical library for C and C++ programmers (mingw-w64)
<br/>mingw/<b>mingw-w64-gsm</b> 1.0.13-2 
    Shared libraries for GSM 06.10 lossy speech compression (mingw-w64)
<br/>mingw/<b>mingw-w64-gss-git</b> r1479.6fdb450-1 
    GNU Generic Security Service (mingw-w64)
<br/>mingw/<b>mingw-w64-gst-editing-services</b> 1.2.1-1
    GStreamer Editing Services (mingw-w64)
<br/>mingw/<b>mingw-w64-gst-libav</b> 1.4.5-1
    GStreamer libav (mingw-w64)
<br/>mingw/<b>mingw-w64-gst-plugins-bad</b> 1.4.5-3
    GStreamer Multimedia Framework Bad Plugins (mingw-w64)
<br/>mingw/<b>mingw-w64-gst-plugins-base</b> 1.4.5-1 
    GStreamer Multimedia Framework Base Plugins (mingw-w64)
<br/>mingw/<b>mingw-w64-gst-plugins-base0.10</b> 0.10.36-1
    GStreamer Multimedia Framework Base Plugins (mingw-w64)
<br/>mingw/<b>mingw-w64-gst-plugins-good</b> 1.4.5-1
    GStreamer Multimedia Framework Base Plugins (mingw-w64)
<br/>mingw/<b>mingw-w64-gst-plugins-good0.10</b> 0.10.31-1
    GStreamer Multimedia Framework Base Plugins (mingw-w64)
<br/>mingw/<b>mingw-w64-gst-plugins-ugly</b> 1.4.5-1
    GStreamer Multimedia Framework Ugly Plugins (mingw-w64)
<br/>mingw/<b>mingw-w64-gst-python-git</b> 1.3.0.1.1283.3483187-1
    GStreamer GObject Introspection overrides for Python 3
<br/>mingw/<b>mingw-w64-gstreamer</b> 1.4.5-1 
    GStreamer Multimedia Framework (mingw-w64)
<br/>mingw/<b>mingw-w64-gstreamer0.10</b> 0.10.36-1
    GStreamer Multimedia Framework (mingw-w64)
<br/>mingw/<b>mingw-w64-gtk-doc</b> 1.21-1 
    Documentation tool for public library API (mingw-w64)
<br/>mingw/<b>mingw-w64-gtk-engine-unico</b> 1.0.2-1
    Unico GTK3 theme engine
<br/>mingw/<b>mingw-w64-gtk-vnc</b> 0.5.4-2
    VNC viewer widget for GTK+ (mingw-w64)
<br/>mingw/<b>mingw-w64-gtk2</b> 2.24.27-1 
    GTK+ is a multi-platform toolkit (v2) (mingw-w64)
<br/>mingw/<b>mingw-w64-gtk3</b> 3.16.1-1 
    GObject-based multi-platform GUI toolkit (v3) (mingw-w64)
<br/>mingw/<b>mingw-w64-gtkglext</b> 1.2.0-1
    opengl extensions for gtk2 (mingw-w64)
<br/>mingw/<b>mingw-w64-gtkhtml3</b> 4.8.5-1
    Library for embedding a lightweight web browser in GTK programs (mingw-w64)
<br/>mingw/<b>mingw-w64-gtkimageview</b> 1.6.4-1 
    Simple image viewer widget for GTK2 (mingw-w64)
<br/>mingw/<b>mingw-w64-gtkmm</b> 2.24.4-2 
    C++ bindings for gtk2 (mingw-w64)
<br/>mingw/<b>mingw-w64-gtkmm3</b> 3.16.0-1 
    C++ bindings for gtk3 (mingw-w64)
<br/>mingw/<b>mingw-w64-gtksourceview2</b> 2.10.5-1
    A text widget adding syntax highlighting and more to GNOME (mingw-w64)
<br/>mingw/<b>mingw-w64-gtksourceview3</b> 3.16.0-1 
    A text widget adding syntax highlighting and more to GNOME (mingw-w64)
<br/>mingw/<b>mingw-w64-gtkspell</b> 2.0.16-3 
    Provides word-processor-style highlighting and replacement of misspelled words in a GtkTextView widget (mingw-w64)
<br/>mingw/<b>mingw-w64-gtkspell3</b> 3.0.6-1 
    Provides word-processor-style highlighting and replacement of misspelled words in a GtkTextView widget (mingw-w64)
<br/>mingw/<b>mingw-w64-gxml</b> 0.4.1-2 (mingw-w64-x86_64)
    LibXML2 GObject wrapper version 0.4 (mingw-w64)
<br/>mingw/<b>mingw-w64-harfbuzz</b> 0.9.40-2 
    OpenType text shaping engine (mingw-w64)
<br/>mingw/<b>mingw-w64-hdf5</b> 1.8.14-1 
    General purpose library and file format for storing scientific data
<br/>mingw/<b>mingw-w64-headers-git</b> 5.0.0.4485.c881cc7-1 (mingw-w64-x86_64-toolchain mingw-w64-x86_64) 
    MinGW-w64 headers for Windows
<br/>mingw/<b>mingw-w64-hicolor-icon-theme</b> 0.14-1 
    Freedesktop.org Hicolor icon theme (mingw-w64)
<br/>mingw/<b>mingw-w64-hidapi</b> 0.8.0rc1-2 
    Library for communicating with USB and Bluetooth HID devices (mingw-w64)
<br/>mingw/<b>mingw-w64-hlsl2glsl-git</b> 0.749.9af03c9-1
    HLSL to GLSL shader language translator
<br/>mingw/<b>mingw-w64-http-parser</b> 2.3-2 
    Parser for HTTP Request/Response written in C (mingw-w64)
<br/>mingw/<b>mingw-w64-hunspell</b> 1.3.3-9 
    Spell checker and morphological analyzer library and program (mingw-w64)
<br/>mingw/<b>mingw-w64-hunspell-en</b> 2014.11.17-1
    Hunspell dictionaries (mingw-w64)
<br/>mingw/<b>mingw-w64-icon-naming-utils</b> 0.8.90-1 
    Maps the new names of icons for Tango to the legacy names used by the GNOME and KDE desktops. (mingw-w64)
<br/>mingw/<b>mingw-w64-icoutils</b> 0.31.0-1
    Create and extract MS Windows icons and cursors (mingw-w64)
<br/>mingw/<b>mingw-w64-icu</b> 55.1-1 
    International Components for Unicode library (mingw-w64)
<br/>mingw/<b>mingw-w64-icu-debug-libs</b> 55.1-1 
    International Components for Unicode library (mingw-w64)
<br/>mingw/<b>mingw-w64-id3lib</b> 3.8.3-1
    Library for reading, writing, and manipulating ID3v1 and ID3v2 tags (mingw-w64)
<br/>mingw/<b>mingw-w64-ilmbase</b> 2.2.0-1 
    Base libraries from ILM for OpenEXR (mingw-w64)
<br/>mingw/<b>mingw-w64-imagemagick</b> 6.9.0.7-1 
    An image viewing/manipulation program (mingw-w64)
<br/>mingw/<b>mingw-w64-indent</b> 2.2.11-3 
    C language source code formatting program (mingw-w64)
<br/>mingw/<b>mingw-w64-inkscape</b> 0.91-5 
    Vector graphics editor using the SVG file format (mingw-w64)
<br/>mingw/<b>mingw-w64-innoextract</b> 1.4-1
    A tool to extract installers created by Inno Setup (mingw-w64).
<br/>mingw/<b>mingw-w64-intel-tbb</b> 4.3_20150209-1 
    High level abstract threading library (mingw-w64)
<br/>mingw/<b>mingw-w64-irrlicht</b> 1.8.1-2
    An open source high performance realtime 3D graphics engine. (mingw-w64)
<br/>mingw/<b>mingw-w64-isl</b> 0.13-1 (mingw-w64-x86_64) 
    Library for manipulating sets and relations of integer points bounded by linear constraints
<br/>mingw/<b>mingw-w64-iso-codes</b> 3.57-1 
    Lists of the country, language, and currency names (mingw-w64)
<br/>mingw/<b>mingw-w64-itk</b> 4.7.1-1
    An open-source C++ toolkit for medical image processing (mingw-w64)
<br/>mingw/<b>mingw-w64-jansson</b> 2.7-1
    A C library for encoding, decoding and manipulating JSON data (mingw-w64)
<br/>mingw/<b>mingw-w64-jasper</b> 1.900.1-3 
    A software-based implementation of the codec specified in the emerging JPEG-2000 Part-1 standard (mingw-w64)
<br/>mingw/<b>mingw-w64-jbigkit</b> 2.1-1 
    Data compression library/utilities for bi-level high-resolution images (mingw-w64)
<br/>mingw/<b>mingw-w64-jemalloc</b> 3.6.0-1
    General-purpose scalable concurrent malloc implementation (mingw64)
<br/>mingw/<b>mingw-w64-json-c</b> 0.12-1
    A JSON implementation in C.
<br/>mingw/<b>mingw-w64-json-glib</b> 1.0.4-1 
    JSON-GLib implements a full suite of JSON-related tools using GLib and GObject (mingw-w64)
<br/>mingw/<b>mingw-w64-jsoncpp</b> 1.6.2-1 
    A C++ library for interacting with JSON (mingw-w64)
<br/>mingw/<b>mingw-w64-kicad-git</b> r6887.91c0868-1 
    Software for the creation of electronic schematic diagrams and printed circuit board artwork
<br/>mingw/<b>mingw-w64-kqoauth-qt4</b> 0.98-1
    kQOAuth is a library written in C++ for Qt that implements the OAuth 1.0 authentication specification RFC 5849.
<br/>mingw/<b>mingw-w64-l-smash</b> 2.3.0-1 
    Loyal to Spec of Mpeg4 and Ad-hoc Simple Hackwork. Yet another opensource mp4 handler (mingw-w64)
<br/>mingw/<b>mingw-w64-lame</b> 3.99.5-3 
    A high quality MPEG Audio Layer III (MP3) encoder (mingw-w64)
<br/>mingw/<b>mingw-w64-lapack</b> 3.5.0-2
    Linear Algebra PACKage (mingw-w64)
<br/>mingw/<b>mingw-w64-latexila</b> 3.16.0-1
    LaTeX editor designed for the GNOME desktop (mingw-w64)
<br/>mingw/<b>mingw-w64-lcms</b> 1.19-4 
    Lightweight color management development library/engine (mingw-w64)
<br/>mingw/<b>mingw-w64-lcms2</b> 2.6-3 
    Small-footprint color management engine, version 2 (mingw-w64)
<br/>mingw/<b>mingw-w64-ldns</b> 1.6.17-2
    Fast DNS library supporting recent RFCs (mingw-w64)
<br/>mingw/<b>mingw-w64-lensfun</b> 0.3.0-1 
    Database of photographic lenses and a library that allows advanced access to the database (mingw-w64)
<br/>mingw/<b>mingw-w64-leptonica</b> 1.71-1
    Leptonica library (mingw-w64)
<br/>mingw/<b>mingw-w64-libarchive</b> 3.1.2-5 
    library that can create and read several streaming archive formats (mingw-w64)
<br/>mingw/<b>mingw-w64-libart_lgpl</b> 2.3.19-1
    Library for high-performance 2D graphics (mingw-w64)
<br/>mingw/<b>mingw-w64-libass</b> 0.12.1-1 
    A portable library for SSA/ASS subtitles rendering (mingw-w64)
<br/>mingw/<b>mingw-w64-libassuan</b> 2.2.0-1
    A IPC library used by some GnuPG related software (mingw-w64)
<br/>mingw/<b>mingw-w64-libatomic_ops</b> 7.4.2-1 
    Provides semi-portable access to hardware provided atomic memory operations
<br/>mingw/<b>mingw-w64-libbluray</b> 0.7.0-1 
    Library to access Blu-Ray disks for video playback (mingw-w64)
<br/>mingw/<b>mingw-w64-libcaca</b> 0.99.beta19-1 
    Color AsCii Art library (mingw-w64)
<br/>mingw/<b>mingw-w64-libcddb</b> 1.3.2-2 
    Library that implements the different protocols (CDDBP, HTTP, SMTP) to access data on a CDDB server (e.g. http://freedb.org).
<br/>mingw/<b>mingw-w64-libcdio</b> 0.93-1 
    GNU Compact Disc Input and Control Library
<br/>mingw/<b>mingw-w64-libcdr</b> 0.1.1-2 
    CorelDraw file format importer library for LibreOffice (mingw-w64)
<br/>mingw/<b>mingw-w64-libchamplain</b> 0.12.10-1
    C library providing ClutterActor to display maps (mingw-w64)
<br/>mingw/<b>mingw-w64-libconfig</b> 1.4.9-1
    C/C++ Configuration File Library (mingw-w64)
<br/>mingw/<b>mingw-w64-libcroco</b> 0.6.8-2 
    A CSS parsing library (mingw-w64)
<br/>mingw/<b>mingw-w64-libdca-svn</b> r91-1 
    Free library for decoding DTS Coherent Acoustics streams (mingw-w64)
<br/>mingw/<b>mingw-w64-libdvbpsi</b> 1.1.2-1 
    A library designed for decoding and generation of MPEG TS and DVB PSI tables (mingw-w64)
<br/>mingw/<b>mingw-w64-libdvdcss</b> 1.3.0-1 
    Portable abstraction library for DVD decryption (mingw-w64)
<br/>mingw/<b>mingw-w64-libdvdnav</b> 5.0.1-1 
    The library for xine-dvdnav plugin (mingw-w64)
<br/>mingw/<b>mingw-w64-libdvdread</b> 5.0.0-1 
    Provides a simple foundation for reading DVD video disks (mingw-w64)
<br/>mingw/<b>mingw-w64-libebml</b> 1.3.1-1 (mingw-w64-x86_64) 
    Extensible Binary Meta Language library (mingw-w64)
<br/>mingw/<b>mingw-w64-libelf</b> 0.8.13-1 (mingw-w64-x86_64)
    ELF object file access library (mingw-w64)
<br/>mingw/<b>mingw-w64-libepoxy</b> 1.2-1 
    A library for handling OpenGL function pointer management for you. (mingw-w64)
<br/>mingw/<b>mingw-w64-libevent</b> 2.0.22-1
    An event notification library
<br/>mingw/<b>mingw-w64-libexif</b> 0.6.21-2 
    A library to parse an EXIF file and read the data from those tags (mingw-w64)
<br/>mingw/<b>mingw-w64-libfbclient</b> 2.5.2.26540-1
    Firebird client libraries (mingw-w64)
<br/>mingw/<b>mingw-w64-libffi</b> 3.2.1-2 (mingw-w64-x86_64) 
    A portable, high level programming interface to various calling conventions (mingw-w64)
<br/>mingw/<b>mingw-w64-libfreexl</b> 1.0.0g-4 
    Library to extract valid data from within an Excel (.xls) spreadsheet
<br/>mingw/<b>mingw-w64-libgadu</b> 1.12.0-1 (mingw-w64-x86_64) 
    This library implements the client side of the Gadu-Gadu protocol (mingw-w64)
<br/>mingw/<b>mingw-w64-libgcrypt</b> 1.6.3-1 (mingw-w64-x86_64) 
    General purpose cryptographic library based on the code from GnuPG (mingw-w64)
<br/>mingw/<b>mingw-w64-libgda</b> 5.2.2-1
    Data abstraction library based on GLib (mingw-w64)
<br/>mingw/<b>mingw-w64-libgdata</b> 0.16.1-1
    Library for accessing GData webservices (mingw-w64)
<br/>mingw/<b>mingw-w64-libgee</b> 0.18.0-1
    A collection library providing GObject-based interfaces and classes for commonly used data structures (mingw-w64)
<br/>mingw/<b>mingw-w64-libgeotiff</b> 1.4.0-1 (mingw-w64-x86_64)
    Cartographic projection software (PROJ.4) (mingw-w64)
<br/>mingw/<b>mingw-w64-libgit2</b> 0.22.2-1 
    A linkable library for Git (mingw-w64)
<br/>mingw/<b>mingw-w64-libgit2-glib</b> 0.22.2-1 
    A glib wrapper library around the libgit2 git access library (mingw-w64)
<br/>mingw/<b>mingw-w64-libglade</b> 2.6.4-3 
    Allows you to load glade interface files in a program at runtime (mingw-w64)
<br/>mingw/<b>mingw-w64-libgme</b> 0.6.0-1 
    Video game music file emulation/playback library (mingw-w64)
<br/>mingw/<b>mingw-w64-libgnomecanvas</b> 2.30.3-1 (mingw-w64-x86_64)
    The GNOME canvas library
<br/>mingw/<b>mingw-w64-libgnurx</b> 2.5.1-2
    libgnurx (mingw-w64)
<br/>mingw/<b>mingw-w64-libgoom2</b> 2k4-1 (mingw-w64-x86_64) 
    Shared library part of the Goom visualization plugin (mingw-w64)
<br/>mingw/<b>mingw-w64-libgpg-error</b> 1.18-1 (mingw-w64-x86_64) 
    Support library for libgcrypt (mingw-w64)
<br/>mingw/<b>mingw-w64-libgsf</b> 1.14.32-1
    An extensible I/O abstraction library for dealing with structured file formats (mingw-w64)
<br/>mingw/<b>mingw-w64-libguess</b> 1.2-1
    High-speed character set detection library (mingw-w64)
<br/>mingw/<b>mingw-w64-libgusb</b> 0.2.4-1
    GLib wrapper around libusb1 (mingw-w64)
<br/>mingw/<b>mingw-w64-libgweather</b> 3.16.0-1
    GWeather shared library (mingw-w64)
<br/>mingw/<b>mingw-w64-libgxps</b> 0.2.2-1
    A library to handling and rendering XPS documents (mingw-w64)
<br/>mingw/<b>mingw-w64-libical</b> 1.0.0-2
    An Open Source implementation of the iCalendar protocols and protocol data units (mingw-w64)
<br/>mingw/<b>mingw-w64-libiconv</b> 1.14-3 (mingw-w64-x86_64) 
    Libiconv is a conversion library
<br/>mingw/<b>mingw-w64-libid3tag</b> 0.15.1b-1 (mingw-w64-x86_64)
    Library for id3 tagging (mingw-w64)
<br/>mingw/<b>mingw-w64-libidn</b> 1.30-1 
    Implementation of the Stringprep, Punycode and IDNA specifications (mingw-w64)
<br/>mingw/<b>mingw-w64-libimobiledevice</b> 1.1.7-2 (mingw-w64-x86_64 xdev) 
    A cross-platform protocol library to communicate with iOS devices (mingw-w64)
<br/>mingw/<b>mingw-w64-libjpeg-turbo</b> 1.4.0-2 (mingw-w64-x86_64) 
    JPEG image codec with accelerated baseline compression and decompression (mingw-w64)
<br/>mingw/<b>mingw-w64-libksba</b> 1.3.1-1 (mingw-w64-x86_64)
    A CMS and X.509 access library (mingw-w64)
<br/>mingw/<b>mingw-w64-liblastfm</b> 1.0.9-1
    A Qt C++ library for the Last.fm webservices http://www.last.fm
<br/>mingw/<b>mingw-w64-liblastfm-qt4</b> 1.0.8-1
    A Qt C++ library for the Last.fm webservices http://www.last.fm
<br/>mingw/<b>mingw-w64-liblqr</b> 0.4.2-2 
    A seam-carving C/C++ library called Liquid Rescale (mingw-w64)
<br/>mingw/<b>mingw-w64-libmad</b> 0.15.1b-1 
    A high-quality MPEG audio decoder
<br/>mingw/<b>mingw-w64-libmangle-git</b> 4.0.0.4328.a913346-1 (mingw-w64-x86_64-toolchain mingw-w64-x86_64) 
    MinGW-w64 libmangle
<br/>mingw/<b>mingw-w64-libmariadbclient</b> 2.1.0-1 
    MariaDB client libraries (mingw-w64)
<br/>mingw/<b>mingw-w64-libmatroska</b> 1.4.2-1 (mingw-w64-x86_64) 
    Matroska library (mingw-w64)
<br/>mingw/<b>mingw-w64-libmaxminddb</b> 1.0.3-1
    C library for reading MaxMind DB files, including the GeoIP2 databases from MaxMind (mingw-w64)
<br/>mingw/<b>mingw-w64-libmimic</b> 1.0.4-1
    An open source video encoding/decoding library for Mimic V2.x (mingw-w64)
<br/>mingw/<b>mingw-w64-libmng</b> 2.0.2-1 
    Simple, small, C++ XML parser that can be easily integrated into other programs (mingw-w64)
<br/>mingw/<b>mingw-w64-libmodplug</b> 0.8.8.5-2 
    A MOD playing library (mingw-w64)
<br/>mingw/<b>mingw-w64-libmongoose-git</b> r1767.2ff2c36-1
    Embedded web server for C/C++ (mingw-w64)
<br/>mingw/<b>mingw-w64-libmowgli</b> 2.0.0-2
    Performance and usability-oriented extensions to C (mingw-w64)
<br/>mingw/<b>mingw-w64-libmpcdec</b> 1.2.6-1 
    Musepack decoding library (mingw-w64)
<br/>mingw/<b>mingw-w64-libmpeg2-svn</b> r1206-1 
    Library for decoding MPEG-1 and MPEG-2 video streams (mingw-w64)
<br/>mingw/<b>mingw-w64-libmtp</b> 1.1.8-1
    Library implementation of the Media Transfer Protocol
<br/>mingw/<b>mingw-w64-libnice</b> 0.1.10-1 
    An implementation of the IETF's draft ICE (for p2p UDP data streams) (mingw-w64)
<br/>mingw/<b>mingw-w64-libnotify</b> 0.7.6-1
    Desktop notification library (mingw-w64)
<br/>mingw/<b>mingw-w64-libntlm</b> 1.4-1 
    Library that implement Microsoft's NTLM authentication (mingw-w64)
<br/>mingw/<b>mingw-w64-liboauth</b> 1.0.3-2
    liboauth is a collection of POSIX-c functions implementing the OAuth Core RFC 5849 standard (mingw-w64)
<br/>mingw/<b>mingw-w64-libogg</b> 1.3.2-1 
    Ogg bitstream and framing library (mingw-w64)
<br/>mingw/<b>mingw-w64-libosmpbf-git</b> 1.3.3.10.g3730430-1
    A library to support OpenStreetMap's protocolbuffer binary .pbf format (mingw-w64)
<br/>mingw/<b>mingw-w64-libotr</b> 4.0.0-2
    Off-the-Record Messaging Library and Toolkit (mingw-w64)
<br/>mingw/<b>mingw-w64-libpeas</b> 1.14.0-1 
    A GObject-based plugins engine (mingw-w64)
<br/>mingw/<b>mingw-w64-libplist</b> 1.12-2 (mingw-w64-x86_64 xdev) 
    A library to handle Apple Property List format in binary or XML (mingw-w64)
<br/>mingw/<b>mingw-w64-libpng</b> 1.6.17-1 (mingw-w64-x86_64) 
    A collection of routines used to create PNG format graphics (mingw-w64)
<br/>mingw/<b>mingw-w64-libproxy</b> 0.4.11-1 
    A library that provides automatic proxy configuration management (mingw-w64)
<br/>mingw/<b>mingw-w64-librescl</b> 0.2.1-1 (mingw-w64-x86_64)
    Reader/Writer SCL IEC 61850-6 files version 0.2.1 (mingw-w64)
<br/>mingw/<b>mingw-w64-librest</b> 0.7.93-1
    Helper library for RESTful services (mingw-w64)
<br/>mingw/<b>mingw-w64-librevenge</b> 0.0.1-1 
    library for REVerses ENGineered formats filters (mingw-w64)
<br/>mingw/<b>mingw-w64-librocket-git</b> r494.761d05a-1 
    The HTML/CSS User Interface Library (mingw-w64)
<br/>mingw/<b>mingw-w64-librsvg</b> 2.40.6-1 
    A SVG viewing library (mingw-w64)
<br/>mingw/<b>mingw-w64-libsamplerate</b> 0.1.8-1 
    Secret Rabbit Code (aka libsamplerate) is a Sample Rate Converter for audio.
<br/>mingw/<b>mingw-w64-libshout</b> 2.3.1-1 
    Library for accessing a shoutcast/icecast server (mingw-w64)
<br/>mingw/<b>mingw-w64-libsigc++</b> 2.4.1-1 
    Libsigc++ implements a full callback system for use in widget libraries - V2 (mingw-w64)
<br/>mingw/<b>mingw-w64-libsmallchange-hg</b> r1055.b646e0d1ccc1-1
    A collection of extensions to the Open Inventor API (mingw-w64)
<br/>mingw/<b>mingw-w64-libsndfile</b> 1.0.25-2 
    A C library for reading and writing files containing sampled sound (mingw-w64)
<br/>mingw/<b>mingw-w64-libsodium</b> 1.0.1-1 
    P(ortable|ackageable) NaCl-based crypto library (mingw-w64)
<br/>mingw/<b>mingw-w64-libsoup</b> 2.50.0-1 
    HTTP client/server library (mingw-w64)
<br/>mingw/<b>mingw-w64-libspatialite</b> 4.2.0-3
    SQLite extension to support spatial data types and operations (mingw-w64)
<br/>mingw/<b>mingw-w64-libspectre</b> 0.2.7-1
    libspectre is a small library for rendering PostScript documents. It provides a convenient easy to use API for handling and rendering PostScript documents. (mingw-w64)
<br/>mingw/<b>mingw-w64-libspiro</b> 20071029-2 
    Simplifies the drawing of beautiful curves (mingw-w64)
<br/>mingw/<b>mingw-w64-libssh</b> 0.6.4-1 (mingw-w64-x86_64) 
    Library for accessing ssh client services through C libraries (mingw-w64)
<br/>mingw/<b>mingw-w64-libssh2</b> 1.5.0-1 (mingw-w64-x86_64) 
    A library implementing the SSH2 protocol as defined by Internet Drafts (mingw-w64)
<br/>mingw/<b>mingw-w64-libsystre</b> 1.0.1-1 
    Wrapper library around TRE that provides POSIX API (mingw-w64)
<br/>mingw/<b>mingw-w64-libtasn1</b> 4.4-1 
    Implementation of the Stringprep, Punycode and IDNA specifications (mingw-w64)
<br/>mingw/<b>mingw-w64-libtheora</b> 1.1.1-2 
    An open video codec developed by the Xiph.org (mingw-w64)
<br/>mingw/<b>mingw-w64-libtiff</b> 4.0.3-4 
    Library for manipulation of TIFF images (mingw-w64)
<br/>mingw/<b>mingw-w64-libtommath</b> 0.42.0-1 (mingw-w64-x86_64) 
    Highly optimized and portable routines for integer based number theoretic applications (mingw-w64)
<br/>mingw/<b>mingw-w64-libtool</b> 2.4.6-1 (mingw-w64-x86_64) 
    A system independent dlopen wrapper for GNU libtool (mingw-w64)
<br/>mingw/<b>mingw-w64-libtorrent-rasterbar</b> 0.16.17-1
    libtorrent is a feature complete C++ bittorrent implementation focusing on efficiency and scalability.
<br/>mingw/<b>mingw-w64-libtre-git</b> r122.c2f5d13-3 
    The approximate regex matching library and agrep command line tool (mingw-w64)
<br/>mingw/<b>mingw-w64-libunistring</b> 0.9.5-1
    Library for manipulating Unicode strings and C strings. (mingw-w64)
<br/>mingw/<b>mingw-w64-libusb</b> 1.0.19-2 
    Library that provides generic access to USB devices'. (mingw-w64)
<br/>mingw/<b>mingw-w64-libusb-compat-git</b> r60.072a5e4-1
    libusb provides generic access to USB devices (mingw-w64)
<br/>mingw/<b>mingw-w64-libusbmuxd</b> 1.0.10-2 (mingw-w64-x86_64 xdev) 
    A client library to multiplex connections from and to iOS devices (mingw-w64)
<br/>mingw/<b>mingw-w64-libuv</b> 1.2.1-1 
    A new platform layer for Node.JS (mingw-w64)
<br/>mingw/<b>mingw-w64-libview</b> 0.6.6-2
    VMware's Incredibly Exciting Widgets (mingw-w64)
<br/>mingw/<b>mingw-w64-libvmime-git</b> r1024.3848556-2
    An open source solution for working with MIME messages and Internet messaging services like IMAP, POP or SMTP (mingw-w64)
<br/>mingw/<b>mingw-w64-libvorbis</b> 1.3.4-1 
    Vorbis codec library (mingw-w64)
<br/>mingw/<b>mingw-w64-libvorbisidec-svn</b> r19222-1 (mingw-w64-x86_64) 
    Integer-only Ogg Vorbis decoder, AKA \"tremor\" (mingw-w64)
<br/>mingw/<b>mingw-w64-libvpx</b> 1.4.0-1 
    The VP8 Codec SDK (mingw-w64)
<br/>mingw/<b>mingw-w64-libwebp</b> 0.4.2-1 
    the WebP library. Includes conversion tools. (mingw-w64)
<br/>mingw/<b>mingw-w64-libwebsockets</b> 1.3-1 
    A lightweight pure C library for websockets (mingw-w64)
<br/>mingw/<b>mingw-w64-libwebsockets-git</b> 1.23.745.5b2d032-1
    A lightweight pure C library for websockets (mingw-w64)
<br/>mingw/<b>mingw-w64-libwinpthread-git</b> 5.0.0.4455.32db221-1 (mingw-w64-x86_64-toolchain mingw-w64-x86_64) 
    MinGW-w64 winpthreads library
<br/>mingw/<b>mingw-w64-libwmf</b> 0.2.8.4-2 
    Library for Converting Metafile Images (mingw-w64)
<br/>mingw/<b>mingw-w64-libwpd</b> 0.10.0-1 
    Library for Importing WordPerfect (tm) Documents (mingw-w64)
<br/>mingw/<b>mingw-w64-libwpg</b> 0.3.0-1 
    Library to read and parse graphics in WordPerfect Graphics format (mingw-w64)
<br/>mingw/<b>mingw-w64-libxml++</b> 2.38.0-1 (mingw-w64-x86_64)
    C++ wrapper for the libxml2 XML parser library (mingw-w64)
<br/>mingw/<b>mingw-w64-libxml2</b> 2.9.2-5 (mingw-w64-x86_64) 
    XML parsing library, version 2 (mingw-w64)
<br/>mingw/<b>mingw-w64-libxslt</b> 1.1.28-4 (mingw-w64-x86_64) 
    XML stylesheet transformation library (mingw-w64)
<br/>mingw/<b>mingw-w64-libyaml</b> 0.1.4-2 
    YAML 1.1 library (mingw-w64)
<br/>mingw/<b>mingw-w64-libzip</b> 0.11.2-1
    A C library for reading, creating, and modifying zip archives (mingw-w64)
<br/>mingw/<b>mingw-w64-live-media</b> 2014.10.21-1
    A set of C++ libraries for multimedia streaming (mingw-w64)
<br/>mingw/<b>mingw-w64-llvm</b> 3.5.1-1 
    Low Level Virtual Machine
<br/>mingw/<b>mingw-w64-llvm-cern-git</b> r106460-1
    Low Level Virtual Machine
<br/>mingw/<b>mingw-w64-llvm-svn</b> r217860-1
    Low Level Virtual Machine
<br/>mingw/<b>mingw-w64-lua</b> 5.3.0-1 
    A powerful light-weight programming language designed for extending applications. (mingw-w64)
<br/>mingw/<b>mingw-w64-lua51</b> 5.1.5-3
    A powerful light-weight programming language designed for extending applications. Version 5.1.x. (mingw-w64)
<br/>mingw/<b>mingw-w64-luabind-git</b> 0.9.1.142.g2b904b3-1
    A library that helps you create bindings between C++ and Lua (mingw-w64)
<br/>mingw/<b>mingw-w64-luajit-git</b> v2.0.3.40.g3f2e4ec-1
    Just-in-time compiler and drop-in replacement for Lua 5.1 (mingw-w64)
<br/>mingw/<b>mingw-w64-lz4</b> 1.6.0.r452-1
    Very fast lossless compression algorithm (mingw-w64)
<br/>mingw/<b>mingw-w64-lzo2</b> 2.09-1 
    Portable lossless data compression library (mingw-w64)
<br/>mingw/<b>mingw-w64-m4</b> 1.4.17-1
    The GNU macro processor (mingw-w64)
<br/>mingw/<b>mingw-w64-make</b> 4.0.2289.432cb65-1 (mingw-w64-x86_64-toolchain) 
    GNU make utility to maintain groups of programs
<br/>mingw/<b>mingw-w64-mcpp</b> 2.7.2-1
    Matsui's CPP implementation precisely conformed to standards (mingw-w64)
<br/>mingw/<b>mingw-w64-meanwhile</b> 1.0.2-2
    Meanwhile libraries (mingw64)
<br/>mingw/<b>mingw-w64-meld3</b> 3.13.0-1 
    Visual diff and merge tool (mingw-w64)
<br/>mingw/<b>mingw-w64-memphis</b> 0.2.3-1
    A map-rendering library for OpenStreetMap (mingw-w64)
<br/>mingw/<b>mingw-w64-mesa</b> 10.5.3-1
    Open-source implementation of the OpenGL specification (mingw-w64)
<br/>mingw/<b>mingw-w64-mhook</b> r7.a159eed-1
    An API hooking library (mingw-w64)
<br/>mingw/<b>mingw-w64-miniupnpc</b> 1.9.20150206-1
    A small UPnP client library/tool to access Internet Gateway Devices (mingw-w64)
<br/>mingw/<b>mingw-w64-mpc</b> 1.0.3-1 (mingw-w64-x86_64) 
    Multiple precision complex arithmetic library (mingw-w64)
<br/>mingw/<b>mingw-w64-mpfr</b> 3.1.2.p11-1 (mingw-w64-x86_64) 
    Multiple-precision floating-point library
<br/>mingw/<b>mingw-w64-mpg123</b> 1.22.1-1 
    A console based real time MPEG Audio Player for Layer 1, 2 and 3 (mingw-w64)
<br/>mingw/<b>mingw-w64-mpv</b> 0.8.0-1
    Video player based on MPlayer/mplayer2 (mingw-w64)
<br/>mingw/<b>mingw-w64-nanovg-git</b> r252.90862ce-1 
    Small antialiased vector graphics rendering library for OpenGL
<br/>mingw/<b>mingw-w64-nasm</b> 2.11.08-1
    An 80x86 assembler designed for portability and modularity (mingw-w64)
<br/>mingw/<b>mingw-w64-ncurses</b> 5.9.20150321-1 
    System V Release 4.0 curses emulation library
<br/>mingw/<b>mingw-w64-nettle</b> 3.1-2 
    A low-level cryptographic library (mingw-w64)
<br/>mingw/<b>mingw-w64-ninja</b> 1.5.3-1 
    Ninja is a small build system with a focus on speed (mingw-w64)
<br/>mingw/<b>mingw-w64-nodejs</b> 0.10.32-4 
    Evented I/O for V8 javascript (mingw-w64)
<br/>mingw/<b>mingw-w64-nspr</b> 4.10.8-1 
    Netscape Portable Runtime (mingw-w64)
<br/>mingw/<b>mingw-w64-nss</b> 3.17.4-1 
    Mozilla Network Security Services (mingw-w64)
<br/>mingw/<b>mingw-w64-ntldd-git</b> r6.fbb52f1-1
    Tracks dependencides in Windows PE binaries (mingw-w64)
<br/>mingw/<b>mingw-w64-nutsnbolts-hg</b> r153.b92bf74dc55f-1
    Extension library for Coin that contains various nuts and bolts (mingw-w64)
<br/>mingw/<b>mingw-w64-nvidia-cg-toolkit</b> 3.1-2
    NVIDIA Cg libraries (mingw-w64)
<br/>mingw/<b>mingw-w64-ocaml</b> 4.02.1-4
    An industrial strength programming language supporting functional, imperative and object-oriented styles (mingw-w64)
<br/>mingw/<b>mingw-w64-ocaml-camlp4</b> 4.02.1-2
    Pre-Processor-Pretty-Printer for OCaml (mingw-w64)
<br/>mingw/<b>mingw-w64-ocaml-findlib</b> 1.5.5-1
    OCaml library manager (mingw-w64)
<br/>mingw/<b>mingw-w64-octopi-git</b> r612.784de21-1 
    a powerful Pacman frontend using Qt libs
<br/>mingw/<b>mingw-w64-ogre3d-hg</b> 2.0.0.r7529.1ea8087257eb-1
    A cross-platform 3D game engine (mingw-w64)
<br/>mingw/<b>mingw-w64-ogreassimp-hg</b> r33.ebcbefe6e081-3
    Open Asset Import Library (Assimp) Loader for Ogre3D (mingw-w64)
<br/>mingw/<b>mingw-w64-ois</b> 1.3-2
    Object Oriented Input System (mingw-w64)
<br/>mingw/<b>mingw-w64-ois-git</b> 1.4.0.65.b3e596c-1
    Object Oriented Input System (mingw-w64)
<br/>mingw/<b>mingw-w64-oniguruma</b> 5.9.5-2 (mingw-w64-x86_64)
    A regular expressions library (mingw-w64)
<br/>mingw/<b>mingw-w64-openal</b> 1.16.0-2 
    OpenAL audio library for use with opengl (mingw-w64)
<br/>mingw/<b>mingw-w64-openblas</b> 0.2.14-1 (mingw-w64-x86_64) 
    An optimized BLAS library based on GotoBLAS2 1.13 BSD, providing optimized blas, lapack, and cblas. (mingw-w64)
<br/>mingw/<b>mingw-w64-openblas-git</b> r1242.f1b9a4a-1 (mingw-w64-x86_64)
    OpenBLAS is an optimized BLAS library (mingw-w64)
<br/>mingw/<b>mingw-w64-opencl-headers</b> 2.0.0-1
    OpenCL (Open Computing Language) header files (mingw-w64)
<br/>mingw/<b>mingw-w64-opencollada-git</b> r1079.2effbf1-1 
    Stream based reader and writer library for COLLADA files (mingw-w64)
<br/>mingw/<b>mingw-w64-opencolorio-git</b> 701.a557a85-1 
    A color management framework for visual effects and animation (mingw-w64)
<br/>mingw/<b>mingw-w64-opencore-amr</b> 0.1.3-2 
    Open source implementation of the Adaptive Multi Rate (AMR) speech codec (mingw-w64)
<br/>mingw/<b>mingw-w64-opencsg</b> 1.4.0-1
    Library for image-based CSG rendering using OpenGL (mingw-w64)
<br/>mingw/<b>mingw-w64-opencv</b> 2.4.11-2 
    Open Source Computer Vision Library (mingw-w64)
<br/>mingw/<b>mingw-w64-openexr</b> 2.2.0-1 
    Openexr library for EXR images (mingw-w64)
<br/>mingw/<b>mingw-w64-openimageio</b> 1.5.12-1 
    A library for reading and writing images, including classes, utilities, and applications (mingw-w64)
<br/>mingw/<b>mingw-w64-openjpeg</b> 1.5.2-2 
    An open source JPEG 2000 codec (mingw-w64)
<br/>mingw/<b>mingw-w64-openjpeg2</b> 2.1.0-2 
    An open source JPEG 2000 codec (mingw-w64)
<br/>mingw/<b>mingw-w64-openldap</b> 2.4.40-1
    OpenLDAP Software is an open source implementation of the Lightweight Directory Access Protocol (only client) (mingw-w64)
<br/>mingw/<b>mingw-w64-openocd-git</b> 0.8.0.r268.ga9c90a0-1
    OpenOCD - Open On-Chip Debugger (mingw-w64)
<br/>mingw/<b>mingw-w64-openscad-git</b> r4930.0bf2d4e-1
    The programmers solid 3D CAD modeller (mingw-w64)
<br/>mingw/<b>mingw-w64-openshadinglanguage</b> 1.5.12-1
    Advanced shading language for production GI renderers (mingw-w64)
<br/>mingw/<b>mingw-w64-openshadinglanguage-git</b> 1.6.1507.9eef4a8-1 
    Advanced shading language for production GI renderers (mingw-w64)
<br/>mingw/<b>mingw-w64-openssl</b> 1.0.2.a-1 
    The Open Source toolkit for Secure Sockets Layer and Transport Layer Security (mingw-w64)
<br/>mingw/<b>mingw-w64-optipng</b> 0.7.5-1
    Compresses PNG files to a smaller size, without losing any information (mingw-w64)
<br/>mingw/<b>mingw-w64-opus</b> 1.1-2 
    Codec designed for interactive speech and audio transmission over the Internet (mingw-w64)
<br/>mingw/<b>mingw-w64-opus-tools</b> 0.1.9-1
    Collection of tools for Opus audio codec (mingw-w64)
<br/>mingw/<b>mingw-w64-opusfile</b> 0.6-1
    Library for opening, seeking, and decoding .opus files (mingw-w64)
<br/>mingw/<b>mingw-w64-orc</b> 0.4.22-1 
    The Oild Runtime Compiler (mingw-w64)
<br/>mingw/<b>mingw-w64-osgbullet-debug-svn</b> r385-1
    Bullet physics and OpenSceneGraph integration (mingw-w64)
<br/>mingw/<b>mingw-w64-osgbullet-svn</b> r385-1
    Bullet physics and OpenSceneGraph integration (mingw-w64)
<br/>mingw/<b>mingw-w64-osgocean-debug-svn</b> r258-2
    An ocean rendering nodekit for OpenSceneGraph (mingw-w64)
<br/>mingw/<b>mingw-w64-osgocean-svn</b> r258-2
    An ocean rendering nodekit for OpenSceneGraph (mingw-w64)
<br/>mingw/<b>mingw-w64-osgworks-debug-svn</b> 3.1.0.565-1
    A toolkit for OpenSceneGraph applications. (mingw-w64)
<br/>mingw/<b>mingw-w64-osgworks-svn</b> 3.1.0.565-1
    A toolkit for OpenSceneGraph applications. (mingw-w64)
<br/>mingw/<b>mingw-w64-osmgpsmap-git</b> r439.834bed2-1
    A Gtk+ Widget for Displaying OpenStreetMap tiles
<br/>mingw/<b>mingw-w64-p11-kit</b> 0.23.1-2 
    Library to work with PKCS#11 modules
<br/>mingw/<b>mingw-w64-pango</b> 1.36.8-2 
    A library for layout and rendering of text (mingw-w64)
<br/>mingw/<b>mingw-w64-pangomm</b> 2.36.0-0 
    C++ bindings for pango (mingw-w64)
<br/>mingw/<b>mingw-w64-pcre</b> 8.36-1 
    A library that implements Perl 5-style regular expressions (mingw-w64)
<br/>mingw/<b>mingw-w64-perl</b> 5.20.2-1
    A highly capable, feature-rich programming language (mingw-w64)
<br/>mingw/<b>mingw-w64-phodav</b> 2.0-1
    A WebDAV server using libsoup (mingw-w64)
<br/>mingw/<b>mingw-w64-physfs</b> 2.0.3-1
    A library to provide abstract access to various archives (mingw-w64)
<br/>mingw/<b>mingw-w64-physfs-hg</b> r1345.29ab417d9453-2
    A library to provide abstract access to various archives (development version)
<br/>mingw/<b>mingw-w64-pidgin-hg</b> r36348.9d62816617b9-1 
    Multi-protocol instant messaging client (mingw-w64)
<br/>mingw/<b>mingw-w64-pitivi-git</b> 0.93.6004.23cd814-1
    Free, intuitive and featureful movie editor for the Linux desktop. (mingw-w64)
<br/>mingw/<b>mingw-w64-pixman</b> 0.32.6-2 
    The pixel-manipulation library for X and cairo (mingw-w64)
<br/>mingw/<b>mingw-w64-pkg-config</b> 0.28-2 
    A system for managing library compile/link flags (mingw-w64)
<br/>mingw/<b>mingw-w64-pkgconf</b> 0.9.7-2
    pkg-config compatible utility which does not depend on glib
<br/>mingw/<b>mingw-w64-plplot</b> 5.10.0-1
    Scientific plotting software (mingw-w64)
<br/>mingw/<b>mingw-w64-pngcrush</b> 1.7.85-1
    A tool for optimizing the compression of PNG files (mingw-w64)
<br/>mingw/<b>mingw-w64-pngnq</b> 1.1-1
    Pngnq is a tool for quantizing PNG images in RGBA format
<br/>mingw/<b>mingw-w64-poco</b> 1.6.0-1
    POrtable COmponents C++ Libraries (mingw-w64)
<br/>mingw/<b>mingw-w64-poppler</b> 0.32.0-2 
    PDF rendering library based on xpdf 3.0 (mingw-w64)
<br/>mingw/<b>mingw-w64-poppler-data</b> 0.4.7-1 
    Encoding data for the poppler PDF rendering library
<br/>mingw/<b>mingw-w64-poppler-qt4</b> 0.26.3-1
    PDF rendering library based on xpdf 3.0 (mingw-w64)
<br/>mingw/<b>mingw-w64-popt</b> 1.10.7-3 
    C library for parsing command line parameters(mingw-w64)
<br/>mingw/<b>mingw-w64-port-scanner</b> 1.3-1 
    A multi threaded TCP port scanner from SecPoint.com (mingw-w64)
<br/>mingw/<b>mingw-w64-portablexdr</b> 4.9.1-1 (mingw-w64-x86_64)
    PortableXDR / RPC Library (mingw-w64)
<br/>mingw/<b>mingw-w64-portaudio</b> 19_20140130-1 
    A free, cross-platform, open source, audio I/O library. (mingw-w64)
<br/>mingw/<b>mingw-w64-postgresql</b> 9.4.1-1 
    Libraries for use with PostgreSQL (mingw-w64)
<br/>mingw/<b>mingw-w64-postr</b> 0.13-1
    Upload photos to Flickr (mingw-w64)
<br/>mingw/<b>mingw-w64-premake</b> 4.3-1
    A build configuration tool. Describe your build using Lua and generate the project files for your specific toolset.
<br/>mingw/<b>mingw-w64-profit-hg</b> r116.8046667edf0e-1
    Open Flight file format support library (mingw-w64)
<br/>mingw/<b>mingw-w64-proj</b> 4.8.0-1 (mingw-w64-x86_64)
    Cartographic projection software (PROJ.4) (mingw-w64)
<br/>mingw/<b>mingw-w64-protobuf</b> 2.6.1-1 (mingw-w64-x86_64) 
    Protocol Buffers - Google's data interchange format (mingw-w64)
<br/>mingw/<b>mingw-w64-protobuf-c</b> 1.1.0-1 (mingw-w64-x86_64) 
    Protocol Buffers implementation in C (mingw-w64)
<br/>mingw/<b>mingw-w64-putty-ssh</b> 0.0-1 
    A wrapper around plink with some nice features (mingw-w64)
<br/>mingw/<b>mingw-w64-putty-svn</b> 0.63.r10285-1 
    A free telnet/SSH client (mingw-w64)
<br/>mingw/<b>mingw-w64-pygobject-devel</b> 3.16.0-1 (mingw-w64-x86_64) 
    Development files for the pygobject bindings
<br/>mingw/<b>mingw-w64-pygobject2-devel</b> 2.28.6-2 (mingw-w64-x86_64) 
    Development files for the pygobject bindings
<br/>mingw/<b>mingw-w64-pygtksourceview2</b> 2.10.1-1 (mingw-w64-x86_64)
    Python bindings for gtksourceview2 (mingw-w64)
<br/>mingw/<b>mingw-w64-pyqt4-common</b> 4.11.2-1
    Common PyQt files shared between python3-pyqt4 and python2-pyqt4
<br/>mingw/<b>mingw-w64-pyqt5-common</b> 5.4.1-1
    Common PyQt files shared between python3-pyqt5 and python2-pyqt5
<br/>mingw/<b>mingw-w64-python-lxml-docs</b> 3.4.2-1
    Python binding for the libxml2 and libxslt libraries (docs)
<br/>mingw/<b>mingw-w64-python-qscintilla-common</b> 2.8.4-1
    Common python qscintilla bindings files shared between python3-qscintilla and python2-qscintilla
<br/>mingw/<b>mingw-w64-python2</b> 2.7.9-2 
    A high-level scripting language (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-Pillow</b> 2.6.0-1 (mingw-w64-x86_64)
    Python Imaging Library (PIL) fork. Python2 version.
<br/>mingw/<b>mingw-w64-python2-beaker</b> 1.6.5-1 
    Caching and sessions WSGI middleware for use with web applications and stand-alone Python scripts and applications (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-beautifulsoup3</b> 3.2.1-1
    A Python HTML/XML parser designed for quick turnaround projects like screen-scraping (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-bsddb3</b> 6.1.0-1 
    Python bindings for Oracle Berkeley DB
<br/>mingw/<b>mingw-w64-python2-cairo</b> 1.10.0-1 
    Python2 bindings for the cairo graphics library (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-cjson</b> 1.1.0-1 
    Fast JSON encoder/decoder for Python (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-cssselect</b> 0.9.1-2
    A Python2 library that parses CSS3 Selectors and translates them to XPath 1.0
<br/>mingw/<b>mingw-w64-python2-cx_Freeze</b> 4.3.3-2
    Python package for freezing scripts into executables (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-dateutil</b> 2.2-2
    Provides powerful extensions to the standard datetime module (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-docutils</b> 0.12-2 
    Set of tools for processing plaintext docs into formats such as HTML, XML, or LaTeX (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-gobject</b> 3.16.0-1 (mingw-w64-x86_64) 
    Python 2 bindings for GObject2 (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-gobject2</b> 2.28.6-2 (mingw-w64-x86_64) 
    Python 2 bindings for GObject2 (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-h5py</b> 2.3.1-1
    General-purpose Python bindings for the HDF5 library. (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-httplib2</b> 0.9-2
    Comprehensive HTTP client library, supporting many features (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-icu</b> 1.8-3
    Python extension wrapping the ICU C++ API
<br/>mingw/<b>mingw-w64-python2-ipython</b> 2.3.1-1
    An enhanced Interactive Python shell.
<br/>mingw/<b>mingw-w64-python2-jinja</b> 2.7.2-2
    A simple pythonic template language written in Python (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-lhafile</b> 0.1.0fs4-2
    LHA module for Python (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-lxml</b> 3.4.2-1
    Python2 binding for the libxml2 and libxslt libraries
<br/>mingw/<b>mingw-w64-python2-mako</b> 1.0.1-2 (mingw-w64-x86_64) 
    A super-fast templating language that borrows the best ideas from the existing templating languages (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-markupsafe</b> 0.23-2 
    Implements a XML/HTML/XHTML Markup safe string for Python (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-matplotlib</b> 1.4.2-1
    A python plotting library, making publication quality plots (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-nose</b> 1.3.6-1 
    A discovery-based unittest extension (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-nuitka</b> 0.5.8-1
    Python to native compiler (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-numexpr</b> 2.4-1
    Fast numerical array expression evaluator for Python, NumPy, PyTables, pandas. (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-numpy</b> 1.9.2-1 
    Scientific tools for Python (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-pandas</b> 0.14.1-4
    Cross-section and time series data analysis toolkit. (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-patsy</b> 0.3.0-1
    A Python package for describing statistical models and for building design matrices (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-pip</b> 6.1.1-1
    An easy_install replacement for installing pypi python packages (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-pygments</b> 2.0.2-1 
    Python syntax highlighter (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-pygtk</b> 2.24.0-3 (mingw-w64-x86_64) 
    Python bindings for the GTK widget set (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-pyparsing</b> 2.0.2-1
    General parsing module for Python (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-pyqt4</b> 4.11.2-1
    A set of Python 2.x bindings for the Qt4 toolkit
<br/>mingw/<b>mingw-w64-python2-pyqt5</b> 5.4.1-1
    A set of Python 2.x bindings for the Qt5 toolkit
<br/>mingw/<b>mingw-w64-python2-pytz</b> 2014.7-1
    Cross platform time zone library for Python (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-qscintilla</b> 2.8.4-1
    Python 2.x bindings for QScintilla2
<br/>mingw/<b>mingw-w64-python2-reportlab</b> 3.0-2
    A proven industry-strength PDF generating solution (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-scipy</b> 0.14.0-2
    SciPy is open-source software for mathematics, science, and engineering. (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-setuptools</b> 12.0.5-1 
    Easily download, build, install, upgrade, and uninstall Python packages (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-sip</b> 4.16.6-1
    Python 2.x SIP bindings for C and C++ libraries
<br/>mingw/<b>mingw-w64-python2-six</b> 1.8.0-1
    Python 2 and 3 compatibility utilities (mingw-w64)
<br/>mingw/<b>mingw-w64-python2-sphinx</b> 1.2.3-2
    Python2 documentation generator
<br/>mingw/<b>mingw-w64-python2-statsmodels</b> 0.5.0-1
    Statistical computations and models for use with SciPy. (mingw-w64)
<br/>mingw/<b>mingw-w64-python3</b> 3.4.3-3 
    A high-level scripting language (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-Pillow</b> 2.6.0-1 (mingw-w64-x86_64)
    Python Imaging Library (PIL) fork. Python3 version (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-beaker</b> 1.6.5-1 
    Caching and sessions WSGI middleware for use with web applications and stand-alone Python scripts and applications (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-bsddb3</b> 6.1.0-1 
    Python bindings for Oracle Berkeley DB
<br/>mingw/<b>mingw-w64-python3-cairo</b> 1.10.0-3 
    Python2 bindings for the cairo graphics library (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-cssselect</b> 0.9.1-2
    A Python3 library that parses CSS3 Selectors and translates them to XPath 1.0
<br/>mingw/<b>mingw-w64-python3-cx_Freeze</b> 4.3.3-2
    Python package for freezing scripts into executables (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-dateutil</b> 2.2-2
    Provides powerful extensions to the standard datetime module (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-docutils</b> 0.12-2 
    Set of tools for processing plaintext docs into formats such as HTML, XML, or LaTeX (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-gobject</b> 3.16.0-1 (mingw-w64-x86_64) 
    Python 3 bindings for GObject2 (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-gobject2</b> 2.28.6-2 (mingw-w64-x86_64)
    Python 3 bindings for GObject2 (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-h5py</b> 2.3.1-1
    General-purpose Python bindings for the HDF5 library. (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-httplib2</b> 0.9-2
    Python3 binding for the libxml2 and libxslt libraries
<br/>mingw/<b>mingw-w64-python3-icu</b> 1.8-3
    Python extension wrapping the ICU C++ API
<br/>mingw/<b>mingw-w64-python3-ipython</b> 2.3.1-1
    An enhanced Interactive Python shell.
<br/>mingw/<b>mingw-w64-python3-jinja</b> 2.7.2-2 
    Python3 documentation generator
<br/>mingw/<b>mingw-w64-python3-lhafile</b> 0.1.0fs4-2
    LHA module for Python (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-lxml</b> 3.4.2-1
    Python3 binding for the libxml2 and libxslt libraries
<br/>mingw/<b>mingw-w64-python3-mako</b> 1.0.1-2 (mingw-w64-x86_64) 
    A super-fast templating language that borrows the best ideas from the existing templating languages (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-markupsafe</b> 0.23-2 
    Implements a XML/HTML/XHTML Markup safe string for Python (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-matplotlib</b> 1.4.2-1
    A python plotting library, making publication quality plots (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-nose</b> 1.3.6-1 
    A discovery-based unittest extension (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-nuitka</b> 0.5.8-1
    Python to native compiler (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-numexpr</b> 2.4-1
    Fast numerical array expression evaluator for Python, NumPy, PyTables, pandas. (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-numpy</b> 1.9.2-1 
    Scientific tools for Python (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-pandas</b> 0.14.1-4
    Cross-section and time series data analysis toolkit. (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-patsy</b> 0.3.0-1
    A Python package for describing statistical models and for building design matrices (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-pip</b> 6.1.1-1 
    An easy_install replacement for installing pypi python packages (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-pygments</b> 2.0.2-1 
    Python syntax highlighter (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-pyparsing</b> 2.0.2-1
    General parsing module for Python (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-pyqt4</b> 4.11.2-1
    A set of Python 3.x bindings for the Qt4 toolkit
<br/>mingw/<b>mingw-w64-python3-pyqt5</b> 5.4.1-1
    A set of Python 3.x bindings for the Qt5 toolkit
<br/>mingw/<b>mingw-w64-python3-pytz</b> 2014.7-1
    Cross platform time zone library for Python (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-qscintilla</b> 2.8.4-1
    Python 3.x bindings for QScintilla2
<br/>mingw/<b>mingw-w64-python3-reportlab</b> 3.0-2
    A proven industry-strength PDF generating solution (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-scipy</b> 0.14.0-2
    SciPy is open-source software for mathematics, science, and engineering. (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-setuptools</b> 12.0.5-1 
    Easily download, build, install, upgrade, and uninstall Python packages (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-sip</b> 4.16.6-1
    Python 3.x SIP bindings for C and C++ libraries
<br/>mingw/<b>mingw-w64-python3-six</b> 1.8.0-1
    Python 2 and 3 compatibility utilities (mingw-w64)
<br/>mingw/<b>mingw-w64-python3-sphinx</b> 1.2.3-2 
    Python3 documentation generator
<br/>mingw/<b>mingw-w64-python3-statsmodels</b> 0.5.0-1
    Statistical computations and models for use with SciPy. (mingw-w64)
<br/>mingw/<b>mingw-w64-qbs</b> 1.3.3-2 
    Qt Build Suite
<br/>mingw/<b>mingw-w64-qemu</b> 2.1.2-1
    A generic and open source processor emulator (mingw-w64)
<br/>mingw/<b>mingw-w64-qhull-git</b> r113.60d5581-2 (mingw-w64-x86_64) 
    A general dimension code for computing convex hulls and related structures (mingw-w64)
<br/>mingw/<b>mingw-w64-qjson-qt4</b> 0.8.1-1
    QJson is a qt-based library that maps JSON data to QVariant objects (mingw-w64)
<br/>mingw/<b>mingw-w64-qrupdate-svn</b> r28-2 (mingw-w64-x86_64) 
    qrupdate is a Fortran library for fast updates of QR and Cholesky decompositions.
<br/>mingw/<b>mingw-w64-qscintilla</b> 2.8.4-1 
    A port to Qt5 of Neil Hodgson's Scintilla C++ editor class
<br/>mingw/<b>mingw-w64-qt-creator</b> 3.3.2-2 
    Cross-patform IDE (mingw-w64)
<br/>mingw/<b>mingw-w64-qt-installer-framework-git</b> r2630.ce703ed-1 
    The Qt Installer Framework used for the Qt SDK installer
<br/>mingw/<b>mingw-w64-qt-solutions-git</b> r39.a558dc7-1
    Qt5 various components (mingw-w64)
<br/>mingw/<b>mingw-w64-qt4</b> 4.8.6-2 (mingw-w64-x86_64-qt4)
    
<br/>mingw/<b>mingw-w64-qt5</b> 5.4.1-3 (mingw-w64-x86_64-qt mingw-w64-x86_64-qt5) 
    A cross-platform application and UI framework (mingw-w64)
<br/>mingw/<b>mingw-w64-qt5-static</b> 5.4.1-3 (mingw-w64-x86_64-qt mingw-w64-x86_64-qt5) 
    A cross-platform application and UI framework (mingw-w64-static)
<br/>mingw/<b>mingw-w64-qtbinpatcher</b> 2.1.3-1 
    Patcher for Qt libraries (mingw-w64)
<br/>mingw/<b>mingw-w64-quarter-hg</b> r488.550ec597831a-1
    Light-weight glue library that provides seamless integration between Coin and Qt5 (mingw-w64)
<br/>mingw/<b>mingw-w64-qwt-qt4</b> 6.1.0-1
    Qt Widgets for Technical Applications
<br/>mingw/<b>mingw-w64-qwt-qt5</b> 6.1.2-1
    Qt Widgets for Technical Applications (mingw-w64)
<br/>mingw/<b>mingw-w64-qxmpp</b> 0.8.0-1
    Cross-platform C++ XMPP client and server library
<br/>mingw/<b>mingw-w64-qxmpp-qt4</b> 0.8.0-1
    Cross-platform C++ XMPP client and server library
<br/>mingw/<b>mingw-w64-readline</b> 6.2.005-3 
    MinGW port of readline for editing typed command lines (mingw-w64)
<br/>mingw/<b>mingw-w64-readosm</b> 1.0.0b-1
    Library to extract valid data from within an Open Street Map input file (mingw-w64)
<br/>mingw/<b>mingw-w64-recode</b> 3.6-4 
    Converts files between various character sets and usages (mingw-w64)
<br/>mingw/<b>mingw-w64-rtmpdump-git</b> r499.a107cef-1 
    A tool to download rtmp streams (mingw-w64)
<br/>mingw/<b>mingw-w64-ruby</b> 2.2.1-1 
    An object-oriented language for quick and easy programming (mingw-w64)
<br/>mingw/<b>mingw-w64-schroedinger</b> 1.0.11-2 
    An implemenation of the Dirac video codec in ANSI C code (mingw-w64)
<br/>mingw/<b>mingw-w64-scite</b> 3.5.4-1
    Editor with facilities for building and running programs (mingw-w64)
<br/>mingw/<b>mingw-w64-scite-defaults</b> 3.5.4-1
    Default language files for the SciTE editor (mingw-w64)
<br/>mingw/<b>mingw-w64-sed</b> 4.2.2-2
    Sed is a stream editor (mingw-w64)
<br/>mingw/<b>mingw-w64-sfml-git</b> 2.1.0.1570.749cbb2-1
    A simple, fast, cross-platform, and object-oriented multimedia API (mingw-w64)
<br/>mingw/<b>mingw-w64-shapelib</b> 1.3.0-1
    simple C API for reading and writing ESRI Shapefiles (mingw-w64)
<br/>mingw/<b>mingw-w64-shared-mime-info</b> 1.4-1 
    Freedesktop.org Shared MIME Info (mingw-w64)
<br/>mingw/<b>mingw-w64-shishi-git</b> r3583.485d3bd-1 
    a GNU implementation of the Kerberos 5 network security system (mingw-w64)
<br/>mingw/<b>mingw-w64-silc-toolkit</b> 1.1.12-2
    Secure Internet Live Conferencing (mingw-w64)
<br/>mingw/<b>mingw-w64-simage-hg</b> r672.8ea3f7b43f03-1
    Provides support for loading and saving images, sound and video (mingw-w64)
<br/>mingw/<b>mingw-w64-simvoleon-hg</b> r1052.197647967b8c-1
    3D graphics development system, in the form of an add-on library to Coin3D (mingw-w64)
<br/>mingw/<b>mingw-w64-sip</b> 4.16.6-1
    A tool that makes it easy to create Python bindings for C and C++ libraries
<br/>mingw/<b>mingw-w64-smpeg2</b> 2.0.0-2
    SDL2 MPEG Player Library (mingw-w64)
<br/>mingw/<b>mingw-w64-snappy</b> 1.1.1-1
    A fast C++ compressor/decompressor library (mingw-w64)
<br/>mingw/<b>mingw-w64-soqt-hg</b> r1943.a5b300353523-1
    The glue between Coin & Qt (mingw-w64)
<br/>mingw/<b>mingw-w64-soundtouch</b> 1.8.0-1
    An audio processing library (mingw-w64)
<br/>mingw/<b>mingw-w64-sparsehash</b> 2.0.2-2
    Library that contains several hash-map implementations, including implementations that optimize for space or speed (mingw-w64)
<br/>mingw/<b>mingw-w64-spatialite-tools</b> 4.2.0-2
    Set of CLI tools for spatialite (mingw-w64)
<br/>mingw/<b>mingw-w64-speex</b> 1.2rc2-1 
    A free codec for free speech (mingw-w64)
<br/>mingw/<b>mingw-w64-speexdsp</b> 1.2rc3-1 
    DSP library derived from Speex (mingw-w64)
<br/>mingw/<b>mingw-w64-spice-gtk</b> 0.27-1
    GTK3 widget for SPICE clients (mingw-w64)
<br/>mingw/<b>mingw-w64-spice-protocol</b> 0.12.7-1
    SPICE protocol headers (mingw-w64)
<br/>mingw/<b>mingw-w64-sqlite-analyzer</b> 3.8.9-1
    An analysis program SQLite database files (mingw-w64)
<br/>mingw/<b>mingw-w64-sqlite3</b> 3.8.9.0-1 (mingw-w64-x86_64) 
    A C library that implements an SQL database engine (mingw-w64)
<br/>mingw/<b>mingw-w64-stxxl-git</b> 1.4.1.2.g6a79caf-1
    Standard Template Library for Extra Large Data Sets (mingw-w64)
<br/>mingw/<b>mingw-w64-swig</b> 3.0.5-1 
    Generate scripting interfaces to C/C++ code
<br/>mingw/<b>mingw-w64-szip</b> 2.1-1 
    Extended-Rice lossless compression algorithm implementation
<br/>mingw/<b>mingw-w64-taglib</b> 1.9.1-3 
    A Library for reading and editing the meta-data of several popular audio formats (mingw-w64)
<br/>mingw/<b>mingw-w64-tcl</b> 8.6.4-1 
    The Tcl scripting language (mingw-w64)
<br/>mingw/<b>mingw-w64-tcllib</b> 1.16-1
    Set of pure-Tcl extensions.
<br/>mingw/<b>mingw-w64-tclvfs-cvs</b> 20130425-1
    Virtual Filesystem support for Tcl
<br/>mingw/<b>mingw-w64-tclx</b> 8.4.1-1 
    Extends Tcl by providing new operating system interface commands, extended file control and many other.
<br/>mingw/<b>mingw-w64-termcap</b> 1.3.1-1 
    Terminal feature database (mingw-w64)
<br/>mingw/<b>mingw-w64-tesseract-ocr</b> 3.04-1
    Tesseract OCR (mingw-w64)
<br/>mingw/<b>mingw-w64-tidyhtml</b> 1.46-1
    A tool to tidy down your HTML code to a clean style
<br/>mingw/<b>mingw-w64-tinyxml</b> 2.6.2-2 
    Simple, small, C++ XML parser that can be easily integrated into other programs (mingw-w64)
<br/>mingw/<b>mingw-w64-tinyxml2</b> 2.2.0-1 
    Simple, small, C++ XML parser that can be easily integrated into other programs (mingw-w64)
<br/>mingw/<b>mingw-w64-tk</b> 8.6.4-1 
    A windowing toolkit for use with tcl (mingw-w64)
<br/>mingw/<b>mingw-w64-tkimg</b> 1.4.2-1
    Adds support to Tk for many other Image formats: BMP, XBM, XPM, GIF, PNG, JPEG, TIFF and postscript.
<br/>mingw/<b>mingw-w64-tklib</b> 0.6-2
    A companion to Tcllib, for Tk related packages.
<br/>mingw/<b>mingw-w64-tktable</b> 2.10-2 
    A full-featured 2D table widget for Tk.
<br/>mingw/<b>mingw-w64-tolua</b> 5.2.0-2
    A tool that greatly simplifies the integration of C/C++ code with Lua. (mingw-w64)
<br/>mingw/<b>mingw-w64-tools-git</b> 4.0.0.4417.77f3bca-1 (mingw-w64-x86_64-toolchain mingw-w64-x86_64) 
    MinGW-w64 tools
<br/>mingw/<b>mingw-w64-totem-pl-parser</b> 3.10.4-2
    Simple GObject-based library to parse and save a host of playlist formats (mingw-w64)
<br/>mingw/<b>mingw-w64-twolame</b> 0.3.13-1 
    An optimized MPEG Audio Layer 2 (MP2) encoder
<br/>mingw/<b>mingw-w64-uhttpmock</b> 0.3.3-1
    uhttpmock is a HTTP web service mocking project for projects which use libsoup (mingw-w64)
<br/>mingw/<b>mingw-w64-unbound</b> 1.4.21-1
    Validating, recursive, and caching DNS resolver (mingw-w64)
<br/>mingw/<b>mingw-w64-usbredir</b> 0.7-1
    Parser for the usbredir protocol (mingw-w64)
<br/>mingw/<b>mingw-w64-vala</b> 0.28.0-1 
    Compiler for the GObject type system (mingw-w64)
<br/>mingw/<b>mingw-w64-vcdimager</b> 0.7.24-1 
    A full-featured mastering suite for authoring disassembling and analyzing Video CD's and Super Video CD's (mingw-w64)
<br/>mingw/<b>mingw-w64-virt-viewer-git</b> 2.0.0.934.824c4b9-2
    Displaying the graphical console of a virtual machine (mingw-w64)
<br/>mingw/<b>mingw-w64-vlc-git</b> 3.0.0.60028.a9b19e4-1 
    A multi-platform MPEG, VCD/DVD, and DivX player
<br/>mingw/<b>mingw-w64-vtk</b> 6.2.0-1
    A software system for 3D computer graphics, image processing and visualization (mingw-w64)
<br/>mingw/<b>mingw-w64-w32pth</b> 2.0.5-2 (mingw-w64-x86_64)
    An emulation of PTH for MS Windows (mingw-w64)
<br/>mingw/<b>mingw-w64-wavpack</b> 4.70.0-1 
    Audio compression format with lossless, lossy and hybrid compression modes (mingw-w64)
<br/>mingw/<b>mingw-w64-webkitgtk2</b> 2.4.8-2 
    GTK+ Web content engine library (mingw-w64) for GTK2
<br/>mingw/<b>mingw-w64-webkitgtk3</b> 2.4.8-2 
    GTK+ Web content engine library (mingw-w64)
<br/>mingw/<b>mingw-w64-wget</b> 1.16.3-1
    Wget retrieves files using HTTP, HTTPS and FTP (mingw-w64)
<br/>mingw/<b>mingw-w64-windows-default-manifest</b> 6.4-1 
    Default Windows application manifest (mingw-w64)
<br/>mingw/<b>mingw-w64-wined3d</b> 1.7.11-1
    Direct3D to OpenGL translator (mingw-w64)
<br/>mingw/<b>mingw-w64-wineditline</b> 2.101-3 
    port of the NetBSD Editline library (mingw-w64)
<br/>mingw/<b>mingw-w64-winico</b> 0.6-1
    Tk extension for Windows for enhanced icon handling and manipulation of an icon in the Windows taskbar and system tray.
<br/>mingw/<b>mingw-w64-winpthreads-git</b> 5.0.0.4455.32db221-1 (mingw-w64-x86_64-toolchain mingw-w64-x86_64) 
    MinGW-w64 winpthreads library
<br/>mingw/<b>mingw-w64-winsparkle-git</b> r261.adc56a8-1
    App update framework for Windows, inspired by Sparkle for OS X (mingw-w64)
<br/>mingw/<b>mingw-w64-winstorecompat-git</b> 4.0.0.4328.a913346-1 (mingw-w64-x86_64-toolchain mingw-w64-x86_64) 
    MinGW-w64 winRT compat library
<br/>mingw/<b>mingw-w64-wintab-sdk</b> 1.4-1 
    Wintab Interface Specification (mingw-w64)
<br/>mingw/<b>mingw-w64-wxPython</b> 3.0.2.0-1 (mingw-w64-x86_64) 
    A wxWidgets GUI toolkit for Python (mingw-w64)
<br/>mingw/<b>mingw-w64-wxWidgets</b> 3.0.2-5 (mingw-w64-x86_64) 
    A C++ library that lets developers create applications for Windows, Linux and UNIX (mingw-w64)
<br/>mingw/<b>mingw-w64-x264</b> r2491.24e4fed-1 
    Library for encoding H264/AVC video streams (mingw-w64)
<br/>mingw/<b>mingw-w64-x265</b> 1.5-1 
    Open Source H265/HEVC video encoder (mingw-w64)
<br/>mingw/<b>mingw-w64-xalan-c</b> 1.11-2
    An XSLT processing library (mingw-w64)
<br/>mingw/<b>mingw-w64-xerces-c</b> 3.1.2-1
    A validating XML parser written in a portable subset of C++. (mingw-w64)
<br/>mingw/<b>mingw-w64-xmlada-gpl</b> 2014-1 (mingw-w64-x86_64)
    A full XML suite for Ada
<br/>mingw/<b>mingw-w64-xmlstarlet-git</b> r678.9a470e3-1
    Command-line XML toolkit
<br/>mingw/<b>mingw-w64-xpm-nox</b> 4.2.0-3 
    X Pixmap library not using X (mingw-w64)
<br/>mingw/<b>mingw-w64-xvidcore</b> 1.3.3-1 
    XviD is an open source MPEG-4 video codec (mingw-w64)
<br/>mingw/<b>mingw-w64-xxhash-svn</b> r37-1 
    Extremely fast non-cryptographic hash algorithm (mingw-w64)
<br/>mingw/<b>mingw-w64-xz</b> 5.2.1-1 
    Library and command line tools for XZ and LZMA compressed files (mingw-w64)
<br/>mingw/<b>mingw-w64-yaml-cpp</b> 0.5.1-2
    A YAML parser and emitter in C++ matching the YAML 1.2 spec (mingw-w64)
<br/>mingw/<b>mingw-w64-yaml-cpp0.3</b> 0.3.0-2
    A YAML parser and emitter in C++ matching the YAML 1.2 spec (mingw-w64) - old version
<br/>mingw/<b>mingw-w64-yasm</b> 1.3.0-1
    A rewrite of NASM to allow for multiple syntax supported (NASM, TASM, GAS, etc.) (mingw-w64)
<br/>mingw/<b>mingw-w64-zeromq</b> 4.0.5-2
    Fast messaging system built on sockets, C and C++ bindings. aka 0MQ, ZMQ. (mingw-w64)
<br/>mingw/<b>mingw-w64-zlib</b> 1.2.8-6 (mingw-w64-x86_64) 
    Compression library implementing the deflate compression method found in gzip and PKZIP (mingw-w64)
<br/>mingw/<b>mingw-w64-zziplib</b> 0.13.62-3
    A lightweight library that offers the ability to easily extract data from files archived in a single zip file (mingw-w64)
<br/>msys/<b>apr</b> 1.5.1-1 (libraries) 
    The Apache Portable Runtime
<br/>msys/<b>apr-devel</b> 1.5.1-1 (development)
    Libapr headers and libraries
<br/>msys/<b>apr-util</b> 1.5.4-1 (libraries) 
    The Apache Portable Runtime
<br/>msys/<b>apr-util-devel</b> 1.5.4-1 (development)
    Libapr-util headers and libraries
<br/>msys/<b>asciidoc</b> 8.6.9-4 (base-devel) 
    Text document format for short documents, articles, books and UNIX man pages.
<br/>msys/<b>autoconf</b> 2.69-3 (base-devel) 
    A GNU tool for automatically configuring source code
<br/>msys/<b>autoconf2.13</b> 2.13-2 (base-devel) 
    A GNU tool for automatically configuring source code
<br/>msys/<b>autogen</b> 5.18.4-2 (base-devel) 
    A tool designed to simplify the creation and maintenance of programs that contain large amounts of repetitious text
<br/>msys/<b>automake-wrapper</b> 10-1 (base-devel) 
    Wrapper scripts for automake and aclocal
<br/>msys/<b>automake1.10</b> 1.10.3-2 (base-devel) 
    A GNU tool for automatically creating Makefiles
<br/>msys/<b>automake1.11</b> 1.11.6-2 (base-devel) 
    A GNU tool for automatically creating Makefiles
<br/>msys/<b>automake1.12</b> 1.12.6-2 (base-devel) 
    A GNU tool for automatically creating Makefiles
<br/>msys/<b>automake1.13</b> 1.13.4-2 (base-devel) 
    A GNU tool for automatically creating Makefiles
<br/>msys/<b>automake1.14</b> 1.14.1-2 (base-devel) 
    A GNU tool for automatically creating Makefiles
<br/>msys/<b>automake1.15</b> 1.15-1 (base-devel) 
    A GNU tool for automatically creating Makefiles
<br/>msys/<b>automake1.6</b> 1.6.3-2 (base-devel) 
    A GNU tool for automatically creating Makefiles
<br/>msys/<b>automake1.7</b> 1.7.9-2 (base-devel) 
    A GNU tool for automatically creating Makefiles
<br/>msys/<b>automake1.8</b> 1.8.5-3 (base-devel) 
    A GNU tool for automatically creating Makefiles
<br/>msys/<b>automake1.9</b> 1.9.6-2 (base-devel) 
    A GNU tool for automatically creating Makefiles
<br/>msys/<b>bash</b> 4.3.033-2 (base) 
    The GNU Bourne Again shell
<br/>msys/<b>bash-completion</b> 2.1-5 (base) 
    Programmable completion for the bash shell
<br/>msys/<b>bash-devel</b> 4.3.033-2 (development)
    Bash headers and libraries
<br/>msys/<b>binutils</b> 2.25-2 (msys2-devel) 
    A set of programs to assemble and manipulate binary and object files
<br/>msys/<b>bison</b> 3.0.4-1 (base-devel) 
    The GNU general-purpose parser generator
<br/>msys/<b>bsdcpio</b> 3.1.2-4 (base) 
    library that can create and read several streaming archive formats
<br/>msys/<b>bsdtar</b> 3.1.2-4 (base) 
    library that can create and read several streaming archive formats
<br/>msys/<b>busybox</b> 1.22.1-2 
    BusyBox: The Swiss Army Knife of Embedded Linux
<br/>msys/<b>bzip2</b> 1.0.6-2 (base compression) 
    A high-quality data compression program
<br/>msys/<b>bzr</b> 2.6.0-2 (VCS) 
    Bazaar is a version control system that helps you track project history over time and to collaborate easily with others.
<br/>msys/<b>bzr-fastimport</b> 0.13.0-1
    Bazaar Fast Import is a plugin providing fast loading of revision control data into Bazaar.
<br/>msys/<b>ca-certificates</b> 20141019-2 
    Common CA certificates
<br/>msys/<b>catgets</b> 1.1-2 (base) 
    catgets message catalog API
<br/>msys/<b>cdecl</b> 2.5-1
    A program for encoding and decoding C (or C++) type declarations
<br/>msys/<b>cgdb</b> 0.6.8-1
    Curses-based interface to the GNU Debugger
<br/>msys/<b>cloog</b> 0.18.1-1 (libraries) 
    Library that generates loops for scanning polyhedra
<br/>msys/<b>cloog-devel</b> 0.18.1-1 (development)
    CLOOG headers and libraries
<br/>msys/<b>cocom</b> 0.996-1 (msys2-devel) 
    Toolset for creation of compilers and interpreters
<br/>msys/<b>coreutils</b> 8.23-4 (base) 
    The basic file, shell and text manipulation utilities of the GNU operating system
<br/>msys/<b>crosstool-ng-git</b> 1.19.314.a483cd9-1 
    A cross-platform open-source toolchain system
<br/>msys/<b>crypt</b> 1.1-6 (base) 
    Encryption/Decryption utility
<br/>msys/<b>cscope</b> 15.8a-1
    A tool for browsing source code
<br/>msys/<b>ctags</b> 5.8-1
    Generate tag files for source code
<br/>msys/<b>curl</b> 7.41.0-1 (base) 
    Multi-protocol file transfer utility
<br/>msys/<b>cvs</b> 1.11.23-2 
    Concurrent Versions System - a source control system
<br/>msys/<b>cygrunsrv</b> 1.61-1
    cygrunsrv is a windows services tool
<br/>msys/<b>cyrus-sasl</b> 2.1.26-7 (sys-utils)
    Cyrus saslauthd SASL authentication daemon
<br/>msys/<b>dash</b> 0.5.8-1 (base) 
    A POSIX compliant shell that aims to be as small as possible
<br/>msys/<b>db</b> 5.3.28-2 (Database) 
    The Berkeley DB embedded database system
<br/>msys/<b>db-docs</b> 5.3.28-2
    BerkleyDB documentation
<br/>msys/<b>delta</b> 20060803-1 
    An useful tool that lets you minimize interesting files subject to a test of their interestingness.
<br/>msys/<b>depot-tools-git</b> r2542.77b74b5-1 
    Build tools for working with Chromium development, include gclient
<br/>msys/<b>diffstat</b> 1.58-1 (base-devel) 
    Display a histogram of diff changes
<br/>msys/<b>diffutils</b> 3.3-3 (base-devel) 
    Utility programs used for creating patch files
<br/>msys/<b>docbook-xml</b> 4.5-2 
    A widely used XML scheme for writing documentation and help
<br/>msys/<b>docbook-xsl</b> 1.78.1-3 
    XML stylesheets for Docbook-xml transformations
<br/>msys/<b>dos2unix</b> 7.2.1-1 (base-devel) 
    Text file format converter
<br/>msys/<b>doxygen</b> 1.8.9.1-1 
    A documentation system for C++, C, Java, IDL and PHP
<br/>msys/<b>ed</b> 1.10-2
    A POSIX-compliant line-oriented text editor
<br/>msys/<b>elinks-git</b> 0.13.3949.f778e66-1 (net-utils)
    Full-Featured Text WWW Browser (net-utils)
<br/>msys/<b>expat</b> 2.1.0-2 
    An XML parser library
<br/>msys/<b>file</b> 5.22-1 (base base-devel) 
    File type identification utility
<br/>msys/<b>filesystem</b> 2015.04-1 (base) 
    Base filesystem
<br/>msys/<b>findutils</b> 4.5.14-4 (base) 
    GNU utilities to locate files
<br/>msys/<b>flex</b> 2.5.39-4 (base base-devel) 
    A tool for generating text-scanning programs
<br/>msys/<b>gamin</b> 0.1.10-2 (libraries) 
    File and directory monitoring system defined to be a subset of the FAM (File Alteration Monitor)
<br/>msys/<b>gamin-devel</b> 0.1.10-2 (development)
    Gamin headers and libraries (development)
<br/>msys/<b>gamin-python</b> 0.1.10-2 (python-modules)
    Gamin python modules
<br/>msys/<b>gawk</b> 4.1.1-3 (base base-devel) 
    GNU version of awk
<br/>msys/<b>gcc</b> 4.9.2-4 (msys2-devel) 
    The GNU Compiler Collection - C and C++ frontends
<br/>msys/<b>gcc-fortran</b> 4.9.2-4 (msys2-devel) 
    Fortran front-end for GCC
<br/>msys/<b>gcc-libs</b> 4.9.2-4 (base) 
    Runtime libraries shipped by GCC
<br/>msys/<b>gdb</b> 7.9-1 (base-devel) 
    GNU Debugger (MSYS2 version)
<br/>msys/<b>gdbm</b> 1.11-3 (Database) 
    GNU database library
<br/>msys/<b>gengetopt</b> 2.22.6-2 
    A tool to write command line option parsing code for C programs.
<br/>msys/<b>gettext</b> 0.19.4-1 (base-devel) 
    GNU internationalization library
<br/>msys/<b>gettext-devel</b> 0.19.4-1 (development) 
    GNU Internationalization development utilities
<br/>msys/<b>git</b> 2.3.5-1 (VCS) 
    The fast distributed version control system
<br/>msys/<b>glib2</b> 2.42.0-1 
    Common C routines used by GTK+ and other libs
<br/>msys/<b>glib2-devel</b> 2.42.0-1 (development) 
    glib2 headers and libraries
<br/>msys/<b>glib2-docs</b> 2.42.0-1
    Documentation for glib2
<br/>msys/<b>global</b> 6.3.4-1
    A source code tagging system
<br/>msys/<b>gmp</b> 6.0.0-3 (libraries) 
    A free library for arbitrary precision arithmetic
<br/>msys/<b>gmp-devel</b> 6.0.0-3 (development) 
    GMP headers and libraries
<br/>msys/<b>gnome-common</b> 3.14.0-1
    Common development macros for GNOME
<br/>msys/<b>gnome-doc-utils</b> 0.20.10-1 
    Documentation utilities for Gnome
<br/>msys/<b>gnu-netcat</b> 0.7.1-1
    GNU rewrite of netcat, the network piping application
<br/>msys/<b>gnupg</b> 1.4.19-1 
    Complete and free implementation of the OpenPGP standard
<br/>msys/<b>gperf</b> 3.0.4-3 (base-devel) 
    Perfect hash function generator
<br/>msys/<b>gradle</b> 1.12-1 
    A powerful build system for the JVM
<br/>msys/<b>gradle-doc</b> 1.12-1
    A powerful build system for the JVM (documentation and samples)
<br/>msys/<b>grep</b> 2.21-1 (base base-devel) 
    A string search utility
<br/>msys/<b>groff</b> 1.22.3-1 (base-devel) 
    GNU troff text-formatting system
<br/>msys/<b>gtk-doc</b> 1.21-1 
    Documentation tool for public library API (mingw-w64)
<br/>msys/<b>guile</b> 2.0.11-3 
    a portable, embeddable Scheme implementation written in C
<br/>msys/<b>gyp-svn</b> r1945-1 
    GYP can Generate Your Projects.
<br/>msys/<b>gzip</b> 1.6-1 (base compression) 
    GNU compression utility
<br/>msys/<b>heimdal</b> 1.5.3-6 (sys-utils) 
    Implementation of Kerberos V5 libraries
<br/>msys/<b>heimdal-devel</b> 1.5.3-6 (development)
    Heimdal headers and libraries
<br/>msys/<b>heimdal-libs</b> 1.5.3-6 (libraries) 
    Implementation of Kerberos V5 libraries
<br/>msys/<b>help2man</b> 1.46.5-1 (base-devel) 
    Conversion tool to create man files
<br/>msys/<b>icu</b> 51.2-2 (libraries) 
    International Components for Unicode library
<br/>msys/<b>icu-devel</b> 51.2-2 (development)
    ICU headers and libraries
<br/>msys/<b>idutils</b> 4.6-1
    A fast, high-capacity, identifier database tool
<br/>msys/<b>inetutils</b> 1.9.2-1 (base)
    A collection of common network programs.
<br/>msys/<b>info</b> 5.2-5 (base) 
    Utilities to work with and produce manuals, ASCII text, and on-line documentation from a single source file
<br/>msys/<b>intltool</b> 0.51.0-1 (base-devel) 
    The internationalization tool collection
<br/>msys/<b>isl</b> 0.12.1-1 (libraries) 
    Library for manipulating sets and relations of integer points bounded by linear constraints
<br/>msys/<b>isl-devel</b> 0.12.1-1 (development)
    ISL headers and libraries
<br/>msys/<b>itstool</b> 2.0.2-2 
    XML to PO and back again)
<br/>msys/<b>jhbuild-git</b> 8206.7f97721-1
    Downloads and compiles Gnome "modules", i.e. source code packages.
<br/>msys/<b>lemon</b> 3.8.7.0-1 (base-devel) 
    The LEMON LALR Parser Generator used in SQLite 3.8.7.0 (MSYS2)
<br/>msys/<b>less</b> 471-1 (base) 
    A terminal based program for viewing text files
<br/>msys/<b>lftp</b> 4.6.1-1 (net-utils)
    Sophisticated command line based FTP client (net-utils)
<br/>msys/<b>libarchive</b> 3.1.2-4 (libraries) 
    library that can create and read several streaming archive formats
<br/>msys/<b>libarchive-devel</b> 3.1.2-4 (development) 
    library that can create and read several streaming archive formats
<br/>msys/<b>libasprintf</b> 0.19.4-1 (libraries) 
    C-style formatted output in C++ (runtime)
<br/>msys/<b>libassuan</b> 2.2.0-1 (libraries) 
    A IPC library used by some GnuPG related software
<br/>msys/<b>libassuan-devel</b> 2.2.0-1 (development) 
    Libassuan headers and libraries
<br/>msys/<b>libatomic_ops-devel</b> 7.2.d-1 (development)
    A garbage collector for C and C++
<br/>msys/<b>libbz2</b> 1.0.6-2 (libraries) 
    A high-quality data compression program
<br/>msys/<b>libbz2-devel</b> 1.0.6-2 (development) 
    Libbz2 headers and libraries
<br/>msys/<b>libcares</b> 1.10.0-2 (libraries)
    C library that performs DNS requests and name resolves asynchronously (libraries)
<br/>msys/<b>libcares-devel</b> 1.10.0-2 (development)
    c-ares headers and libraries (development)
<br/>msys/<b>libcatgets</b> 1.1-2 (libraries) 
    catgets message catalog API
<br/>msys/<b>libcatgets-devel</b> 1.1-2 (development)
    Libcatgets headers and libraries
<br/>msys/<b>libcrypt</b> 1.1-6 (libraries) 
    Encryption/Decryption utility and library
<br/>msys/<b>libcrypt-devel</b> 1.1-6 (development) 
    Libcrypt headers and libraries
<br/>msys/<b>libcurl</b> 7.41.0-1 (libraries) 
    Multi-protocol file transfer library (runtime)
<br/>msys/<b>libcurl-devel</b> 7.41.0-1 (development) 
    Libcurl headers and libraries
<br/>msys/<b>libdb</b> 5.3.28-2 (libraries) 
    The Berkeley DB embedded database system
<br/>msys/<b>libdb-devel</b> 5.3.28-2 (development)
    libdb headers and libraries
<br/>msys/<b>libedit</b> 3.1-20130712 (libraries) 
    Libedit is an autotool- and libtoolized port of the NetBSD Editline library.
<br/>msys/<b>libedit-devel</b> 3.1-20130712 (development)
    libedit headers and libraries
<br/>msys/<b>libevent</b> 2.1.4-1
    An event notification library
<br/>msys/<b>libevent-devel</b> 2.1.4-1 (development)
    Libevent headers and libraries
<br/>msys/<b>libexpat</b> 2.1.0-2 (libraries) 
    An XML parser library
<br/>msys/<b>libexpat-devel</b> 2.1.0-2 (development) 
    Libexpat headers and libraries
<br/>msys/<b>libffi</b> 3.2.1-1 (libraries) 
    Portable, high level programming interface to various calling conventions
<br/>msys/<b>libffi-devel</b> 3.2.1-1 (development) 
    Libffi headers and libraries
<br/>msys/<b>libgc</b> 7.2.d-1 
    A garbage collector for C and C++
<br/>msys/<b>libgc-devel</b> 7.2.d-1 (development)
    A garbage collector for C and C++
<br/>msys/<b>libgcrypt</b> 1.6.3-1 (libraries) 
    General purpose cryptographic library based on the code from GnuPG
<br/>msys/<b>libgcrypt-devel</b> 1.6.3-1 (development)
    Libgcrypt headers and libraries
<br/>msys/<b>libgdbm</b> 1.11-3 (libraries) 
    GNU database library
<br/>msys/<b>libgdbm-devel</b> 1.11-3 (development)
    libgdbm headers and libraries
<br/>msys/<b>libgettextpo</b> 0.19.4-1 (libraries) 
    GNU Internationalization runtime library
<br/>msys/<b>libgpg-error</b> 1.12-3 (libraries) 
    Support library for libgcrypt
<br/>msys/<b>libgpg-error-devel</b> 1.12-3 (development) 
    Libgpg-error headers and libraries
<br/>msys/<b>libgpgme</b> 1.5.3-1 (libraries) 
    A C wrapper library for GnuPG
<br/>msys/<b>libgpgme-devel</b> 1.5.3-1 (development) 
    Libgpgme headers and libraries
<br/>msys/<b>libguile</b> 2.0.11-3 (libraries) 
    a portable, embeddable Scheme implementation written in C
<br/>msys/<b>libguile-devel</b> 2.0.11-3 (development)
    a portable, embeddable Scheme implementation written in C
<br/>msys/<b>libhogweed</b> 3.0-2 (libraries) 
    A low-level cryptographic library
<br/>msys/<b>libiconv</b> 1.14-2 (libraries) 
    Libiconv is a conversion library
<br/>msys/<b>libiconv-devel</b> 1.14-2 (development) 
    libiconv headers and libraries
<br/>msys/<b>libidn</b> 1.30-1 (libraries) 
    Implementation of the Stringprep, Punycode and IDNA specifications
<br/>msys/<b>libidn-devel</b> 1.30-1 (development) 
    Libidn headers and libraries
<br/>msys/<b>libintl</b> 0.19.4-1 (libraries) 
    GNU Internationalization runtime library
<br/>msys/<b>libksba</b> 1.3.0-2 (libraries)
    A CMS and X.509 access library
<br/>msys/<b>libksba-devel</b> 1.3.0-2 (development)
    Libassuan headers and libraries
<br/>msys/<b>libltdl</b> 2.4.6-1 
    A system independent dlopen wrapper for GNU libtool
<br/>msys/<b>liblzma</b> 5.2.1-1 (libraries) 
    Library for XZ and LZMA compressed files
<br/>msys/<b>liblzma-devel</b> 5.2.1-1 (development) 
    Liblzma headers and libraries
<br/>msys/<b>liblzo2</b> 2.09-1 (libraries compression) 
    Portable lossless data compression library
<br/>msys/<b>liblzo2-devel</b> 2.09-1 (development) 
    Liblzo2 headers and libraries
<br/>msys/<b>libmetalink</b> 0.1.2-2 (libraries) 
    Metalink XML parser library.
<br/>msys/<b>libmetalink-devel</b> 0.1.2-2 (development) 
    libmetalink headers and libraries
<br/>msys/<b>libneon</b> 0.30.0-1 (libraries)
    HTTP and WebDAV client library with a C interface
<br/>msys/<b>libneon-devel</b> 0.30.0-1 (development)
    Libneon headers and libraries
<br/>msys/<b>libnettle</b> 3.0-2 (libraries) 
    A low-level cryptographic library
<br/>msys/<b>libnettle-devel</b> 3.0-2 (development) 
    Libnettle headers and libraries
<br/>msys/<b>libopenssl</b> 1.0.2.a-1 (libraries) 
    The Open Source toolkit for Secure Sockets Layer and Transport Layer Security
<br/>msys/<b>libp11-kit</b> 0.22.1-1 (libraries) 
    Library to work with PKCS#11 modules
<br/>msys/<b>libp11-kit-devel</b> 0.22.1-1 (development)
    Libp11-kit headers and libraries
<br/>msys/<b>libpcre</b> 8.36-2 (libraries) 
    A library that implements Perl 5-style regular expressions
<br/>msys/<b>libpcre16</b> 8.36-2 (libraries) 
    A library that implements Perl 5-style regular expressions
<br/>msys/<b>libpcre32</b> 8.36-2 (libraries) 
    A library that implements Perl 5-style regular expressions
<br/>msys/<b>libpcrecpp</b> 8.36-2 (libraries) 
    A library that implements Perl 5-style regular expressions
<br/>msys/<b>libpcreposix</b> 8.36-2 (libraries) 
    A library that implements Perl 5-style regular expressions
<br/>msys/<b>libpipeline</b> 1.4.0-1 (libraries) 
    a C library for manipulating pipelines of subprocesses in a flexible and convenient way
<br/>msys/<b>libpipeline-devel</b> 1.4.0-1 (development)
    libpipeline headers and libraries
<br/>msys/<b>libreadline</b> 6.3.008-4 (libraries) 
    GNU readline library
<br/>msys/<b>libreadline-devel</b> 6.3.008-4 (development) 
    readline headers and libraries
<br/>msys/<b>libsasl</b> 2.1.26-7 (libraries) 
    Cyrus Simple Authentication Service Layer (SASL) Library
<br/>msys/<b>libsasl-devel</b> 2.1.26-7 (development)
    Libsasl headers and libraries
<br/>msys/<b>libserf</b> 1.3.8-1 (libraries) 
    High-performance asynchronous HTTP client library
<br/>msys/<b>libserf-devel</b> 1.3.8-1 (development)
    Libserf headers and libraries
<br/>msys/<b>libsqlite</b> 3.8.8.2-1 (libraries) 
    Sqlite3 library
<br/>msys/<b>libsqlite-devel</b> 3.8.8.2-1 (development)
    Sqlite3 headers and libraries
<br/>msys/<b>libssh2</b> 1.4.3-3 (libraries) 
    Multi-protocol file transfer library (runtime)
<br/>msys/<b>libssh2-devel</b> 1.4.3-3 (development) 
    Libssh2 headers and libraries
<br/>msys/<b>libtasn1</b> 4.2-3 (libraries) 
    A library for Abstract Syntax Notation One (ASN.1) and Distinguish Encoding Rules (DER) manipulation.
<br/>msys/<b>libtasn1-devel</b> 4.2-3 (development)
    Libtasn1 headers and libraries
<br/>msys/<b>libtirpc</b> 0.2.5-1 (libraries)
    A port of Sun's Transport-Independent RPC library
<br/>msys/<b>libtirpc-devel</b> 0.2.5-1 (development)
    Libtirpc headers and libraries
<br/>msys/<b>libtool</b> 2.4.6-1 (base-devel) 
    A generic library support script
<br/>msys/<b>libtre-devel-git</b> 0.8.0.122.c2f5d13-1 (development)
    Libtre headers and libraries (development)
<br/>msys/<b>libtre-git</b> 0.8.0.122.c2f5d13-1 (libraries)
    The free and portable approximate regex matching library (libraries)
<br/>msys/<b>libunistring</b> 0.9.4-2 (libraries) 
    Library for manipulating Unicode strings and C strings.
<br/>msys/<b>libunistring-devel</b> 0.9.4-2 (development) 
    libunistring headers and libraries
<br/>msys/<b>libunrar</b> 5.2.2-1 (base-devel) 
    Library and header file for applications that use libunrar
<br/>msys/<b>libutil-linux</b> 2.26.1-1 
    Block device ID and Universally Unique ID libraries
<br/>msys/<b>libutil-linux-devel</b> 2.26.1-1
    Block device ID and Universally Unique ID headers and libraries.
<br/>msys/<b>libxml2</b> 2.9.2-2 (libraries) 
    XML parsing library, version 2
<br/>msys/<b>libxml2-devel</b> 2.9.2-2 (development) 
    Libxml2 headers and libraries
<br/>msys/<b>libxml2-python</b> 2.9.2-2 (python-modules) 
    Libxml2 python modules
<br/>msys/<b>libxslt</b> 1.1.28-7 (libraries) 
    XML stylesheet transformation library
<br/>msys/<b>libxslt-devel</b> 1.1.28-7 (development)
    Libxslt headers and libraries
<br/>msys/<b>libxslt-python</b> 1.1.28-7 (python-modules) 
    Libxslt python modules
<br/>msys/<b>libyaml</b> 0.1.4-1 (libraries) 
    YAML 1.1 library
<br/>msys/<b>libyaml-devel</b> 0.1.4-1 (development)
    YAML 1.1 library
<br/>msys/<b>lndir</b> 1.0.3-1 (base) 
    Create a shadow directory of symbolic links to another directory tree
<br/>msys/<b>lzip</b> 1.16-1
    A lossless file compressor based on the LZMA algorithm
<br/>msys/<b>m4</b> 1.4.17-4 (base-devel) 
    The GNU macro processor
<br/>msys/<b>make</b> 4.1-3 (base-devel) 
    GNU make utility to maintain groups of programs
<br/>msys/<b>make-git</b> 4.1.8.g292da6f-1
    GNU make utility to maintain groups of programs
<br/>msys/<b>man-db</b> 2.7.1-1 (base-devel) 
    A utility for reading man pages
<br/>msys/<b>man-pages-posix</b> 2013_a-1
    POSIX Manual Pages
<br/>msys/<b>markdown</b> 1.0.1-1
    A text-to-HTML conversion tool
<br/>msys/<b>mc</b> 4.8.14-1
    Midnight Commander is a text based filemanager/shell that emulates Norton Commander
<br/>msys/<b>mercurial</b> 3.3.3-1 (VCS) 
    A scalable distributed SCM tool
<br/>msys/<b>mingw-w64-cross-binutils</b> 2.25-1 (mingw-w64-cross-toolchain mingw-w64-cross) 
    A set of programs to assemble and manipulate binary and object files
<br/>msys/<b>mingw-w64-cross-crt-git</b> 4.0.0.4384.404d457-1 (mingw-w64-cross-toolchain mingw-w64-cross) 
    MinGW-w64 CRT for cross-compiler
<br/>msys/<b>mingw-w64-cross-gcc</b> 4.9.2-2 (mingw-w64-cross-toolchain mingw-w64-cross) 
    Cross GCC for the MinGW-w64
<br/>msys/<b>mingw-w64-cross-headers-git</b> 4.0.0.4384.404d457-1 (mingw-w64-cross-toolchain mingw-w64-cross) 
    MinGW-w64 headers for cross-compiler
<br/>msys/<b>mingw-w64-cross-windows-default-manifest</b> 6.4-1 (mingw-w64-cross-toolchain mingw-w64-cross) 
    Default Windows application manifest
<br/>msys/<b>mingw-w64-cross-winpthreads-git</b> 4.0.0.4305.9bd8fe9-1 (mingw-w64-cross-toolchain mingw-w64-cross) 
    MinGW-w64 winpthreads library for cross-compiler
<br/>msys/<b>mingw-w64-cross-zlib</b> 1.2.8-1 (mingw-w64-cross-toolchain mingw-w64-cross) 
    Compression library implementing the deflate compression method found in gzip and PKZIP
<br/>msys/<b>mintty</b> 1322-2 (base) 
    Terminal emulator with native Windows look and feel
<br/>msys/<b>mksh</b> 50.e-1
    The MirBSD Korn Shell
<br/>msys/<b>mpc</b> 1.0.3-1 (libraries) 
    Multiple precision complex arithmetic library
<br/>msys/<b>mpc-devel</b> 1.0.3-1 (development)
    MPC headers and libraries
<br/>msys/<b>mpfr</b> 3.1.2.p11-1 (libraries) 
    Multiple-precision floating-point library
<br/>msys/<b>mpfr-devel</b> 3.1.2.p11-1 (development)
    MPFR headers and libraries
<br/>msys/<b>msys2-keyring</b> r8.3864337-1 (base) 
    MSYS2 PGP keyring
<br/>msys/<b>msys2-runtime</b> 2.1.0.16305.2579661-2 (base) 
    Posix emulation engine for Windows
<br/>msys/<b>msys2-runtime-devel</b> 2.1.0.16305.2579661-2 (MSYS2-devel) 
    MSYS2 headers and libraries
<br/>msys/<b>msys2-w32api-headers</b> 5.0.0.4456.c8b6742-1 (msys2-devel) 
    Win32 API headers for MSYS2 32bit toolchain
<br/>msys/<b>msys2-w32api-runtime</b> 5.0.0.4455.32db221-1 (msys2-devel) 
    Win32 API import libs for MSYS2 toolchain
<br/>msys/<b>nano</b> 2.4.0-1 (editors) 
    Pico editor clone with enhancements
<br/>msys/<b>nasm</b> 2.11.08-1 
    An 80x86 assembler designed for portability and modularity
<br/>msys/<b>ncurses</b> 5.9.20150110-1 (base) 
    System V Release 4.0 curses emulation library
<br/>msys/<b>ncurses-devel</b> 5.9.20150110-1 (development) 
    NCURSES headers and libraries
<br/>msys/<b>nettle</b> 3.0-2 (net-utils)
    A low-level cryptographic library
<br/>msys/<b>openssh</b> 6.7p1-1 (net-utils) 
    Free version of the SSH connectivity tools
<br/>msys/<b>openssl</b> 1.0.2.a-1 
    The Open Source toolkit for Secure Sockets Layer and Transport Layer Security
<br/>msys/<b>openssl-devel</b> 1.0.2.a-1 (development) 
    Openssl headers and libraries
<br/>msys/<b>p11-kit</b> 0.22.1-1 
    Library to work with PKCS#11 modules
<br/>msys/<b>p7zip</b> 9.38-1 (compression) 
    Command-line version of the 7zip compressed file archiver
<br/>msys/<b>pacman</b> 4.2.0.6106.9b2114c-1 (base base-devel) 
    A library-based package manager with dependency support (MSYS2 port)
<br/>msys/<b>pacman-mirrors</b> 20141223-1 (base) 
    MSYS2 mirror list for use by pacman
<br/>msys/<b>patch</b> 2.7.5-1 (base-devel) 
    A utility to apply patch files to original sources
<br/>msys/<b>patchutils</b> 0.3.3-2 (base-devel) 
    Utilities to work with patches
<br/>msys/<b>pcre</b> 8.36-2 
    A library that implements Perl 5-style regular expressions
<br/>msys/<b>pcre-devel</b> 8.36-2 (development) 
    PCRE headers and libraries
<br/>msys/<b>perl</b> 5.20.2-1 (base-devel) 
    A highly capable, feature-rich programming language
<br/>msys/<b>perl-Archive-Zip</b> 1.41-1 (perl-modules)
    Provide a perl interface to ZIP archive files
<br/>msys/<b>perl-Authen-SASL</b> 2.16-2 (perl-modules) 
    Perl/CPAN Module Authen::SASL : SASL authentication framework
<br/>msys/<b>perl-Benchmark-Timer</b> 0.7102-1 (perl-modules) 
    Provide commonly requested regular expressions
<br/>msys/<b>perl-Capture-Tiny</b> 0.24-1 (perl-modules)
    Capture STDOUT and STDERR from Perl, XS or external programs
<br/>msys/<b>perl-Compress-Bzip2</b> 2.19-1 (perl-modules)
    Interface to Bzip2 compression library
<br/>msys/<b>perl-Convert-BinHex</b> 1.123-2 
    Perl module to extract data from Macintosh BinHex files
<br/>msys/<b>perl-Crypt-SSLeay</b> 0.72-1 (perl-modules)
    OpenSSL glue that provides LWP https support
<br/>msys/<b>perl-DBI</b> 1.633-1 (perl-modules)
    Database independent interface for Perl
<br/>msys/<b>perl-Digest-HMAC</b> 1.03-2 (perl-modules)
    Perl Module: Keyed-Hashing for Message Authentication.
<br/>msys/<b>perl-Encode-Locale</b> 1.03-2 (perl-modules) 
    Determine the locale encoding
<br/>msys/<b>perl-Error</b> 0.17023-1 (perl-modules) 
    Perl/CPAN Error module - Error/exception handling in an OO-ish way
<br/>msys/<b>perl-Exporter-Lite</b> 0.06-1 (perl-modules) 
    lightweight exporting of functions and variables
<br/>msys/<b>perl-ExtUtils-Depends</b> 0.308-2 (perl-modules)
    The Perl depends module
<br/>msys/<b>perl-ExtUtils-PkgConfig</b> 1.15-2 (perl-modules)
    The Perl Pkgconfig module
<br/>msys/<b>perl-File-Copy-Recursive</b> 0.38-2 (perl-modules)
    extension for recursively copying files and directories
<br/>msys/<b>perl-File-Listing</b> 6.04-2 (perl-modules) 
    parse directory listing
<br/>msys/<b>perl-File-Next</b> 1.12-2 (perl-modules) 
    File-finding iterator
<br/>msys/<b>perl-File-Which</b> 1.09-2 (perl-modules) 
    Portable implementation of which
<br/>msys/<b>perl-Getopt-Tabular</b> 0.3-1 (perl-modules) 
    table-driven argument parsing for Perl 5
<br/>msys/<b>perl-HTML-Parser</b> 3.71-2 (perl-modules) 
    Perl HTML parser class
<br/>msys/<b>perl-HTML-Tagset</b> 3.20-2 (perl-modules) 
    Data tables useful in parsing HTML
<br/>msys/<b>perl-HTTP-Cookies</b> 6.01-2 (perl-modules) 
    HTTP cookie jars
<br/>msys/<b>perl-HTTP-Daemon</b> 6.01-2 (perl-modules) 
    A simple http server class
<br/>msys/<b>perl-HTTP-Date</b> 6.02-2 (perl-modules) 
    Date conversion routines
<br/>msys/<b>perl-HTTP-Message</b> 6.06-2 (perl-modules) 
    HTTP style messages
<br/>msys/<b>perl-HTTP-Negotiate</b> 6.01-2 (perl-modules) 
    choose a variant to serve
<br/>msys/<b>perl-IO-HTML</b> 1.001-1 (perl-modules)
    Open an HTML file with automatic charset detection
<br/>msys/<b>perl-IO-Socket-INET6</b> 2.72-2 (perl-modules)
    Object interface for AF_INET|AF_INET6 domain sockets
<br/>msys/<b>perl-IO-Socket-SSL</b> 2.008-1 (perl-modules) 
    Nearly transparent SSL encapsulation for IO::Socket::INET
<br/>msys/<b>perl-IO-stringy</b> 2.110-2 (perl-modules) 
    I/O on in-core objects like strings/arrays
<br/>msys/<b>perl-IPC-Run3</b> 0.048-1 (perl-modules) 
    run a subprocess with input/ouput redirection
<br/>msys/<b>perl-LWP-MediaTypes</b> 6.02-2 (perl-modules) 
    Guess the media type of a file or a URL
<br/>msys/<b>perl-LWP-Protocol-https</b> 6.06-1 (perl-modules)
    Provide https support for LWP::UserAgent
<br/>msys/<b>perl-Locale-Gettext</b> 1.05-3 (perl-modules) 
    Permits access from Perl to the gettext() family of functions
<br/>msys/<b>perl-MIME-tools</b> 5.505-2 
    Parses streams to create MIME entities
<br/>msys/<b>perl-MailTools</b> 2.13-2 
    Various e-mail related modules
<br/>msys/<b>perl-Mozilla-CA</b> 20130114-2 (perl-modules)
    Mozilla's CA cert bundle in PEM format
<br/>msys/<b>perl-Net-DNS</b> 0.77-2 (perl-modules)
    Perl Module: Interface to the DNS resolver.
<br/>msys/<b>perl-Net-HTTP</b> 6.06-2 (perl-modules) 
    Low-level HTTP connection (client)
<br/>msys/<b>perl-Net-IP</b> 1.26-2 (perl-modules)
    Perl Module: Easy manipulation of IPv4 and IPv6 addresses
<br/>msys/<b>perl-Net-SMTP-SSL</b> 1.01-2 (perl-modules) 
    SSL support for Net::SMTP
<br/>msys/<b>perl-Net-SSLeay</b> 1.64-1 (perl-modules) 
    Perl extension for using OpenSSL
<br/>msys/<b>perl-Path-Class</b> 0.33-1 (perl-modules)
    Cross-platform path specification manipulation for Perl
<br/>msys/<b>perl-Probe-Perl</b> 0.03-2 (perl-modules) 
    Information about the currently running perl
<br/>msys/<b>perl-Regexp-Common</b> 2013031301-1 (perl-modules) 
    Provide commonly requested regular expressions
<br/>msys/<b>perl-Socket6</b> 0.25-1
    A getaddrinfo/getnameinfo support module
<br/>msys/<b>perl-Sys-CPU</b> 0.61-1 (perl-modules) 
    Provide commonly requested regular expressions
<br/>msys/<b>perl-TermReadKey</b> 2.32-2 (perl-modules) 
    Provides simple control over terminal driver modes
<br/>msys/<b>perl-Test-Pod</b> 1.48-2 (perl-modules) 
    Check for POD errors in files
<br/>msys/<b>perl-Test-Script</b> 1.07-2 (perl-modules) 
    Basic cross-platform tests for scripts
<br/>msys/<b>perl-TimeDate</b> 2.30-2 
    Date formating subroutines
<br/>msys/<b>perl-Try-Tiny</b> 0.22-2 (perl-modules)
    Minimal try/catch with proper localization of $@
<br/>msys/<b>perl-URI</b> 1.65-1 (perl-modules) 
    Uniform Resource Identifiers (absolute and relative)
<br/>msys/<b>perl-WWW-RobotRules</b> 6.02-2 (perl-modules) 
    Database of robots.txt-derived permissions
<br/>msys/<b>perl-XML-LibXML</b> 2.0116-1 (perl-modules)
    Expat-based XML parser module for perl
<br/>msys/<b>perl-XML-NamespaceSupport</b> 1.11-2 (perl-modules)
    Generic namespace helpers (ported from SAX2)
<br/>msys/<b>perl-XML-Parser</b> 2.43-1 (perl-modules) 
    Expat-based XML parser module for perl
<br/>msys/<b>perl-XML-SAX</b> 0.99-2 (perl-modules)
    Simple API for XML
<br/>msys/<b>perl-XML-SAX-Base</b> 1.08-2 (perl-modules)
    Base class SAX Drivers and Filters
<br/>msys/<b>perl-XML-Simple</b> 2.20-2 (perl-modules) 
    Simple XML parser for perl
<br/>msys/<b>perl-YAML</b> 1.11-1 (perl-modules)
    Perl/CPAN Module YAML : YAML Aint Markup Language
<br/>msys/<b>perl-YAML-Syck</b> 1.27-2 (perl-modules) 
    Fast, lightweight YAML loader and dumper
<br/>msys/<b>perl-ack</b> 2.13_06-3 (perl-modules) 
    A Perl-based grep replacement, aimed at programmers with large trees of heterogeneous source code
<br/>msys/<b>perl-common-sense</b> 3.73-1 (perl-modules)
    Implements some sane defaults for Perl programs
<br/>msys/<b>perl-libwww</b> 6.08-1 (perl-modules) 
    The World-Wide Web library for Perl
<br/>msys/<b>pkg-config</b> 0.28-2 (base-devel) 
    A system for managing library compile/link flags
<br/>msys/<b>pkgconf</b> 0.9.7-1
    pkg-config compatible utility which does not depend on glib
<br/>msys/<b>pkgfile</b> 15-1 (base base-devel) 
    A pacman .files metadata explorer
<br/>msys/<b>procps</b> 3.2.8-2 (sys-utils) 
    System and process monitoring utilities
<br/>msys/<b>psmisc</b> 22.21-1 (sys-utils)
    Miscellaneous procfs tools
<br/>msys/<b>python</b> 3.3.3-4
    Next generation of the python high-level scripting language
<br/>msys/<b>python2</b> 2.7.9-3 
    A high-level scripting language
<br/>msys/<b>python2-beaker</b> 1.6.5-1
    Easily download, build, install, upgrade, and uninstall Python packages
<br/>msys/<b>python2-colorama</b> 0.3.2-1 
    Python API for cross-platform colored terminal text.
<br/>msys/<b>python2-distutils-extra</b> 2.38-1
    Enhancements to the Python build system
<br/>msys/<b>python2-fastimport</b> 0.9.4-1
    VCS fastimport/fastexport parser
<br/>msys/<b>python2-mako</b> 1.0.1-1
    A super-fast templating language that borrows the best ideas from the existing templating languages
<br/>msys/<b>python2-markupsafe</b> 0.23-1
    Implements a XML/HTML/XHTML Markup safe string for Python
<br/>msys/<b>python2-nose</b> 1.3.4-1
    A discovery-based unittest extension
<br/>msys/<b>python2-pygments</b> 2.0.2-1
    A syntax highlighting engine written in Python
<br/>msys/<b>python2-setuptools</b> 12.0.5-1 
    Easily download, build, install, upgrade, and uninstall Python packages
<br/>msys/<b>python3-beaker</b> 1.6.5-1
    Easily download, build, install, upgrade, and uninstall Python packages
<br/>msys/<b>python3-distutils-extra</b> 2.38-1
    Enhancements to the Python build system
<br/>msys/<b>python3-fastimport</b> 0.9.4-1
    VCS fastimport/fastexport parser
<br/>msys/<b>python3-mako</b> 1.0.1-1
    A super-fast templating language that borrows the best ideas from the existing templating languages
<br/>msys/<b>python3-markupsafe</b> 0.23-1
    Implements a XML/HTML/XHTML Markup safe string for Python
<br/>msys/<b>python3-nose</b> 1.3.4-1
    A discovery-based unittest extension
<br/>msys/<b>python3-pygments</b> 2.0.2-1
    A syntax highlighting engine written in Python
<br/>msys/<b>python3-setuptools</b> 12.0.5-1
    Easily download, build, install, upgrade, and uninstall Python packages
<br/>msys/<b>rarian</b> 0.8.1-1 
    Documentation meta-data library, designed as a replacement for Scrollkeeper.
<br/>msys/<b>rcs</b> 5.9.4-1 (base-devel) 
    Revision Control System: manages multiple revisions of files
<br/>msys/<b>rebase</b> 4.4.1-6 (base) 
    The Cygwin rebase distribution contains four utilities, rebase, rebaseall, peflags, and peflagsall.
<br/>msys/<b>repman-git</b> r23.87bf865-1 (base)
    Pacman repository manager
<br/>msys/<b>rsync</b> 3.1.1-1 (net-utils) 
    A file transfer program to keep remote files in sync
<br/>msys/<b>ruby</b> 2.1.5-1 
    An object-oriented language for quick and easy programming
<br/>msys/<b>ruby-docs</b> 2.1.5-1
    Documentation files for ruby
<br/>msys/<b>scons</b> 2.3.4-2 (base-devel) 
    Extensible Python-based build utility
<br/>msys/<b>sed</b> 4.2.2-2 (base base-devel) 
    GNU stream editor
<br/>msys/<b>setconf</b> 0.6.2-1 
    Utility to easily change settings in configuration files
<br/>msys/<b>sharutils</b> 4.15-1
    Makes so-called shell archives out of many files
<br/>msys/<b>sqlite</b> 3.8.8.2-1
    A C library that implements an SQL database engine
<br/>msys/<b>sqlite-doc</b> 3.8.8.2-1
    Most of the static HTML files that comprise this website, including all of the SQL Syntax and the C/C++ interface specs and other miscellaneous documentation
<br/>msys/<b>sshpass</b> 1.05-1
    Full ssh into accepting an interactive password non-interactively
<br/>msys/<b>subversion</b> 1.8.13-1 (VCS) 
    A Modern Concurrent Version Control System
<br/>msys/<b>swig</b> 3.0.5-1 (base-devel) 
    Generate scripting interfaces to C/C++ code
<br/>msys/<b>tar</b> 1.28-3 (compression) 
    Utility used to store, backup, and transport files
<br/>msys/<b>tcsh</b> 6.18.01-2
    C shell with file name completion and command line editing
<br/>msys/<b>texinfo</b> 5.2-5 (base-devel) 
    Utilities to work with and produce manuals, ASCII text, and on-line documentation from a single source file
<br/>msys/<b>texinfo-tex</b> 5.2-5 (base-devel) 
    Utilities to work with and produce manuals, ASCII text, and on-line documentation from a single source file
<br/>msys/<b>tftp-hpa</b> 5.2-1 (base)
    Official tftp server
<br/>msys/<b>tig</b> 2.0.3-1
    Text-mode interface for Git.
<br/>msys/<b>time</b> 1.7-1 (base) 
    Utility for monitoring a program's use of system resources
<br/>msys/<b>tmux-git</b> 1.9.4851.f8481f9-1
    A terminal multiplexer
<br/>msys/<b>tree</b> 1.7.0-1
    A directory listing program displaying a depth indented list of files
<br/>msys/<b>tzcode</b> 2015.b-1 (base) 
    Sources for time zone and daylight saving time data
<br/>msys/<b>ucl</b> 1.03-1
    Portable lossless data compression library written in ANSI C
<br/>msys/<b>ucl-devel</b> 1.03-1 (development)
    ucl headers and libraries
<br/>msys/<b>unrar</b> 5.2.2-1 (base-devel) 
    The RAR uncompression program
<br/>msys/<b>unzip</b> 6.0-2 (compression) 
    Unpacks .zip archives such as those made by PKZIP
<br/>msys/<b>upx</b> 3.91-1
    Ultimate executable compressor.
<br/>msys/<b>util-linux</b> 2.26.1-1 (base) 
    Collection of basic system utilities
<br/>msys/<b>util-macros</b> 1.19.0-1 (development)
    X.Org Autotools macros
<br/>msys/<b>vim</b> 7.4.691-1 (editors) 
    
<br/>msys/<b>wget</b> 1.16.3-1 (base-devel) 
    A network utility to retrieve files from the Web
<br/>msys/<b>which</b> 2.21-1 (base) 
    A utility to show the full path of commands
<br/>msys/<b>whois</b> 5.2.7-1
    The whois client by Marco d'Itri
<br/>msys/<b>windows-default-manifest</b> 6.4-1 
    Default Windows application manifest
<br/>msys/<b>winpty-git</b> 1.1.1.148.47a69d0-2 
    A Windows software package providing an interface similar to a Unix pty-master for communicating with Windows console programs
<br/>msys/<b>xmlto</b> 0.0.26-1 (base-devel) 
    Convert xml to many other formats
<br/>msys/<b>xproto</b> 7.0.26-1 (development)
    X11 core wire protocol and auxiliary headers
<br/>msys/<b>xz</b> 5.2.1-1 (compression) 
    Library and command line tools for XZ and LZMA compressed files
<br/>msys/<b>yasm</b> 1.3.0-2 
    A rewrite of NASM to allow for multiple syntax supported (NASM, TASM, GAS, etc.)
<br/>msys/<b>yasm-devel</b> 1.3.0-2 
    A rewrite of NASM to allow for multiple syntax supported (NASM, TASM, GAS, etc.)
<br/>msys/<b>yelp-tools</b> 3.14.1-1 
    Tools for creating Yelp documentation
<br/>msys/<b>yelp-xsl</b> 3.16.0-1 
    Stylesheets for Yelp
<br/>msys/<b>zip</b> 3.0-1 
    Creates PKZIP-compatible .zip files
<br/>msys/<b>zlib</b> 1.2.8-3 (libraries) 
    Compression library implementing the deflate compression method found in gzip and PKZIP
<br/>msys/<b>zlib-devel</b> 1.2.8-3 (development) 
    zlib headers and libraries
<br/>msys/<b>zsh</b> 5.0.7-4 
    A very advanced and programmable command interpreter (shell) for UNIX
<br/>msys/<b>zsh-doc</b> 5.0.7-4
    Info, HTML and PDF format of the ZSH documentation
