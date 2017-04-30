This is a dump from `pacman` of all the packages we provide as of 2017-03-05. The commands used to generate this list are:

```
LANG=C pacman -Ss | grep '^mingw64/' -A 1 | sed -r -e 's/\[installed.*\]//' -e 's#^mingw64/([^ ]+)#<br/>mingw/<b>\1</b>#' -e 's/-x86_64//' -e 's/$/<br\/>/'
LANG=C pacman -Ss | grep '^msys/' -A 1 | sed -r -e 's/\[installed.*\]//' -e 's#^msys/([^ ]+)#<br/>msys/<b>\1</b>#' -e 's/$/<br\/>/'
```

<br/>mingw/<b>mingw-w64-OpenSceneGraph</b> 3.5.5-3<br/>
    Open source high performance 3D graphics toolkit (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-OpenSceneGraph-debug</b> 3.5.5-3<br/>
    Open source high performance 3D graphics toolkit (debug) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-SDL</b> 1.2.15-7<br/>
    A library for portable low-level access to a video framebuffer, audio output, mouse, and keyboard (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-SDL2</b> 2.0.5-1<br/>
    A library for portable low-level access to a video framebuffer, audio output, mouse, and keyboard (Version 2) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-SDL2_gfx</b> 1.0.1-2<br/>
    SDL graphics drawing primitives and other support functions wrapped up in an addon library for the Simple Direct Media (SDL) cross-platform API layer<br/>
<br/>mingw/<b>mingw-w64-SDL2_image</b> 2.0.1-1<br/>
    A simple library to load images of various formats as SDL surfaces (Version 2)<br/>
<br/>mingw/<b>mingw-w64-SDL2_mixer</b> 2.0.1-3<br/>
    A simple multi-channel audio mixer (Version 2) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-SDL2_net</b> 2.0.1-1<br/>
    A small sample cross-platform networking library (Version 2) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-SDL2_ttf</b> 2.0.14-1<br/>
    A library that allows you to use TrueType fonts in your SDL applications (Version 2) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-SDL_gfx</b> 2.0.25-3<br/>
    SDL Graphic Primitives (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-SDL_image</b> 1.2.12-4<br/>
    A simple library to load images of various formats as SDL surfaces (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-SDL_mixer</b> 1.2.12-5<br/>
    A simple multi-channel audio mixer (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-SDL_net</b> 1.2.8-1<br/>
    A small sample cross-platform networking library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-SDL_ttf</b> 2.0.11-4<br/>
    A library that allows you to use TrueType fonts in your SDL applications (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-a52dec</b> 0.7.4-3<br/>
    A free library for decoding ATSC A/52 streams (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-adns</b> 1.4.g10.7-1 <br/>
    adns is an asyncronous replacement resolver library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-adwaita-icon-theme</b> 3.22.0-1 <br/>
    GNOME icon theme (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ag</b> 0.31.0.r1666.0e577cc-1<br/>
    The Silver Searcher: An attempt to make something better than ack, which itself is better than grep (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-allegro</b> 5.1.13.1-1<br/>
    Portable library mainly aimed at video game and multimedia programming (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-angleproject-git</b> 2.1.r5684-1 <br/>
    ANGLE project built from git source (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ansicon-git</b> 1.70.r65.3acc7a9-2 <br/>
    Process ANSI escape sequences for Windows console programs (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-antiword</b> 0.37-2<br/>
    Convert MS Word 2.0-2003 documents to plain text or PostScript (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-antlr3</b> 3.5.2-1<br/>
    ANother Tool for Language Recognition (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-antlr4-runtime-cpp</b> 4.6-1<br/>
    ANother Tool for Language Recognition v4 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-apr</b> 1.5.2-2 <br/>
    The Apache Portable Runtime (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-apr-util</b> 1.5.4-2 <br/>
    The Apache Portable Runtime (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-aria2</b> 1.24.0-1 <br/>
    A multi-protocol & multi-source, cross platform download utility (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-aribb24</b> 1.0.3-2<br/>
    A library for ARIB STD-B24, decoding JIS 8 bit characters and parsing MPEG-TS stream (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-armadillo</b> 7.500.0-1<br/>
    C++ linear algebra library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-arpack</b> 3.4.0-1<br/>
    Fortran77 subroutines designed to solve large scale eigenvalue problems (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-aspell</b> 0.60.7.20131207-3 <br/>
    A spell checker designed to eventually replace Ispell (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-aspell-de</b> 20030222-1<br/>
    German dictionary for aspell (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-aspell-en</b> 7.1-1<br/>
    English dictionary for aspell (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-aspell-es</b> 1.11.2-1<br/>
    Spanish dictionary for aspell (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-aspell-fr</b> 0.50-1<br/>
    French dictionary for aspell (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-aspell-ru</b> 0.99f7.1-1<br/>
    Russian dictionary for aspell (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-assimp</b> 3.3.1-1 <br/>
    Portable Open Source library to import various well-known 3D model formats in an uniform manner (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-astyle</b> 2.05.1-2<br/>
    A free, fast and small automatic formatter for C, C++, C#, and Java source code (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-atk</b> 2.22.0-1 <br/>
    A library providing a set of interfaces for accessibility (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-atkmm</b> 2.24.2-2<br/>
    C++ bindings for atk (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-avrdude</b> 6.3-1<br/>
    Software for programming Atmel AVR Microcontrollers (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-aztecgen</b> 1.0.1-1<br/>
    A simple library for encoding "Aztec Code" barcodes (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-babl</b> 0.1.24-1<br/>
    Dynamic Pixel Format Translation Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-badvpn</b> 1.999.130-2<br/>
    NCD scripting language, tun2socks proxifier, P2P VPN (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-binutils</b> 2.27-5 (mingw-w64-x86_64-toolchain) <br/>
    A set of programs to assemble and manipulate binary and object files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-blender</b> 2.78.c-1<br/>
    A fully integrated 3D graphics creation suite (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-boost</b> 1.63.0-1 <br/>
    Free peer-reviewed portable C++ source libraries (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-box2d</b> 2.3.1-1<br/>
    2D rigid body simulation library for games (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-breakpad-git</b> r1451.8915f7b-1<br/>
    An open-source multi-platform crash reporting system (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-breakpad-svn</b> r1471-1<br/>
    An open-source multi-platform crash reporting system (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-bsdfprocessor</b> 1.1.6-1<br/>
    Application for displaying and editing of BSDF files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-bullet</b> 2.85-1<br/>
    A 3D Collision Detection and Rigid Body Dynamics Library for games and animation (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-bullet-debug</b> 2.85-1<br/>
    A 3D Collision Detection and Rigid Body Dynamics Library for games and animation (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-bwidget</b> 1.9.10-1<br/>
    A companion to Tcllib, for Tk related packages (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-bzip2</b> 1.0.6-6 <br/>
    A high-quality data compression program (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-c-ares</b> 1.12.0-1 <br/>
    C library that performs DNS requests and name resolves asynchronously (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-c99-to-c89-git</b> r169.b3d496d-1<br/>
    Tool to convert C99 code to MSVC-compatible C89 (git) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ca-certificates</b> 20150426-2 <br/>
    Common CA certificates (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-cairo</b> 1.15.4-4 <br/>
    Cairo vector graphics library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-cairomm</b> 1.12.0-2<br/>
    C++ bindings to Cairo vector graphics library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-catch</b> 1.6.0-1<br/>
    Multi-paradigm automated test framework for C++ and Objective-C (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ccache</b> 3.3.3-1<br/>
    A compiler cache (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-cego</b> 2.32.7-1<br/>
    Cego database system (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-celt</b> 0.11.3-3<br/>
    Low-latency audio communication codec (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-cereal</b> 1.1.2-1<br/>
    A C++11 library for serialization (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ceres-solver</b> 1.12.0-1<br/>
    A large scale non-linear optimization library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-cfitsio</b> 3.380-1<br/>
    A library of C and Fortran subroutines for reading and writing data files in FITS (Flexible Image Transport System) data format (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-cgal</b> 4.9-1<br/>
    Computational Geometry Algorithms Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-check</b> 0.10.0-1<br/>
    A unit testing framework for C (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-chipmunk</b> 6.2.2-1<br/>
    A high-performance 2D rigid body physics library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-chromaprint</b> 1.4-1<br/>
    Library that implements a custom algorithm for extracting fingerprints from any audio source (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-clang</b> 3.9.1-3 <br/>
    C language family frontend for LLVM (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-clang-analyzer</b> 3.9.1-3<br/>
    A source code analysis framework (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-clang-analyzer35</b> 3.5.2-1<br/>
    A source code analysis framework<br/>
<br/>mingw/<b>mingw-w64-clang-tools-extra</b> 3.9.1-3<br/>
    Extra tools built using Clang's tooling APIs (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-clang-tools-extra35</b> 3.5.2-1<br/>
    Extra tools built using Clang's tooling APIs<br/>
<br/>mingw/<b>mingw-w64-clang35</b> 3.5.2-1<br/>
    C language family frontend for LLVM<br/>
<br/>mingw/<b>mingw-w64-clucene</b> 2.3.3.4-1<br/>
    CLucene - a C++ search engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-clutter</b> 1.26.0-1<br/>
    A GObject based library for creating fast, visually rich graphical user interfaces (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-clutter-gst</b> 3.0.20-1<br/>
    A GStreamer integration library for Clutter (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-clutter-gtk</b> 1.8.2-1<br/>
    Clutter integration with GTK+ (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-cmake</b> 3.7.2-2 <br/>
    A cross-platform open-source make system (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-codelite-git</b> 10.0.28.g1f1e42b-1<br/>
    Open-source, cross platform IDE for the C/C++ programming languages (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-cogl</b> 1.22.2-1<br/>
    An object oriented GL/GLES Abstraction/Utility Layer (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-collada-dom-svn</b> 2.4.1.r889-6<br/>
    API that provides a C++ object representation of a COLLADA XML instance document (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-compiler-rt</b> 3.9.1-3<br/>
    Runtime libraries for Clang and LLVM (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-confuse</b> 2.8-1<br/>
    Library for parsing configuration files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-connect</b> 1.104-1<br/>
    Make socket connection using SOCKS4/5 and HTTP tunnel (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-cotire</b> 1.7.9_3.7-1<br/>
    CMake module to speed up builds (automated PCH, unity builds). (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-cppcheck</b> 1.76.1-1<br/>
    static analysis of C/C++ code (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-cpptest</b> 1.1.2-1<br/>
    A C++ Unit Testing Framework (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-cppunit</b> 1.13.2-5 <br/>
    A C++ unit testing framework (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-creduce</b> 2.4.0-1<br/>
    A C program reducer (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-crt-git</b> 5.0.0.4795.e3d96cb1-1 (mingw-w64-x86_64-toolchain) <br/>
    MinGW-w64 CRT for Windows<br/>
<br/>mingw/<b>mingw-w64-crypto++</b> 5.6.5-1<br/>
    Crypto++ Library is a free C++ class library of cryptographic schemes (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-csfml</b> 2.3-4<br/>
    A simple, fast, cross-platform, and object-oriented multimedia API for C (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ctags</b> 5.8-4 <br/>
    A multilanguage implementation of Ctags (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ctpl-git</b> 0.3.3.391.6dd5c14-1 <br/>
    C Template (Parser) Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-cunit</b> 2.1.3-2<br/>
    Lightweight system for writing, administering, and running unit tests in C (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-curl</b> 7.53.1-1 <br/>
    An URL retrival utility and library. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-cyrus-sasl</b> 2.1.26-5<br/>
    Cyrus Simple Authentication Service Layer (SASL) library<br/>
<br/>mingw/<b>mingw-w64-cython</b> 0.25.2-1<br/>
    C-Extensions for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-cython2</b> 0.25.2-1<br/>
    C-Extensions for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-d-feet</b> 0.3.10-1<br/>
    D-Bus debugger for GNOME (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-daala-git</b> r1373.efb96ed-1<br/>
    Daala is next-next-gen video compression technology from Xiph.org, Mozilla and others (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-db</b> 6.0.19-3<br/>
    The Berkeley DB embedded database system (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-dbus</b> 1.10.16-1 <br/>
    Freedesktop.org message bus system (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-dbus-glib</b> 0.108-1 <br/>
    D-Bus Message Bus System (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-dcadec</b> 0.2.0-1<br/>
    dcadec is a free DTS Coherent Acoustics decoder with support for HD extensions (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-dcadec-git</b> 0.0.0.207.2a9186e-4<br/>
    dcadec is a free DTS Coherent Acoustics decoder with support for HD extensions (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-devcon-git</b> r35.818f6ee-1<br/>
    Search for and manipulate devices (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-devhelp</b> 3.8.2-2<br/>
    Remote desktop client for the GNOME Desktop (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-devil</b> 1.8.0-2<br/>
    Library for reading several different image formats (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-diffutils</b> 3.3-2<br/>
    GNU Diffutils is a package of several programs related to finding differences between files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-discount</b> 2.2.2-1<br/>
    A Markdown implementation written in C (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-distorm</b> 3.3.0-1<br/>
    Powerful disassembler library for x86/AMD64 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-djvulibre</b> 3.5.27-1 <br/>
    Suite to create, manipulate and view DjVu (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-dlfcn</b> 1.0.0-2<br/>
    A wrapper for dlfcn to the Win32 API (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-dmake</b> 4.12.2-6<br/>
    Dmake is a make utility similar to GNU make or the Workshop dmake (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-dnscrypt-proxy</b> 1.6.0-2<br/>
    A tool for securing communications between a client and a DNS resolver (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-docbook-dsssl</b> 1.79-1<br/>
    DSSSL Stylesheets for DocBook (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-docbook-mathml</b> 1.1CR1-1<br/>
    MathML XML scheme (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-docbook-sgml</b> 4.5-1<br/>
    Document type definitions for verification of SGML data files against the DocBook rule set. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-docbook-sgml31</b> 3.1-1<br/>
    Legacy docbook-sgml (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-docbook-xml</b> 5.0-1<br/>
    A widely used XML scheme for writing documentation and help<br/>
<br/>mingw/<b>mingw-w64-docbook-xsl</b> 1.79.1-1<br/>
    XML stylesheets for Docbook-xml transformations (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-doxygen</b> 1.8.13-1<br/>
    A documentation system for C++, C, Java, IDL and PHP (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-drmingw</b> 0.8.1-1 <br/>
    Just-in-Time (JIT) debugger (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-dumb</b> 0.9.3-4<br/>
    IT, XM, S3M and MOD player library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-edd-dbg</b> 0.2.1-2<br/>
    C++ library of debugging tools for OS X and Windows (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-edd-fungo</b> 0.2.4-1<br/>
    C++ library for storing and re-throwing exceptions (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-editrights</b> 1.03-3<br/>
    Edit special privileges of Windows accounts (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-eigen3</b> 3.3.0-1<br/>
    Lightweight C++ template library for vector and matrix math (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-emacs</b> 25.1-1<br/>
    The extensible, customizable, self-documenting, real-time display editor (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-enca</b> 1.19-1<br/>
    Charset analyser and converter (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-enchant</b> 1.6.0-11 <br/>
    Enchanting Spell Checking Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-enet</b> 1.3.13-1<br/>
    Reliable UDP networking library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-eog</b> 3.16.3-1<br/>
    Eye of GNOME graphics viewer program (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-eog-plugins</b> 3.16.3-1<br/>
    Eye of GNOME graphics viewer program - plugins (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-evince</b> 3.22.1-3<br/>
    Document (PostScript, PDF) viewer (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-exiv2</b> 0.25-2<br/>
    Exif and Iptc metadata manipulation library and tools (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-expat</b> 2.2.0-2 <br/>
    An XML parser library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-extra-cmake-modules</b> 5.20.0-1<br/>
    Extra CMake modules (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-faac</b> 1.28-2<br/>
    FAAC is an AAC audio encoder (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-faad2</b> 2.7-2<br/>
    ISO AAC audio decoder (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-farstream</b> 0.2.7-2<br/>
    Farstream (formerly Farsight) - Audio/Video Communications Framework (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-fdk-aac</b> 0.1.4-1<br/>
    A standalone library of the Fraunhofer FDK AAC code from Android (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ffmpeg</b> 3.2.4-1<br/>
    Complete and free Internet live audio and video broadcasting solution (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-fftw</b> 3.3.5-1 <br/>
    A library for computing the discrete Fourier transform (DFT) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-field3d</b> 1.7.2-2<br/>
    Open source library for storing voxel data (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-firebird2-git</b> 2.5.6.26956.c3587aa-1<br/>
    Cross-platform relational database offering many ANSI SQL standard features - version 2.x (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-flac</b> 1.3.2-1<br/>
    Free Lossless Audio Codec (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-flatbuffers</b> 1.6.0-1<br/>
    Memory Efficient Serialization Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-flexdll</b> 0.34-2<br/>
    An implementation of a dlopen-like API for Windows (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-flickcurl</b> 1.26-1<br/>
    Flickcurl is a C library for the Flickr API (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-fltk</b> 1.3.4-1<br/>
    C++ user interface toolkit (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-fluidsynth</b> 1.1.6-3<br/>
    A real-time software synthesizer based on the SoundFont 2 specifications (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-fontconfig</b> 2.12.1-1 <br/>
    A library for configuring and customizing font access (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-fossil</b> 1.36-2 <br/>
    Simple, high-reliability, distributed software configuration management (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-fox</b> 1.6.53-1 (mingw-w64-x86_64)<br/>
    C++ user interface toolkit (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-freeglut</b> 3.0.0-4 <br/>
    Freeglut allows the user to create and manage windows containing OpenGL contexts (mingw32-w64)<br/>
<br/>mingw/<b>mingw-w64-freeimage</b> 3.17.0-3<br/>
    Library project for developers who would like to support popular graphics image formats (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-freetype</b> 2.7.1-1 <br/>
    TrueType font rendering library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-fribidi</b> 0.19.7-1 <br/>
    A Free Implementation of the Unicode Bidirectional Algorithm (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ftgl</b> 2.1.3rc5-2<br/>
    OpenGL library to use arbitrary fonts (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gc</b> 7.4.2-2 <br/>
    A garbage collector for C and C++ (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gcc</b> 6.3.0-2 (mingw-w64-x86_64-toolchain) <br/>
    GNU Compiler Collection (C,C++,OpenMP) for MinGW-w64<br/>
<br/>mingw/<b>mingw-w64-gcc-ada</b> 6.3.0-2 (mingw-w64-x86_64-toolchain) <br/>
    GNU Compiler Collection (Ada) for MinGW-w64<br/>
<br/>mingw/<b>mingw-w64-gcc-fortran</b> 6.3.0-2 (mingw-w64-x86_64-toolchain) <br/>
    GNU Compiler Collection (Fortran) for MinGW-w64<br/>
<br/>mingw/<b>mingw-w64-gcc-libgfortran</b> 6.3.0-2 (mingw-w64-x86_64-toolchain) <br/>
    GNU Compiler Collection (libgfortran) for MinGW-w64<br/>
<br/>mingw/<b>mingw-w64-gcc-libs</b> 6.3.0-2 (mingw-w64-x86_64-toolchain) <br/>
    GNU Compiler Collection (libraries) for MinGW-w64<br/>
<br/>mingw/<b>mingw-w64-gcc-objc</b> 6.3.0-2 (mingw-w64-x86_64-toolchain) <br/>
    GNU Compiler Collection (ObjC,Obj-C++) for MinGW-w64<br/>
<br/>mingw/<b>mingw-w64-gd</b> 2.1.1-3<br/>
    Library for the dynamic creation of images by programmers (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gdal</b> 2.1.3-2<br/>
    A translator library for raster geospatial data formats (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gdb</b> 7.12.1-1 (mingw-w64-x86_64-toolchain) <br/>
    GNU Debugger (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gdbm</b> 1.12-1 <br/>
    GNU database library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gdk-pixbuf2</b> 2.36.5-2 <br/>
    An image loading library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gdl</b> 3.22.0-1<br/>
    GNOME Docking Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gdl2</b> 2.31.2-2<br/>
    GNOME Docking Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gdlmm2</b> 2.30.0-2<br/>
    GNOME Docking Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-geany</b> 1.29-1 <br/>
    Fast and lightweight IDE (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-geany-plugins</b> 1.29-1 <br/>
    Plugins for Geany (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gedit</b> 3.20.2-2<br/>
    A text editor for GNOME (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gedit-plugins</b> 3.20.0-1<br/>
    Collection of plugins for the gedit Text Editor (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gegl</b> 0.3.12-1<br/>
    Generic Graphics Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-geoclue</b> 0.12.99-3 <br/>
    Modular Geoinformation Service (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-geocode-glib</b> 3.20.1-1<br/>
    geocoding and reverse geocoding GLib library using Yahoo! Place Finder (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-geoip2-database</b> 20150720-1<br/>
    GeoLite country geolocation database compiled by MaxMind (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-geos</b> 3.6.1-1<br/>
    C++ port of the Java Topology Suite (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gettext</b> 0.19.8.1-2 <br/>
    GNU internationalization library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gexiv2</b> 0.10.3-3<br/>
    GObject-based wrapper around the Exiv2 library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gflags</b> 2.2.0-1<br/>
    Google's Commandline flags module for C++ (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ghex</b> 3.18.3-1<br/>
    GNOME Hex editor for files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ghostscript</b> 9.20-1 <br/>
    An interpreter for the PostScript language (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-giflib</b> 5.1.4-1 <br/>
    A library for reading and writing gif images (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gimp</b> 2.9.4-5<br/>
    GNU Image Manipulation Program (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gimp-ufraw</b> 0.22-1 (mingw-w64-x86_64-gimp-plugins)<br/>
    Converter for raw files; utility and GIMP plugin (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-git-repo</b> 0.4.10-1 (mingw-w64-x86_64)<br/>
    The multiple Git repository tool (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gitg</b> 3.22.0-1<br/>
    git repository viewer for GTK+/GNOME (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gl2ps</b> 1.3.8-4<br/>
    an OpenGL to PostScript printing library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-glade</b> 3.20.0-2<br/>
    User interface builder for GTK+ and GNOME (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-glade3</b> 3.8.5-2<br/>
    User interface builder for GTK+ and GNOME (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-glbinding</b> 2.1.1-2<br/>
    A C++ binding for the OpenGL API, generated using the gl.xml specification (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-glew</b> 2.0.0-1<br/>
    GLEW, The OpenGL Extension Wrangler Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-glfw</b> 3.2.1-2<br/>
    A free, open source, portable framework for OpenGL application development (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-glib-networking</b> 2.50.0-1 <br/>
    Network-related GIO modules for glib (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-glib2</b> 2.50.3-2 <br/>
    Common C routines used by GTK+ 2.4 and other libs (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-glibmm</b> 2.50.0-1<br/>
    Glib-- (glibmm) is a C++ interface for glib (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-glm</b> 0.9.8.3-1<br/>
    C++ mathematics library for 3D software based on the OpenGL Shading Language (GLSL) specification (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-global</b> 6.5.3-1<br/>
    GNU GLOBAL source code tagging system (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-globjects</b> 1.0.0-1<br/>
    Cross-platform C++ wrapper for OpenGL API objects. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-glog</b> 0.3.4.4d391fe-3<br/>
    C++ implementation of the Google logging module (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-glpk</b> 4.61-1<br/>
    GNU Linear Programming Kit: solve LP, MIP and other problems (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-glsl-optimizer-git</b> r66905.5cee0ef05b-1<br/>
    C++ library that takes GLSL shaders, does some GPU-independent optimizations on them and outputs GLSL back (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-glslang</b> 3.0.git2.eee9d53-1<br/>
    An OpenGL and OpenGL ES shader front end and validator (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gmime</b> 2.6.20-2<br/>
    Glorious MIME Utility Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gmp</b> 6.1.2-1 <br/>
    A free library for arbitrary precision arithmetic (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gnome-common</b> 3.18.0-1 <br/>
    Common development macros for GNOME (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gnonlin</b> 1.4.0-1<br/>
    GStreamer Non-Linear plugins (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gnu-cobol-svn</b> 2.0.r599-2<br/>
    GNU Cobol is a free, modern COBOL compiler (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gnupg</b> 2.1.16-1 <br/>
    GNU Privacy Guard - a PGP replacement tool (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gnutls</b> 3.5.8-2 <br/>
    A library which provides a secure layer over a reliable transport layer (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-go</b> 1.8-1<br/>
    Go Lang (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gobject-introspection</b> 1.50.0-2 <br/>
    Introspection system for GObject-based libraries (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gobject-introspection-runtime</b> 1.50.0-2 <br/>
    Introspection system for GObject-based libraries - runtime files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-goocanvas</b> 2.0.2-4<br/>
    Canvas widget for GTK+ that uses the Cairo 2D library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-googletest-git</b> r975.aa148eb-1<br/>
    Google Test (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gpgme</b> 1.6.0-2 <br/>
    A C wrapper library for GnuPG (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gplugin</b> 0.0.21-3<br/>
    A GObject based library that implements a reusable plugin system (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-graphene</b> 1.4.0-2<br/>
    A thin layer of types for graphic libraries (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-graphicsmagick</b> 1.3.25-2<br/>
    An image viewing/manipulation program (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-graphite2</b> 1.3.9-1 <br/>
    Font rendering capabilities for complex non-Roman writing systems (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-grpc</b> 1.1.0pre1-1<br/>
    gRPC - Google's high performance, open source, general RPC framework (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gsasl</b> 1.8.0-4<br/>
    Simple Authentication and Security Layer framework and a few common SASL mechanisms (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gsettings-desktop-schemas</b> 3.22.0-1 <br/>
    Shared GSettings schemas for the desktop (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gsl</b> 2.1-1 <br/>
    The GNU Scientific Library (GSL) is a modern numerical library for C and C++ programmers (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gsm</b> 1.0.14-1<br/>
    Shared libraries for GSM 06.10 lossy speech compression (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gspell</b> 1.0.3-1<br/>
    Spell-checking library for GTK+ (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gss</b> 1.0.3-1<br/>
    GNU Generic Security Service (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gst-editing-services</b> 1.10.2-1<br/>
    GStreamer Editing Services (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gst-libav</b> 1.10.2-1<br/>
    GStreamer libav (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gst-plugins-bad</b> 1.10.2-1<br/>
    GStreamer Multimedia Framework Bad Plugins (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gst-plugins-base</b> 1.10.2-1 <br/>
    GStreamer Multimedia Framework Base Plugins (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gst-plugins-good</b> 1.10.2-1<br/>
    GStreamer Multimedia Framework Base Plugins (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gst-plugins-ugly</b> 1.10.2-1<br/>
    GStreamer Multimedia Framework Ugly Plugins (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gst-python</b> 1.10.2-1<br/>
    GStreamer GObject Introspection overrides for Python 3 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gst-rtsp-server</b> 1.10.2-1<br/>
    GStreamer RTSP server library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gstreamer</b> 1.10.2-1 <br/>
    GStreamer Multimedia Framework (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gtest</b> 1.7.0-1<br/>
    Google Test<br/>
<br/>mingw/<b>mingw-w64-gtk-engine-murrine</b> 0.98.2-2<br/>
    GTK2 engine to make your desktop look like a 'murrina', an italian word meaning the art glass works done by Venicians glass blowers. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gtk-engine-unico</b> 1.0.2-2 <br/>
    Unico GTK3 theme engine<br/>
<br/>mingw/<b>mingw-w64-gtk-engines</b> 2.21.0-2<br/>
    Theme engines for GTK+ 2 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gtk-vnc</b> 0.6.0-1<br/>
    VNC viewer widget for GTK+ (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gtk2</b> 2.24.31-4 <br/>
    GTK+ is a multi-platform toolkit (v2) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gtk3</b> 3.22.8-1 <br/>
    GObject-based multi-platform GUI toolkit (v3) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gtkglext</b> 1.2.0-3<br/>
    opengl extensions for gtk2 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gtkimageview</b> 1.6.4-3<br/>
    Simple image viewer widget for GTK2 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gtkmm</b> 2.24.4-4<br/>
    C++ bindings for gtk2 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gtkmm3</b> 3.22.0-1<br/>
    C++ bindings for gtk3 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gtksourceview2</b> 2.10.5-3<br/>
    A text widget adding syntax highlighting and more to GNOME (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gtksourceview3</b> 3.20.4-1 <br/>
    A text widget adding syntax highlighting and more to GNOME (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gtksourceviewmm3</b> 3.18.0-1<br/>
    C++ bindings to gtksourceview3 library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gtkspell</b> 2.0.16-5 <br/>
    Provides word-processor-style highlighting and replacement of misspelled words in a GtkTextView widget (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gtkspell3</b> 3.0.9-1<br/>
    Provides word-processor-style highlighting and replacement of misspelled words in a GtkTextView widget (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-gtkwave</b> 3.3.79-1<br/>
    GTKWaveGTKWave is a fully featured GTK+ based wave viewer for Unix, Win32, and Mac OSX<br/>
<br/>mingw/<b>mingw-w64-gxml</b> 0.12.0-1<br/>
    GObject Libxml2 wrapper and Serializer Framework (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-harfbuzz</b> 1.3.4-1 <br/>
    OpenType text shaping engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-hclient-git</b> 37.efd8c0a-1<br/>
    Sample GUI for communicating with HIDs (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-hdf5</b> 1.8.16-4 <br/>
    General purpose library and file format for storing scientific data<br/>
<br/>mingw/<b>mingw-w64-headers-git</b> 5.0.0.4797.31e66d7e-1 (mingw-w64-x86_64-toolchain) <br/>
    MinGW-w64 headers for Windows<br/>
<br/>mingw/<b>mingw-w64-hicolor-icon-theme</b> 0.15-2 <br/>
    Freedesktop.org Hicolor icon theme (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-hidapi</b> 0.8.0rc1-3<br/>
    Library for communicating with USB and Bluetooth HID devices (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-hlsl2glsl-git</b> r848.957cd20-1<br/>
    HLSL to GLSL shader language translator<br/>
<br/>mingw/<b>mingw-w64-http-parser</b> 2.7.1-1 <br/>
    Parser for HTTP Request/Response written in C (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-hunspell</b> 1.6.0-1 <br/>
    Spell checker and morphological analyzer library and program (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-hunspell-en</b> 2016.11.20-2<br/>
    Hunspell dictionaries (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-hyphen</b> 2.8.8-1<br/>
    library for high quality hyphenation and justification (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-hyphen-en</b> 2.8.8-1<br/>
    English hyphenation rules<br/>
<br/>mingw/<b>mingw-w64-iconv</b> 1.14-6 <br/>
    Character encoding conversion utility (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-icoutils</b> 0.31.0-2<br/>
    Create and extract MS Windows icons and cursors (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-icu</b> 57.1-2 <br/>
    International Components for Unicode library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-icu-debug-libs</b> 57.1-2 <br/>
    International Components for Unicode library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-id3lib</b> 3.8.3-2<br/>
    Library for reading, writing, and manipulating ID3v1 and ID3v2 tags (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ilmbase</b> 2.2.0-3 <br/>
    Base libraries from ILM for OpenEXR (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-imagemagick</b> 7.0.5.0-1 <br/>
    An image viewing/manipulation program (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-indent</b> 2.2.11-4<br/>
    C language source code formatting program (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-inkscape</b> 0.92.1-3<br/>
    Vector graphics editor using the SVG file format (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-innoextract</b> 1.6-2<br/>
    A tool to extract installers created by Inno Setup (mingw-w64).<br/>
<br/>mingw/<b>mingw-w64-intel-tbb</b> 1~2017_20161128-1 <br/>
    High level abstract threading library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-irrlicht</b> 1.8.3-1<br/>
    An open source high performance realtime 3D graphics engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-isl</b> 0.17.1-1 <br/>
    Library for manipulating sets and relations of integer points bounded by linear constraints (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-iso-codes</b> 3.74-1<br/>
    Lists of the country, language, and currency names (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-jansson</b> 2.9-1 <br/>
    A C library for encoding, decoding and manipulating JSON data (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-jasper</b> 2.0.10-1 <br/>
    A software-based implementation of the codec specified in the emerging JPEG-2000 Part-1 standard (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-jbigkit</b> 2.1-3 <br/>
    Data compression library/utilities for bi-level high-resolution images (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-jemalloc</b> 4.4.0-1<br/>
    General-purpose scalable concurrent malloc implementation (mingw64)<br/>
<br/>mingw/<b>mingw-w64-jpegoptim</b> 1.4.4-1<br/>
    Utility to optimize jpeg files<br/>
<br/>mingw/<b>mingw-w64-jq</b> 1.5-3<br/>
    Command-line JSON processor (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-json-c</b> 0.12-2<br/>
    A JSON implementation in C.<br/>
<br/>mingw/<b>mingw-w64-json-glib</b> 1.2.2-1 <br/>
    JSON-GLib implements a full suite of JSON-related tools using GLib and GObject (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-jsoncpp</b> 1.8.0-1 <br/>
    A C++ library for interacting with JSON (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-jxrlib</b> 1.1-1<br/>
    Open source implementation of jpegxr (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-kicad-git</b> r5971.ba32ccb-1<br/>
    Software for the creation of electronic schematic diagrams and printed circuit board artwork (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-kiss_fft</b> 1.3.0-2<br/>
    A Fast Fourier Transform based up on the principle: Keep It Simple, Stupid (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-kqoauth-qt4</b> 0.98-3<br/>
    kQOAuth is a library written in C++ for Qt that implements the OAuth 1.0 authentication specification RFC 5849 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-l-smash</b> 2.9.1-2<br/>
    Loyal to Spec of Mpeg4 and Ad-hoc Simple Hackwork. Yet another opensource mp4 handler (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ladspa-sdk</b> 1.13-2<br/>
    Linux Audio Developer's Simple Plugin API (LADSPA) SDK (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lame</b> 3.99.5-4<br/>
    A high quality MPEG Audio Layer III (MP3) encoder (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lapack</b> 3.6.1-1<br/>
    Linear Algebra PACKage (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-laszip</b> 2.2.0-1<br/>
    Free and lossless LiDAR compression (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-latexila</b> 3.22.0-1<br/>
    LaTeX editor designed for the GNOME desktop (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lcms</b> 1.19-5<br/>
    Lightweight color management development library/engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lcms2</b> 2.8-1 <br/>
    Small-footprint color management engine, version 2 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lcov</b> 1.12-1<br/>
    front-end for GCC's coverage testing tool gcov<br/>
<br/>mingw/<b>mingw-w64-ldns</b> 1.6.17-4<br/>
    Fast DNS library supporting recent RFCs (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lensfun</b> 0.3.2-1<br/>
    Database of photographic lenses and a library that allows advanced access to the database (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-leptonica</b> 1.73-1<br/>
    Leptonica library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lfcbase</b> 1.8.11-1<br/>
    LFC C++ base classes (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lfcxml</b> 1.2.4-2<br/>
    LFC C++ xml classes (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libarchive</b> 3.2.2-4 <br/>
    library that can create and read several streaming archive formats (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libart_lgpl</b> 2.3.21-1<br/>
    Library for high-performance 2D graphics (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libass</b> 0.13.6-1<br/>
    A portable library for SSA/ASS subtitles rendering (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libassuan</b> 2.4.3-1 <br/>
    A IPC library used by some GnuPG related software (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libatomic_ops</b> 7.4.2-2 <br/>
    Provides semi-portable access to hardware provided atomic memory operations (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libbluray</b> 0.9.3-1<br/>
    Library to access Blu-Ray disks for video playback (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libbotan</b> 2.0.1-1<br/>
    Botan is a C++ cryptography library released under the permissive Simplified BSD license. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libbs2b</b> 3.1.0-1<br/>
    Bauer stereophonic-to-binaural DSP effect library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libbsdf</b> 0.9.4-1<br/>
    Library for handling BSDF files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libc++</b> 3.9.1-3<br/>
    C++ Standard Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libc++abi</b> 3.9.1-3<br/>
    C++ Standard Library Support (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libcaca</b> 0.99.beta19-2<br/>
    Color AsCii Art library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libcddb</b> 1.3.2-3<br/>
    Library that implements the different protocols (CDDBP, HTTP, SMTP) to access data on a CDDB server (e.g. http://freedb.org).<br/>
<br/>mingw/<b>mingw-w64-libcdio</b> 0.94-1<br/>
    GNU Compact Disc Input and Control Library<br/>
<br/>mingw/<b>mingw-w64-libcdio-paranoia</b> 10.2+0.93+1-2<br/>
    CD paranoia libraries from libcdio (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libcdr</b> 0.1.3-2<br/>
    libcdr is a library and a set of tools for reading and converting binary files produced by Corel DRAW (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libcerf</b> 1.5-1<br/>
    Complex error functions, Dawson, Faddeeva, and Voigt function (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libchamplain</b> 0.12.13-1<br/>
    C library providing ClutterActor to display maps (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libconfig</b> 1.5-1<br/>
    C/C++ Configuration File Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libcroco</b> 0.6.11-2 <br/>
    A CSS parsing library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libdca-svn</b> r91-2<br/>
    Free library for decoding DTS Coherent Acoustics streams (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libdvbpsi</b> 1.3.0-1<br/>
    A library designed for decoding and generation of MPEG TS and DVB PSI tables (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libdvdcss</b> 1.4.0-1<br/>
    Portable abstraction library for DVD decryption (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libdvdnav</b> 5.0.3-1<br/>
    The library for xine-dvdnav plugin (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libdvdread</b> 5.0.3-1<br/>
    Provides a simple foundation for reading DVD video disks (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libebml</b> 1.3.4-1<br/>
    Extensible Binary Meta Language library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libelf</b> 0.8.13-3<br/>
    ELF object file access library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libepoxy</b> 1.3.1-1 <br/>
    A library for handling OpenGL function pointer management for you. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libevent</b> 2.0.22-2<br/>
    An event notification library<br/>
<br/>mingw/<b>mingw-w64-libexif</b> 0.6.21-3<br/>
    A library to parse an EXIF file and read the data from those tags (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libffi</b> 3.2.1-4 <br/>
    A portable, high level programming interface to various calling conventions (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libfreexl</b> 1.0.2-3<br/>
    Library to extract valid data from within an Excel (.xls) spreadsheet<br/>
<br/>mingw/<b>mingw-w64-libftdi</b> 1.2-1<br/>
    Library to talk to FTDI chips, with Python 2 bindings (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgadu</b> 1.12.1-1<br/>
    This library implements the client side of the Gadu-Gadu protocol (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgcrypt</b> 1.7.6-1 <br/>
    General purpose cryptographic library based on the code from GnuPG (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgd</b> 2.2.4-2<br/>
    GD is an open source code library for the dynamic creation of images by programmers. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgda</b> 5.2.4-1<br/>
    Data abstraction library based on GLib (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgdata</b> 0.17.6-1<br/>
    Library for accessing GData webservices (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgee</b> 0.18.1-1<br/>
    A collection library providing GObject-based interfaces and classes for commonly used data structures (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgeotiff</b> 1.4.2-1<br/>
    Cartographic projection software (PROJ.4) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgit2</b> 0.24.0-1<br/>
    A linkable library for Git (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgit2-glib</b> 0.24.4-1<br/>
    A glib wrapper library around the libgit2 git access library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libglade</b> 2.6.4-4<br/>
    Allows you to load glade interface files in a program at runtime (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgme</b> 0.6.0-1<br/>
    Video game music file emulation/playback library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgnomecanvas</b> 2.30.3-2<br/>
    The GNOME canvas library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgoom2</b> 2k4-2<br/>
    Shared library part of the Goom visualization plugin (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgpg-error</b> 1.25-1 <br/>
    Support library for libgcrypt (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgphoto2</b> 2.5.12-1<br/>
    libgphoto2 is a free, redistributable, ready to use set of digital camera software applications for Unix-like system. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgsf</b> 1.14.41-1<br/>
    An extensible I/O abstraction library for dealing with structured file formats (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libguess</b> 1.2-2<br/>
    High-speed character set detection library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgusb</b> 0.2.8-1<br/>
    GLib wrapper around libusb1 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgweather</b> 3.20.4-1<br/>
    GWeather shared library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libgxps</b> 0.2.5-1<br/>
    A library to handling and rendering XPS documents (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libharu</b> 2.3.0-1<br/>
    C library for generating PDF documents (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libical</b> 2.0.0-3<br/>
    An Open Source implementation of the iCalendar protocols and protocol data units (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libical-glib</b> 1.0.4-1<br/>
    An iCalendar library based on libical and introspectable by GObject Introspection (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libiconv</b> 1.14-6 <br/>
    Character encoding conversion library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libidn</b> 1.33-1 <br/>
    Implementation of the Stringprep, Punycode and IDNA specifications (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libimagequant</b> 2.8.2-2<br/>
    Palette quantization library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libimobiledevice</b> 1.2.0-1<br/>
    A cross-platform protocol library to communicate with iOS devices (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libjpeg-turbo</b> 1.5.1-1 <br/>
    JPEG image codec with accelerated baseline compression and decompression (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libkml</b> 1.3.0-3<br/>
    Reference implementation of OGC KML 2.2 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libksba</b> 1.3.5-1 <br/>
    A CMS and X.509 access library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-liblas</b> 1.8.0-1<br/>
    ASPRS LiDAR data translation toolset (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-liblastfm</b> 1.0.9-2<br/>
    A Qt C++ library for the Last.fm webservices http://www.last.fm<br/>
<br/>mingw/<b>mingw-w64-liblastfm-qt4</b> 1.0.9-1<br/>
    A Qt C++ library for the Last.fm webservices http://www.last.fm (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-liblqr</b> 0.4.2-3 <br/>
    A seam-carving C/C++ library called Liquid Rescale (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmad</b> 0.15.1b-2<br/>
    A high-quality MPEG audio decoder (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmangle-git</b> 5.0.0.4760.d3089b5-1 (mingw-w64-x86_64-toolchain) <br/>
    MinGW-w64 libmangle<br/>
<br/>mingw/<b>mingw-w64-libmariadbclient</b> 2.3.2-1<br/>
    MariaDB client libraries (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmatroska</b> 1.4.5-1<br/>
    Matroska library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmaxminddb</b> 1.2.0-1<br/>
    C library for reading MaxMind DB files, including the GeoIP2 databases from MaxMind (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmetalink</b> 0.1.3-3 <br/>
    Metalink library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmicrohttpd</b> 0.9.50-3<br/>
    GNU libmicrohttpd is a small C library that is supposed to make it easy to run an HTTP server as part of another application (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmikmod</b> 3.3.8-2<br/>
    A portable sound library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmimic</b> 1.0.4-2<br/>
    An open source video encoding/decoding library for Mimic V2.x (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmng</b> 2.0.3-3 <br/>
    A collection of routines used to create and manipulate MNG format graphics files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmodbus-git</b> 658.0e2f470-1<br/>
    A Modbus library for Linux, Mac OS X, FreeBSD, QNX and Win32 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmodplug</b> 0.8.8.5-3<br/>
    A MOD playing library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmongoose</b> 6.4-1<br/>
    Embedded web server for C/C++ (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmongoose-git</b> r1793.41b405d-3<br/>
    Embedded web server for C/C++ (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmowgli</b> 2.0.0-3<br/>
    Performance and usability-oriented extensions to C (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmpcdec</b> 1.2.6-2<br/>
    Musepack decoding library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmpeg2-svn</b> r1206-2<br/>
    Library for decoding MPEG-1 and MPEG-2 video streams (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libmypaint</b> 1.3.0-2<br/>
    Brush engine used by MyPaint (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libnice</b> 0.1.13-2<br/>
    An implementation of the IETF's draft ICE (for p2p UDP data streams) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libnotify</b> 0.7.6-2<br/>
    Desktop notification library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libntlm</b> 1.4-2<br/>
    Library that implement Microsoft's NTLM authentication (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-liboauth</b> 1.0.3-5<br/>
    liboauth is a collection of POSIX-c functions implementing the OAuth Core RFC 5849 standard (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libodfgen</b> 0.1.6-1<br/>
    Library to generate ODF documents (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libogg</b> 1.3.2-2 <br/>
    Ogg bitstream and framing library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libosmpbf-git</b> 1.3.3.13.g4edb4f0-1<br/>
    A library to support OpenStreetMap's protocolbuffer binary .pbf format (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libotr</b> 4.1.1-1<br/>
    Off-the-Record Messaging Library and Toolkit (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libpaper</b> 1.1.24-1 <br/>
    library for handling paper characteristics (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libpeas</b> 1.20.0-1<br/>
    A GObject-based plugins engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libplist</b> 1.12-4<br/>
    A library to handle Apple Property List format in binary or XML (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libpng</b> 1.6.28-1 <br/>
    A collection of routines used to create PNG format graphics (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libproxy</b> 0.4.12-3<br/>
    A library that provides automatic proxy configuration management (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libraqm</b> 0.2.0-1 <br/>
    A library that encapsulates the logic for complex text layout (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libraw</b> 0.18.1-1<br/>
    Library for reading RAW files obtained from digital photo cameras (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-librescl</b> 0.3.3-1<br/>
    Reader/Writer SCL IEC 61850-6 files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-librest</b> 0.7.93-2<br/>
    Helper library for RESTful services (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-librevenge</b> 0.0.4-2<br/>
    Library for REVerses ENGineered formats filters (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-librsvg</b> 2.40.16-2 <br/>
    A SVG viewing library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libsamplerate</b> 0.1.9-1<br/>
    Secret Rabbit Code (aka libsamplerate) is a Sample Rate Converter for audio (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libsecret</b> 0.18-3<br/>
    Library for storing and retrieving passwords and other secrets (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libshout</b> 2.3.1-2<br/>
    Library for accessing a shoutcast/icecast server (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libsigc++</b> 2.10.0-1<br/>
    Libsigc++ implements a full callback system for use in widget libraries - V2 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libsignal-protocol-c-git</b> r34.16bfd04-1<br/>
    Signal Protocol C Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libsndfile</b> 1.0.26-1<br/>
    A C library for reading and writing files containing sampled sound (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libsodium</b> 1.0.11-1<br/>
    P(ortable|ackageable) NaCl-based crypto library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libsoup</b> 2.56.0-1 <br/>
    HTTP client/server library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libspatialite</b> 4.3.0.a-2<br/>
    SQLite extension to support spatial data types and operations (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libspectre</b> 0.2.8-1<br/>
    libspectre is a small library for rendering PostScript documents. It provides a convenient easy to use API for handling and rendering PostScript documents (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libspiro</b> 1~0.5.20150702-1<br/>
    Simplifies the drawing of beautiful curves (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libsquish</b> 1.14-1<br/>
    Open source DXT compression library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libsrtp</b> 1.5.3-2<br/>
    Library for SRTP (Secure Realtime Transport Protocol) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libssh</b> 0.7.4-1 <br/>
    Library for accessing ssh client services through C libraries (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libssh2</b> 1.8.0-1 <br/>
    A library implementing the SSH2 protocol as defined by Internet Drafts (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libswift</b> 1.0.0-1<br/>
    a library that attempts to satisfy the most fundamental needs of C programmers by providing Data structures, Networking, IO, Threading, and so forth. libswift was originally created by S.J.R. van Schaik and is currently being managed by Andrew Wheeler<br/>
<br/>mingw/<b>mingw-w64-libsystre</b> 1.0.1-2 <br/>
    Wrapper library around TRE that provides POSIX API (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libtasn1</b> 4.9-1 <br/>
    A library for Abstract Syntax Notation One (ASN.1) and Distinguish Encoding Rules (DER) manipulation (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libtheora</b> 1.1.1-3 <br/>
    An open video codec developed by the Xiph.org (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libtiff</b> 4.0.7-1 <br/>
    Library for manipulation of TIFF images (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libtommath</b> 0.42.0-2<br/>
    Highly optimized and portable routines for integer based number theoretic applications (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libtool</b> 2.4.6-8 <br/>
    A system independent dlopen wrapper for GNU libtool (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libtorrent-rasterbar</b> 1.0.7-1<br/>
    libtorrent is a feature complete C++ bittorrent implementation focusing on efficiency and scalability (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libtre-git</b> r122.c2f5d13-4 <br/>
    The approximate regex matching library and agrep command line tool (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libunistring</b> 0.9.7-1 <br/>
    Library for manipulating Unicode strings and C strings. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libunwind</b> 3.9.1-3<br/>
    A new implementation of a stack unwinder for C++ exceptions (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libusb</b> 1.0.21-1 <br/>
    Library that provides generic access to USB devices (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libusb-compat-git</b> r60.072a5e4-3 <br/>
    libusb provides generic access to USB devices (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libusb-usbdk</b> 1.0.21-1<br/>
    Library that provides generic access to USB devices via UsbDk backend (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libusbmuxd</b> 1.0.10-3<br/>
    A client library to multiplex connections from and to iOS devices (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libuv</b> 1.10.2-1 <br/>
    Cross-platform asychronous I/O (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libview</b> 0.6.6-3<br/>
    VMware's Incredibly Exciting Widgets (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libvirt</b> 2.3.0-1<br/>
    Windows libvirt virtualization library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libvirt-glib</b> 0.2.3-1<br/>
    libvirt GLib and GObject mapping library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libvisio</b> 0.1.5-0<br/>
    libvisio is a library and a set of tools for reading and converting MS Visio diagram (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libvmime-git</b> r1032.7e36a74-1<br/>
    An open source solution for working with MIME messages and Internet messaging services like IMAP, POP or SMTP (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libvorbis</b> 1.3.5-1 <br/>
    Vorbis codec library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libvorbisidec-svn</b> r19494-1 <br/>
    Integer-only Ogg Vorbis decoder, AKA \"tremor\" (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libvpx</b> 1.6.0-1<br/>
    The VP8 Codec SDK (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libwebp</b> 0.5.2-1 <br/>
    the WebP library. Includes conversion tools (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libwebsockets</b> 2.1.0-2<br/>
    A lightweight pure C library for websockets (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libwinpthread-git</b> 5.0.0.4761.02bea78-1 (mingw-w64-x86_64-toolchain) <br/>
    MinGW-w64 winpthreads library<br/>
<br/>mingw/<b>mingw-w64-libwmf</b> 0.2.8.4-3<br/>
    Library for Converting Metafile Images (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libwpd</b> 0.10.1-2<br/>
    Library for Importing WordPerfect (tm) Documents (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libwpg</b> 0.3.1-2<br/>
    Library to read and parse graphics in WordPerfect Graphics format (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libxml++</b> 3.0.0-2<br/>
    C++ wrapper for the libxml2 XML parser library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libxml++2.6</b> 2.40.0-2<br/>
    C++ wrapper for the libxml2 XML parser library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libxml2</b> 2.9.4-4 <br/>
    XML parsing library, version 2 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libxslt</b> 1.1.29-3 <br/>
    XML stylesheet transformation library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libyaml</b> 0.1.6-2 <br/>
    YAML 1.1 library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-libzip</b> 1.2.0-1<br/>
    A C library for reading, creating, and modifying zip archives (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-live-media</b> 2015.06.25-1<br/>
    A set of C++ libraries for multimedia streaming (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lld</b> 3.9.1-3<br/>
    Linker tools for LLVM (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lldb</b> 3.9.1-3<br/>
    Next generation, high-performance debugger (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-llvm</b> 3.9.1-3 <br/>
    Low Level Virtual Machine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-llvm35</b> 3.5.2-1<br/>
    Low Level Virtual Machine<br/>
<br/>mingw/<b>mingw-w64-lmdb</b> 0.9.18-1<br/>
    Lightning Memory-mapped Database (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lmdbxx</b> 0.9.14.0-1<br/>
    C++11 wrapper for LMDB (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lua</b> 5.3.3-2 <br/>
    A powerful light-weight programming language designed for extending applications. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lua-lpeg</b> 0.12-2<br/>
    Pattern-matching library for Lua (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lua51</b> 5.1.5-4 <br/>
    A powerful light-weight programming language designed for extending applications. Version 5.1.x (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lua51-bitop</b> 1.0.2-1<br/>
    C extension adding bitwise operations on numbers for Lua (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lua51-lgi</b> 0.9.1-1<br/>
    LGI is gobject-introspection based dynamic Lua binding to GObject based libraries (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lua51-lpeg</b> 0.12-2<br/>
    Pattern-matching library for Lua 5.1 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lua51-lsqlite3</b> 0.9.3-1<br/>
    LuaSQLite is a Lua 5 binding to allow users/developers to manipulate SQLite 2 and SQLite 3 databases (through different implementations) from lua<br/>
<br/>mingw/<b>mingw-w64-lua51-luarocks</b> 2.4.1-1<br/>
    the package manager for Lua modules (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-luabind-git</b> 0.9.1.144.ge414c57-1<br/>
    A library that helps you create bindings between C++ and Lua (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-luajit-git</b> 2.0.4.49.ga68c411-1<br/>
    Just-in-time compiler and drop-in replacement for Lua 5.1 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lz4</b> 1.7.5-1 <br/>
    Very fast lossless compression algorithm (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-lzo2</b> 2.09-2 <br/>
    Portable lossless data compression library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-make</b> 4.2.1-1 (mingw-w64-x86_64-toolchain) <br/>
    GNU make utility to maintain groups of programs (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-mbedtls</b> 2.4.0-1<br/>
    mbed TLS is an open source and commercial SSL library licensed by ARM Limited. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-mcpp</b> 2.7.2-2<br/>
    Matsui's CPP implementation precisely conformed to standards (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-meanwhile</b> 1.0.2-3<br/>
    Meanwhile libraries (mingw64)<br/>
<br/>mingw/<b>mingw-w64-meld3</b> 3.16.4-1 <br/>
    Visual diff and merge tool (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-memphis</b> 0.2.3-3<br/>
    A map-rendering library for OpenStreetMap (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-mesa</b> 17.0.0-1<br/>
    Open-source implementation of the OpenGL specification (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-meson</b> 0.38.1-1<br/>
    High-productivity build system (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-mhook</b> r7.a159eed-1<br/>
    An API hooking library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-miniupnpc</b> 1.9.20150609-1<br/>
    A small UPnP client library/tool to access Internet Gateway Devices (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-mlpack</b> 1.0.12-2<br/>
    An intuitive, fast, scalable C++ machine learning library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-mpc</b> 1.0.3-2 (mingw-w64-x86_64) <br/>
    Multiple precision complex arithmetic library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-mpdecimal</b> 2.4.2-1<br/>
    Package for correctly-rounded arbitrary precision decimal floating point arithmetic (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-mpfr</b> 3.1.5.p1-1 <br/>
    Multiple-precision floating-point library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-mpg123</b> 1.23.8-1<br/>
    A console based real time MPEG Audio Player for Layer 1, 2 and 3 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-mpv</b> 0.24.0-1<br/>
    Video player based on MPlayer/mplayer2 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-msgpack-c</b> 2.0.0-1<br/>
    MessagePack implementation for C and C++ (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-msmtp</b> 1.6.2-1<br/>
    An SMTP client (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-muparser</b> 2.2.5-1<br/>
    A fast math parser library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-mypaint</b> 1.2.1-1<br/>
    Simple drawing & painting program that works well with Wacom-style graphics tablets (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-nanodbc</b> 2.12.4-1<br/>
    A small C++ wrapper for the native C ODBC API (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-nanovg-git</b> r259.6ae0873-1<br/>
    Small antialiased vector graphics rendering library for OpenGL<br/>
<br/>mingw/<b>mingw-w64-nasm</b> 2.12.02-1 <br/>
    An 80x86 assembler designed for portability and modularity (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ncurses</b> 6.0.20170114-1 <br/>
    System V Release 4.0 curses emulation library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-netcdf</b> 4.4.1.1-1<br/>
    Interface for scientific data access to large binary data (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-nettle</b> 3.3-1 <br/>
    A low-level cryptographic library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-nghttp2</b> 1.19.0-1 <br/>
    Framing layer of HTTP/2 is implemented as a reusable C library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ngraph-gtk</b> 6.07.02-1<br/>
    create scientific 2-dimensional graphs (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-nim</b> 0.11.2-1<br/>
    Imperative, multi-paradigm, compiled programming language (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ninja</b> 1.7.2-1<br/>
    Ninja is a small build system with a focus on speed (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-nlopt</b> 2.4.2-3<br/>
    A library for nonlinear optimization (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-nodejs</b> 6.9.5-1 <br/>
    Evented I/O for V8 javascript (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-npth</b> 1.3-1 <br/>
    New portable threads library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-nsis</b> 3.01-1<br/>
    Windows installer development tool (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-nsis-nsisunz</b> 1.0-1<br/>
    NSIS plugin which allows you to extract files from ZIP archives (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-nspr</b> 4.10.10-1<br/>
    Netscape Portable Runtime (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-nss</b> 3.20.2-1<br/>
    Mozilla Network Security Services (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ntldd-git</b> r15.e7622f6-2 <br/>
    Tracks dependencides in Windows PE binaries (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ocaml</b> 4.04.0-1<br/>
    An industrial strength programming language supporting functional, imperative and object-oriented styles (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ocaml-camlp4</b> 4.02.1-5<br/>
    Pre-Processor-Pretty-Printer for OCaml (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ocaml-findlib</b> 1.7.1-1<br/>
    OCaml library manager (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-oce</b> 0.17.2-4<br/>
    Open CASCADE Community Edition: patches/improvements/experiments contributed by users over the official Open CASCADE library.<br/>
<br/>mingw/<b>mingw-w64-octopi-git</b> r941.6df0f8a-1<br/>
    a powerful Pacman frontend using Qt libs<br/>
<br/>mingw/<b>mingw-w64-ogre3d-hg</b> 2.1.0.r10230.62834e3ac215-1<br/>
    A cross-platform 3D game engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ois-git</b> 1.4.0.50.6129c0a-1<br/>
    Object Oriented Input System (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-oniguruma</b> 6.0.0-1<br/>
    A regular expressions library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-openal</b> 1.16.0-4<br/>
    OpenAL audio library for use with opengl (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-openblas</b> 0.2.17-1<br/>
    An optimized BLAS library based on GotoBLAS2 1.13 BSD, providing optimized blas, lapack, and cblas (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-opencl-headers</b> 2~2.1.20161129-3<br/>
    OpenCL (Open Computing Language) header files<br/>
<br/>mingw/<b>mingw-w64-opencollada-git</b> r1471.9fea0aa-1<br/>
    Stream based reader and writer library for COLLADA files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-opencolorio-git</b> 721.de9491e-1<br/>
    A color management framework for visual effects and animation (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-opencore-amr</b> 0.1.3-3<br/>
    Open source implementation of the Adaptive Multi Rate (AMR) speech codec (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-opencsg</b> 1.4.0-2<br/>
    Library for image-based CSG rendering using OpenGL (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-opencv</b> 3.2.0-2 <br/>
    Open Source Computer Vision Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-openexr</b> 2.2.0-3 <br/>
    Openexr library for EXR images (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-openh264</b> 1.6.0-2<br/>
    Library for encoding/decoding H264/AVC video streams (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-openimageio</b> 1.7.11-1<br/>
    A library for reading and writing images, including classes, utilities, and applications (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-openjpeg</b> 1.5.2-7<br/>
    An open source JPEG 2000 codec (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-openjpeg2</b> 2.1.0-7 <br/>
    An open source JPEG 2000 codec (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-openldap</b> 2.4.43-1<br/>
    OpenLDAP Software is an open source implementation of the Lightweight Directory Access Protocol (only client) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-openocd</b> 0.10.0-1<br/>
    OpenOCD - Open On-Chip Debugger (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-openocd-git</b> 0.9.0.r2.g79fdeb3-1<br/>
    OpenOCD - Open On-Chip Debugger (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-openscad</b> 2015.03-2<br/>
    The programmers solid 3D CAD modeller (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-openshadinglanguage</b> 1.7.5-1<br/>
    Advanced shading language for production GI renderers (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-openssl</b> 1.0.2.k-1 <br/>
    The Open Source toolkit for Secure Sockets Layer and Transport Layer Security (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-optipng</b> 0.7.6-1<br/>
    Compresses PNG files to a smaller size, without losing any information (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-opus</b> 1.1.3-1<br/>
    Codec designed for interactive speech and audio transmission over the Internet (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-opus-tools</b> 0.1.9-2<br/>
    Collection of tools for Opus audio codec (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-opusfile</b> 0.8-1<br/>
    Library for opening, seeking, and decoding .opus files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-orc</b> 0.4.26-1 <br/>
    The Oild Runtime Compiler (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-osgQt</b> 3.5.5-1<br/>
    OpenSceneGraph Qt5 Modules (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-osgQt-debug</b> 3.5.5-1<br/>
    OpenSceneGraph Qt5 Modules (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-osgQtQuick</b> 2.0.0.7-1<br/>
    OpenSceneGraph QML Modules (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-osgQtQuick-debug</b> 2.0.0.7-1<br/>
    OpenSceneGraph QML Modules (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-osgbullet-debug-git</b> 3.0.0.259-1<br/>
    Bullet physics and OpenSceneGraph integration (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-osgbullet-git</b> 3.0.0.259-1<br/>
    Bullet physics and OpenSceneGraph integration (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-osgearth</b> 2.8-1<br/>
    A terrain rendering toolkit for OpenSceneGraph (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-osgearth-debug</b> 2.8-1<br/>
    A terrain rendering toolkit for OpenSceneGraph (debug) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-osgocean-debug-git</b> 1.0.1.r147-1<br/>
    An ocean rendering nodekit for OpenSceneGraph (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-osgocean-git</b> 1.0.1.r147-1<br/>
    An ocean rendering nodekit for OpenSceneGraph (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-osgworks-debug-git</b> 3.1.0.442-1<br/>
    A toolkit for OpenSceneGraph applications (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-osgworks-git</b> 3.1.0.442-1<br/>
    A toolkit for OpenSceneGraph applications (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-osm-gps-map</b> 1.1.0-1<br/>
    A Gtk+ Widget for Displaying OpenStreetMap tiles. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-osmgpsmap-git</b> r443.c24d08d-1<br/>
    A Gtk+ Widget for Displaying OpenStreetMap tiles<br/>
<br/>mingw/<b>mingw-w64-osslsigncode</b> 1.7.1-3<br/>
    Tool for Authenticode signing of PE, CAB and MSI files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-p11-kit</b> 0.23.2-2 <br/>
    Library to work with PKCS#11 modules<br/>
<br/>mingw/<b>mingw-w64-paho.mqtt.c</b> 1.1.0-1<br/>
    Eclipse Paho MQTT C client (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-pango</b> 1.40.3-1 <br/>
    A library for layout and rendering of text (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-pangomm</b> 2.40.0-2<br/>
    C++ bindings for pango (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-pcre</b> 8.40-1 <br/>
    A library that implements Perl 5-style regular expressions (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-perl</b> 5.22.0-1<br/>
    A highly capable, feature-rich programming language (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-phodav</b> 2.0-2<br/>
    A WebDAV server using libsoup (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-physfs-hg</b> r1363.a3dabf75a0d0-1<br/>
    A library to provide abstract access to various archives (development version)<br/>
<br/>mingw/<b>mingw-w64-pidgin++</b> 15.1-2<br/>
    An improved version of Pidgin (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-pidgin-hg</b> r37207.e666f49a3e86-1<br/>
    Multi-protocol instant messaging client (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-pixman</b> 0.34.0-3 <br/>
    The pixel-manipulation library for X and cairo (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-pkg-config</b> 0.29.1-3 (mingw-w64-x86_64-toolchain) <br/>
    A system for managing library compile/link flags (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-png2ico</b> 2002.12.08-1<br/>
    Converts PNG files to Windows icon resource files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-pngcrush</b> 1.8.10-1 <br/>
    A tool for optimizing the compression of PNG files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-pngnq</b> 1.1-2<br/>
    Pngnq is a tool for quantizing PNG images in RGBA format (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-poco</b> 1.7.7-1<br/>
    POrtable COmponents C++ Libraries (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-podofo</b> 0.9.3-1<br/>
    A C++ library to work with the PDF file format (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-poppler</b> 0.52.0-1<br/>
    PDF rendering library based on xpdf 3.0 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-poppler-data</b> 0.4.7-2<br/>
    Encoding data for the poppler PDF rendering library<br/>
<br/>mingw/<b>mingw-w64-poppler-qt4</b> 0.36.0-1<br/>
    PDF rendering library based on xpdf 3.0 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-popt</b> 1.16-1<br/>
    C library for parsing command line parameters (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-port-scanner</b> 1.3-2<br/>
    A multi threaded TCP port scanner from SecPoint.com (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-portablexdr</b> 4.9.2.r27.94fb83c-1<br/>
    PortableXDR / RPC Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-portaudio</b> 190600_20161030-1<br/>
    A free, cross-platform, open source, audio I/O library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-portmidi</b> 217-2<br/>
    Platform independent library for real-time MIDI input/output (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-postgresql</b> 9.5.2-1<br/>
    Libraries for use with PostgreSQL (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-postr</b> 0.13.1-1<br/>
    Upload photos to Flickr (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-potrace</b> 1.13-1<br/>
    Tool for tracing a bitmap, which means, transforming a bitmap into a smooth, scalable image (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-premake</b> 4.3-2<br/>
    A build configuration tool. Describe your build using Lua and generate the project files for your specific toolset (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-proj</b> 4.9.3-1<br/>
    Cartographic projection software (PROJ.4) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-protobuf</b> 3.1.0-1<br/>
    Protocol Buffers - Google's data interchange format (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-protobuf-c</b> 1.2.1-2<br/>
    Protocol Buffers implementation in C (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-pugixml</b> 1.8-1<br/>
    Light-weight, simple and fast XML parser for C++ with XPath support (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-purple-facebook</b> 20160907.66ee773.bf8ed95-1<br/>
    Facebook plugin for libpurple (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-purple-hangouts-hg</b> r287+.574c112aa35c+-1<br/>
    Hangouts plugin for libpurple (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-purple-skypeweb</b> 1.1-1<br/>
    Skype plugin for libpurple (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-putty</b> 0.67-1 <br/>
    A free telnet/SSH client (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-putty-ssh</b> 0.0-3 <br/>
    A wrapper around plink with some nice features (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-putty-svn</b> 0.63.r10297-4<br/>
    A free telnet/SSH client (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-pygobject-devel</b> 3.22.0-1 <br/>
    Development files for the pygobject bindings<br/>
<br/>mingw/<b>mingw-w64-pygobject2-devel</b> 2.28.6-4<br/>
    Development files for the pygobject bindings<br/>
<br/>mingw/<b>mingw-w64-pyqt4-common</b> 4.11.4-2<br/>
    Common PyQt files shared between python3-pyqt4 and python2-pyqt4<br/>
<br/>mingw/<b>mingw-w64-pyqt5-common</b> 5.8-1<br/>
    Common PyQt files shared between python3-pyqt5 and python2-pyqt5<br/>
<br/>mingw/<b>mingw-w64-pyside-common-qt4</b> 1.2.2-3<br/>
    Provides LGPL Qt bindings for Python and related tools for binding generation (Common files)(mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-pyside-tools-common-qt4</b> 1.2.2-3<br/>
    PySide lupdate, rcc, and uic development tools (Common Files) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python-lxml-docs</b> 3.6.0-1<br/>
    Python binding for the libxml2 and libxslt libraries (docs)<br/>
<br/>mingw/<b>mingw-w64-python-qscintilla-common</b> 2.9-1<br/>
    Common python qscintilla bindings files shared between python3-qscintilla and python2-qscintilla<br/>
<br/>mingw/<b>mingw-w64-python2</b> 2.7.13-1 <br/>
    A high-level scripting language (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-babel</b> 2.3.4-1<br/>
    A collection of tools for internationalizing Python applications<br/>
<br/>mingw/<b>mingw-w64-python2-beaker</b> 1.8.0-1 <br/>
    Caching and sessions WSGI middleware for use with web applications and stand-alone Python scripts and applications (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-beautifulsoup3</b> 3.2.1-2<br/>
    A Python HTML/XML parser designed for quick turnaround projects like screen-scraping (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-bsddb3</b> 6.1.0-3<br/>
    Python bindings for Oracle Berkeley DB (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-cairo</b> 1.10.0-3 <br/>
    Python2 bindings for the cairo graphics library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-characteristic</b> 14.3.0-1<br/>
    Python attributes without boilerplate (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-cjson</b> 1.1.0-2<br/>
    Fast JSON encoder/decoder for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-colorama</b> 0.3.7-1<br/>
    Python API for cross-platform colored terminal text (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-coverage</b> 4.0.3-1<br/>
    Code coverage measurement for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-cssselect</b> 0.9.1-4<br/>
    A Python2 library that parses CSS3 Selectors and translates them to XPath 1.0<br/>
<br/>mingw/<b>mingw-w64-python2-cx_Freeze</b> 4.3.3-7 <br/>
    Python package for freezing scripts into executables (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-cycler</b> 0.10.0-1<br/>
    Composable style cycles<br/>
<br/>mingw/<b>mingw-w64-python2-dateutil</b> 2.6.0-1<br/>
    Provides powerful extensions to the standard datetime module (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-decorator</b> 4.0.11-1<br/>
    Better living through Python with decorators (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-distutils-extra</b> 2.39-2<br/>
    Enhancements to the Python build system (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-docutils</b> 0.12-5 <br/>
    Set of tools for processing plaintext docs into formats such as HTML, XML, or LaTeX (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-enum34</b> 1.0.4-1<br/>
    Python 3.4 Enum backported to 3.3, 3.2, 3.1, 2.7, 2.6, 2.5, and 2.4 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-et-xmlfile</b> 1.0.1-1<br/>
    A low memory library for creating large XML files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-funcsigs</b> 0.4-1<br/>
    Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+<br/>
<br/>mingw/<b>mingw-w64-python2-gobject</b> 3.22.0-1 <br/>
    Python 2 bindings for GObject2 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-gobject2</b> 2.28.6-4<br/>
    Python 2 bindings for GObject2 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-h5py</b> 2.5.0-2<br/>
    General-purpose Python bindings for the HDF5 library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-httplib2</b> 0.9.2-1<br/>
    Comprehensive HTTP client library, supporting many features (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-icu</b> 1.9.3-1<br/>
    Python extension wrapping the ICU C++ API (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-idna</b> 2.0-1<br/>
    Internationalized Domain Names in Applications (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-imagesize</b> 0.7.1-1<br/>
    Getting image size from png/jpeg/jpeg2000/gif file (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-ipaddress</b> 1.0.16-1<br/>
    Port of the 3.3+ ipaddress module to 2.6, 2.7, 3.2 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-ipykernel</b> 4.3.1-1<br/>
    The ipython kernel for Jupyter (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-ipython</b> 5.3.0-1<br/>
    An enhanced Interactive Python shell (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-ipython_genutils</b> 0.1.0-1<br/>
    IPython vestigial utilities (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-jdcal</b> 1.2-1<br/>
    Julian dates, from proleptic Gregorian and Julian calendars (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-jinja</b> 2.8-1<br/>
    A simple pythonic template language written in Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-jsonschema</b> 2.5.1-1<br/>
    An implementation of JSON Schema validation for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-jupyter_client</b> 4.3.0-1<br/>
    The reference implementation of the Jupyter protocol. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-jupyter_console</b> 5.0.0-1<br/>
    A terminal-based console frontend for Jupyter kernels. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-jupyter_core</b> 4.1.0-1<br/>
    Core common functionality of Jupyter projects. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-lhafile</b> 0.2.1-1<br/>
    LHA module for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-lxml</b> 3.6.0-1<br/>
    Python2 binding for the libxml2 and libxslt libraries<br/>
<br/>mingw/<b>mingw-w64-python2-mako</b> 1.0.4-1 <br/>
    A super-fast templating language that borrows the best ideas from the existing templating languages (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-markupsafe</b> 0.23-4 <br/>
    Implements a XML/HTML/XHTML Markup safe string for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-matplotlib</b> 2.0.0-1<br/>
    A python plotting library, making publication quality plots (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-mistune</b> 0.7.2-1<br/>
    The fastest markdown parser in pure Python with renderer feature (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-mock</b> 2.0.0-1<br/>
    Rolling backport of unittest.mock for all Pythons (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-networkx</b> 1.11-1<br/>
    High-productivity software for complex networks (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-nose</b> 1.3.7-3<br/>
    A discovery-based unittest extension (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-nuitka</b> 0.5.14.3-3<br/>
    Python to native compiler (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-numexpr</b> 2.4.6-1<br/>
    Fast numerical array expression evaluator for Python, NumPy, PyTables, pandas. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-numpy</b> 1.11.2-1<br/>
    Scientific tools for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-openmdao</b> 1.7.1-1<br/>
    An open-source MDAO framework written in Python. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-openpyxl</b> 2.3.5-1<br/>
    A python library to read/write Excel 2007 xlsx/xlsm file (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pandas</b> 0.19.1-1<br/>
    Cross-section and time series data analysis toolkit (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-path</b> 10.1-1<br/>
    File system based database that uses python pickles (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-patsy</b> 0.4.1-1<br/>
    A Python package for describing statistical models and for building design matrices (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pbr</b> 1.10.0-1<br/>
    Python Build Reasonableness (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pdfrw</b> 0.2-1<br/>
    Convert restructured text to PDF via reportlab (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pgen2</b> 0.1.0-1<br/>
    Pure Python implementation of pgen, the Python parser generator (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pickleshare</b> 0.7.4-1<br/>
    File system based database that uses python pickles (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pillow</b> 3.3.0-1<br/>
    Python Imaging Library (PIL) fork. Python2 version (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pip</b> 9.0.1-1<br/>
    An easy_install replacement for installing pypi python packages (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pptx</b> 0.6.1-1<br/>
    Create Open XML PowerPoint documents in Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-prompt_toolkit</b> 1.0.9-1<br/>
    Library for building powerful interactive command lines in Python<br/>
<br/>mingw/<b>mingw-w64-python2-psutil</b> 4.3.0-1<br/>
    A cross-platform process and system utilities module for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-py</b> 1.4.31-1<br/>
    library with cross-python path, ini-parsing, io, code, log facilities (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pyasn1</b> 0.1.9-1<br/>
    ASN.1 types and codecs (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pyasn1-modules</b> 0.0.8-1<br/>
    A collection of ASN.1-based protocols modules (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pycparser</b> 2.14-1<br/>
    Complete parser of the C language, written in pure Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pygments</b> 2.1.3-1<br/>
    Python syntax highlighter (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pygtk</b> 2.24.0-6<br/>
    Python bindings for the GTK widget set (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pyparsing</b> 2.1.10-1<br/>
    General parsing module for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pyqt4</b> 4.11.4-2<br/>
    A set of Python 2.x bindings for the Qt4 toolkit<br/>
<br/>mingw/<b>mingw-w64-python2-pyqt5</b> 5.8-1<br/>
    A set of Python 2.x bindings for the Qt5 toolkit<br/>
<br/>mingw/<b>mingw-w64-python2-pyside-qt4</b> 1.2.2-3<br/>
    Provides LGPL Qt bindings for Python and related tools for binding generation (Python2)(mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pyside-tools-qt4</b> 1.2.2-3<br/>
    PySide lupdate, rcc, and uic development tools (for Python 2) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pytest</b> 3.0.3-1<br/>
    simple powerful testing with Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pytz</b> 2016.10-1<br/>
    Cross platform time zone library for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-pyzmq</b> 15.2.0-1<br/>
    Python bindings for zeromq, written in Cython (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-qscintilla</b> 2.9-1<br/>
    Python 2.x bindings for QScintilla2<br/>
<br/>mingw/<b>mingw-w64-python2-qtconsole</b> 4.2.1-1<br/>
    A rich Qt-based console for working with Jupyter kernels, supporting rich media output, session export, and more. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-reportlab</b> 3.0-4<br/>
    A proven industry-strength PDF generating solution (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-requests</b> 2.13.0-1<br/>
    Requests is the only Non-GMO HTTP library for Python, safe for human consumption. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-rst2pdf</b> 0.93-2<br/>
    Create PDFs from simple text markup, no LaTeX required (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-scipy</b> 0.18.1-1<br/>
    SciPy is open-source software for mathematics, science, and engineering. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-setuptools</b> 31.0.0-1<br/>
    Easily download, build, install, upgrade, and uninstall Python packages (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-shiboken-qt4</b> 1.2.2-3<br/>
    Support library for Python2 bindings (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-simplegeneric</b> 0.8.1-1<br/>
    File system based database that uses python pickles (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-sip</b> 4.19.1-1<br/>
    Python 2.x SIP bindings for C and C++ libraries (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-six</b> 1.10.0-1 <br/>
    Python 2 and 3 compatibility utilities (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-snowballstemmer</b> 1.2.1-1<br/>
    Snowball stemming library collection for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-sphinx</b> 1.5.3-1<br/>
    Python2 documentation generator<br/>
<br/>mingw/<b>mingw-w64-python2-sphinx-alabaster-theme</b> 0.7.9-1<br/>
    Modified Kr Sphinx doc theme (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-sphinx_rtd_theme</b> 0.1.9-1<br/>
    Python Sphinx Read The Docs Theme (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-sqlitedict</b> 1.4.1-1<br/>
    Persistent dict, backed by sqlite3 and pickle, multithread-safe (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-statsmodels</b> 0.6.1-2<br/>
    Statistical computations and models for use with SciPy (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-traitlets</b> 4.3.2-1<br/>
    A lightweight Traits like module (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-wcwidth</b> 0.1.7-1<br/>
    Measures number of Terminal column cells of wide-character codes<br/>
<br/>mingw/<b>mingw-w64-python2-win_unicode_console</b> 0.5-1<br/>
    Measures number of Terminal column cells of wide-character codes<br/>
<br/>mingw/<b>mingw-w64-python2-xlsxwriter</b> 0.9.3-1<br/>
    A Python module for creating Excel XLSL files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-zope.event</b> 4.2.0-1<br/>
    Very basic event publishing system (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python2-zope.interface</b> 4.1.3-1<br/>
    Interfaces for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3</b> 3.5.3-1 <br/>
    A high-level scripting language (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-babel</b> 2.3.4-1<br/>
    A collection of tools for internationalizing Python applications<br/>
<br/>mingw/<b>mingw-w64-python3-beaker</b> 1.8.0-1<br/>
    Caching and sessions WSGI middleware for use with web applications and stand-alone Python scripts and applications (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-bsddb3</b> 6.1.0-3<br/>
    Python bindings for Oracle Berkeley DB (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-cairo</b> 1.10.0-7 <br/>
    Python 3 bindings for the cairo graphics library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-characteristic</b> 14.3.0-1<br/>
    Python attributes without boilerplate (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-colorama</b> 0.3.7-1<br/>
    Python API for cross-platform colored terminal text (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-coverage</b> 4.0.3-1<br/>
    Code coverage measurement for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-cssselect</b> 0.9.1-4<br/>
    A Python3 library that parses CSS3 Selectors and translates them to XPath 1.0<br/>
<br/>mingw/<b>mingw-w64-python3-cx_Freeze</b> 4.3.3-7 <br/>
    Python package for freezing scripts into executables (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-cycler</b> 0.10.0-1<br/>
    Composable style cycles<br/>
<br/>mingw/<b>mingw-w64-python3-dateutil</b> 2.6.0-1<br/>
    Provides powerful extensions to the standard datetime module (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-decorator</b> 4.0.11-1<br/>
    Better living through Python with decorators (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-distutils-extra</b> 2.39-2<br/>
    Enhancements to the Python build system (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-docutils</b> 0.12-5<br/>
    Set of tools for processing plaintext docs into formats such as HTML, XML, or LaTeX (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-et-xmlfile</b> 1.0.1-1<br/>
    A low memory library for creating large XML files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-funcsigs</b> 0.4-1<br/>
    Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+<br/>
<br/>mingw/<b>mingw-w64-python3-gobject</b> 3.22.0-1<br/>
    Python 3 bindings for GObject2 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-gobject2</b> 2.28.6-4<br/>
    Python 3 bindings for GObject2 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-h5py</b> 2.5.0-2<br/>
    General-purpose Python bindings for the HDF5 library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-httplib2</b> 0.9.2-1<br/>
    Python3 binding for the libxml2 and libxslt libraries<br/>
<br/>mingw/<b>mingw-w64-python3-icu</b> 1.9.3-1<br/>
    Python extension wrapping the ICU C++ API (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-idna</b> 2.0-1<br/>
    Internationalized Domain Names in Applications (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-imagesize</b> 0.7.1-1<br/>
    Getting image size from png/jpeg/jpeg2000/gif file (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-ipykernel</b> 4.3.1-1<br/>
    The ipython kernel for Jupyter (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-ipython</b> 5.3.0-1<br/>
    An enhanced Interactive Python shell (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-ipython_genutils</b> 0.1.0-1<br/>
    IPython vestigial utilities (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-jdcal</b> 1.2-1<br/>
    Julian dates, from proleptic Gregorian and Julian calendars (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-jinja</b> 2.8-1<br/>
    A simple pythonic template language written in Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-jsonschema</b> 2.5.1-1<br/>
    An implementation of JSON Schema validation for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-jupyter_client</b> 4.3.0-1<br/>
    The reference implementation of the Jupyter protocol. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-jupyter_console</b> 5.0.0-1<br/>
    A terminal-based console frontend for Jupyter kernels. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-jupyter_core</b> 4.1.0-1<br/>
    Core common functionality of Jupyter projects. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-lhafile</b> 0.2.1-1<br/>
    LHA module for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-lxml</b> 3.6.0-1<br/>
    Python3 binding for the libxml2 and libxslt libraries<br/>
<br/>mingw/<b>mingw-w64-python3-mako</b> 1.0.4-1<br/>
    A super-fast templating language that borrows the best ideas from the existing templating languages (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-markupsafe</b> 0.23-4<br/>
    Implements a XML/HTML/XHTML Markup safe string for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-matplotlib</b> 2.0.0-1<br/>
    A python plotting library, making publication quality plots (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-mistune</b> 0.7.2-1<br/>
    The fastest markdown parser in pure Python with renderer feature (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-mock</b> 2.0.0-1<br/>
    Rolling backport of unittest.mock for all Pythons (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-networkx</b> 1.11-1<br/>
    High-productivity software for complex networks (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-nose</b> 1.3.7-3<br/>
    A discovery-based unittest extension (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-nuitka</b> 0.5.14.3-3<br/>
    Python to native compiler (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-numexpr</b> 2.4.6-1<br/>
    Fast numerical array expression evaluator for Python, NumPy, PyTables, pandas. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-numpy</b> 1.11.2-1<br/>
    Scientific tools for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-openmdao</b> 1.7.1-1<br/>
    An open-source MDAO framework written in Python. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-openpyxl</b> 2.3.5-1<br/>
    A python library to read/write Excel 2007 xlsx/xlsm file (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pandas</b> 0.19.1-1<br/>
    Cross-section and time series data analysis toolkit (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-path</b> 10.1-1<br/>
    File system based database that uses python pickles (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-patsy</b> 0.4.1-1<br/>
    A Python package for describing statistical models and for building design matrices (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pbr</b> 1.10.0-1<br/>
    Python Build Reasonableness (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pdfrw</b> 0.2-1<br/>
    Convert restructured text to PDF via reportlab (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pgen2</b> 0.1.0-1<br/>
    Pure Python implementation of pgen, the Python parser generator (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pickleshare</b> 0.7.4-1<br/>
    File system based database that uses python pickles (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pillow</b> 3.3.0-1<br/>
    Python Imaging Library (PIL) fork Python3 version (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pip</b> 9.0.1-1 <br/>
    An easy_install replacement for installing pypi python packages (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pptx</b> 0.6.1-1<br/>
    Create Open XML PowerPoint documents in Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-prompt_toolkit</b> 1.0.9-1<br/>
    Library for building powerful interactive command lines in Python<br/>
<br/>mingw/<b>mingw-w64-python3-psutil</b> 4.3.0-1<br/>
    A cross-platform process and system utilities module for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-py</b> 1.4.31-1<br/>
    library with cross-python path, ini-parsing, io, code, log facilities (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pyasn1</b> 0.1.9-1<br/>
    ASN.1 types and codecs (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pyasn1-modules</b> 0.0.8-1<br/>
    A collection of ASN.1-based protocols modules (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pycparser</b> 2.14-1<br/>
    Complete parser of the C language, written in pure Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pygments</b> 2.1.3-1<br/>
    Python syntax highlighter (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pyparsing</b> 2.1.10-1<br/>
    General parsing module for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pyqt4</b> 4.11.4-2<br/>
    A set of Python 3.x bindings for the Qt4 toolkit<br/>
<br/>mingw/<b>mingw-w64-python3-pyqt5</b> 5.8-1<br/>
    A set of Python 3.x bindings for the Qt5 toolkit<br/>
<br/>mingw/<b>mingw-w64-python3-pyside-qt4</b> 1.2.2-3<br/>
    Provides LGPL Qt bindings for Python and related tools for binding generation (Python3)(mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pyside-tools-qt4</b> 1.2.2-3<br/>
    PySide lupdate, rcc, and uic development tools (for Python 3) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pytest</b> 3.0.3-1<br/>
    simple powerful testing with Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pytz</b> 2016.10-1<br/>
    Cross platform time zone library for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-pyzmq</b> 15.2.0-1<br/>
    Python bindings for zeromq, written in Cython (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-qscintilla</b> 2.9-1<br/>
    Python 3.x bindings for QScintilla2<br/>
<br/>mingw/<b>mingw-w64-python3-qtconsole</b> 4.2.1-1<br/>
    A rich Qt-based console for working with Jupyter kernels, supporting rich media output, session export, and more. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-reportlab</b> 3.0-4<br/>
    A proven industry-strength PDF generating solution (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-requests</b> 2.13.0-1<br/>
    Requests is the only Non-GMO HTTP library for Python, safe for human consumption. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-rst2pdf</b> 0.93-2<br/>
    Create PDFs from simple text markup, no LaTeX required (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-scipy</b> 0.18.1-1<br/>
    SciPy is open-source software for mathematics, science, and engineering. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-setuptools</b> 31.0.0-1 <br/>
    Easily download, build, install, upgrade, and uninstall Python packages (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-shiboken-qt4</b> 1.2.2-3<br/>
    Support library for Python3 bindings (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-simplegeneric</b> 0.8.1-1<br/>
    File system based database that uses python pickles (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-sip</b> 4.19.1-1<br/>
    Python 3.x SIP bindings for C and C++ libraries (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-six</b> 1.10.0-1 <br/>
    Python 2 and 3 compatibility utilities (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-snowballstemmer</b> 1.2.1-1<br/>
    Snowball stemming library collection for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-sphinx</b> 1.5.3-1<br/>
    Python3 documentation generator<br/>
<br/>mingw/<b>mingw-w64-python3-sphinx-alabaster-theme</b> 0.7.9-1<br/>
    Modified Kr Sphinx doc theme (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-sphinx_rtd_theme</b> 0.1.9-1<br/>
    Python Sphinx Read The Docs Theme (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-sqlitedict</b> 1.4.1-1<br/>
    Persistent dict, backed by sqlite3 and pickle, multithread-safe (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-statsmodels</b> 0.6.1-2<br/>
    Statistical computations and models for use with SciPy (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-traitlets</b> 4.3.2-1<br/>
    A lightweight Traits like module (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-wcwidth</b> 0.1.7-1<br/>
    Measures number of Terminal column cells of wide-character codes<br/>
<br/>mingw/<b>mingw-w64-python3-win_unicode_console</b> 0.5-1<br/>
    Measures number of Terminal column cells of wide-character codes<br/>
<br/>mingw/<b>mingw-w64-python3-xlsxwriter</b> 0.9.3-1<br/>
    A Python module for creating Excel XLSL files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-zope.event</b> 4.2.0-1<br/>
    Very basic event publishing system (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-python3-zope.interface</b> 4.1.3-1<br/>
    Interfaces for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-qbs</b> 1.7.1-1 <br/>
    Qt Build Suite (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-qca-qt4-git</b> 2220.66b9754-1<br/>
    Qt Cryptographic Architecture (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-qca-qt5-git</b> 2219.4fd11c4-1<br/>
    Qt Cryptographic Architecture (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-qemu</b> 2.8.0-1<br/>
    A generic and open source processor emulator (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-qhull-git</b> r157.f0bd8ce-1<br/>
    A general dimension code for computing convex hulls and related structures (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-qjson-qt4</b> 0.8.1-3<br/>
    QJson is a qt-based library that maps JSON data to QVariant objects (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-qrencode</b> 3.4.4-1<br/>
    C library for encoding data in a QR Code symbol (mingw-w64).<br/>
<br/>mingw/<b>mingw-w64-qrupdate-svn</b> r28-4<br/>
    qrupdate is a Fortran library for fast updates of QR and Cholesky decompositions (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-qscintilla</b> 2.9-1<br/>
    A port to Qt5 of Neil Hodgson's Scintilla C++ editor class<br/>
<br/>mingw/<b>mingw-w64-qt-creator</b> 4.2.1-2 <br/>
    Cross-platform IDE (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-qt-installer-framework-git</b> r2902.557c96f-1<br/>
    The Qt Installer Framework used for the Qt SDK installer (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-qt4</b> 4.8.7-4 (mingw-w64-x86_64-qt4)<br/>
    <br/>
<br/>mingw/<b>mingw-w64-qt5</b> 5.8.0-3 (mingw-w64-x86_64-qt mingw-w64-x86_64-qt5) <br/>
    A cross-platform application and UI framework (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-qt5-static</b> 5.8.0-1 (mingw-w64-x86_64-qt mingw-w64-x86_64-qt5)<br/>
    A cross-platform application and UI framework (mingw-w64-static)<br/>
<br/>mingw/<b>mingw-w64-qtbinpatcher</b> 2.2.0-1 <br/>
    Patcher for Qt libraries (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-qtwebkit</b> tp5-3<br/>
    Webkit module for Qt5 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-quantlib</b> 1.6.2-1<br/>
    QuantLib - A free/open-source library for quantitative finance (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-quassel</b> 0.12.2-3<br/>
    Next-generation distributed IRC client (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-quazip</b> 0.7.1-1<br/>
    C++ wrapper for the Gilles Vollant's ZIP/UNZIP C package (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-qwt-qt4</b> 6.1.2-2<br/>
    Qt Widgets for Technical Applications for Qt4 (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-qwt-qt5</b> 6.1.2-2<br/>
    Qt Widgets for Technical Applications (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-qxmpp</b> 0.9.3-1<br/>
    Cross-platform C++ XMPP client and server library<br/>
<br/>mingw/<b>mingw-w64-qxmpp-qt4</b> 0.8.3-2<br/>
    Cross-platform C++ XMPP client and server library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-rabbitmq-c</b> 0.8.0-1<br/>
    RabbitMQ C client (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ragel</b> 6.9-2<br/>
    Compiles finite state machines from regular languages into executable C, C++, Objective-C, or D code (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-rapidjson</b> 1.0.2-1<br/>
    A fast JSON parser/generator for C++ with both SAX/DOM style API (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-readline</b> 7.0.003-1 <br/>
    MinGW port of readline for editing typed command lines (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-readosm</b> 1.0.0e-1<br/>
    Library to extract valid data from within an Open Street Map input file (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-recode</b> 3.6-5<br/>
    Converts files between various character sets and usages (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-rtmpdump-git</b> r512.fa8646d-2 <br/>
    A tool to download rtmp streams (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-rubberband</b> 1.8.1-2<br/>
    High quality software library for audio time-stretching and pitch-shifting. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-ruby</b> 2.4.0-1 <br/>
    An object-oriented language for quick and easy programming (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-rust</b> 1.15.1-1<br/>
    Systems programming language focused on safety, speed and concurrency (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-rxspencer</b> alpha3.8.g6-2<br/>
    Henry Spencer's BSD regular expression library modified to allow building as a shared library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-schroedinger</b> 1.0.11-3<br/>
    An implemenation of the Dirac video codec in ANSI C code (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-scite</b> 3.7.3-1 <br/>
    Editor with facilities for building and running programs (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-scite-defaults</b> 3.7.3-1 <br/>
    Default language files for the SciTE editor (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-sfml</b> 2.4.2-1<br/>
    A simple, fast, cross-platform, and object-oriented multimedia API (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-sgml-common</b> 0.6.3-1<br/>
    Tools for maintaining centralized SGML catalogs. (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-shapelib</b> 1.3.0-2<br/>
    simple C API for reading and writing ESRI Shapefiles (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-shared-mime-info</b> 1.4-2 <br/>
    Freedesktop.org Shared MIME Info (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-shiboken-qt4</b> 1.2.2-3<br/>
    CPython bindings generator for C++ libraries (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-shishi-git</b> r3585.51e0f1c-1<br/>
    a GNU implementation of the Kerberos 5 network security system (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-silc-toolkit</b> 1.1.12-2<br/>
    Secure Internet Live Conferencing (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-sip</b> 4.19.1-1<br/>
    A tool that makes it easy to create Python bindings for C and C++ libraries (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-smpeg</b> 0.4.5-1<br/>
    SDL MPEG Player Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-smpeg2</b> 2.0.0-4<br/>
    SDL2 MPEG Player Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-snappy</b> 1.1.4-1<br/>
    A fast C++ compressor/decompressor library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-snoregrowl</b> 0.4.0-3<br/>
    A C and C++ library providing an api to use Growl notifications, based on the GNTP protocol (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-snorenotify</b> 0.7.0-1<br/>
    Snorenotify is a multi platform Qt notification framework. Using a plugin system it is possible to create notifications with many different notification systems on Windows, Mac OS and Unix and mobile Devices (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-soci</b> 3.2.3-1<br/>
    SOCI - The C++ Database Access Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-soundtouch</b> 1.9.2-1<br/>
    An audio processing library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-source-highlight</b> 3.1.8-1<br/>
    Convert source code to syntax highlighted document (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-sparsehash</b> 2.0.2-3<br/>
    Library that contains several hash-map implementations, including implementations that optimize for space or speed (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-spatialite-tools</b> 4.3.0-2<br/>
    Set of CLI tools for spatialite (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-spdylay</b> 1.4.0-1 <br/>
    The experimental SPDY protocol version 2, 3 and 3.1 implementation in C (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-speex</b> 1.2.0-1<br/>
    A free codec for free speech (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-speexdsp</b> 1.2rc3-2<br/>
    DSP library derived from Speex (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-spice-gtk</b> 0.33-1<br/>
    GTK3 widget for SPICE clients (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-spice-protocol</b> 0.12.12-1<br/>
    SPICE protocol headers (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-spirv-tools</b> 2016.6-1 (mingw-w64-x86_64-vulkan-devel)<br/>
    API and commands for processing SPIR-V modules (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-sqlheavy</b> 0.1.1-2<br/>
    GNOME Docking Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-sqlite-analyzer</b> 3.16.1-1 <br/>
    An analysis program SQLite database files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-sqlite3</b> 3.16.1-1 <br/>
    A C library that implements an SQL database engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-stxxl-git</b> 1.4.1.343.gf7389c7-2<br/>
    Standard Template Library for Extra Large Data Sets (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-suitesparse</b> 4.4.4-1<br/>
    A suite of sparse matrix algorithms (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-swig</b> 3.0.6-1<br/>
    Generate scripting interfaces to C/C++ code<br/>
<br/>mingw/<b>mingw-w64-szip</b> 2.1-5 <br/>
    Extended-Rice lossless compression algorithm implementation (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-taglib</b> 1.10beta-1<br/>
    A Library for reading and editing the meta-data of several popular audio formats (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tcl</b> 8.6.6-1 <br/>
    The Tcl scripting language (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tcllib</b> 1.18-1<br/>
    Set of pure-Tcl extensions (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tclvfs-cvs</b> 20130425-3<br/>
    Virtual Filesystem support for Tcl<br/>
<br/>mingw/<b>mingw-w64-tclx</b> 8.4.1-3<br/>
    Extends Tcl by providing new operating system interface commands, extended file control and many other.<br/>
<br/>mingw/<b>mingw-w64-termcap</b> 1.3.1-2 <br/>
    Terminal feature database (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-afr</b> 3.04.00-1 (tesseract-data)<br/>
    (afr) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-amh</b> 3.04.00-1 (tesseract-data)<br/>
    (amh) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-ara</b> 3.04.00-1 (tesseract-data)<br/>
    (ara) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-asm</b> 3.04.00-1 (tesseract-data)<br/>
    (asm) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-aze</b> 3.04.00-1 (tesseract-data)<br/>
    (aze) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-aze_cyrl</b> 3.04.00-1 (tesseract-data)<br/>
    (aze_cyrl) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-bel</b> 3.04.00-1 (tesseract-data)<br/>
    (bel) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-ben</b> 3.04.00-1 (tesseract-data)<br/>
    (ben) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-bod</b> 3.04.00-1 (tesseract-data)<br/>
    (bod) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-bos</b> 3.04.00-1 (tesseract-data)<br/>
    (bos) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-bul</b> 3.04.00-1 (tesseract-data)<br/>
    (bul) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-cat</b> 3.04.00-1 (tesseract-data)<br/>
    (cat) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-ceb</b> 3.04.00-1 (tesseract-data)<br/>
    (ceb) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-ces</b> 3.04.00-1 (tesseract-data)<br/>
    (ces) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-chi_sim</b> 3.04.00-1 (tesseract-data)<br/>
    (chi_sim) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-chi_tra</b> 3.04.00-1 (tesseract-data)<br/>
    (chi_tra) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-chr</b> 3.04.00-1 (tesseract-data)<br/>
    (chr) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-cym</b> 3.04.00-1 (tesseract-data)<br/>
    (cym) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-dan</b> 3.04.00-1 (tesseract-data)<br/>
    (dan) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-dan_frak</b> 3.04.00-1 (tesseract-data)<br/>
    (dan_frak) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-deu</b> 3.04.00-1 (tesseract-data)<br/>
    (deu) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-deu_frak</b> 3.04.00-1 (tesseract-data)<br/>
    (deu_frak) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-dzo</b> 3.04.00-1 (tesseract-data)<br/>
    (dzo) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-ell</b> 3.04.00-1 (tesseract-data)<br/>
    (ell) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-eng</b> 3.04.00-1 (tesseract-data)<br/>
    (eng) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-enm</b> 3.04.00-1 (tesseract-data)<br/>
    (enm) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-epo</b> 3.04.00-1 (tesseract-data)<br/>
    (epo) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-equ</b> 3.04.00-1 (tesseract-data)<br/>
    (equ) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-est</b> 3.04.00-1 (tesseract-data)<br/>
    (est) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-eus</b> 3.04.00-1 (tesseract-data)<br/>
    (eus) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-fas</b> 3.04.00-1 (tesseract-data)<br/>
    (fas) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-fin</b> 3.04.00-1 (tesseract-data)<br/>
    (fin) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-fra</b> 3.04.00-1 (tesseract-data)<br/>
    (fra) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-frk</b> 3.04.00-1 (tesseract-data)<br/>
    (frk) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-frm</b> 3.04.00-1 (tesseract-data)<br/>
    (frm) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-gle</b> 3.04.00-1 (tesseract-data)<br/>
    (gle) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-glg</b> 3.04.00-1 (tesseract-data)<br/>
    (glg) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-grc</b> 3.04.00-1 (tesseract-data)<br/>
    (grc) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-guj</b> 3.04.00-1 (tesseract-data)<br/>
    (guj) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-hat</b> 3.04.00-1 (tesseract-data)<br/>
    (hat) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-heb</b> 3.04.00-1 (tesseract-data)<br/>
    (heb) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-hin</b> 3.04.00-1 (tesseract-data)<br/>
    (hin) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-hrv</b> 3.04.00-1 (tesseract-data)<br/>
    (hrv) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-hun</b> 3.04.00-1 (tesseract-data)<br/>
    (hun) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-iku</b> 3.04.00-1 (tesseract-data)<br/>
    (iku) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-ind</b> 3.04.00-1 (tesseract-data)<br/>
    (ind) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-isl</b> 3.04.00-1 (tesseract-data)<br/>
    (isl) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-ita</b> 3.04.00-1 (tesseract-data)<br/>
    (ita) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-ita_old</b> 3.04.00-1 (tesseract-data)<br/>
    (ita_old) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-jav</b> 3.04.00-1 (tesseract-data)<br/>
    (jav) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-jpn</b> 3.04.00-1 (tesseract-data)<br/>
    (jpn) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-kan</b> 3.04.00-1 (tesseract-data)<br/>
    (kan) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-kat</b> 3.04.00-1 (tesseract-data)<br/>
    (kat) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-kat_old</b> 3.04.00-1 (tesseract-data)<br/>
    (kat_old) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-kaz</b> 3.04.00-1 (tesseract-data)<br/>
    (kaz) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-khm</b> 3.04.00-1 (tesseract-data)<br/>
    (khm) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-kir</b> 3.04.00-1 (tesseract-data)<br/>
    (kir) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-kor</b> 3.04.00-1 (tesseract-data)<br/>
    (kor) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-kur</b> 3.04.00-1 (tesseract-data)<br/>
    (kur) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-lao</b> 3.04.00-1 (tesseract-data)<br/>
    (lao) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-lat</b> 3.04.00-1 (tesseract-data)<br/>
    (lat) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-lav</b> 3.04.00-1 (tesseract-data)<br/>
    (lav) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-lit</b> 3.04.00-1 (tesseract-data)<br/>
    (lit) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-mal</b> 3.04.00-1 (tesseract-data)<br/>
    (mal) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-mar</b> 3.04.00-1 (tesseract-data)<br/>
    (mar) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-mkd</b> 3.04.00-1 (tesseract-data)<br/>
    (mkd) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-mlt</b> 3.04.00-1 (tesseract-data)<br/>
    (mlt) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-msa</b> 3.04.00-1 (tesseract-data)<br/>
    (msa) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-mya</b> 3.04.00-1 (tesseract-data)<br/>
    (mya) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-nep</b> 3.04.00-1 (tesseract-data)<br/>
    (nep) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-nld</b> 3.04.00-1 (tesseract-data)<br/>
    (nld) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-nor</b> 3.04.00-1 (tesseract-data)<br/>
    (nor) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-ori</b> 3.04.00-1 (tesseract-data)<br/>
    (ori) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-pan</b> 3.04.00-1 (tesseract-data)<br/>
    (pan) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-pol</b> 3.04.00-1 (tesseract-data)<br/>
    (pol) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-por</b> 3.04.00-1 (tesseract-data)<br/>
    (por) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-pus</b> 3.04.00-1 (tesseract-data)<br/>
    (pus) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-ron</b> 3.04.00-1 (tesseract-data)<br/>
    (ron) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-rus</b> 3.04.00-1 (tesseract-data)<br/>
    (rus) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-san</b> 3.04.00-1 (tesseract-data)<br/>
    (san) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-sin</b> 3.04.00-1 (tesseract-data)<br/>
    (sin) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-slk</b> 3.04.00-1 (tesseract-data)<br/>
    (slk) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-slk_frak</b> 3.04.00-1 (tesseract-data)<br/>
    (slk_frak) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-slv</b> 3.04.00-1 (tesseract-data)<br/>
    (slv) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-spa</b> 3.04.00-1 (tesseract-data)<br/>
    (spa) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-spa_old</b> 3.04.00-1 (tesseract-data)<br/>
    (spa_old) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-sqi</b> 3.04.00-1 (tesseract-data)<br/>
    (sqi) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-srp</b> 3.04.00-1 (tesseract-data)<br/>
    (srp) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-srp_latn</b> 3.04.00-1 (tesseract-data)<br/>
    (srp_latn) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-swa</b> 3.04.00-1 (tesseract-data)<br/>
    (swa) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-swe</b> 3.04.00-1 (tesseract-data)<br/>
    (swe) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-syr</b> 3.04.00-1 (tesseract-data)<br/>
    (syr) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-tam</b> 3.04.00-1 (tesseract-data)<br/>
    (tam) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-tel</b> 3.04.00-1 (tesseract-data)<br/>
    (tel) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-tgk</b> 3.04.00-1 (tesseract-data)<br/>
    (tgk) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-tgl</b> 3.04.00-1 (tesseract-data)<br/>
    (tgl) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-tha</b> 3.04.00-1 (tesseract-data)<br/>
    (tha) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-tir</b> 3.04.00-1 (tesseract-data)<br/>
    (tir) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-tur</b> 3.04.00-1 (tesseract-data)<br/>
    (tur) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-uig</b> 3.04.00-1 (tesseract-data)<br/>
    (uig) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-ukr</b> 3.04.00-1 (tesseract-data)<br/>
    (ukr) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-urd</b> 3.04.00-1 (tesseract-data)<br/>
    (urd) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-uzb</b> 3.04.00-1 (tesseract-data)<br/>
    (uzb) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-uzb_cyrl</b> 3.04.00-1 (tesseract-data)<br/>
    (uzb_cyrl) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-vie</b> 3.04.00-1 (tesseract-data)<br/>
    (vie) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-data-yid</b> 3.04.00-1 (tesseract-data)<br/>
    (yid) Language tessdata for Tesseract OCR engine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tesseract-ocr</b> 3.04.01-2<br/>
    Tesseract OCR (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tinyformat</b> 2.0.1-1<br/>
    A minimal type safe printf() replacement (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tinyxml</b> 2.6.2-3<br/>
    Simple, small, C++ XML parser that can be easily integrated into other programs (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tinyxml2</b> 4.0.1-1<br/>
    Simple, small, C++ XML parser that can be easily integrated into other programs (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tk</b> 8.6.6-1 <br/>
    A windowing toolkit for use with tcl (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tkimg</b> 1.4.2-3<br/>
    Adds support to Tk for many other Image formats: BMP, XBM, XPM, GIF, PNG, JPEG, TIFF and postscript (mingw-64)<br/>
<br/>mingw/<b>mingw-w64-tklib</b> 0.6-5<br/>
    A companion to Tcllib, for Tk related packages (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tktable</b> 2.10-4<br/>
    A full-featured 2D table widget for Tk (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tolua</b> 5.2.4-3<br/>
    A tool that greatly simplifies the integration of C/C++ code with Lua (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-tools-git</b> 5.0.0.4760.d3089b5-1 (mingw-w64-x86_64-toolchain) <br/>
    MinGW-w64 tools<br/>
<br/>mingw/<b>mingw-w64-totem-pl-parser</b> 3.10.7-1<br/>
    Simple GObject-based library to parse and save a host of playlist formats (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-twolame</b> 0.3.13-2<br/>
    An optimized MPEG Audio Layer 2 (MP2) encoder (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-uchardet</b> 0.0.6-1<br/>
    An encoding detector library ported from Mozilla (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-udis86</b> 1.7.2-1<br/>
    A minimalistic disassembler library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-uhttpmock</b> 0.5.0-1<br/>
    uhttpmock is a HTTP web service mocking project for projects which use libsoup (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-unbound</b> 1.5.10-1<br/>
    Validating, recursive, and caching DNS resolver (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-unibilium</b> 1.2.0-1<br/>
    A terminfo parsing library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-universal-ctags-git</b> r2635.80256f4-1<br/>
    A maintained Ctags implementation (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-uriparser</b> 0.8.4-1<br/>
    RFC 3986 URI parsing and processing libary (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-usbredir</b> 0.7.1-1<br/>
    Parser for the usbredir protocol (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-usbview-git</b> 42.c4ba9c6-1<br/>
    GUI for browsing all USB controllers and connected USB devices on your computer (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-usql</b> 0.8.1-1<br/>
    SQL parser engine for C++ (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-usrsctp</b> 0.9.3.0-1<br/>
    A portable SCTP userland stack (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-vala</b> 0.34.0-1 <br/>
    Compiler for the GObject type system (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-vamp-plugin-sdk</b> 2.6-1<br/>
    Vamp plugins extract descriptive information from audio data (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-vcdimager</b> 0.7.24-2<br/>
    A full-featured mastering suite for authoring disassembling and analyzing Video CD's and Super Video CD's (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-verilator</b> 3.900-1<br/>
    The fastest free Verilog HDL simulator (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-virt-viewer</b> 4.0-1<br/>
    Displaying the graphical console of a virtual machine (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-vlc-git</b> 3.0.0.61503.1d43e72-1<br/>
    A multi-platform MPEG, VCD/DVD, and DivX player<br/>
<br/>mingw/<b>mingw-w64-vtk</b> 7.0.0-1<br/>
    A software system for 3D computer graphics, image processing and visualization (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-vulkan-headers</b> 1~1.0.38-1 (mingw-w64-x86_64-vulkan-devel)<br/>
    Vulkan header files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-vulkan-html-docs</b> 1~1.0.38-1 (mingw-w64-x86_64-vulkan-devel)<br/>
    Vulkan html documentation (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-vulkan-man-pages</b> 1~1.0.38-1 (mingw-w64-x86_64-vulkan-devel)<br/>
    Vulkan man pages (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-waf</b> 1.9.6-1<br/>
    General-purpose build system modelled after Scons (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-wavpack</b> 5.0.0-1<br/>
    Audio compression format with lossless, lossy and hybrid compression modes (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-webkitgtk2</b> 2.4.11-2 <br/>
    GTK+ Web content engine library (mingw-w64) for GTK2<br/>
<br/>mingw/<b>mingw-w64-webkitgtk3</b> 2.4.11-2<br/>
    GTK+ Web content engine library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-win7appid</b> 1.1-3 <br/>
    Windows 7 (and up) shortcut application id tool<br/>
<br/>mingw/<b>mingw-w64-windows-default-manifest</b> 6.4-3 <br/>
    Default Windows application manifest (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-wined3d</b> 1.9.2-1<br/>
    Direct3D to OpenGL translator (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-wineditline</b> 2.101-4 <br/>
    port of the NetBSD Editline library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-winico</b> 0.6-2<br/>
    Tk extension for Windows for enhanced icon handling and manipulation of an icon in the Windows taskbar and system tray (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-winpthreads-git</b> 5.0.0.4761.02bea78-1 (mingw-w64-x86_64-toolchain) <br/>
    MinGW-w64 winpthreads library<br/>
<br/>mingw/<b>mingw-w64-winsparkle</b> 0.5.2-1<br/>
    App update framework for Windows, inspired by Sparkle for OS X (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-winstorecompat-git</b> 5.0.0.4760.d3089b5-1 (mingw-w64-x86_64-toolchain)<br/>
    MinGW-w64 winRT compat library<br/>
<br/>mingw/<b>mingw-w64-wintab-sdk</b> 1.4-2<br/>
    Wintab Interface Specification (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-wkhtmltopdf-git</b> 0.13.r1049.51f9658-1<br/>
    Convert HTML to PDF using QtWebkit (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-wslay</b> 1.0.0-2<br/>
    The WebSocket library in C (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-wxPython</b> 3.0.2.0-6<br/>
    A wxWidgets GUI toolkit for Python (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-wxWidgets</b> 3.0.2-17 <br/>
    A C++ library that lets developers create applications for Windows, Linux and UNIX (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-x264-git</b> r2721.72d53ab-1<br/>
    Library for encoding H264/AVC video streams (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-x265</b> 2.1-1<br/>
    Open Source H265/HEVC video encoder (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-xalan-c</b> 1.11-5<br/>
    An XSLT processing library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-xapian-core</b> 1~1.4.2-1<br/>
    Open source search engine library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-xerces-c</b> 3.1.4-1<br/>
    A validating XML parser written in a portable subset of C++ (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-xmlstarlet-git</b> r678.9a470e3-2<br/>
    Command-line XML toolkit<br/>
<br/>mingw/<b>mingw-w64-xpdf</b> 3.04-1<br/>
    Utilities for PDF files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-xpm-nox</b> 4.2.0-4 <br/>
    X Pixmap library not using X (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-xvidcore</b> 1.3.4-2<br/>
    XviD is an open source MPEG-4 video codec (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-xxhash</b> 0.6.1-1<br/>
    Extremely fast non-cryptographic hash algorithm (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-xz</b> 5.2.3-1 <br/>
    Library and command line tools for XZ and LZMA compressed files (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-yajl</b> 2.1.0-1<br/>
    Yet Another JSON Library (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-yaml-cpp</b> 0.5.3-1<br/>
    A YAML parser and emitter in C++ matching the YAML 1.2 spec (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-yaml-cpp0.3</b> 0.3.0-2<br/>
    A YAML parser and emitter in C++ matching the YAML 1.2 spec (mingw-w64) - old version<br/>
<br/>mingw/<b>mingw-w64-yasm</b> 1.3.0-2 <br/>
    A rewrite of NASM to allow for multiple syntax supported (NASM, TASM, GAS, etc.) (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-zeromq</b> 4.2.2-1<br/>
    Fast messaging system built on sockets, C and C++ bindings. aka 0MQ, ZMQ (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-zlib</b> 1.2.11-1 <br/>
    Compression library implementing the deflate compression method found in gzip and PKZIP (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-zopfli</b> 1.0.1-1<br/>
    A compression library programmed in C to perform very good, but slow, deflate or zlib compression (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-zstd</b> 1.1.2-1<br/>
    Zstandard - Fast real-time compression algorithm (mingw-w64)<br/>
<br/>mingw/<b>mingw-w64-zziplib</b> 0.13.62-5 <br/>
    A lightweight library that offers the ability to easily extract data from files archived in a single zip file (mingw-w64)<br/>
<br/>msys/<b>apr</b> 1.5.2-1 (libraries) <br/>
    The Apache Portable Runtime<br/>
<br/>msys/<b>apr-devel</b> 1.5.2-1 (development)<br/>
    Libapr headers and libraries<br/>
<br/>msys/<b>apr-util</b> 1.5.4-2 (libraries) <br/>
    The Apache Portable Runtime<br/>
<br/>msys/<b>apr-util-devel</b> 1.5.4-2 (development)<br/>
    Libapr-util headers and libraries<br/>
<br/>msys/<b>asciidoc</b> 8.6.9-4 (base-devel) <br/>
    Text document format for short documents, articles, books and UNIX man pages.<br/>
<br/>msys/<b>atool</b> 0.39.0-1<br/>
    A script for managing file archives of various types<br/>
<br/>msys/<b>autoconf</b> 2.69-3 (base-devel) <br/>
    A GNU tool for automatically configuring source code<br/>
<br/>msys/<b>autoconf-archive</b> 2016.09.16-1<br/>
    Autoconf Macro Archive<br/>
<br/>msys/<b>autoconf2.13</b> 2.13-2 (base-devel) <br/>
    A GNU tool for automatically configuring source code<br/>
<br/>msys/<b>autogen</b> 5.18.4-2 (base-devel) <br/>
    A tool designed to simplify the creation and maintenance of programs that contain large amounts of repetitious text<br/>
<br/>msys/<b>automake-wrapper</b> 10-1 (base-devel) <br/>
    Wrapper scripts for automake and aclocal<br/>
<br/>msys/<b>automake1.10</b> 1.10.3-3 (base-devel) <br/>
    A GNU tool for automatically creating Makefiles<br/>
<br/>msys/<b>automake1.11</b> 1.11.6-3 (base-devel) <br/>
    A GNU tool for automatically creating Makefiles<br/>
<br/>msys/<b>automake1.12</b> 1.12.6-3 (base-devel) <br/>
    A GNU tool for automatically creating Makefiles<br/>
<br/>msys/<b>automake1.13</b> 1.13.4-4 (base-devel) <br/>
    A GNU tool for automatically creating Makefiles<br/>
<br/>msys/<b>automake1.14</b> 1.14.1-3 (base-devel) <br/>
    A GNU tool for automatically creating Makefiles<br/>
<br/>msys/<b>automake1.15</b> 1.15-2 (base-devel) <br/>
    A GNU tool for automatically creating Makefiles<br/>
<br/>msys/<b>automake1.6</b> 1.6.3-2 (base-devel) <br/>
    A GNU tool for automatically creating Makefiles<br/>
<br/>msys/<b>automake1.7</b> 1.7.9-2 (base-devel) <br/>
    A GNU tool for automatically creating Makefiles<br/>
<br/>msys/<b>automake1.8</b> 1.8.5-3 (base-devel) <br/>
    A GNU tool for automatically creating Makefiles<br/>
<br/>msys/<b>automake1.9</b> 1.9.6-2 (base-devel) <br/>
    A GNU tool for automatically creating Makefiles<br/>
<br/>msys/<b>bash</b> 4.4.012-1 (base) <br/>
    The GNU Bourne Again shell<br/>
<br/>msys/<b>bash-completion</b> 2.3-1 (base) <br/>
    Programmable completion for the bash shell<br/>
<br/>msys/<b>bash-devel</b> 4.4.012-1 (development) <br/>
    Bash headers and libraries<br/>
<br/>msys/<b>bc</b> 1.06-3<br/>
    An arbitrary precision calculator language<br/>
<br/>msys/<b>binutils</b> 2.25.1-2 (msys2-devel) <br/>
    A set of programs to assemble and manipulate binary and object files<br/>
<br/>msys/<b>bison</b> 3.0.4-1 (base-devel) <br/>
    The GNU general-purpose parser generator<br/>
<br/>msys/<b>bsdcpio</b> 3.2.2-2 (base) <br/>
    library that can create and read several streaming archive formats<br/>
<br/>msys/<b>bsdtar</b> 3.2.2-2 (base) <br/>
    library that can create and read several streaming archive formats<br/>
<br/>msys/<b>busybox</b> 1.22.1-2<br/>
    BusyBox: The Swiss Army Knife of Embedded Linux<br/>
<br/>msys/<b>bzip2</b> 1.0.6-2 (base compression) <br/>
    A high-quality data compression program<br/>
<br/>msys/<b>bzr</b> 2.7.0-2 (VCS)<br/>
    Bazaar is a version control system that helps you track project history over time and to collaborate easily with others.<br/>
<br/>msys/<b>bzr-fastimport</b> 0.13.0-1<br/>
    Bazaar Fast Import is a plugin providing fast loading of revision control data into Bazaar.<br/>
<br/>msys/<b>ca-certificates</b> 20150426-1 <br/>
    Common CA certificates<br/>
<br/>msys/<b>catgets</b> 1.1-2 (base) <br/>
    catgets message catalog API<br/>
<br/>msys/<b>ccache</b> 3.3.3-1<br/>
    A compiler cache (mingw-w64)<br/>
<br/>msys/<b>cdecl</b> 2.5-1<br/>
    A program for encoding and decoding C (or C++) type declarations<br/>
<br/>msys/<b>cgdb</b> 0.6.8-2<br/>
    Curses-based interface to the GNU Debugger<br/>
<br/>msys/<b>clang-svn</b> 60106.1d5b05f-1<br/>
    C language family frontend for LLVM (mingw-w64)<br/>
<br/>msys/<b>cloc</b> 1.66-1<br/>
    Count lines of code<br/>
<br/>msys/<b>cmake</b> 3.6.2-1<br/>
    A cross-platform open-source make system<br/>
<br/>msys/<b>cocom</b> 0.996-2 (msys2-devel) <br/>
    Toolset for creation of compilers and interpreters<br/>
<br/>msys/<b>colordiff</b> 1.0.16-1<br/>
    Diff wrapper with pretty syntax highlighting<br/>
<br/>msys/<b>colormake-git</b> r8.9c1d2e6-1<br/>
    Colorized build output<br/>
<br/>msys/<b>conemu-git</b> r3330.34a88ed-1<br/>
    Customizable Windows console emulator with tabs<br/>
<br/>msys/<b>coreutils</b> 8.26-1 (base) <br/>
    The basic file, shell and text manipulation utilities of the GNU operating system<br/>
<br/>msys/<b>crosstool-ng</b> 1.21.0-1<br/>
    A cross-platform open-source toolchain system<br/>
<br/>msys/<b>crosstool-ng-git</b> 1.19.314.a483cd9-1<br/>
    A cross-platform open-source toolchain system<br/>
<br/>msys/<b>crypt</b> 1.4-1 (base) <br/>
    Encryption/Decryption utility<br/>
<br/>msys/<b>cscope</b> 15.8b-1<br/>
    A tool for browsing source code<br/>
<br/>msys/<b>ctags</b> 5.8-1<br/>
    Generate tag files for source code<br/>
<br/>msys/<b>curl</b> 7.53.1-1 (base) <br/>
    Multi-protocol file transfer utility<br/>
<br/>msys/<b>cvs</b> 1.11.23-2<br/>
    Concurrent Versions System - a source control system<br/>
<br/>msys/<b>cygrunsrv</b> 1.62-1<br/>
    cygrunsrv is a windows services tool<br/>
<br/>msys/<b>cyrus-sasl</b> 2.1.26-8 (sys-utils) <br/>
    Cyrus saslauthd SASL authentication daemon<br/>
<br/>msys/<b>dash</b> 0.5.9.1-1 (base) <br/>
    A POSIX compliant shell that aims to be as small as possible<br/>
<br/>msys/<b>db</b> 5.3.28-2 (Database) <br/>
    The Berkeley DB embedded database system<br/>
<br/>msys/<b>db-docs</b> 5.3.28-2<br/>
    BerkleyDB documentation<br/>
<br/>msys/<b>dejagnu</b> 1.5.3-1<br/>
    Framework for testing other programs<br/>
<br/>msys/<b>delta</b> 20060803-1<br/>
    An useful tool that lets you minimize interesting files subject to a test of their interestingness.<br/>
<br/>msys/<b>depot-tools-git</b> r2542.77b74b5-1<br/>
    Build tools for working with Chromium development, include gclient<br/>
<br/>msys/<b>diffstat</b> 1.58-1 (base-devel) <br/>
    Display a histogram of diff changes<br/>
<br/>msys/<b>diffutils</b> 3.5-1 (base-devel) <br/>
    Utility programs used for creating patch files<br/>
<br/>msys/<b>docbook-dsssl</b> 1.79-1<br/>
    DSSSL Stylesheets for DocBook<br/>
<br/>msys/<b>docbook-mathml</b> 1.1CR1-1<br/>
    MathML XML scheme<br/>
<br/>msys/<b>docbook-sgml</b> 4.5-1<br/>
    Document type definitions for verification of SGML data files against the DocBook rule set.<br/>
<br/>msys/<b>docbook-sgml31</b> 3.1-1<br/>
    Legacy docbook-sgml<br/>
<br/>msys/<b>docbook-xml</b> 4.5-2 <br/>
    A widely used XML scheme for writing documentation and help<br/>
<br/>msys/<b>docbook-xsl</b> 1.78.1-3 <br/>
    XML stylesheets for Docbook-xml transformations<br/>
<br/>msys/<b>docx2txt</b> 1.4-1<br/>
    docx2txt is a perl based command line utility to convert Microsoft Office(Tm) Docx documents to equivalent Text documents<br/>
<br/>msys/<b>dos2unix</b> 7.3.4-1 (base-devel) <br/>
    Text file format converter<br/>
<br/>msys/<b>doxygen</b> 1.8.11-1 <br/>
    A documentation system for C++, C, Java, IDL and PHP<br/>
<br/>msys/<b>easyoptions-git</b> r37.c481763-1<br/>
    Easy option parsing for Ruby and Bash<br/>
<br/>msys/<b>ed</b> 1.12-1<br/>
    A POSIX-compliant line-oriented text editor<br/>
<br/>msys/<b>elinks-git</b> 0.13.3994.e957e60d-1 (net-utils)<br/>
    Full-Featured Text WWW Browser (net-utils)<br/>
<br/>msys/<b>emacs</b> 25.1-1 (editors)<br/>
    The extensible, customizable, self-documenting, real-time display editor (msys2)<br/>
<br/>msys/<b>expat</b> 2.2.0-2 <br/>
    An XML parser library<br/>
<br/>msys/<b>expect</b> 5.45-1<br/>
    A tool for automating interactive applications<br/>
<br/>msys/<b>file</b> 5.30-1 (base base-devel) <br/>
    File type identification utility<br/>
<br/>msys/<b>filesystem</b> 2017.02-4 (base) <br/>
    Base filesystem<br/>
<br/>msys/<b>findutils</b> 4.6.0-1 (base) <br/>
    GNU utilities to locate files<br/>
<br/>msys/<b>fish</b> 2.5.0-1<br/>
    a smart and user-friendly command line shell<br/>
<br/>msys/<b>flex</b> 2.6.3-1 (base base-devel) <br/>
    A tool for generating text-scanning programs<br/>
<br/>msys/<b>gamin</b> 0.1.10-3 (libraries)<br/>
    File and directory monitoring system defined to be a subset of the FAM (File Alteration Monitor)<br/>
<br/>msys/<b>gamin-devel</b> 0.1.10-3 (development)<br/>
    Gamin headers and libraries (development)<br/>
<br/>msys/<b>gamin-python</b> 0.1.10-3 (python-modules)<br/>
    Gamin python modules<br/>
<br/>msys/<b>gawk</b> 4.1.4-2 (base base-devel) <br/>
    GNU version of awk<br/>
<br/>msys/<b>gcc</b> 6.3.0-1 (msys2-devel) <br/>
    The GNU Compiler Collection - C and C++ frontends<br/>
<br/>msys/<b>gcc-fortran</b> 6.3.0-1 (msys2-devel) <br/>
    Fortran front-end for GCC<br/>
<br/>msys/<b>gcc-libs</b> 6.3.0-1 (base) <br/>
    Runtime libraries shipped by GCC<br/>
<br/>msys/<b>gdb</b> 7.11.1-1 (base-devel) <br/>
    GNU Debugger (MSYS2 version)<br/>
<br/>msys/<b>gdbm</b> 1.11-3 (Database) <br/>
    GNU database library<br/>
<br/>msys/<b>gengetopt</b> 2.22.6-2<br/>
    A tool to write command line option parsing code for C programs.<br/>
<br/>msys/<b>getent</b> 2.18.90-2 (base) <br/>
    Get entries from Name Service Switch libraries<br/>
<br/>msys/<b>gettext</b> 0.19.7-3 (base-devel) <br/>
    GNU internationalization library<br/>
<br/>msys/<b>gettext-devel</b> 0.19.7-3 (development base-devel) <br/>
    GNU Internationalization development utilities<br/>
<br/>msys/<b>git</b> 2.12.0-1 (VCS) <br/>
    The fast distributed version control system<br/>
<br/>msys/<b>git-bzr-ng-git</b> r61.9878a30-1<br/>
    Bi-directional Git-to-Bzr bridge<br/>
<br/>msys/<b>git-flow</b> 1.10.1-1<br/>
    Git extensions to provide high-level repository operations for Vincent Driessen's branching model (AVH edition)<br/>
<br/>msys/<b>glib2</b> 2.48.0-1 <br/>
    Common C routines used by GTK+ and other libs<br/>
<br/>msys/<b>glib2-devel</b> 2.48.0-1 (development)<br/>
    glib2 headers and libraries<br/>
<br/>msys/<b>glib2-docs</b> 2.48.0-1<br/>
    Documentation for glib2<br/>
<br/>msys/<b>global</b> 6.5.2-1<br/>
    A source code tagging system<br/>
<br/>msys/<b>gmp</b> 6.1.2-1 (libraries) <br/>
    A free library for arbitrary precision arithmetic<br/>
<br/>msys/<b>gmp-devel</b> 6.1.2-1 (development) <br/>
    GMP headers and libraries<br/>
<br/>msys/<b>gnome-doc-utils</b> 0.20.10-1 <br/>
    Documentation utilities for Gnome<br/>
<br/>msys/<b>gnu-netcat</b> 0.7.1-1<br/>
    GNU rewrite of netcat, the network piping application<br/>
<br/>msys/<b>gnupg</b> 1.4.21-2 <br/>
    Complete and free implementation of the OpenPGP standard<br/>
<br/>msys/<b>gnutls</b> 3.4.10-1<br/>
    A library which provides a secure layer over a reliable transport layer<br/>
<br/>msys/<b>gperf</b> 3.1-1 (base-devel) <br/>
    Perfect hash function generator<br/>
<br/>msys/<b>gradle</b> 2.12-1<br/>
    A powerful build system for the JVM<br/>
<br/>msys/<b>gradle-doc</b> 2.12-1<br/>
    A powerful build system for the JVM (documentation and samples)<br/>
<br/>msys/<b>grep</b> 3.0-1 (base base-devel) <br/>
    A string search utility<br/>
<br/>msys/<b>grml-zsh-config</b> 0.12.6-1<br/>
    grml's zsh setup<br/>
<br/>msys/<b>groff</b> 1.22.3-1 (base-devel) <br/>
    GNU troff text-formatting system<br/>
<br/>msys/<b>gtk-doc</b> 1.25-1 <br/>
    Documentation tool for public library API (mingw-w64)<br/>
<br/>msys/<b>guile</b> 2.0.11-3<br/>
    a portable, embeddable Scheme implementation written in C<br/>
<br/>msys/<b>gyp-git</b> r2097.691cecc-1 <br/>
    GYP can Generate Your Projects.<br/>
<br/>msys/<b>gzip</b> 1.8-1 (base compression) <br/>
    GNU compression utility<br/>
<br/>msys/<b>heimdal</b> 1.5.3-9 (sys-utils) <br/>
    Implementation of Kerberos V5 libraries<br/>
<br/>msys/<b>heimdal-devel</b> 1.5.3-9 (development) <br/>
    Heimdal headers and libraries<br/>
<br/>msys/<b>heimdal-libs</b> 1.5.3-9 (libraries) <br/>
    Implementation of Kerberos V5 libraries<br/>
<br/>msys/<b>help2man</b> 1.47.3-1 (base-devel) <br/>
    Conversion tool to create man files<br/>
<br/>msys/<b>icon-naming-utils</b> 0.8.90-1<br/>
    Maps the new names of icons for Tango to the legacy names used by the GNOME and KDE desktops<br/>
<br/>msys/<b>icu</b> 56.1-1 (libraries) <br/>
    International Components for Unicode library<br/>
<br/>msys/<b>icu-devel</b> 56.1-1 (development) <br/>
    ICU headers and libraries<br/>
<br/>msys/<b>idutils</b> 4.6-1<br/>
    A fast, high-capacity, identifier database tool<br/>
<br/>msys/<b>inetutils</b> 1.9.2-1 (base) <br/>
    A collection of common network programs.<br/>
<br/>msys/<b>info</b> 6.3-1 (base) <br/>
    Utilities to work with and produce manuals, ASCII text, and on-line documentation from a single source file<br/>
<br/>msys/<b>intltool</b> 0.51.0-2 (base-devel) <br/>
    The internationalization tool collection<br/>
<br/>msys/<b>irssi</b> 1.0.1-1<br/>
    Modular text mode IRC client with Perl scripting<br/>
<br/>msys/<b>isl</b> 0.16.1-1 (libraries) <br/>
    Library for manipulating sets and relations of integer points bounded by linear constraints<br/>
<br/>msys/<b>isl-devel</b> 0.16.1-1 (development) <br/>
    ISL headers and libraries<br/>
<br/>msys/<b>itstool</b> 2.0.2-2 <br/>
    XML to PO and back again)<br/>
<br/>msys/<b>jhbuild-git</b> 8206.7f97721-1<br/>
    Downloads and compiles Gnome "modules", i.e. source code packages.<br/>
<br/>msys/<b>jsoncpp</b> 1.7.5-1<br/>
    A C++ library for interacting with JSON<br/>
<br/>msys/<b>lemon</b> 3.8.7.0-1 (base-devel) <br/>
    The LEMON LALR Parser Generator used in SQLite 3.8.7.0 (MSYS2)<br/>
<br/>msys/<b>less</b> 481-1 (base) <br/>
    A terminal based program for viewing text files<br/>
<br/>msys/<b>lftp</b> 4.7.6-1 (net-utils)<br/>
    Sophisticated command line based FTP client (net-utils)<br/>
<br/>msys/<b>libarchive</b> 3.2.2-2 (libraries) <br/>
    library that can create and read several streaming archive formats<br/>
<br/>msys/<b>libarchive-devel</b> 3.2.2-2 (development) <br/>
    library that can create and read several streaming archive formats<br/>
<br/>msys/<b>libargp</b> 20110921-1 (base) <br/>
    Interface for parsing command-line arguments<br/>
<br/>msys/<b>libargp-devel</b> 20110921-1 (development) <br/>
    Interface for parsing command-line arguments<br/>
<br/>msys/<b>libasprintf</b> 0.19.7-3 (libraries) <br/>
    C-style formatted output in C++ (runtime)<br/>
<br/>msys/<b>libassuan</b> 2.4.2-1 (libraries) <br/>
    A IPC library used by some GnuPG related software<br/>
<br/>msys/<b>libassuan-devel</b> 2.4.2-1 (development) <br/>
    Libassuan headers and libraries<br/>
<br/>msys/<b>libatomic_ops-devel</b> 7.2.d-1 (development)<br/>
    A garbage collector for C and C++<br/>
<br/>msys/<b>libbz2</b> 1.0.6-2 (libraries) <br/>
    A high-quality data compression program<br/>
<br/>msys/<b>libbz2-devel</b> 1.0.6-2 (development) <br/>
    Libbz2 headers and libraries<br/>
<br/>msys/<b>libcares</b> 1.10.0-2 (libraries)<br/>
    C library that performs DNS requests and name resolves asynchronously (libraries)<br/>
<br/>msys/<b>libcares-devel</b> 1.10.0-2 (development)<br/>
    c-ares headers and libraries (development)<br/>
<br/>msys/<b>libcatgets</b> 1.1-2 (libraries) <br/>
    catgets message catalog API<br/>
<br/>msys/<b>libcatgets-devel</b> 1.1-2 (development)<br/>
    Libcatgets headers and libraries<br/>
<br/>msys/<b>libcrypt</b> 1.4-1 (libraries) <br/>
    Encryption/Decryption utility and library<br/>
<br/>msys/<b>libcrypt-devel</b> 1.4-1 (development) <br/>
    Libcrypt headers and libraries<br/>
<br/>msys/<b>libcurl</b> 7.53.1-1 (libraries) <br/>
    Multi-protocol file transfer library (runtime)<br/>
<br/>msys/<b>libcurl-devel</b> 7.53.1-1 (development) <br/>
    Libcurl headers and libraries<br/>
<br/>msys/<b>libdb</b> 5.3.28-2 (libraries) <br/>
    The Berkeley DB embedded database system<br/>
<br/>msys/<b>libdb-devel</b> 5.3.28-2 (development) <br/>
    libdb headers and libraries<br/>
<br/>msys/<b>libedit</b> 3.1-20150325 (libraries) <br/>
    Libedit is an autotool- and libtoolized port of the NetBSD Editline library.<br/>
<br/>msys/<b>libedit-devel</b> 3.1-20150325 (development) <br/>
    libedit headers and libraries<br/>
<br/>msys/<b>libevent</b> 2.1.4-1 <br/>
    An event notification library<br/>
<br/>msys/<b>libevent-devel</b> 2.1.4-1 (development)<br/>
    Libevent headers and libraries<br/>
<br/>msys/<b>libexpat</b> 2.2.0-2 (libraries) <br/>
    An XML parser library<br/>
<br/>msys/<b>libexpat-devel</b> 2.2.0-2 (development) <br/>
    Libexpat headers and libraries<br/>
<br/>msys/<b>libffi</b> 3.2.1-1 (libraries) <br/>
    Portable, high level programming interface to various calling conventions<br/>
<br/>msys/<b>libffi-devel</b> 3.2.1-1 (development)<br/>
    Libffi headers and libraries<br/>
<br/>msys/<b>libgc</b> 7.2.d-1 <br/>
    A garbage collector for C and C++<br/>
<br/>msys/<b>libgc-devel</b> 7.2.d-1 (development)<br/>
    A garbage collector for C and C++<br/>
<br/>msys/<b>libgcrypt</b> 1.6.4-1 (libraries) <br/>
    General purpose cryptographic library based on the code from GnuPG<br/>
<br/>msys/<b>libgcrypt-devel</b> 1.6.4-1 (development)<br/>
    Libgcrypt headers and libraries<br/>
<br/>msys/<b>libgdbm</b> 1.11-3 (libraries) <br/>
    GNU database library<br/>
<br/>msys/<b>libgdbm-devel</b> 1.11-3 (development)<br/>
    libgdbm headers and libraries<br/>
<br/>msys/<b>libgettextpo</b> 0.19.7-3 (libraries) <br/>
    GNU Internationalization runtime library<br/>
<br/>msys/<b>libgnutls</b> 3.4.10-1 (libraries)<br/>
    A library which provides a secure layer over a reliable transport layer<br/>
<br/>msys/<b>libgnutls-devel</b> 3.4.10-1 (development)<br/>
    Libgnutls headers and libraries<br/>
<br/>msys/<b>libgpg-error</b> 1.25-1 (libraries) <br/>
    Support library for libgcrypt<br/>
<br/>msys/<b>libgpg-error-devel</b> 1.25-1 (development) <br/>
    Libgpg-error headers and libraries<br/>
<br/>msys/<b>libgpgme</b> 1.6.0-1 (libraries) <br/>
    A C wrapper library for GnuPG<br/>
<br/>msys/<b>libgpgme-devel</b> 1.6.0-1 (development) <br/>
    Libgpgme headers and libraries<br/>
<br/>msys/<b>libguile</b> 2.0.11-3 (libraries) <br/>
    a portable, embeddable Scheme implementation written in C<br/>
<br/>msys/<b>libguile-devel</b> 2.0.11-3 (development)<br/>
    a portable, embeddable Scheme implementation written in C<br/>
<br/>msys/<b>libhogweed</b> 3.3-1 (libraries) <br/>
    A low-level cryptographic library<br/>
<br/>msys/<b>libiconv</b> 1.14-2 (libraries) <br/>
    Libiconv is a conversion library<br/>
<br/>msys/<b>libiconv-devel</b> 1.14-2 (development) <br/>
    libiconv headers and libraries<br/>
<br/>msys/<b>libidn</b> 1.33-1 (libraries) <br/>
    Implementation of the Stringprep, Punycode and IDNA specifications<br/>
<br/>msys/<b>libidn-devel</b> 1.33-1 (development) <br/>
    Libidn headers and libraries<br/>
<br/>msys/<b>libintl</b> 0.19.7-3 (libraries) <br/>
    GNU Internationalization runtime library<br/>
<br/>msys/<b>libksba</b> 1.3.3-1 (libraries)<br/>
    A CMS and X.509 access library<br/>
<br/>msys/<b>libksba-devel</b> 1.3.3-1 (development)<br/>
    Libassuan headers and libraries<br/>
<br/>msys/<b>libltdl</b> 2.4.6-2 <br/>
    A system independent dlopen wrapper for GNU libtool<br/>
<br/>msys/<b>liblzma</b> 5.2.3-1 (libraries) <br/>
    Library for XZ and LZMA compressed files<br/>
<br/>msys/<b>liblzma-devel</b> 5.2.3-1 (development) <br/>
    Liblzma headers and libraries<br/>
<br/>msys/<b>liblzo2</b> 2.09-1 (libraries compression) <br/>
    Portable lossless data compression library<br/>
<br/>msys/<b>liblzo2-devel</b> 2.09-1 (development) <br/>
    Liblzo2 headers and libraries<br/>
<br/>msys/<b>libmetalink</b> 0.1.2-2 (libraries) <br/>
    Metalink XML parser library.<br/>
<br/>msys/<b>libmetalink-devel</b> 0.1.2-2 (development) <br/>
    libmetalink headers and libraries<br/>
<br/>msys/<b>libneon</b> 0.30.0-1 (libraries)<br/>
    HTTP and WebDAV client library with a C interface<br/>
<br/>msys/<b>libneon-devel</b> 0.30.0-1 (development)<br/>
    Libneon headers and libraries<br/>
<br/>msys/<b>libnettle</b> 3.3-1 (libraries) <br/>
    A low-level cryptographic library<br/>
<br/>msys/<b>libnettle-devel</b> 3.3-1 (development) <br/>
    Libnettle headers and libraries<br/>
<br/>msys/<b>libnpth</b> 1.2-1 (libraries)<br/>
    New portable threads library<br/>
<br/>msys/<b>libnpth-devel</b> 1.2-1 (development)<br/>
    Libnpth headers and libraries<br/>
<br/>msys/<b>libopenssl</b> 1.0.2.k-1 (libraries) <br/>
    The Open Source toolkit for Secure Sockets Layer and Transport Layer Security<br/>
<br/>msys/<b>libp11-kit</b> 0.23.2-1 (libraries) <br/>
    Library to work with PKCS#11 modules<br/>
<br/>msys/<b>libp11-kit-devel</b> 0.23.2-1 (development)<br/>
    Libp11-kit headers and libraries<br/>
<br/>msys/<b>libpcre</b> 8.40-2 (libraries) <br/>
    A library that implements Perl 5-style regular expressions<br/>
<br/>msys/<b>libpcre16</b> 8.40-2 (libraries) <br/>
    A library that implements Perl 5-style regular expressions<br/>
<br/>msys/<b>libpcre32</b> 8.40-2 (libraries) <br/>
    A library that implements Perl 5-style regular expressions<br/>
<br/>msys/<b>libpcrecpp</b> 8.40-2 (libraries) <br/>
    A library that implements Perl 5-style regular expressions<br/>
<br/>msys/<b>libpcreposix</b> 8.40-2 (libraries) <br/>
    A library that implements Perl 5-style regular expressions<br/>
<br/>msys/<b>libpipeline</b> 1.4.0-1 (libraries) <br/>
    a C library for manipulating pipelines of subprocesses in a flexible and convenient way<br/>
<br/>msys/<b>libpipeline-devel</b> 1.4.0-1 (development)<br/>
    libpipeline headers and libraries<br/>
<br/>msys/<b>libreadline</b> 7.0.003-1 (libraries) <br/>
    GNU readline library<br/>
<br/>msys/<b>libreadline-devel</b> 7.0.003-1 (development) <br/>
    readline headers and libraries<br/>
<br/>msys/<b>libsasl</b> 2.1.26-8 (libraries) <br/>
    Cyrus Simple Authentication Service Layer (SASL) Library<br/>
<br/>msys/<b>libsasl-devel</b> 2.1.26-8 (development)<br/>
    Libsasl headers and libraries<br/>
<br/>msys/<b>libserf</b> 1.3.8-3 (libraries) <br/>
    High-performance asynchronous HTTP client library<br/>
<br/>msys/<b>libserf-devel</b> 1.3.8-3 (development)<br/>
    Libserf headers and libraries<br/>
<br/>msys/<b>libsqlite</b> 3.10.0.0-1 (libraries) <br/>
    Sqlite3 library<br/>
<br/>msys/<b>libsqlite-devel</b> 3.10.0.0-1 (development) <br/>
    Sqlite3 headers and libraries<br/>
<br/>msys/<b>libssh2</b> 1.7.0-1 (libraries) <br/>
    Multi-protocol file transfer library (runtime)<br/>
<br/>msys/<b>libssh2-devel</b> 1.7.0-1 (development) <br/>
    Libssh2 headers and libraries<br/>
<br/>msys/<b>libtasn1</b> 4.9-1 (libraries) <br/>
    A library for Abstract Syntax Notation One (ASN.1) and Distinguish Encoding Rules (DER) manipulation.<br/>
<br/>msys/<b>libtasn1-devel</b> 4.9-1 (development)<br/>
    Libtasn1 headers and libraries<br/>
<br/>msys/<b>libtirpc</b> 0.2.5-1 (libraries)<br/>
    A port of Sun's Transport-Independent RPC library<br/>
<br/>msys/<b>libtirpc-devel</b> 0.2.5-1 (development)<br/>
    Libtirpc headers and libraries<br/>
<br/>msys/<b>libtool</b> 2.4.6-2 (base-devel) <br/>
    A generic library support script<br/>
<br/>msys/<b>libtre-devel-git</b> 0.8.0.122.c2f5d13-1 (development)<br/>
    Libtre headers and libraries (development)<br/>
<br/>msys/<b>libtre-git</b> 0.8.0.122.c2f5d13-1 (libraries)<br/>
    The free and portable approximate regex matching library (libraries)<br/>
<br/>msys/<b>libunistring</b> 0.9.6-1 (libraries) <br/>
    Library for manipulating Unicode strings and C strings.<br/>
<br/>msys/<b>libunistring-devel</b> 0.9.6-1 (development)<br/>
    libunistring headers and libraries<br/>
<br/>msys/<b>libunrar</b> 5.3.7-1 (base-devel) <br/>
    Library and header file for applications that use libunrar<br/>
<br/>msys/<b>libutil-linux</b> 2.26.2-1 <br/>
    Block device ID and Universally Unique ID libraries<br/>
<br/>msys/<b>libutil-linux-devel</b> 2.26.2-1<br/>
    Block device ID and Universally Unique ID headers and libraries.<br/>
<br/>msys/<b>libxml2</b> 2.9.2-3 (libraries) <br/>
    XML parsing library, version 2<br/>
<br/>msys/<b>libxml2-devel</b> 2.9.2-3 (development) <br/>
    Libxml2 headers and libraries<br/>
<br/>msys/<b>libxml2-python</b> 2.9.2-3 (python-modules) <br/>
    Libxml2 python modules<br/>
<br/>msys/<b>libxslt</b> 1.1.28-7 (libraries) <br/>
    XML stylesheet transformation library<br/>
<br/>msys/<b>libxslt-devel</b> 1.1.28-7 (development)<br/>
    Libxslt headers and libraries<br/>
<br/>msys/<b>libxslt-python</b> 1.1.28-7 (python-modules) <br/>
    Libxslt python modules<br/>
<br/>msys/<b>libyaml</b> 0.1.4-1 (libraries)<br/>
    YAML 1.1 library<br/>
<br/>msys/<b>libyaml-devel</b> 0.1.4-1 (development)<br/>
    YAML 1.1 library<br/>
<br/>msys/<b>lld-svn</b> 4595.3511ec1-1<br/>
    Linker tools for LLVM (mingw-w64)<br/>
<br/>msys/<b>llvm-svn</b> 124592.2aebced-1<br/>
    Low Level Virtual Machine (mingw-w64)<br/>
<br/>msys/<b>lndir</b> 1.0.3-1 (base) <br/>
    Create a shadow directory of symbolic links to another directory tree<br/>
<br/>msys/<b>lzip</b> 1.16-1<br/>
    A lossless file compressor based on the LZMA algorithm<br/>
<br/>msys/<b>m4</b> 1.4.18-1 (base-devel) <br/>
    The GNU macro processor<br/>
<br/>msys/<b>make</b> 4.2.1-1 (base-devel) <br/>
    GNU make utility to maintain groups of programs<br/>
<br/>msys/<b>make-git</b> 4.1.8.g292da6f-1<br/>
    GNU make utility to maintain groups of programs<br/>
<br/>msys/<b>man-db</b> 2.7.4-1 (base-devel) <br/>
    A utility for reading man pages<br/>
<br/>msys/<b>man-pages-posix</b> 2013_a-1<br/>
    POSIX Manual Pages<br/>
<br/>msys/<b>markdown</b> 1.0.1-1<br/>
    A text-to-HTML conversion tool<br/>
<br/>msys/<b>mc</b> 4.8.18-1 <br/>
    Midnight Commander is a text based filemanager/shell that emulates Norton Commander<br/>
<br/>msys/<b>mercurial</b> 4.0.2-1 (VCS) <br/>
    A scalable distributed SCM tool<br/>
<br/>msys/<b>mingw-w64-cross-binutils</b> 2.25.1-1 (mingw-w64-cross-toolchain mingw-w64-cross) <br/>
    A set of programs to assemble and manipulate binary and object files<br/>
<br/>msys/<b>mingw-w64-cross-crt-clang-git</b> 5.0.0.4631.3deeda3-1<br/>
    MinGW-w64 CRT for cross-compiler<br/>
<br/>msys/<b>mingw-w64-cross-crt-git</b> 5.0.0.4766.db8f08d-1 (mingw-w64-cross-toolchain mingw-w64-cross) <br/>
    MinGW-w64 CRT for cross-compiler<br/>
<br/>msys/<b>mingw-w64-cross-gcc</b> 6.3.0-1 (mingw-w64-cross-toolchain mingw-w64-cross) <br/>
    Cross GCC for the MinGW-w64<br/>
<br/>msys/<b>mingw-w64-cross-headers-git</b> 5.0.0.4766.db8f08d-1 (mingw-w64-cross-toolchain mingw-w64-cross) <br/>
    MinGW-w64 headers for cross-compiler<br/>
<br/>msys/<b>mingw-w64-cross-tools-git</b> 5.0.0.4766.db8f08d-1 (mingw-w64-cross-toolchain mingw-w64-cross)<br/>
    MinGW-w64 headers for cross-compiler<br/>
<br/>msys/<b>mingw-w64-cross-windows-default-manifest</b> 6.4-2 (mingw-w64-cross-toolchain mingw-w64-cross) <br/>
    Default Windows application manifest<br/>
<br/>msys/<b>mingw-w64-cross-winpthreads-git</b> 5.0.0.4767.34ac6b9-1 (mingw-w64-cross-toolchain mingw-w64-cross) <br/>
    MinGW-w64 winpthreads library for cross-compiler<br/>
<br/>msys/<b>mingw-w64-cross-winstorecompat-git</b> 5.0.0.4766.db8f08d-1 (mingw-w64-cross-toolchain mingw-w64-cross)<br/>
    MinGW-w64 winRT compat library<br/>
<br/>msys/<b>mingw-w64-cross-zlib</b> 1.2.11-1 (mingw-w64-cross-toolchain mingw-w64-cross) <br/>
    Compression library implementing the deflate compression method found in gzip and PKZIP<br/>
<br/>msys/<b>mintty</b> 1~2.7.3-1 (base) <br/>
    Terminal emulator with native Windows look and feel<br/>
<br/>msys/<b>mksh</b> 51-1<br/>
    The MirBSD Korn Shell<br/>
<br/>msys/<b>mosh</b> 1.2.5-1 (net-utils)<br/>
    Mobile shell, surviving disconnects with local echo and line editing<br/>
<br/>msys/<b>mpc</b> 1.0.3-1 (libraries) <br/>
    Multiple precision complex arithmetic library<br/>
<br/>msys/<b>mpc-devel</b> 1.0.3-1 (development) <br/>
    MPC headers and libraries<br/>
<br/>msys/<b>mpfr</b> 3.1.5.1-3 (libraries) <br/>
    Multiple-precision floating-point library<br/>
<br/>msys/<b>mpfr-devel</b> 3.1.5.1-3 (development) <br/>
    MPFR headers and libraries<br/>
<br/>msys/<b>msys2-keyring</b> r9.397a52e-1 (base) <br/>
    MSYS2 PGP keyring<br/>
<br/>msys/<b>msys2-launcher-git</b> 0.3.32.56c2ba7-2 (base) <br/>
    Helper for launching MSYS2 shells<br/>
<br/>msys/<b>msys2-runtime</b> 2.7.0-1 (base) <br/>
    Posix emulation engine for Windows<br/>
<br/>msys/<b>msys2-runtime-devel</b> 2.7.0-1 (MSYS2-devel) <br/>
    MSYS2 headers and libraries<br/>
<br/>msys/<b>msys2-w32api-headers</b> 5.0.0.4766.db8f08d-1 (msys2-devel) <br/>
    Win32 API headers for MSYS2 32bit toolchain<br/>
<br/>msys/<b>msys2-w32api-runtime</b> 5.0.0.4766.db8f08d-1 (msys2-devel) <br/>
    Win32 API import libs for MSYS2 toolchain<br/>
<br/>msys/<b>mutt</b> 1.6.0-1<br/>
    Small but very powerful text-based mail client<br/>
<br/>msys/<b>nano</b> 2.7.5-1 (editors)<br/>
    Pico editor clone with enhancements<br/>
<br/>msys/<b>nano-syntax-highlighting-git</b> 285.9befa91-1<br/>
    Nano editor syntax highlighting enhancements<br/>
<br/>msys/<b>nasm</b> 2.12-1<br/>
    An 80x86 assembler designed for portability and modularity<br/>
<br/>msys/<b>ncurses</b> 6.0.20170121-1 (base) <br/>
    System V Release 4.0 curses emulation library<br/>
<br/>msys/<b>ncurses-devel</b> 6.0.20170121-1 (development) <br/>
    NCURSES headers and libraries<br/>
<br/>msys/<b>nettle</b> 3.3-1 (net-utils)<br/>
    A low-level cryptographic library<br/>
<br/>msys/<b>openssh</b> 7.3p1-2 (net-utils) <br/>
    Free version of the SSH connectivity tools<br/>
<br/>msys/<b>openssl</b> 1.0.2.k-1 <br/>
    The Open Source toolkit for Secure Sockets Layer and Transport Layer Security<br/>
<br/>msys/<b>openssl-devel</b> 1.0.2.k-1 (development) <br/>
    Openssl headers and libraries<br/>
<br/>msys/<b>p11-kit</b> 0.23.2-1 <br/>
    Library to work with PKCS#11 modules<br/>
<br/>msys/<b>p7zip</b> 9.38.1-1 (compression) <br/>
    Command-line version of the 7zip compressed file archiver<br/>
<br/>msys/<b>pacman</b> 5.0.1-2 (base base-devel) <br/>
    A library-based package manager with dependency support (MSYS2 port)<br/>
<br/>msys/<b>pacman-mirrors</b> 20160112-1 (base) <br/>
    MSYS2 mirror list for use by pacman<br/>
<br/>msys/<b>pactoys-git</b> r2.07ca37f-1 (base base-devel) <br/>
    A set of pacman packaging utilities<br/>
<br/>msys/<b>pass</b> 1.6.5-2<br/>
    Stores, retrieves, generates, and synchronizes passwords securely<br/>
<br/>msys/<b>patch</b> 2.7.5-1 (base-devel) <br/>
    A utility to apply patch files to original sources<br/>
<br/>msys/<b>patchutils</b> 0.3.4-1 (base-devel) <br/>
    Utilities to work with patches<br/>
<br/>msys/<b>pax-git</b> 20140703.2.1.g469552a-1 (base)<br/>
    POSIX standard archive tool<br/>
<br/>msys/<b>pcre</b> 8.40-2 <br/>
    A library that implements Perl 5-style regular expressions<br/>
<br/>msys/<b>pcre-devel</b> 8.40-2 (development) <br/>
    PCRE headers and libraries<br/>
<br/>msys/<b>perl</b> 5.24.1-2 (base-devel) <br/>
    A highly capable, feature-rich programming language<br/>
<br/>msys/<b>perl-Algorithm-Diff</b> 1.1903-1 (perl-modules)<br/>
    Compute 'intelligent' differences between two files / lists<br/>
<br/>msys/<b>perl-Archive-Zip</b> 1.46-1 (perl-modules)<br/>
    Provide a perl interface to ZIP archive files<br/>
<br/>msys/<b>perl-Authen-SASL</b> 2.16-2 (perl-modules) <br/>
    Perl/CPAN Module Authen::SASL : SASL authentication framework<br/>
<br/>msys/<b>perl-Benchmark-Timer</b> 0.7107-1 (perl-modules)<br/>
    Provide commonly requested regular expressions<br/>
<br/>msys/<b>perl-Capture-Tiny</b> 0.30-1 (perl-modules)<br/>
    Capture STDOUT and STDERR from Perl, XS or external programs<br/>
<br/>msys/<b>perl-Carp-Clan</b> 6.04-1 (perl-modules)<br/>
    Carp::Clan - Report errors from perspective of caller of a "clan" of modules<br/>
<br/>msys/<b>perl-Compress-Bzip2</b> 2.22-1 (perl-modules)<br/>
    Interface to Bzip2 compression library<br/>
<br/>msys/<b>perl-Convert-BinHex</b> 1.123-2 <br/>
    Perl module to extract data from Macintosh BinHex files<br/>
<br/>msys/<b>perl-Crypt-SSLeay</b> 0.73_04-2 (perl-modules)<br/>
    OpenSSL glue that provides LWP https support<br/>
<br/>msys/<b>perl-DBI</b> 1.634-1 (perl-modules)<br/>
    Database independent interface for Perl<br/>
<br/>msys/<b>perl-Date-Calc</b> 6.4-1 (perl-modules)<br/>
    Date::Calc - Gregorian calendar date calculations<br/>
<br/>msys/<b>perl-Digest-HMAC</b> 1.03-2 (perl-modules)<br/>
    Perl Module: Keyed-Hashing for Message Authentication.<br/>
<br/>msys/<b>perl-Digest-MD4</b> 1.9-1 (perl-modules)<br/>
    Perl Module: Perl interface to the MD4 Algorithm.<br/>
<br/>msys/<b>perl-Encode-Locale</b> 1.04-1 (perl-modules) <br/>
    Determine the locale encoding<br/>
<br/>msys/<b>perl-Encode-compat</b> 0.07-1 (perl-modules)<br/>
    Encode::compat - Encode.pm emulation layer<br/>
<br/>msys/<b>perl-Error</b> 0.17024-1 (perl-modules) <br/>
    Perl/CPAN Error module - Error/exception handling in an OO-ish way<br/>
<br/>msys/<b>perl-Exporter-Lite</b> 0.06-1 (perl-modules)<br/>
    lightweight exporting of functions and variables<br/>
<br/>msys/<b>perl-Exporter-Tiny</b> 0.042-1 (perl-modules)<br/>
    List::MoreUtils provides some trivial but commonly needed functionality on lists which is not going to go into List::Util<br/>
<br/>msys/<b>perl-ExtUtils-Depends</b> 0.404-1 (perl-modules)<br/>
    The Perl depends module<br/>
<br/>msys/<b>perl-ExtUtils-PkgConfig</b> 1.15-2 (perl-modules)<br/>
    The Perl Pkgconfig module<br/>
<br/>msys/<b>perl-File-Copy-Recursive</b> 0.38-2 (perl-modules)<br/>
    extension for recursively copying files and directories<br/>
<br/>msys/<b>perl-File-Listing</b> 6.04-2 (perl-modules) <br/>
    parse directory listing<br/>
<br/>msys/<b>perl-File-Next</b> 1.12-2 (perl-modules)<br/>
    File-finding iterator<br/>
<br/>msys/<b>perl-File-Which</b> 1.18-1 (perl-modules)<br/>
    Portable implementation of which<br/>
<br/>msys/<b>perl-Getopt-Tabular</b> 0.3-1 (perl-modules)<br/>
    table-driven argument parsing for Perl 5<br/>
<br/>msys/<b>perl-HTML-Parser</b> 3.72-1 (perl-modules) <br/>
    Perl HTML parser class<br/>
<br/>msys/<b>perl-HTML-Tagset</b> 3.20-2 (perl-modules) <br/>
    Data tables useful in parsing HTML<br/>
<br/>msys/<b>perl-HTTP-Cookies</b> 6.01-2 (perl-modules) <br/>
    HTTP cookie jars<br/>
<br/>msys/<b>perl-HTTP-Daemon</b> 6.01-2 (perl-modules) <br/>
    A simple http server class<br/>
<br/>msys/<b>perl-HTTP-Date</b> 6.02-2 (perl-modules) <br/>
    Date conversion routines<br/>
<br/>msys/<b>perl-HTTP-Message</b> 6.06-2 (perl-modules) <br/>
    HTTP style messages<br/>
<br/>msys/<b>perl-HTTP-Negotiate</b> 6.01-2 (perl-modules) <br/>
    choose a variant to serve<br/>
<br/>msys/<b>perl-IO-HTML</b> 1.001-1 (perl-modules)<br/>
    Open an HTML file with automatic charset detection<br/>
<br/>msys/<b>perl-IO-Socket-INET6</b> 2.72-4 (perl-modules)<br/>
    Object interface for AF_INET|AF_INET6 domain sockets<br/>
<br/>msys/<b>perl-IO-Socket-SSL</b> 2.016-1 (perl-modules) <br/>
    Nearly transparent SSL encapsulation for IO::Socket::INET<br/>
<br/>msys/<b>perl-IO-stringy</b> 2.111-1 (perl-modules) <br/>
    I/O on in-core objects like strings/arrays<br/>
<br/>msys/<b>perl-IPC-Run3</b> 0.048-1 (perl-modules)<br/>
    run a subprocess with input/ouput redirection<br/>
<br/>msys/<b>perl-LWP-MediaTypes</b> 6.02-2 (perl-modules) <br/>
    Guess the media type of a file or a URL<br/>
<br/>msys/<b>perl-LWP-Protocol-https</b> 6.06-1 (perl-modules)<br/>
    Provide https support for LWP::UserAgent<br/>
<br/>msys/<b>perl-Locale-Gettext</b> 1.07-1 (perl-modules) <br/>
    Permits access from Perl to the gettext() family of functions<br/>
<br/>msys/<b>perl-MIME-Charset</b> 1.012-1 (perl-modules)<br/>
    MIME::Charset - Charset Information for MIME<br/>
<br/>msys/<b>perl-MIME-tools</b> 5.506-1 <br/>
    Parses streams to create MIME entities<br/>
<br/>msys/<b>perl-MailTools</b> 2.14-1 <br/>
    Various e-mail related modules<br/>
<br/>msys/<b>perl-Module-Build</b> 0.4212-1 <br/>
    Build, test, and install Perl modules<br/>
<br/>msys/<b>perl-Mozilla-CA</b> 20141217-1 (perl-modules)<br/>
    Mozilla's CA cert bundle in PEM format<br/>
<br/>msys/<b>perl-Net-DNS</b> 1.05-1 (perl-modules)<br/>
    Perl Module: Interface to the DNS resolver.<br/>
<br/>msys/<b>perl-Net-HTTP</b> 6.09-1 (perl-modules) <br/>
    Low-level HTTP connection (client)<br/>
<br/>msys/<b>perl-Net-IP</b> 1.26-2 (perl-modules)<br/>
    Perl Module: Easy manipulation of IPv4 and IPv6 addresses<br/>
<br/>msys/<b>perl-Net-SMTP-SSL</b> 1.02-1 (perl-modules) <br/>
    SSL support for Net::SMTP<br/>
<br/>msys/<b>perl-Net-SSLeay</b> 1.80-1 (perl-modules) <br/>
    Perl extension for using OpenSSL<br/>
<br/>msys/<b>perl-Path-Class</b> 0.35-1 (perl-modules)<br/>
    Cross-platform path specification manipulation for Perl<br/>
<br/>msys/<b>perl-Probe-Perl</b> 0.03-2 (perl-modules)<br/>
    Information about the currently running perl<br/>
<br/>msys/<b>perl-Regexp-Common</b> 2016010801-1 (perl-modules)<br/>
    Provide commonly requested regular expressions<br/>
<br/>msys/<b>perl-Socket6</b> 0.25-2<br/>
    A getaddrinfo/getnameinfo support module<br/>
<br/>msys/<b>perl-Sys-CPU</b> 0.61-3 (perl-modules)<br/>
    Provide commonly requested regular expressions<br/>
<br/>msys/<b>perl-TAP-Harness-Archive</b> 0.17-1 (perl-modules)<br/>
    Create an archive of TAP test results<br/>
<br/>msys/<b>perl-TermReadKey</b> 2.37-1 (perl-modules) <br/>
    Provides simple control over terminal driver modes<br/>
<br/>msys/<b>perl-Test-Harness</b> 3.36-1 (perl-modules)<br/>
    Test::Harness - Run Perl standard test scripts with statistics<br/>
<br/>msys/<b>perl-Test-Pod</b> 1.50-1 (perl-modules) <br/>
    Check for POD errors in files<br/>
<br/>msys/<b>perl-Test-Script</b> 1.10-1 (perl-modules)<br/>
    Basic cross-platform tests for scripts<br/>
<br/>msys/<b>perl-Text-CharWidth</b> 0.04-1 (perl-modules)<br/>
    Text::CharWidth - Get number of occupied columns of a string on terminal<br/>
<br/>msys/<b>perl-Text-WrapI18N</b> 0.06-1 (perl-modules)<br/>
    Text::WrapI18N - Line wrapping module with support for multibyte, fullwidth, and combining characters and languages without whitespaces between words<br/>
<br/>msys/<b>perl-TimeDate</b> 2.30-2 <br/>
    Date formating subroutines<br/>
<br/>msys/<b>perl-Try-Tiny</b> 0.22-2 (perl-modules)<br/>
    Minimal try/catch with proper localization of $@<br/>
<br/>msys/<b>perl-URI</b> 1.68-1 (perl-modules) <br/>
    Uniform Resource Identifiers (absolute and relative)<br/>
<br/>msys/<b>perl-Unicode-GCString</b> 2016.003-2 (perl-modules)<br/>
    Unicode::GCString - String as Sequence of UAX #29 Grapheme Clusters<br/>
<br/>msys/<b>perl-WWW-RobotRules</b> 6.02-2 (perl-modules) <br/>
    Database of robots.txt-derived permissions<br/>
<br/>msys/<b>perl-XML-LibXML</b> 2.0121-1 (perl-modules)<br/>
    Expat-based XML parser module for perl<br/>
<br/>msys/<b>perl-XML-NamespaceSupport</b> 1.11-2 (perl-modules)<br/>
    Generic namespace helpers (ported from SAX2)<br/>
<br/>msys/<b>perl-XML-Parser</b> 2.44-2 (perl-modules) <br/>
    Expat-based XML parser module for perl<br/>
<br/>msys/<b>perl-XML-SAX</b> 0.99-2 (perl-modules)<br/>
    Simple API for XML<br/>
<br/>msys/<b>perl-XML-SAX-Base</b> 1.08-2 (perl-modules)<br/>
    Base class SAX Drivers and Filters<br/>
<br/>msys/<b>perl-XML-Simple</b> 2.20-2 (perl-modules)<br/>
    Simple XML parser for perl<br/>
<br/>msys/<b>perl-YAML</b> 1.15-1 (perl-modules)<br/>
    Perl/CPAN Module YAML : YAML Aint Markup Language<br/>
<br/>msys/<b>perl-YAML-Syck</b> 1.29-2 (perl-modules) <br/>
    Fast, lightweight YAML loader and dumper<br/>
<br/>msys/<b>perl-YAML-Tiny</b> 1.67-1 (perl-modules)<br/>
    Read/Write YAML files with as little code as possible<br/>
<br/>msys/<b>perl-ack</b> 2.14-1 (perl-modules)<br/>
    A Perl-based grep replacement, aimed at programmers with large trees of heterogeneous source code<br/>
<br/>msys/<b>perl-common-sense</b> 3.73-1 (perl-modules)<br/>
    Implements some sane defaults for Perl programs<br/>
<br/>msys/<b>perl-libwww</b> 6.13-1 (perl-modules) <br/>
    The World-Wide Web library for Perl<br/>
<br/>msys/<b>perl-sgmls</b> 1.03ii-1<br/>
    A Post-Processor for SGMLS and NSGMLS<br/>
<br/>msys/<b>pinentry</b> 0.9.7-1<br/>
    A collection of simple PIN or passphrase entry dialogs which utilize the Assuan protocol<br/>
<br/>msys/<b>pkg-config</b> 0.29.1-1 (base-devel) <br/>
    A system for managing library compile/link flags<br/>
<br/>msys/<b>pkgfile</b> 15-1 (base base-devel) <br/>
    A pacman .files metadata explorer<br/>
<br/>msys/<b>po4a</b> 0.48-2<br/>
    The po4a (PO for anything) project goal is to ease translations (and more interestingly, the maintenance of translations) using gettext tools on areas where they were not expected like documentation<br/>
<br/>msys/<b>procps</b> 3.2.8-2 (sys-utils)<br/>
    System and process monitoring utilities<br/>
<br/>msys/<b>procps-ng</b> 3.3.12-1 (sys-utils)<br/>
    Utilities for monitoring your system and its processes<br/>
<br/>msys/<b>protobuf</b> 2.6.1-1 (libraries)<br/>
    Protocol Buffers - Google's data interchange format<br/>
<br/>msys/<b>protobuf-devel</b> 2.6.1-1 (development)<br/>
    Protobuf headers and libraries<br/>
<br/>msys/<b>psmisc</b> 22.21-1 (sys-utils)<br/>
    Miscellaneous procfs tools<br/>
<br/>msys/<b>pv</b> 1.6.0-2<br/>
    Pipe viewer<br/>
<br/>msys/<b>pwgen</b> 2.07-1<br/>
    Password generator for creating easily memorable passwords<br/>
<br/>msys/<b>python</b> 3.4.5-1 <br/>
    Next generation of the python high-level scripting language<br/>
<br/>msys/<b>python2</b> 2.7.13-1 <br/>
    A high-level scripting language<br/>
<br/>msys/<b>python2-beaker</b> 1.7.0-1<br/>
    Caching and sessions WSGI middleware for use with web applications and stand-alone Python scripts and applications<br/>
<br/>msys/<b>python2-colorama</b> 0.3.7-1<br/>
    Python API for cross-platform colored terminal text.<br/>
<br/>msys/<b>python2-distutils-extra</b> 2.38-2<br/>
    Enhancements to the Python build system<br/>
<br/>msys/<b>python2-fastimport</b> 0.9.4-1<br/>
    VCS fastimport/fastexport parser<br/>
<br/>msys/<b>python2-mako</b> 1.0.4-1<br/>
    A super-fast templating language that borrows the best ideas from the existing templating languages<br/>
<br/>msys/<b>python2-markupsafe</b> 0.23-2<br/>
    Implements a XML/HTML/XHTML Markup safe string for Python<br/>
<br/>msys/<b>python2-mock</b> 1.0.1-1<br/>
    Mocking and Patching Library for Testing<br/>
<br/>msys/<b>python2-nose</b> 1.3.7-1<br/>
    A discovery-based unittest extension<br/>
<br/>msys/<b>python2-py</b> 1.4.31-1<br/>
    library with cross-python path, ini-parsing, io, code, log facilities<br/>
<br/>msys/<b>python2-pyalpm</b> 0.8-3<br/>
    Libalpm bindings for Python<br/>
<br/>msys/<b>python2-pygments</b> 2.1.3-1<br/>
    A syntax highlighting engine written in Python<br/>
<br/>msys/<b>python2-setuptools</b> 20.2.2-1 <br/>
    Easily download, build, install, upgrade, and uninstall Python packages<br/>
<br/>msys/<b>python3-beaker</b> 1.7.0-1<br/>
    Caching and sessions WSGI middleware for use with web applications and stand-alone Python scripts and applications<br/>
<br/>msys/<b>python3-colorama</b> 0.3.7-1<br/>
    Python API for cross-platform colored terminal text.<br/>
<br/>msys/<b>python3-distutils-extra</b> 2.38-2<br/>
    Enhancements to the Python build system<br/>
<br/>msys/<b>python3-fastimport</b> 0.9.4-1<br/>
    VCS fastimport/fastexport parser<br/>
<br/>msys/<b>python3-mako</b> 1.0.4-1<br/>
    A super-fast templating language that borrows the best ideas from the existing templating languages<br/>
<br/>msys/<b>python3-markupsafe</b> 0.23-2<br/>
    Implements a XML/HTML/XHTML Markup safe string for Python<br/>
<br/>msys/<b>python3-mock</b> 1.0.1-1<br/>
    Mocking and Patching Library for Testing<br/>
<br/>msys/<b>python3-nose</b> 1.3.7-1<br/>
    A discovery-based unittest extension<br/>
<br/>msys/<b>python3-py</b> 1.4.31-1<br/>
    library with cross-python path, ini-parsing, io, code, log facilities<br/>
<br/>msys/<b>python3-pyalpm</b> 0.8-3<br/>
    Libalpm bindings for Python<br/>
<br/>msys/<b>python3-pygments</b> 2.1.3-1<br/>
    A syntax highlighting engine written in Python<br/>
<br/>msys/<b>python3-setuptools</b> 20.2.2-1<br/>
    Easily download, build, install, upgrade, and uninstall Python packages<br/>
<br/>msys/<b>quilt</b> 0.65-1 (base-devel)<br/>
    Manage large numbers of patches<br/>
<br/>msys/<b>rarian</b> 0.8.1-1 <br/>
    Documentation meta-data library, designed as a replacement for Scrollkeeper.<br/>
<br/>msys/<b>rcs</b> 5.9.4-1 (base-devel) <br/>
    Revision Control System: manages multiple revisions of files<br/>
<br/>msys/<b>re2c</b> 0.16-1<br/>
    A tool for generating C-based recognizers from regular expressions<br/>
<br/>msys/<b>rebase</b> 4.4.2-1 (base) <br/>
    The Cygwin rebase distribution contains four utilities, rebase, rebaseall, peflags, and peflagsall.<br/>
<br/>msys/<b>remake-git</b> 4.1.2943.f059924-1<br/>
    Enhanced GNU Make - tracing, error reporting, debugging, profiling and more<br/>
<br/>msys/<b>rsync</b> 3.1.2-2 (net-utils) <br/>
    A file transfer program to keep remote files in sync<br/>
<br/>msys/<b>ruby</b> 2.3.3-1<br/>
    An object-oriented language for quick and easy programming<br/>
<br/>msys/<b>ruby-docs</b> 2.3.3-1<br/>
    Documentation files for ruby<br/>
<br/>msys/<b>scons</b> 2.5.0-1 (base-devel) <br/>
    Extensible Python-based build utility<br/>
<br/>msys/<b>screenfetch</b> 3.7.0-1<br/>
    Bash screenshot information tool<br/>
<br/>msys/<b>sed</b> 4.4-2 (base base-devel) <br/>
    GNU stream editor<br/>
<br/>msys/<b>setconf</b> 0.7.2-1<br/>
    Utility to easily change settings in configuration files<br/>
<br/>msys/<b>sgml-common</b> 0.6.3-1<br/>
    Tools for maintaining centralized SGML catalogs.<br/>
<br/>msys/<b>sharutils</b> 4.15-1<br/>
    Makes so-called shell archives out of many files<br/>
<br/>msys/<b>socat</b> 1.7.3.2-1<br/>
    Multipurpose relay<br/>
<br/>msys/<b>sqlite</b> 3.10.0.0-1<br/>
    A C library that implements an SQL database engine<br/>
<br/>msys/<b>sqlite-doc</b> 3.10.0.0-1<br/>
    Most of the static HTML files that comprise this website, including all of the SQL Syntax and the C/C++ interface specs and other miscellaneous documentation<br/>
<br/>msys/<b>ssh-pageant-git</b> 1.4.4.gf09e76e-1 <br/>
    An SSH authentication agent for Cygwin/MSYS to PuTTY's Pageant<br/>
<br/>msys/<b>sshpass</b> 1.05-1<br/>
    Full ssh into accepting an interactive password non-interactively<br/>
<br/>msys/<b>subversion</b> 1.9.5-1 (VCS) <br/>
    A Modern Concurrent Version Control System<br/>
<br/>msys/<b>swig</b> 3.0.10-1 (base-devel) <br/>
    Generate scripting interfaces to C/C++ code<br/>
<br/>msys/<b>tar</b> 1.29-1 (compression) <br/>
    Utility used to store, backup, and transport files<br/>
<br/>msys/<b>task</b> 2.5.1-1<br/>
    A command-line todo list manager<br/>
<br/>msys/<b>tcl</b> 8.5.18-1 <br/>
    The Tcl scripting language<br/>
<br/>msys/<b>tcsh</b> 6.19.00-1<br/>
    C shell with file name completion and command line editing<br/>
<br/>msys/<b>termbox</b> 1.1.0-1<br/>
    Library for writing text-based user interfaces<br/>
<br/>msys/<b>texinfo</b> 6.3-1 (base-devel) <br/>
    Utilities to work with and produce manuals, ASCII text, and on-line documentation from a single source file<br/>
<br/>msys/<b>texinfo-tex</b> 6.3-1 (base-devel) <br/>
    Utilities to work with and produce manuals, ASCII text, and on-line documentation from a single source file<br/>
<br/>msys/<b>tftp-hpa</b> 5.2-1 (base) <br/>
    Official tftp server<br/>
<br/>msys/<b>tig</b> 2.2-1<br/>
    Text-mode interface for Git<br/>
<br/>msys/<b>time</b> 1.7-1 (base) <br/>
    Utility for monitoring a program's use of system resources<br/>
<br/>msys/<b>tmux-git</b> 2.1.263.g5083e93-1 <br/>
    A terminal multiplexer<br/>
<br/>msys/<b>tree</b> 1.7.0-1<br/>
    A directory listing program displaying a depth indented list of files<br/>
<br/>msys/<b>ttyrec</b> 1.0.8-1 (base base-devel) <br/>
    A tty recorder<br/>
<br/>msys/<b>txt2tags</b> 2.6-4<br/>
    A text formatting and conversion tool.<br/>
<br/>msys/<b>tzcode</b> 2015.e-1 (base) <br/>
    Sources for time zone and daylight saving time data<br/>
<br/>msys/<b>ucl</b> 1.03-1<br/>
    Portable lossless data compression library written in ANSI C<br/>
<br/>msys/<b>ucl-devel</b> 1.03-1 (development)<br/>
    ucl headers and libraries<br/>
<br/>msys/<b>unrar</b> 5.3.7-1 (base-devel) <br/>
    The RAR uncompression program<br/>
<br/>msys/<b>unzip</b> 6.0-2 (compression) <br/>
    Unpacks .zip archives such as those made by PKZIP<br/>
<br/>msys/<b>upx</b> 3.91-1<br/>
    Ultimate executable compressor.<br/>
<br/>msys/<b>util-linux</b> 2.26.2-1 (base) <br/>
    Collection of basic system utilities<br/>
<br/>msys/<b>util-macros</b> 1.19.0-1 (development)<br/>
    X.Org Autotools macros<br/>
<br/>msys/<b>vim</b> 8.0.0237-1 (editors) <br/>
    <br/>
<br/>msys/<b>vimpager</b> 2.02-1<br/>
    Use ViM as PAGER<br/>
<br/>msys/<b>vimpager-git</b> r279.bc5548d-1<br/>
    Use ViM as PAGER<br/>
<br/>msys/<b>w3m</b> 0.5.3-1<br/>
    w3m is a pager with WWW capability<br/>
<br/>msys/<b>wcd</b> 6.0.0-1 (sys-utils)<br/>
    Wherever Change Directory<br/>
<br/>msys/<b>wget</b> 1.19.1-1 (base-devel) <br/>
    A network utility to retrieve files from the Web<br/>
<br/>msys/<b>which</b> 2.21-2 (base) <br/>
    A utility to show the full path of commands<br/>
<br/>msys/<b>whois</b> 5.2.9-1<br/>
    The whois client by Marco d'Itri<br/>
<br/>msys/<b>windows-default-manifest</b> 6.4-1 <br/>
    Default Windows application manifest<br/>
<br/>msys/<b>winpty</b> 0.4.2-1 <br/>
    A Windows software package providing an interface similar to a Unix pty-master for communicating with Windows console programs<br/>
<br/>msys/<b>xdelta3</b> 3.0.11-1<br/>
    Diff utility which works with binary files<br/>
<br/>msys/<b>xmlto</b> 0.0.28-1 (base-devel) <br/>
    Convert xml to many other formats<br/>
<br/>msys/<b>xproto</b> 7.0.26-1 (development)<br/>
    X11 core wire protocol and auxiliary headers<br/>
<br/>msys/<b>xz</b> 5.2.3-1 (compression) <br/>
    Library and command line tools for XZ and LZMA compressed files<br/>
<br/>msys/<b>yasm</b> 1.3.0-2 <br/>
    A rewrite of NASM to allow for multiple syntax supported (NASM, TASM, GAS, etc.)<br/>
<br/>msys/<b>yasm-devel</b> 1.3.0-2<br/>
    A rewrite of NASM to allow for multiple syntax supported (NASM, TASM, GAS, etc.)<br/>
<br/>msys/<b>yelp-tools</b> 3.18.0-1 <br/>
    Tools for creating Yelp documentation<br/>
<br/>msys/<b>yelp-xsl</b> 3.20.0-1 <br/>
    Stylesheets for Yelp<br/>
<br/>msys/<b>zip</b> 3.0-1<br/>
    Creates PKZIP-compatible .zip files<br/>
<br/>msys/<b>zlib</b> 1.2.11-1 (libraries) <br/>
    Compression library implementing the deflate compression method found in gzip and PKZIP<br/>
<br/>msys/<b>zlib-devel</b> 1.2.11-1 (development) <br/>
    zlib headers and libraries<br/>
<br/>msys/<b>znc-git</b> r4470.9b31a07-1<br/>
    An IRC bouncer with modules & scripts support<br/>
<br/>msys/<b>zsh</b> 5.3.1-1<br/>
    A very advanced and programmable command interpreter (shell) for UNIX<br/>
<br/>msys/<b>zsh-doc</b> 5.3.1-1<br/>
    Info, HTML and PDF format of the ZSH documentation<br/>
