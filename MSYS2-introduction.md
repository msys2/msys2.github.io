MSYS2 is an independent rewrite of MSYS, based on modern Cygwin (POSIX compatibility layer) and MinGW-w64 with the aim of better interoperability with native Windows software.

The name is a contraction of Minimal SYStem 2, and aims to provide support to facilitate using the bash shell, Autotools, revision control systems and the like for building native Windows applications using MinGW-w64 toolchains.

We wanted a package management system to provide easy installation of packages, and ported Arch Linux's Pacman. This brings many powerful features such as dependency resolution and simple complete system upgrades, as well as providing the build system - makepkg{,-mingw} - which is used to make these packages.

Both 32 and 64-bit are supported.

Here is an irregularly updated [list of packages we provide](Packages)

MSYS2 consists of three subsystems and their corresponding package repositories, `msys2`, `mingw32`, and `mingw64`.

The `mingw` subsystems provide native Windows programs and are the main focus of the project. These programs are built to co-operate well with other Windows programs, independently of the other subsystems.

The `msys2` subsystem provides an emulated mostly-POSIX-compliant environment for building software, package management, and shell scripting. These programs live in a virtual single-root filesystem (the root is the MSYS2 installation directory). Some effort is made to have the programs work well with native Windows programs, but it's not seamless.

Each of the subsystems provides its own native (i.e. _target=host_) compiler toolchain, in `msys2-devel`, `mingw-w64-i686-toolchain`, and `mingw-w64-x86_64-toolchain`. There are also cross compiler toolchains with _host={i686,x86_64}-pc-msys_ and _target={i686,x86_64}-w64-mingw32_ in `mingw-w64-cross-toolchain`, but these are of limited use because there are no library packages for them.

Every subsystem has an associated "shell", which is essentially a set of environment variables that allow the subsystems to co-operate properly. These shells can be invoked using scripts in the MSYS2 installation directory or shortcuts in the Start menu. The scripts set the `MSYSTEM` variable and start a terminal emulator with bash. Bash in turn sources `/etc/profile` which sets the environment depending on the value of `MSYSTEM`.

Without the correct environment, various things may and will (sometimes silently) break. The exception is using mingw subsystems from pure Windows, which shouldn't require any special environment apart from an entry in `PATH`. Do not set `MSYSTEM` outside of the shells, because that will also break things.

When using the shells, try to remove as many entries from `PATH` as you can, ideally only leaving something like `C:\Windows\system32`. Mixing in programs from other MSYS2 installations, Cygwin installations or compiler toolchains is not supported and will probably break things in unexpected ways. Do not have these things in `PATH` when running MSYS2 unless you know exactly what you're doing.

Use `msys2` shell for running `pacman`, `makepkg`, `makepkg-mingw` and for building POSIX-dependent software that you don't intend to distribute. Use `mingw` shells for building native software and other tasks.

Packages for `msys2` are built from recipes in the `msys2-packages` Git repository, packages for `mingw` are in `mingw-packages`. Official repositories are on GitHub under user Alexpux and on SF.net under the MSYS2 project. When looking for `msys2` packages or deciding to create a new one, keep in mind that MSYS2 doesn't intend to compete with Cygwin or duplicate their efforts. The set of things that belong to the `msys2` subsystem is pretty small:
- essential POSIX stuff: `filesystem`, `msys2-runtime`, ...
- the native toolchain: `gcc`, `binutils`, `gdb`, ...
- supporting programs that are hard to port to Windows: `bash`, `automake`, `make`, ...
- supporting programs, even though they're portable: `mintty`, `winpty`, `python`, `man`, `vim`, `git`, ...
- random, highly useful stuff: `mc`, `ssh`, `rsync`, `lftp`, ...
- dependencies of these packages

In other words, if a program is needed to build native software, but is itself hard to port, it can be made into a `msys2` package. Anything else needs to be done as a `mingw` package or vetted individually.

The virtual filesystem contains:

Paths                                                   | Contents
--------------------------------------------------------|--------------------------------
`/bin`, `/dev`, `/home`, `/opt`, `/proc`, `/tmp`, `/var`| essential POSIX stuff
`/etc`, `/usr`                                          | `msys2` subsystem
`/mingw32`, `/mingw64`                                  | `mingw` subsystems
`/c`, `/d`, ...                                         | mount points for Windows drives
`/*.xml`, `/maintenancetool.*`, `InstallationLog.txt`   | installer
`/autorebase.bat`, `/*_shell.bat`, `/msys2.ico`          | shell entry points
