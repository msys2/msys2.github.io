---
summary: MSYS2 is software distribution and a building platform for Windows.
---

# MSYS2-Introduction

MSYS2 is software distribution and a building platform for Windows. It provides a Unix-like environment, a command-line interface and a software repository making it easier to install, use, build and port software on Windows. That means Bash, Autotools, Make, Git, GCC, GDB..., all easily installable through Pacman, a fully-featured package manager.

It is an independent rewrite of MSys, based on modern Cygwin (POSIX compatibility layer) and MinGW-w64 with the aim of better interoperability with native Windows software.

Both 32-bit and 64-bit variants exist and receive mostly the same level of support.

## Subsystems

MSYS2 consists of three subsystems and their corresponding package repositories, `msys2`, `mingw32`, and `mingw64`.

The `mingw` subsystems provide native Windows programs and are the main focus of the project. These programs are built to co-operate well with other Windows programs, independently of the other subsystems. This part builds on the MinGW-w64 project.

The `msys2` subsystem provides an emulated mostly-POSIX-compliant environment for building software, package management, and shell scripting. These programs live in a virtual single-root filesystem (the root is the MSYS2 installation directory). Some effort is made to have the programs work well with native Windows programs, but it's not seamless. This part builds on the Cygwin project.

Each of the subsystems provides its own native (i.e. _target=host_) compiler toolchain, in `mingw-w64-i686-toolchain`, and `mingw-w64-x86_64-toolchain`. There are also cross compiler toolchains with _host={i686,x86_64}-pc-msys_ and _target={i686,x86_64}-w64-mingw32_ in `mingw-w64-cross-toolchain`, but these are of limited use because there are no library packages for them.

## Shells

Every subsystem has an associated "shell", which is essentially a set of environment variables that allow the subsystems to co-operate properly. These shells can be invoked using launchers in the MSYS2 installation directory or using the shortcuts in the Windows Start menu. The launchers set the `MSYSTEM` variable and open a terminal window (*mintty*) with a proper shell (*bash*). Bash in turn sources `/etc/profile` which sets the environment depending on the value of `MSYSTEM`.

Without the correct environment, various things may and will (sometimes silently) break. The exception is using mingw subsystems from pure Windows, which shouldn't require any special environment apart from an entry in `PATH`. Do not set `MSYSTEM` outside of the shells, because that will also break things.

## PATH

For optimal usage, MSYS2 automatically strips your `PATH` environment variable, essentially only leaving `C:\Windows\System32` and few others. This behavior can be controlled by setting the variable `MSYS2_PATH_TYPE` before starting a shell or using a correct argument when executing the launcher script. Beware that mixing in programs from other MSYS2 installations, Cygwin installations, compiler toolchains or even various other programs is not supported and will probably break things in unexpected ways. Do not have these things in `PATH` when running MSYS2 unless you know what you're doing.

Use `msys2` shell for running `pacman`, `makepkg`, `makepkg-mingw` and for building POSIX-dependent software that you don't intend to distribute. Use `mingw` shells for building native Windows software and other tasks.

## Packages

MSYS2 uses a port of **pacman** (known from Arch Linux) for package management. This brings many powerful features such as dependency resolution and simple complete system upgrades, as well as providing the build system (`makepkg-mingw`) - which is used to make these packages.

Packages for `msys2` are built from recipes in the `msys2-packages` Git repository, packages for `mingw` are in `mingw-packages`. Official repositories are on GitHub under user the *msys2* organization. When looking for `msys2` packages or deciding to create a new one, keep in mind that MSYS2 doesn't intend to compete with Cygwin or duplicate their efforts. The set of things that belong to the `msys2` subsystem is pretty small and needs to stay that way.

You might be wondering why there appears to be only one architecture variant of the `msys2` repository. In reality there are two, but the decision about which one to use is made at the time you install it, depending on whether you installed the i686 or the x86_64 version. It is possible to install both if you wish. Actually, you can have multiple installations of each on your computer, but you should never run programs from two different MSYS2 XXbit variants at the same time due to DLL address space and version conflicts. Also note that the uninstaller will only remove the most recently installed one of each variant).

## File system

The virtual filesystem contains:

Paths                                                    | Contents
---------------------------------------------------------|--------------------------------
`/bin`, `/dev`, `/home`, `/opt`, `/proc`, `/tmp`, `/var` | essential POSIX stuff
`/etc`, `/usr`                                           | `msys2` subsystem
`/mingw32`, `/mingw64`                                   | `mingw` subsystems
`/c`, `/d`, ...                                          | mount points for Windows drives
`/*.xml`, `/maintenancetool.*`, `InstallationLog.txt`    | (un)installer
`/autorebase.bat`, `/msys2_shell.cmd`, `/msys2.ico`      | shell entry points
