# What is MSYS2?

MSYS2 is a free, open-source, and libre package management system for Windows. It uses a rolling-release model and a package management system called `pacman`.

## MSYS2 vs Other Projects

#### MSYS2 vs WSL

WSL is a software distribution and virtual machine management system on Windows. Rather than providing packages for Windows, it provides a Linux distribution where you can natively run their Linux package manager and Linux applications. Such a system trades off performance and requires virtualization, a feature that is computationally expensive and sometimes hard for developers to work natively with.

#### MSYS2 vs Chocolatey

Chocolatey is a package manager for Windows. Unlike MSYS2, it is a completely Windows-based package manager. That is, it does not use a "root" directory, but instead the `ProgramData` directory in Windows. The system is based on .NET and PowerShell. It has major community package support, and has a wide variety of packages. Because of the community focus in the open source version, however, you might not always find an up-to-date package. It comes in a open source or commercial edition.

#### MSYS2 vs Cygwin

Cygwin is a package manager for Windows. It is what MSYS2 is based off of, and is easily more like MSYS2 than any other system on this list. Some key features MSYS2 has are the seperate MinGW directories inside its root, and occasionally much more recent packages. It also has a dedicated package manager. On the other hand, Cygwin has _many_ more packages. It is open source.

#### MSYS2 vs Scoop

Scoop is a package manager for Windows. It is also based off of PowerShell and .NET, like Chocolatey. It is a smaller project than Chocolatey by far, though, and does not offer packages as extensively as Chocolatey. It is also open source.

#### MSYS2 vs Arch Linux

Arch Linux is a rolling-release Linux distribution. It shares a package manager, `pacman`, with MSYS2. It has nothing else to do with MSYS2 and does not provide packages for Windows. It does not even have a WSL distro. It is a Linux distro, and so is open source.
