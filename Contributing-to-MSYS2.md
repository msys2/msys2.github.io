Introduction
============

The MSYS2 software distribution uses a port of Pacman from Arch Linux to manage (install, remove and update) binary packages and also to build those packages in the first place.

There are 3 package repositories, `msys2`, `mingw32`, and `mingw64`. `msys2` software (from the `msys2` repository) is software that depends on `msys-2.0.dll` and is very similar to Cygwin software (which is a POSIX emulation layer for Windows). Native Windows software (from this project's perspective) is software that doesn't depend on `msys-2.0.dll`, and links dynamically to the highly compatible `msvcrt.dll`.

The source from which `msys2` packages are built is located at <https://github.com/Alexpux/MSYS2-packages> and the source from which `mingw{32,64}` packages are built is located at <https://github.com/Alexpux/MINGW-packages>.

In this document, to attempt to avoid confusion, MSYS2 refers to the software distribution while `msys2` refers to the repository, the packages in that repository and the software in those packages that link to `msys-2.0.dll`.

Building Packages
=================

The build system part of Pacman is called `makepkg` for `msys2` or `makepkg-mingw` for `mingw{32,64}`; hereafter `makepkg*`. You execute `makepkg*` from a folder containing, at minimum, a `PKGBUILD` file. Both `makepkg*` and `PKGBUILD` are shell scripts. `PKGBUILD` provides some shell functions, variables and arrays that are used by `makepkg*`. `makepkg-mingw` is a simple wrapper which calls `makepkg` twice, once with specialised environment to do the 32-bit build and once for 64-bit.

The core packages groups you need to install if you wish to build from `PKGBUILD`s are:
 - `base-devel` for any building
 - `msys2-devel` for building `msys2` packages
 - `mingw-w64-i686-toolchain` for building `mingw32` packages
 - `mingw-w64-x86_64-toolchain` for building `mingw64` packages

If you don't install the required package group, building might fail with unexpected errors. Note that -- contrary to what you might expect -- `base-devel` doesn't contain `gcc` nor `binutils`.

If you want to build for just one architecture (e.g. if you're on 32-bit Windows), you'll need to define `MINGW_INSTALLS` in the environment, with either `mingw32` or `mingw64` as the value, for example:

    MINGW_INSTALLS=mingw32 makepkg-mingw -sLf

... or you could export it from `~/.profile` so you don't need to remember it each time:

    export MINGW_INSTALLS=mingw32

<br>
Note that if you want to contribute, we'd appreciate it if you test your packages on both architectures (32 and 64 bits), which is only possible on a 64-bit Windows system. If you can't do that for some reason, we can test your pull requests on a 64-bit system.

You might be wondering why there appears to be only one arch variant of the `msys2` repository. In reality there are two, but the decision about which one to use is made at the time you install it, depending on whether you installed the i686 or the x86_64 version. It is possible to install both if you wish (actually, you can have multiple installations of each on your computer, but you should never run programs from two different MSYS2 XXbit variants at the same time due to DLL address space and version conflicts, also, the uninstaller will only remove the most recently installed one of each variant).

To contribute new packages or fixes, you should clone the relevant git repository above, commit and push your changes to a new, descriptively named branch and submit a pull request to us through GitHub. If we ask for fixes, please force-push them to this branch so that our history is clean.

When building *either* `msys2` or native software, you should use `msys2_shell.bat`. `makepkg-mingw` manipulates `PATH` appropriately for you.

An example of fetching the `msys2` repository source, building and then installing a package from it is:

    git clone "https://github.com/Alexpux/MSYS2-packages"
    cd MSYS2-packages/flex
    makepkg -sLf
    pacman -U flex-*.pkg.tar.xz

<br>
An example of fetching the `mingw{32,64}` repository source, building and then installing a package from it is:

    git clone "https://github.com/Alexpux/MINGW-packages"
    cd MINGW-packages/mingw-w64-python3
    makepkg-mingw -sLf
    pacman -U mingw-w64-*-python3-*-any.pkg.tar.xz

<br>
The `-sLf` passed to `makepkg*` means:

Flag Name          | Flag Description
-------------------|-----------------------------------------
`-s`, `--syncdeps` | Install missing dependencies with pacman
`-L`, `--log`      | Log package build process
`-f`, `--force`    | Overwrite existing package


Creating packages
=================

Try to find some existing working packages that use the same build system that your software does and try to use them as a template for your package.

Do *not* create pull requests for PKGBUILDs that just repackage binary releases from other projects. This is contrary to the goals of MSYS2. If the software cannot be built for some reason then fix the cause of that.

Patching
--------

When the software doesn't build straight away, you'll probably need to pass some arguments to the build scripts, or modify (patch) the source code. Such patches are stored as files in our repositories along with the `PKGBUILD` files. While it is probably okay to make quick (monkey-)patches that fix the software for Windows (and possibly break it for every other platform), is it better to make proper surgical-precision patches and attempt to have them accepted by the software developer ("upstream"). These patches may need to use platform checks to switch between the old and the new behaviour. Some useful identifiers:

Identifier           | Platform(s)                | Usage
---------------------|----------------------------|----------------------------
`_WIN32`             | mingw, msvc                | C code (`#ifdef ...`)
`_WIN64`             | 64-bit mingw, 64-bit msvc  | C code (`#ifdef ...`)
`__CYGWIN__`         | msys2, cygwin              | C code (`#ifdef ...`)
`__MSYS__`           | msys2                      | C code (`#ifdef ...`)
`x86_64-pc-msys2`    | 64-bit msys2               | Build scripts (`if [ $host = '...' ]`)
`i686-pc-msys2`      | 32-bit msys2               | Build scripts (`if [ $host = '...' ]`)
`x86_64-w64-mingw32` | 64-bit mingw               | Build scripts (`if [ $host = '...' ]`)
`i686-w64-mingw32`   | 32-bit mingw               | Build scripts (`if [ $host = '...' ]`)
`msys`               | msys2                      | Python (`sys.platform`)
`win32`              | mingw                      | Python (`sys.platform`)


Resources
=========

Read through our wiki, especially the [Porting](https://sourceforge.net/p/msys2/wiki/Porting/) section.

Useful Packages and Tools
-------------------------

Package                                | Purpose
---------------------------------------|------------------------------------------------------------
`mingw-w64-{i686,x86_64}-qt-creator`   | to build/debug qmake, qbs, autotools and cmake based packages
`mingw-w64-{i686,x86_64}-codelite-git` | if you dislike qt-creator
`mingw-w64-{i686,x86_64}-gedit`        | to avoid notepad and notepad++
`mingw-w64-{i686,x86_64}-meld3`        | to compare files and directories
`perl-ack`                             | Faster, better replacement for `grep`
`mingw-w64-{i686,x86_64}-ag`           | Very fast replacement for `grep` or `perl-ack`
`agm2`                                 | Comes with MSYS2, very fast search in MSYS2 PKGBUILD repos

Web Links
---------

- [Pacman on ArchWiki](https://wiki.archlinux.org/index.php/Pacman)
- [Pacman tips on ArchWiki](https://wiki.archlinux.org/index.php/Pacman_tips)
- [makepkg on ArchWiki](https://wiki.archlinux.org/index.php/makepkg)
- [bash on ArchWiki](https://wiki.archlinux.org/index.php/bash)
