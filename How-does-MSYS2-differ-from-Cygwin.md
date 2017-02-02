Goals
=====

Cygwin and MSYS2 -- as projects -- have significantly different goals.

Cygwin tries to bring a POSIX-compatible environment to Windows so that most software that runs on unices will build and run on Cygwin without any significant modifications. Cygwin provides a large collection of packages containing such software, and libraries for their development.

MSYS2 tries to provide an environment for building native Windows software. MSYS2 provides a large collection of packages containing such software, and libraries for their development. As a large portion of the software uses GNU build tools which are tightly coupled to the unix world, this environment is also POSIX-compatible, and is in fact based on Cygwin. 

MSYS2 provies a minimal shell required to run autotools and other build systems which get the source for software from the Internet from different repositories, configure them and build them. The shell and core tools exist mainly to allow porting Unix programs to run natively on Windows (i.e. without requiring a POSIX emulation layer). MSYS2 doesn't try to duplicate Cygwin's efforts more than necessary, so the number of provided POSIX-emulated software is very small.


History and future
==================

MSYS2 is ideologically a successor to MSYS, which is again a Cygwin fork that optionally accompanies the mingw.org compiler toolchain. MSYS -- although definitely useful -- is really old and getting in the way of developers. MSYS2 was created to replace the original MSYS while avoiding its problems.

It is our hope that MSYS2 be viewed as a complimentary off-shot of Cygwin (even *hopefully* by the Cygwin developers!), and we still hold out hopes that MSYS2 can someday operate as a special mode for Cygwin (via a DLL plugin mechanism).


Packages
========

MSYS2 uses Pacman (of Arch Linux) to manage its packages and comes with three different package repositories:
- `msys2`: Containing MSYS2-dependent software
- `mingw64`: Containing 64-bit native Windows software (compiled with mingw-w64 x86_64 toolchain)
- `mingw32`: Containing 32-bit native Windows software (compiled with mingw-w64 i686 toolchain)

Cygwin comes only with Cygwin-dependent software. It uses its own package management system, commonly called setup.exe.


Runtime
=======

Cygwin provides a runtime library called `cygwin1.dll` that provides the POSIX compatibility layer where necessary. The MSYS2 variant of this library is called `msys-2.0.dll` and includes the following changes to support using native Windows programs:

1. Automatic path mangling of command line arguments and environment variables to Windows form on the fly.
2. Ability to change `OSNAME` with an environment variable (`MSYSTEM`) which changes between `MSYS2` and `MINGW32` or `MINGW64` according to the nature of the software people are trying to build.
3. Conversion of output of native Windown applications from Windows line endings to POSIX line endings by removing trailing `'\r'` characters, so that e.g. `bb=$(gcc --print-search-dirs)` works as expected.
4. Replacement of symlinks with copying, so that Windown programs don't trip up on these files. MSYS2 also supports creating native NTFS symlinks, but these only work if the user has been granted the appropriate Windows permissions and are subject to other limitations.
5. Addition of the "-W" option to the `pwd` command in bash for compatibility with the old MSYS.
6. Removal of the `/cygdrive` prefix for automounts. Again this is to retain compatibility with MSYS-enabled software that makes assumptions about `/c/` being equivalent to `C:/`, and it saves a bit of typing.
7. MSYS2-provided userland software also includes various changes to help retain compatibility and interoperability. (An example is Perl reporting `msys` as `$^O`.)
8. Switch to `noacl` on default mounts. This prevents any permission mangling from MSYS2.
9. MSYS2 releases are based Cygwin's trunk, so they're more recent than contemporary Cygwin releases most of the time.

Other notable differences:

1. System root is `/usr`, not `/`.
2. Removal of system integration stuff, such as `cyglsa`, `cygserver`, `cygstart`...
