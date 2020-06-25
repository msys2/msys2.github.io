## MSYS2

**MSYS2** is an independent rewrite of MSYS, based on modern Cygwin and MinGW-w64 with the aim of better interoperability with native Windows software.

The name is a contraction of Minimal SYStem 2, and aims to provide support to facilitate using the bash shell, Autotools, revision control systems and the like for building native Windows applications using MinGW-w64 toolchains.

We wanted a package management system to provide easy installation of packages, and ported Pacman (known from Arch Linux). This brings many powerful features such as dependency resolution and simple complete system upgrades, as well as providing the build system which is used to make these packages.

## Cygwin

Cygwin is a POSIX platform atop of Windows (the Win32 subsystem), running in user-mode. It requires a POSIX compatibility layer at runtime. It doesn't emulate Linux, it's not the same thing as WSL.

It is our hope that MSYS2 be viewed as a complementary off-shot of Cygwin (even *hopefully* by the Cygwin developers!), and we still hold out hopes that MSYS2 can someday operate as a special mode for Cygwin (via a DLL plugin mechanism).

## MinGW-w64

MinGW is an abbreviation of *Minimalist GNU for Windows*. The idea of MinGW is to provide a development platform for building cross-platform applications on Windows. The important pieces are:

* a set of FOSS Windows specific header files and import libraries which enable the use of the Windows API,
* a supplementary library and a runtime that fill in some gaps.

... but the term generally encompasses the cross-platform GNU development tools:

* GNU Compiler Collection (GCC),
* GNU Binutils (assembler, linker, archive manager),
* GNU Debugger (GDB),
* and miscellaneous utilities.

There are at least two projects implementing this idea:

* the original MinGW project, sometimes referred to as mingw.org
* and the MinGW-w64 project.

The MinGW-w64 project itself doesn't aim to be a software distribution. There are multiple builds of mingw-w64 toolchains and multiple software distributions built using MinGW-w64.

## MSYS and MinGW

MinGW is a software distribution and development platform. It is accompanied by MSYS, an old Cygwin fork. The MSYS2 and MinGW-w64 projects are not associated with MSYS and MinGW, other than by the name and common goals.

MSYS2 is ideologically a successor to MSYS and MinGW. MSYS -- although definitely useful -- is really old and getting in the way of developers. MSYS2 was created to replace the original MSYS while avoiding its problems.
