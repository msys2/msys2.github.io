Goals
=====

Cygwin and MSYS2 -- as projects -- have significantly different goals.

Cygwin tries to bring a POSIX-compatible environment to Windows so that most software that runs on unices will build and run on Cygwin without any significant modifications. Cygwin provides a large collection of packages containing such software, and libraries for their development.

MSYS2 tries to provide an environment for building native Windows software. MSYS2 provides a large collection of packages containing such software, and libraries for their development. As a large portion of the software uses GNU build tools which are tightly coupled to the unix world, this environment is also POSIX-compatible, and is in fact based on Cygwin. 

MSYS2 provides a minimal shell required to run autotools and other build systems which get the source for software from the Internet from different repositories, configure them and build them. The shell and core tools exist mainly to allow porting Unix programs to run natively on Windows (i.e. without requiring a POSIX emulation layer). MSYS2 doesn't try to duplicate Cygwin's efforts more than necessary, so the number of provided POSIX-emulated software is very small.

Packages
========

MSYS2 uses Pacman (known from Arch Linux) to manage its packages and comes with three different package repositories:
- `msys2`: Containing MSYS2-dependent software
- `mingw64`: Containing 64-bit native Windows software (compiled with mingw-w64 x86_64 toolchain)
- `mingw32`: Containing 32-bit native Windows software (compiled with mingw-w64 i686 toolchain)

Cygwin comes only with Cygwin-dependent software. It uses its own package management system, commonly called setup.exe.

Runtime
=======

Cygwin provides a runtime library called `cygwin1.dll` that provides the POSIX compatibility layer where necessary. The MSYS2 variant of this library is called `msys-2.0.dll` and includes the following changes to support using native Windows programs:

1. Automatic path mangling of command line arguments and environment variables to Windows form on the fly. (This can be [selectively turned off](Porting#user-content-filesystem-namespaces).)
2. Ability to change the reported OS using an environment variable (`MSYSTEM`, with values of `MSYS2`, `MINGW32`, and `MINGW64`).  This allows mingw-w64 software to be built in native build mode (as opposed to cross-compilation mode).
3. Conversion of output of native Windown applications from Windows line endings to POSIX line endings by removing trailing `'\r'` characters, so that e.g. `bb=$(gcc --print-search-dirs)` works as expected.
4. Replacement of symlinks with copying, so that Windows programs don't trip up on these files. MSYS2 also supports creating native NTFS symlinks, but these are limited in other ways.
5. Removal of the `/cygdrive` prefix for automounts. This is to retain compatibility with MSYS-enabled software that makes assumptions about `/c/` being equivalent to `C:/`, and it saves a bit of typing.
6. Switch to `noacl` on default mounts. This prevents any permission mangling from MSYS2.
7. MSYS2 releases might be ahead of or behind Cygwin releases.

Other notable differences:

1. System root is `/usr`, not `/`.
2. Removal of system integration stuff, such as `cyglsa`, `cygserver`, `cygstart`...
3. Dynamic libraries are prefixed `msys` instead of `cyg` (most other platforms, including mingw-w64, use `lib`).
4. Addition of the "-W" option to the `pwd` command in shells for compatibility with the old MSYS.
5. Various changes in utilities to help retain compatibility and interoperability.  An example is Perl reporting `msys` as `$^O`, or Sed recognizing CRLF as a line ending.
