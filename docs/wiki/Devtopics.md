Here are some topics and milestones that deserve more discussion or work. This page should serve as an overview of our long-term issues and goals and be a place to write down the decisions and open questions so that they don't get buried in IRC logs or mailing list archives. Each goal should be described in appropriate detail and should be broken up into smaller tasks for interested members to tackle the goal step by step.


Unify public relations, solidify hosting
---
People are sometimes (often?) confused about where to get information about the project. It would be great if all the user-facing parts were on msys2.org and all the developer-facing parts on GitHub. Back-ends can be wherever (mailing lists and big file storage would be examples of things that we can't do with GitHub).

@alexpux doesn't agree, but @elieux believes one issue tracker for the whole project is better than separate ones. [Git for Windows](https://github.org/git-for-windows/git/issues) sets a particularly good example.

We currently have:

- [GitHub org](https://github.com/msys2) for our main repositories
- [a secondary GitHub org](https://github.com/msys2-contrib) for contributions upstream and as a working place
- other GitHub repos for source and issue tracking, [msys2-pacman](https://github.com/Alexpux/MSYS2-pacman), [msys2-keyring](https://github.com/Alexpux/MSYS2-keyring), [path_convert](https://github.com/Alexpux/path_convert)
- [SourceForge project](https://sourceforge.net/p/msys2/) for mailing lists and as a secondary mirror (it had forums and the wiki in the past)
- https://msys2.org (also msys2.com and msys2.net), our own domains (owned by @elieux), with installation and donation instructions [with source on GitHub](https://github.com/msys2/msys2.github.io)
- [an online repo browser](https://packages.msys2.org/), hosted by @lazka
- http://repo.msys2.org as the primary mirror, hosted by Diablo-D3

What to do:

- migrate tickets from SF to GH; close them on SF afterwards
- migrate forums and discussion from SF to GH
- move active MSYS2-related repositories on GH to the msys2 org, including issues (Alexpux/..., maybe Elieux/msys2-launcher and other contributed tools)
- maybe find more (fast and reliable) mirrors so we can ditch SF file hosting
- try moving the mailing list including archives from SF, see [mbox export](https://sourceforge.net/p/forge/documentation/Mailing%20List%20Archives/); can we use Sourceware? can we have our own (some say that mailman on our own server would be spam-filtered badly)? notify list members of the change (possibly set up a redirect for some time)
- change links in packages ("submit bug" URLs) and elsewhere


Off-load package building and uploading
---
Currently, Alexey is responsible for building and uploading packages (both new and updated ones). Approving packages for inclusion is done mostly by him and sometimes by other contributors. We need to delegate the burden of building packages to more people so that Alexey has time for other stuff and updates are not put on hold in times of his unavailability. The build queue is maintained by a script and displayed separately [for new packages](https://packages.msys2.org/new) and [for updated packages](https://packages.msys2.org/queue).

A buildbot for uploading packages would be the best solution, but it may take a long time to get one. Ray, Renato, Qian, and other people have tried to use AppVeyor for building MSYS2 packages, with varying results. It currently isn't completely feasible for us due to their time limits on individual builds (GCC and Qt are the biggest offenders here).

We have buildbot integrations with both AppVeyor and Azure for checking pull requests, merges and pushes to mingw-packages and msys2-packages.

What to do:

- write down packaging rules (rules inherited from Arch Linux, rules about `pkgbase`, `pkgname`, `description`, FHS, 32+64 bits, ...)
- prepare automated checks to prevent mistakes (an idea: compare package file list between latest and new version of the package)
- agree on a way to make sure the repository is updated by at most one person at a time
- designate packagers and sign packager keys if necessary
- get a buildbot that can build all packages
- make the buildbot automatically upload packages
- also work towards reproducible builds (https://reproducible-builds.org/)

Additional discussions:
- [#2616](https://github.com/Alexpux/MINGW-packages/issues/2616)
- [#2006](https://github.com/Alexpux/MINGW-packages/issues/2006)


Official release
---
MSYS2 is currently marketed as a potentially unstable developer tool and it's not yet advertised in any way to end users. People are sometimes confusing it (in their minds, or in their words, or both) with MSys, much like MinGW-w64 is confused with MinGW.org. The naming clash of MSYS2 the distribution vs. msys2 the emulation layer is also unfortunate (again reminiscent of the MinGW-w64 projects vs. its distributions).

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
Altough we are probably not so big among end-users yet, a lot of cross-platform developers know about MSYS2 and support it and even some big projects use it for their official builds.  We should get in touch with them and help them (it is, after all, one of the core goals of the project).

Links:

- https://github.com/git-for-windows/git/issues/284
- https://github.com/Alexpux/Cygwin/pull/8
- https://gitlab.haskell.org/ghc/ghc/wikis/building/preparation/windows
- https://wiki.qt.io/MSYS2
- https://www.gtk.org/download/windows.php#MSYS2
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
- https://github.com/msys2/msys2/wiki/Contributing-to-MSYS2


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


Midipix
---
Maybe?
