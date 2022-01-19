---
title: TODO LIST
summary: Here are some topics and milestones that deserve more discussion or work. This page should serve as an overview of our long-term issues and goals and be a place
    to write down the decisions and open questions so that they don't get buried in IRC logs or mailing list archives.
---
Here are some topics and milestones that deserve more discussion or work. This page should serve as an overview of our long-term issues and goals and be a place to write down the decisions and open questions so that they don't get buried in IRC logs or mailing list archives. Each goal should be described in appropriate detail and should be broken up into smaller tasks for interested members to tackle the goal step by step.

## Finish the SourceForge migration

- triage/migrate tickets from SF to GH; close them on SF afterwards
- archive the (closed) mailing list maybe? see [mbox export](https://sourceforge.net/p/forge/documentation/Mailing%20List%20Archives/)

Off-load package building and uploading
---
For a long time, @alexpux was responsible for building all packages.  Ray, Renato, Qian, and other people had tried to use various CI platforms, with varying results.  Since 2020, @lazka and @eine have set up a CI to automatically build most packages in https://github.com/msys2/msys2-autobuild in cooperation with an API on https://packages.msys2.org/.  Now @elieux is only responsible for uploading and signing them.

Approving pull requests for packages is done by a number of people.

What to do:

- write down packaging rules (rules inherited from Arch Linux, rules about `pkgbase`, `pkgname`, `description`, FHS, 32+64 bits, ...)
- prepare automated checks to prevent mistakes (an idea: compare package file list between latest and new version of the package)
- automate signing and uploading of packages?
- also work towards reproducible builds (https://reproducible-builds.org/)


Official release
---
MSYS2 is quite known but it's not obvious e.g. how stable and reliable it's supposed to be.  People are sometimes confusing it (in their minds, or in their words, or both) with MSys, much like MinGW-w64 is confused with MinGW.org.  The naming clash of MSYS2 the distribution vs. msys2 the emulation layer is also unfortunate (again reminiscent of the MinGW-w64 projects vs. its distributions).

What to do:

- decide if there's a need for a different name for *the whole thing*; if yes, decide upon one
- split release Qt runtime from debug Qt runtime and Qt developer files (those debug and dev files are really huge)
- make core updates fool-proof
- maybe approve and polish one graphical front-end to pacman
- create and/or polish packages for most popular open-source software (browsers, video players, email clients, office suites, IDEs, web servers) and maybe some additional useful software (like password managers, games, image editors)


Merge with Cygwin
---
The MSYS2 runtime is forked from Cygwin and the code bases are irregularly (but often) synchronized. There has been some talk about modifying Cygwin to make it pluggable so that the MSYS2 runtime can be reduced to a plugin DLL that will make all the desired behavior changes.

There has been a lot of requests for additional POSIX-only software in MSYS2 (X, various daemons...) and the response was always "MSYS2 is not for you; use Cygwin". It would be nice if people could just install one POSIX emulation layer and have everything available from there.

What to do:

- write down every difference between Cygwin and MSYS2 runtimes (see [the patches](https://github.com/msys2/msys2-packages/tree/master/msys2-runtime))
- offer appropriate patches to Cygwin as configurable behavior (e.g. CYGWIN=winsymlinks:copy)
- design an interface prototype for unacceptable features; figure out if the idea is sound
- design and implement the plug-in interface in cooperation with Cygwin
- re-implement MSYS2 runtime as a Cygwin plugin
- figure out if we can use Cygwin package repositories or if MSYS2 repositories can be used from Cygwin

Links:

- https://github.com/Alexpux/Cygwin/commit/4f756d6cc28179319ceccce01dd698de3f22c212
- https://sourceforge.net/p/mingw-w64/mailman/mingw-w64-public/thread/2F9017D3-8357-48C2-B887-A32FDF4E2141@gmail.com/
- http://sourceware.org/ml/cygwin/2014-12/msg00084.html
- https://github.com/Alexpux/MSYS2-packages/issues/83


Connect with upstreams
---
Where possible, we shouldn't maintain a bunch of patches, but rather polish them and have them accepted by upstreams.

Another change to consider is to start building only release versions of the core packages. Although MSYS2 is a rolling release distro, there seems to be little need to use less tested, potentially more buggy code directly from git. If there's a really important, not yet realeased patch, we apply it in the PKGBUILD until the next release. Currently the mingw-w64 toolchains are the most prominent examples.

- switch to release versions of upstream code
- improve technical quality of packages (make sure they follow all the packaging rules, tests are succeeding)
- send ideas and patches upstream, be prepared to compromise

Connect with downstreams
---
Altough we are probably not so big among end-users yet, a lot of cross-platform developers know about MSYS2 and support it and even some big projects use it for their official builds.  Some applications and environments use MSYS2 internally.  We should get in touch with them and help them (it is, after all, one of the core goals of the project).

Links:

- https://vcpkg.readthedocs.io/en/latest/maintainers/vcpkg_acquire_msys/
- https://chocolatey.org/packages/msys2/
- https://github.com/msys2/setup-msys2
- https://github.com/actions/virtual-environments/blob/master/images/win/Windows2019-Readme.md (https://github.com/actions/virtual-environments/pull/632 + https://github.com/actions/virtual-environments/pull/630)
- https://www.appveyor.com/docs/windows-images-software/#mingw-msys-cygwin
- https://docs.travis-ci.com/user/reference/windows/#how-do-i-use-msys2
- https://circleci.com/docs/2.0/hello-world-windows/
- https://github.com/git-for-windows/git/issues/284
- https://github.com/Alexpux/Cygwin/pull/8
- https://gitlab.haskell.org/ghc/ghc/wikis/building/preparation/windows
- https://wiki.qt.io/MSYS2
- https://www.gtk.org/download/windows.php#MSYS2
- https://cran.r-project.org/bin/windows/Rtools/
- https://wiki.inkscape.org/wiki/index.php?title=Compiling_Inkscape_on_Windows_with_MSYS2
- https://wiki.gnome.org/Initiatives/Windows
- https://github.com/xmrig/xmrig/wiki/Windows-Build
- https://github.com/LuminanceHDR/LuminanceHDR/tree/master/build_files/platforms/msys2
- https://sigrok.org/gitweb/?p=sigrok-util.git;a=blob;f=cross-compile/msys2/README
- https://blogs.gnome.org/nacho/2014/08/01/how-to-build-your-gtk-application-on-windows/


Get more people
---
The MSYS2 team is pretty small and we could use more people.  Some contributors become pretty active and motivated from time to time, but often they burn out after a while.  Since there are so few of core people, the occasional interested users, contributors and issue reporters are often greeted by silence and turned off.

What to do to get them:

- respond to them on IRC, Gitter, ML, handle their bug reports and contributions on GitHub in a timely fashion
- good documentation helps with frequent inquiries, automated checks help with code reviews
- get money and pay people?
- other ideas?

Links:

- https://www.msys2.org/wiki/Contributing-to-MSYS2/


Fix pacman errors wrt. conflicts in `bin/foo` vs `bin/foo.exe`
---
The runtime emulates extension-less executables by also looking for `.exe` on various FS calls. (There are more of these hacks, for example for symlink emulation.) This is causing pacman to complain when two packages independently provide both `foo` and `foo.exe`, or even worse `dir/` and `dir.exe`. People have to either disregard these conflicts with `--force`or (re-)install packages in a specific order.

A possible solution to these conflicts would be to disable the .exe interpolation, but then something would break, either users wouldn't be able to either run MSYS2 executables directly from Windows, or couldn't use the short extension-less names of commands in MSYS2. Therefore there also has to be a change that will mitigate that. We can for example design some passes for `makepkg`:

- make sure every `.exe` going into `{,/usr}/{bin,lib,libexec}/` has its extension stripped
- make sure only `.{exe,dll}` go into `/mingw{32,64}/bin/`
- build a good `.exe` wrapper for every executable in MSYS-land
- build a good shell wrapper for every executable in MINGW-land

This way, we can even make all non-binaries like shell scripts directly executable from Windows.

What to help with:

- think/discuss if this is a good idea


Provide more mingw-w64 versions of common CLI tools
---
It would be nice to allow people to have as complete as possible GNU-like environment without having to fall back to msys2 bash and the likes. The roadblock in this is that by putting every possible tool into `/mingw{32,64}/bin` will inevitably screw up native (i.e. non-cross) builds. Ideas for solutions:

- for every tool that's known to cause problems inside of MSYS2, include shell scripts in `/mingw{32,64}/bin/` that take priority over the `.exe`s.
- separate the essential build tools from everything else; (by using symlinks, aliases, or just using the package manager) we could have gcc, binutils and friends in `/mingw{32,64}/bin/` and everything else for instance in `/mingw{32,64}/morebin/` so that a MSYS2/MINGW shell only uses the `bin`, but people can opt in for using `morebin` outside of MSYS2

What to help with:

- design, test, agree on, and implement a way to prevent problems when building
- port all the tools!

Links:

- [Pull requests from @pfmoore](https://github.com/Alexpux/MINGW-packages/pulls?q=author%3Apfmoore)
- [GnuWin](http://gnuwin32.sourceforge.net)
- [UnxUtils](http://unxutils.sourceforge.net/)
- [GNU on Windows](https://github.com/bmatzelle/gow/wiki)
- [mksh/Win32](https://www.mirbsd.org/permalinks/wlog-10_e20130718-tg.htm)
- [busybox-w32](https://frippery.org/busybox/) and [MinGit](https://github.com/git-for-windows/git/wiki/MinGit#experimental-busybox-based-mingit) and [mingw-w64-busybox](https://github.com/git-for-windows/MINGW-packages/tree/main/mingw-w64-busybox)


Midipix
---
Maybe?
