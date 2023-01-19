---
summary: MSYS2 provides a native build environment, based on open source software, and
     makes you feel right at home when you are already comfortable with Linux.
---
# What is MSYS2?

MSYS2 isn't "one tool to rule them all", but tries to focus on what it's good
at. It provides a native build environment, based on open source software, and
makes you feel right at home when you are already comfortable with Linux. There
are good reasons to use multiple different environments and tools for different
tasks on Windows.

## MSYS2 vs Other Projects

In case you'd like to see more comparisons or feel that they could be improved
please let us know.

#### MSYS2 vs WSL

MSYS2 allows you to build native Windows programs, while with
[WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) you can only
cross compile them which makes things more complicated. If you are just looking
for Linux CLI tools, or want to build software that ends up on a Linux server
anyway then WSL is the better choice.

#### MSYS2 vs Chocolatey

[Chocolatey](https://chocolatey.org/) mainly bundles already built (open and
closed source) software and makes it easy to install/update them. In MSYS2 on
the other hand all packages are built from source and you can easily reproduce
the builds on your machine. Chocolatey packages have the advantage that the
bundled installers usually have better Windows integration, in that they set up
file associations, shortcuts, etc. and because they are not built from source
there are also lots of packages for closed source software like Visual Studio
etc. that would be hard to manage/update otherwise.

#### MSYS2 vs Cygwin

The unixy tools in MSYS2 are directly based on [Cygwin](https://cygwin.com), so
there is some overlap there. While Cygwin focuses on building Unix software on
Windows as is, MSYS2 focuses on building native software built against the
Windows APIs.

#### MSYS2 vs Arch Linux

MSYS2 and [Arch Linux](https://www.archlinux.org) share the package manager and
all that comes with it, like build definitions, rules for how to package things,
how updates work, how packages are signed, how packages are shipped, the rolling
release nature and so on. By re-using this functionality and concepts we can
focus on the actual packages and profit from the experience and work of Arch
Linux developers. Users already familiar with Arch Linux will also have an
easier time getting started.

#### MSYS2 vs Scoop

Due to lack of experience with [scoop](https://scoop.sh) see their comparison page:

* https://github.com/lukesampson/scoop/wiki/Chocolatey-Comparison
* https://github.com/lukesampson/scoop/wiki/Cygwin-and-MSYS-Comparison
