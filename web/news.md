---
summary: Important events happening.
---
# News

This page lists important changes or issues affecting MSYS2 users. We also post them to [Mastodon](https://fosstodon.org/@msys2org) / [Bluesky](https://bsky.app/profile/msys2org.bsky.social), including some not-so-important things :)

### 2025-06-20 - Replacing `x86_64-pc-msys` with `x86_64-pc-cygwin`

As part of our ongoing effort to move MSYS2 closer to Cygwin, we have now
replaced the `x86_64-pc-msys` triplet with `x86_64-pc-cygwin` as the default
host triplet for the MSYS environment.

This means:

* The `$MSYSTEM_CHOST` environment variable will now report `x86_64-pc-cygwin`
  instead of `x86_64-pc-msys`
* Autotools based configure scripts will default to `x86_64-pc-cygwin` instead
  of `x86_64-pc-msys`
* `gcc -dumpmachine` will report `x86_64-pc-cygwin` instead of `x86_64-pc-msys`

Ideally this should not affect most users. If there are any issues with this
change, please let us know.

### 2025-04-18 - Hosted Windows ARM64 Runners on GitHub Actions

Earlier this week, GitHub finally [added Windows ARM64 runners to GitHub Actions](https://github.blog/changelog/2025-04-14-windows-arm64-hosted-runners-now-available-in-public-preview/), which is great news and will help us a lot producing native ARM64 packages in MSYS2 in the future. Since many of our packages are already available for ARM64, you might be wondering how we managed to do this until now. Let's take a look back:

In early 2021, [Jeremy](https://github.com/jeremyd2019) bootstrapped our CLANGARM64 environment from a Cygwin LLVM build and built our first CLANGARM64 packages. To automate our package builds, we needed GitHub Actions support, which Jeremy also took on himself, and set up a WoA machine with an ARM64 version of GitHub runner, which we integrated into msys2-autobuild in late 2021. The whole ecosystem was in a very early stage at the time, such as the Actions runner itself, ARM64 support for Node.js, ARM64 Windows itself, Windows x64 emulation, etc., so things were not easy. Hardware was also an issue, as emulation was very slow, real hardware was very underpowered, and there were no dev kits in the beginning, so the runner had to move hardware several times over its lifetime.

Another challenge was that the self-hosted runner builds were not isolated, which meant that we could only use them for final package builds, so as not to expose them to untrusted users. So no CI checks on random PRs or other repos that are exposed in any way. While this meant that ARM64-only issues were sometimes found very late in the process, fortunately there was always someone around to debug things on real hardware if needed.

Some stats on the last year of the self-hosted ARM64 runner:

* It ran 1835 jobs
* It built packages for 1593 hours
* It built 9869 packages
* It produced 52.4 GB worth of packages

After building for 3-4 years we now have ~93% of all MSYS2 packages available for ARM64.

Thanks to [Jeremy](https://github.com/jeremyd2019) for maintaining the self-hosted runner for so long, setting it up, updating it, moving it, fixing it, scaling it up for large rebuilds, being very responsive when things got stuck or debugging ARM64-only build issues, and much more. Also thanks to [Dennis Ameling](https://github.com/dennisameling) for funding the "QC710 Dev Kit" and [Zac Walker @ Microsoft](https://github.com/ZacWalk) for providing us with a "Dev Kit 2023".

The future:

With the new hosted runners, we can now test with ARM64 in many more places, such as package updates before they are merged, for all our forks of external projects, our GitHub action, our installer, our integration test, and much more. We can also run more jobs in parallel, which will be helpful for large rebuilds like major Python updates. And it allows our community to debug ARM64 related issues even if they do not have ARM64 hardware available, even though debugging in CI is not much fun.

For users of our "setup-msys2" GitHub Action this means they can easily add ARM64 testing/building to their project:

```yaml
jobs:
  msys2-clangarm64:
    runs-on: windows-11-arm
    steps:
      - uses: actions/checkout@v4
      - uses: msys2/setup-msys2@v2
        with:
          msystem: CLANGARM64
          update: true
      - name: CI-Build
        shell: msys2 {0}
        run: |
          ./ci-build.sh
```

### 2025-02-14 - Moving MSYS(2) closer to Cygwin

In MSYS2, in addition to the native environments such as UCRT64/CLANG64, there is also the "MSYS" environment, which contains mostly Cygwin-based software. Since the start of the MSYS2 project, the Cygwin tools in MSYS have been modified to build for MSYS instead of Cygwin. This means that the languages and tools have been patched to report their platform as "msys", and for the build tools this means that we have our own MSYS specific target triplet (x86_64-pc-msys), and uname reports "MSYS" as well.

Whatever the motivation was back then, the reality today is that our Cygwin packages are 99% the same as Cygwin's, with only a few things needing tweaking. The downside of defining our own platform/system/triplet is that every build system has to be patched to treat us as Cygwin-like, which is tedious and error-prone when adding/updating packages, and also divides the community. Another drawback is that it's confusing to users, as the names of MSYS2, the project, and MSYS are too similar, and it's not clear that MSYS mostly just means Cygwin.

Some time ago we started to remove these differences by replacing "msys" with "cygwin" + patches where possible. So instead of MSYS being a fork of Cygwin, it would just be a slightly modified/extended variant of Cygwin. The goal is that any software that supports Cygwin should be buildable as is under MSYS2. The first change in this direction already happened some time ago, when CMake would define both CYGWIN and MSYS as true when building under MSYS. Since then, we have tweaked several more things to get closer to that goal:

* CMake has reported CYGWIN as true since 2021
* Meson has reported to be running under Cygwin since we added it in 2018
* Python has been changed to report "sys.platform" as "cygwin", and recently "sysconfig.get_platform()" has been changed to report "cygwin-x86_64" as well.
* Perl has recently been changed to report "$^O" as "cygwin" instead of "msys".
* Bash has recently been changed to report "$OSTYPE" as "cygwin" instead of "msys".
* Almost all of our packages have been ported to build for the Cygwin triplet, except for the toolchain packages.

The rule of thumb is that where possible, things will continue to identify as both Cygwin and MSYS, for example, CMake will set both MSYS and CYGWIN, C/C++ will define both `__MSYS__` and `__CYGWIN__`. Where this is not possible, things will simply identify as Cygwin, or we will have to find workarounds.

The next planned steps for this transition are currently:

* Change the default host triplet from "x86_64-pc-msys" to "x86_64-pc-cygwin"
* Change the runtime to be a superset of Cygwin in more places, e.g. make the CYGWIN env var work as a fallback if MSYS is not set. The goal is to make the Cygwin documentation mostly applicable to MSYS2 as well.

For MSYS2 users these changes should be mostly invisible, but if you are a developer targeting the MSYS environment there might be some fallout. Despite that, we hope these changes will lead to better compatibility and easier maintenance in the long run. Let us know if you experience any problems.

### 2025-02-13 - Server maintenance on 2025-02-15/16

There will be a short server maintenance around the weekend of 2025-02-15/16 which will affect repo.msys2.org, mirror.msys2.org, packages.msys2.org, and some subdomain redirects of our website.

Update: all done now

### 2024-12-18 - Removal of the CLANG32 Environment

The previously announced removal of the CLANG32 environment is now complete.
This concludes the gradual phase-out process that began several months ago.

### 2024-11-09 - Python 3.12 Update

Over the last week we finally moved from Python 3.11 to 3.12. Thanks to
[@naveen521kk](https://github.com/naveen521kk) for updating the fork, and
everyone else who helped with rebuild issues. Also thanks to
[@jeremyd2019](https://github.com/jeremyd2019) for watching the external arm64
runner while it rebuilt all those 940 packages and fixing arm64 related issues.

There are some minor things to watch out for with this update:

* We've enabled [PEP 668](https://peps.python.org/pep-0668/) by marking the
  system site-packages directory as externally managed. To prevent this from
  causing too many problems right away [we have patched our version of
  pip](https://github.com/msys2/MINGW-packages/commit/4447a7ba7971d3480e7bd24951ec8e51328d23c9)
  to only give a warning instead of an error if you install outside of a venv.
  However, we may change this back to a real error in the future. If this is
  causing any problems or if there are any concerns with re-enabling the error
  in the future let us know.
* While not MSYS2 specific, 3.12 is the version that [dropped the included
  distutils package](https://peps.python.org/pep-0632) and distutils is now only
  available as part of setuptools. While the current setuptools should handle
  our Python out of the box, there may be slight differences. Make sure to
  remove anything setting `SETUPTOOLS_USE_DISTUTILS=stdlib` as that will lead to
  distutils import errors.
* As with every major Python update we had to drop a few packages that were
  incompatible with the new version and for which no update or patch was
  available. One notable package there is py2exe which does not support 3.12+
  right now and there is also no patch available, see [the upstream
  issue](https://github.com/py2exe/py2exe/issues/191) for details.

### 2024-11-03 - Disabling mingw-w64 wildcard support by default

For historical reasons MSYS2 enabled wildcard support in mingw-w64 at build
time. This means that every built executable had wildcard support enabled by
default, unless it explicitly opted out. Wildcard support in this case means
that program arguments containing `?`and `*` can be expanded to one or more file
paths if the pattern happens to match paths of files on disk. Note that this
happens directly in the target program, not in a shell beforehand.

This expansion has several problems:

* Behave differently than MSVC built executables
* It's confusing to users when wildcard handling is accidentally triggered. For
  example, passing a regex as an argument to a CLI tool that starts matching
  random files, breaking the pattern.
* It may have security implications if arguments to executables are forwarded
  from user-controlled input, in which case an argument could expand to a
  different string depending on the files present on the filesystem.

Given all this, we have decided to disable wildcard handling by default. This
means that any package and executable that is built after this change will get
the new default behavior.

```console
$ python -c 'import sys; print(sys.argv)' '*a.txt' # before
['-c', 'a.txt', 'aaaa.txt', 'bla.txt']
$ python -c 'import sys; print(sys.argv)' '*a.txt' # after
['-c', '*a.txt']
```

Our hope/assumption is that this will not affect many users, as most will rely
on globbing at a higher level, be it bash, or build systems. If you experience
any problems, please let us know. See also [the
documentation](./docs/c.md#expanding-wildcard-arguments) on how to force
wildcard handling for your applications even after this change.

### 2024-09-23 - Starting to drop the CLANG32 environment

9 months ago we started to reduce the number of packages for the 32-bit
environments. Now we are starting to drop the CLANG32 environment. This means
that we will no longer add new packages for this environment and will remove the
existing ones over the next months. If this is affecting you, please let us
know.

While CLANG32 has some unique features in the context of MSYS2, such as being
the only environment to use UCRT for 32-bit and the LLVM toolchain, it has seen
very little use in our download statistics, and we don't think it's worth
supporting any longer.

If you are in need for a 32-bit LLVM toolchain, consider using [LLVM
MinGW](https://github.com/mstorsjo/llvm-mingw) instead.

### 2024-07-28 - MSYS2 support in setuptools v70.0.2

Setuptools v70.0.2 now supports mingw Python and MSYS2 natively. This eliminates
the need for SETUPTOOLS_USE_DISTUTILS=stdlib when building C extensions,
enabling "pip install" to just work for most packages without extra steps.

With the stdlib distutils now no longer being required to build packages we can
continue our work to update to Python 3.12.

### 2024-07-08 - File conflicts when updating python

Due to the recent Python 3.12 update missing .pyc files, you might see file
conflicts when updating:

```console
error: failed to commit transaction (conflicting files)
python: /usr/lib/python3.12/__pycache__/ast.cpython-312.pyc exists in filesystem
python: /usr/lib/python3.12/__pycache__/dis.cpython-312.pyc exists in filesystem
python: /usr/lib/python3.12/__pycache__/inspect.cpython-312.pyc exists in filesystem
python: /usr/lib/python3.12/__pycache__/opcode.cpython-312.pyc exists in filesystem
...
```

This can be fixed by running

```console
$ pacman --overwrite "/usr/lib/python3.12/*" -Suy
```

Sorry for the inconvenience.

### 2024-06-21 - Server changes

Over the past few weeks we've been experiencing various problems with our
server, which also led to an extended downtime on 2024-06-12. It turned out that
both disks were failing and instead of replacing them both we decided to simply
move to a new server. This transition is now complete and everything should be
back to normal.

* Old IP: `178.63.98.68`
* New IP: `88.99.69.85`

Many thanks to [Dmitriy Akulov](https://dakulov.com) of
[jsDelivr](https://www.jsdelivr.com/) and
[Globalping](https://www.jsdelivr.com/globalping) for helping us diagnose the
problem and generously providing us with a new server.

### 2024-05-10 - GCC 14.1

We have updated GCC to version 14.1. See the [GCC 14.1 release
notes](https://gcc.gnu.org/gcc-14/changes.html) for more information. Similar to
recent Clang releases, GCC also got stricter and multiple warnings are now
errors by default, see the [GCC 14.1 porting
guide](https://gcc.gnu.org/gcc-14/porting_to.html) for details.

To reduce the maintenance burden we have dropped Ada/Objective-C/libgccjit
support from the 32-bit/mingw32 variant.

### 2024-05-03 - Update to Cygwin 3.5 on Unsupported Systems

The update to Cygwin 3.5 means MSYS2 will no longer start on long unsupported
systems like Windows 7 and 8.0.

To keep MSYS2 running for a bit longer on such systems you can switch to the
legacy runtime using:

```console
$ pacman --noconfirm -Sy msys2-runtime-3.4 msys2-runtime-3.4-devel
```

In case you have already updated and can't start MSYS2 anymore, you can use the
following steps to downgrade:

* Get the [last MSYS2 installer release](https://github.com/msys2/msys2-installer/releases/download/2024-01-13/msys2-base-x86_64-20240113.sfx.exe) and extract it
* Copy the "msys64\usr\bin\msys-2.0.dll" from there to the same location in your existing MSYS2 installation
* Start a MSYS2 terminal and switch to the legacy runtime using the command above

### 2024-05-02 - MSYS2 on Linux (Experimental)

We've created a Docker image including a Wine fork + Cygwin fixes + MSYS2, as an
experiment, so you can run MSYS2 on Linux: https://github.com/msys2/msys2-docker

Be warned, it's very slow and flaky, and signature verification is disabled for
packages/repos, because otherwise things would be unacceptably slow. Don't
use it for anything important.

Shout out to [@pojntfx (Felicitas Pojtinger)](https://github.com/pojntfx) for
the idea and initial Dockerfile and to [@jhol (Joel
Holdsworth)](https://github.com/jhol) for developing the wine fork.

### 2024-04-23 - TLS/SSL Support for the Repository Rsync Server

We have added TLS/SSL support for the repository rsync server. This means that
you can now use

```console
$ rsync-ssl rsync://repo.msys2.org/builds
```

to sync the repository over an encrypted connection.

### 2024-04-02 - Automated Vulnerability Reporting System

The [package index](https://packages.msys2.org/security) now has some
rudimentary support for detecting and displaying
[CVEs](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) and
other vulnerability reports for the packages included in MSYS2.

We piggyback on existing security scanner tools by using the metadata in the
package recipes to create a dummy
[SBOM](https://www.ntia.gov/page/software-bill-materials) file and then feed the
scan results to our website. This gives us some insight into which
packages have potential vulnerabilities or which updates should be prioritized.
For more information on the process see [Vulnerability
Reporting](./dev/vulnerabilities.md).

Some caveats:

* Only about half of our packages have the necessary metadata to be scanned at
  all. This is mainly because packages that have never had a CVE assigned also
  don't have a [CPE](https://nvd.nist.gov/products/cpe) to link to, and partly
  because it's just incomplete on our end.
* The CVE system is currently [not fully
  operational](https://nvd.nist.gov/general/news/nvd-program-transition-announcement),
  and for the past few weeks most of the incoming CVEs have not been processed
  at all. This means that newer CVEs are likely not linked to our packages.
  Since we use [grype](https://github.com/anchore/grype) for scanning we do get
  some new data from their [nvd-data-overrides
  effort](https://github.com/anchore/nvd-data-overrides) though.
* Note that we will not try to reduce the number of reported vulnerabilities to
  zero. We will mainly use them to prioritize updates and be better informed
  about the security status of our packages.

### 2024-03-30 - xz-utils Backdoor

In response to the recent [xz
backdoor](https://en.wikipedia.org/wiki/XZ_Utils_backdoor) we have rebuilt the
xz packages for [msys](https://github.com/msys2/MSYS2-packages/pull/4475) and
[mingw](https://github.com/msys2/MINGW-packages/pull/20479) from the git source
instead of the tarball, following what [Arch Linux
did](https://gitlab.archlinux.org/archlinux/packaging/packages/xz/-/commits/main).

Although we have built and shipped the affected versions, there is no indication
at this time that this issue has affected MSYS2 users.

### 2024-02-21 - Note to the remaining Windows 7 / 8.0 users

Note to Windows 7 / 8.0 users: While we stopped supporting these systems over a year
ago, many things in MSYS2 continued to work as before. With the upcoming update
to Cygwin 3.5, this will change and MSYS2 will no longer start on these systems.
We're trying to come up with a migration path, but it's not clear yet if and how
this will work. We'll post here when we know more.

### 2024-02-19 - Removal of non C/C++ packages from the mingw-w64-toolchain group

Unlike the LLVM variant, the GCC variant of the
[mingw-w64-toolchain](https://packages.msys2.org/basegroups/mingw-w64-toolchain)
package group also contained non C/C++ toolchains, such as
fortran/ada/objc/libgccjit due to the nature of them being built from the same
source. Since this was never the intention of the group and was causing a lot of
unnecessary downloads and bandwidth usage, we decided to clean this up now.

If this broke things for you, make sure you explicitly install [Fortran/Ada/ObjC
packages](https://packages.msys2.org/base/mingw-w64-gcc) if you depend on them.

### 2024-02-01 - mingw-w64-gettext converted to split package

[mingw-w64-gettext](https://packages.msys2.org/base/mingw-w64-gettext) has been
split into "gettext-tools" and "gettext-runtime" subpackages. While this is a
backwards compatible change, this means that the gettext tools, like msgmerge
and msgfmt, are less likely to be installed as transitive dependencies via other
packages, and may now be missing for you if you were implicitly depending on
them.

If this broke things for you, make sure you explicitly install the [gettext
tools](https://packages.msys2.org/base/mingw-w64-gettext) if you depend on them.

### 2023-12-13 - Starting to drop some 32-bit Packages

Three years ago we dropped 32-bit Windows support for running MSYS2 itself, now
we are taking the next step and slowly starting to reduce the number of 32-bit
packages, meaning the packages for the MINGW32 and CLANG32 environments. The
goal of the phase-out is to reduce maintenance costs and server resources while
not affecting most users. The focus will be on packages that aren't likely to
see much use anyway, or where 64-bit alternatives are available and viable:

* Packages which are likely not used outside of MSYS2 (re-packaged)
* End-user applications which are likely not used outside of MSYS2 (GUI apps,
  ...)
* Packages for resource intensive work where most external users are likely
  already on 64-bit (some scientific packages, ...)
* Leaf packages with complex and resource intensive builds that are likely not used
* New leaf packages

To find out if a package you have installed is affected you can run `pacman -Qm`
which lists all installed packages which are no longer available in the repo.
Ideally not many people should notice these changes, but in case they affect
you:

* Switch your workflow to use 64-bit packages instead ;)
* Tell us which packages that were removed you still need, so we can consider reinstating them. Please use the [issue template](https://github.com/msys2/MINGW-packages/issues/new?assignees=&labels=package-request&projects=&template=environment_request.yml&title=Build+%5Bpackage+name%5D+for+%5Benvironment%5D) to file your request.

If you are wondering if you should continue to support 32-bit Windows for your
users, here are some relevant resources:

Usage stats:

* https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam
  32-bit Win8.1+ below the list threshold. Heavily biased towards newer hardware
  though.
* https://www.pcbenchmarks.net/os-marketshare.html 32-bit users at ~0.1%.
  Heavily biased towards newer hardware though.
* https://data.firefox.com/dashboard/hardware 32-bit at ~14%, but this includes
  ~11% Win7 and other operating systems which we don't support, so it's not
  clear.
* In MSYS2 32-bit packages made up ~3.95% of all downloads at the end of 2023,
  and ~6.45% one year before (ignoring CI downloads)

Some applications dropping 32-bit support:

* [Krita](https://krita.org/) dropped 32-bit support in 2021
* [qBittorrent](https://www.qbittorrent.org/) dropped 32-bit support in 2022
* [KeePassXC](https://keepassxc.org) dropped 32-bit support in 2022
* [SciPy](https://scipy.org/) dropped 32-bit support in 2022

There are of course lots of applications not planning to drop support and 32-bit
Windows is still supported until at least October 2025, so we understand that 32-bit
support is still required in various cases, and we will try to keep important
packages around for as long as possible.

### 2023-11-05 - Package installation issues for very old/outdated installations

If you haven't updated pacman in 2.5 years or longer, but are installing
new packages, you will see errors like this, due to a format change in the
package database:

```
error: mingw-w64-ucrt-x86_64-shared-mime-info: missing required signature
error: mingw-w64-ucrt-x86_64-gtk3: missing required signature
error: failed to commit transaction (package missing required signature)
Errors occurred, no packages were upgraded.
```

This can be fixed by [updating your installation](./docs/updating.md).

### 2023-08-06 - Python: Changed behavior when loading DLL dependencies of extension modules

Starting with CPython 3.8, upstream CPython changed their DLL lookup behavior to
a safer default when loading extension modules, which meant no longer looking in
PATH and the current working directory as a fallback, but requiring code to
explicitly add directories containing dependencies via
[`os.add_dll_directory()`](https://docs.python.org/3/library/os.html#os.add_dll_directory).

Because many packages weren't ported yet back then, and this behavior interfered
with our MinGW port build process we reverted this change and kept the old
behavior. This had the downsides of being less secure and
`os.add_dll_directory()` not working.

We have now finally managed to fix this in our port, so that DLL loading works
the same as with the official CPython distribution.

If this change is causing problems for you:

* Make sure to use `os.add_dll_directory()` where needed, as recommended by
  upstream, see https://docs.python.org/3/library/os.html#os.add_dll_directory
  for details
* To ease the transition we've temporarily added a
  `PYTHONLEGACYWINDOWSDLLLOADING` environment variable, which you can set to `1`
  to get back the old behavior. We will remove this workaround after some time,
  so please let us know if there are any problems that can't be solved without
  it.

### 2023-04-01 - LLVM 16

LLVM/Clang has now been updated to v16, here are some things to look out for:

* Stricter C compiler: Various previously warnings are now errors by default and
  might make your build fail. See the following for more information:

    * The upstream changelog entry: https://releases.llvm.org/16.0.0/tools/clang/docs/ReleaseNotes.html#potentially-breaking-changes
    * The Gentoo guide for how to adjust your code for the new stricter defaults: https://wiki.gentoo.org/wiki/Modern_C_porting
    * The Gentoo bug which tracks all related issues in Gentoo: https://bugs.gentoo.org/870412

* autoconf bugs: The stricter defaults in clang v16 exposed some autoconf bugs
  which lead to some compiler checks returning the wrong results. We have
  backported the respective fixes into all our autoconf versions (2.13, 2.69 and
  2.71) and updated autoconf-archive, but this means you will have to run
  autoreconf to get those fixes. There is also a chance that other checks in
  configure.ac or m4 macros shipped with your project will need to be updated.
  So watch out for changes in your configure results.

* fortran/flang: flang, the llvm based Fortran compiler, is now capable of
  building some of our Fortran based packages. But despite that, it still has
  known issues of generating wrong or broken code without warnings and should
  not be used in production. The same is true for all Fortran based packages we
  are building with it.

* Packages not compatible with llvm v16: So we don't have to wait for all
  packages/projects to support the newest llvm version, we added new packages for
  llvm v14 and v15 which only contain static builds and are now used by the
  packages not supporting llvm v16. This currently affects python-llvmlite,
  openshadinglanguage and include-what-you-use.

### 2023-02-10 - Server maintenance on 2023-02-18/19

There will be a short server maintenance around the weekend of 2023-02-18/19 which will affect repo.msys2.org, mirror.msys2.org, packages.msys2.org, and some subdomain redirects of our website.

Update: all done now

### 2023-01-15 - Dropping support for Windows 7 and 8.0

As announced last April we will no longer support Windows 7 / 8.0 from now on.

### 2023-01-15 - OpenSSL updated from 1.1.1 to 3.0.x

With v3.0 being out for more than a year and the EOL of v1.1.1 approaching this year we have moved both cygwin and mingw builds to v3.0.x now. If there are any issues let us know.

Note that the license of OpenSSL has changed to Apache-2.0 starting with v3.

### 2023-01-05 - Dropping 32bit support for Qt 6

Qt project dropped support for Windows version older than Windows 10 from Qt 6,
see this official [blog post](https://www.qt.io/blog/qt6-development-hosts-and-targets).
It was also added that we will not have 32 bit x86 Windows support available.
With this above condition, we too have very few users who are using 32 bit x86
Windows 10. So, we decided to remove 32 bit builds for Qt 6 and their dependencies.
The remaining 32 bit x86 packages which depends on Qt will be linked with Qt 5.
With this, our Qt 6 packages will be available for all official
[Windows platforms](https://doc.qt.io/qt-6/windows.html).

### 2022-12-26 - Default `_WIN32_WINNT` bumped to Windows 8.1 for UCRT environments

We have bumped the default `_WIN32_WINNT` version defined in mingw-w64 from Windows 7 to Windows 8.1 for non-arm UCRT environments (CLANG32, CLANG64, UCRT64). For projects that don't define their own `_WIN32_WINNT` and conditionally include features depending on the minimum supported Windows version this might mean that new builds will start depending on Windows 8.1. MINGW32/64 will default to Windows 7 for a bit longer to smooth over the transition.

This is part of our goal to phase out Windows 7 support and target newer Windows versions by default.

### 2022-12-16 - Dropping Windows 7 support for the MSYS2 installer

The latest release of the MSYS2 installer (v2022-12-16) has dropped support for Windows 7. It will show an error message and abort if started on Windows 7.

### 2022-10-29 - Changing the default environment from MINGW64 to UCRT64

About 1.5 years ago we started adding a new variant of the MINGW64 environment called [UCRT64](./docs/environments.md), which uses the Universal CRT instead of
the old msvcrt.dll. Now that all our packages are available in this new environment and a very large percentage of our users (~97%) are on a system that includes UCRT, we recommend it as the default environment instead of MINGW64.

The MINGW32/64 environments will continue to exist and there are no plans to remove them, but we will focus our attention more on UCRT64 and the other UCRT-using environments such as CLANG64 and CLANGARM64.

### 2022-10-23 - mingw packages now built with `-D_FORTIFY_SOURCE=2` and `-fstack-protector-strong`

Our mingw packages will be built with `-D_FORTIFY_SOURCE=2` and `-fstack-protector-strong` from now on.

### 2022-10-18 - New minimum hardware requirements (CPUs from ~2006/7+)

As a first step of phasing out support for Windows 7, we're raising the minimum hardware requirements to match Windows 8.1, which roughly equals Intel Core 2 / AMD Phenom, so anything after 2006/7 is fine.

In terms of GCC/Clang compiler flags this means going from `-march=x86-64` to `-march=nocona -msahf`. This only affects 64bit packages, and only those that use features only available in those newer CPUs, and only once they are updated or rebuilt.

### 2022-10-10 - libssp is no longer required

Building with `_FORTIFY_SOURCE` no longer requires explicitly linking with libssp (-lssp) and enabling stack protection no longer pulls in libssp. This brings things in line with other platforms. Thanks to [Martin Storsjö](https://github.com/mstorsjo) for implementing this in mingw-w64. Once all our affected packages are rebuilt we will remove the libssp package from our repo.

2022-10-13: We have decided to keep just the libssp DLL around for some more time to avoid breaking existing users

### 2022-09-24 - Changed behavior for empty env vars

Empty environment variables are no longer removed when starting a new non-cygwin process.

```console
$ FOO= python -c "import os; print('FOO' in os.environ)" # Old
False
$ FOO= python -c "import os; print('FOO' in os.environ)" # New
True
```

You can **revert to the old behavior** by setting `MSYS=noemptyenvvalues`. Please let us know if this is breaking anything that can't be solved by just unsetting the env var where needed.

### 2022-09-24 - ConPTY support enabled by default

ConPTY support in our cygwin fork is now enabled by default. This means any non-cygwin apps will now behave as if they are run in with a console attached and not redirected. This feature has been enabled in upstream cygwin for quite a while but we wanted to wait until there are no more known issues. We now feel that not enabling it causes more problems then enabling it.

You can **disable it again** by setting `MSYS=disable_pcon`.

### 2022-04-06 - Windows 7 / 8 support will be dropped late 2022 or early 2023

Cygwin 3.5 will drop support for Windows <8.1, which means the new requirement will be "64 bit Windows 8.1 / Windows Server 2012 R2". We expect the update to Cygwin 3.5 to be around late 2022, early 2023. For more information, look [here](https://www.msys2.org/docs/windows_support/).

A recent survey suggests that ~2-3% of our active users (excluding cloud servers and CI systems) are still using Windows <8.1. We recommend them stopping to update at the end of the year. We've enabled an inline warning message for them when they open a terminal.

For developers bundling our packages, we recommend simply pointing out the last version of their application that still worked with Windows 7 / 8 on their download page.

### 2022-03-04 - Sunsetting the SourceForge mirror in 30 days from now

*Note: This should only affect systems not updated in over a year, or users that actively switched to this mirror, which is unlikely.*

Due to space constrains and our ever growing package archive we can no longer update the [SourceForge mirror](https://sourceforge.net/projects/msys2/files/). We already hit the space limit last year but worked around it by no longer syncing source packages. We have now hit the limit again, and decided that it is no longer worth it maintaining it.

**We will remove the SourceForge mirror on 2022-04-03**. We will delete the package databases as well to make DB syncs fail to avoid users using outdated software without them knowing it. After 4 more weeks we will delete the remaining packages and installers.

**2022-05-07**: The mirror has now been removed.

### 2022-02-24 - repo.msys2.org only available via HTTPS/TLS

We have switched repo.msys2.org to always redirect to a secure connection. If
for some reason you require HTTP you can use one of our [tier 1
mirrors](./dev/mirrors.md).

### 2021-12-22 - Ongoing Cleanup of the `base-devel` Package Group

The `base-devel` package group is the set of packages required to be installed
before running `makepkg` / `makepkg-mingw`. We have recently started to clean
this group up and moved some of the packages to be explicit dependencies in the
`PKGBUILD` files instead.

One notable removal is various autotools related packages. There now exists an
`autotools` and a `${MINGW_PACKAGE_PREFIX}-autotools` meta package which will
pull in anything related to autotools which packages can add to their
`makedepends`.

Further more the group was replaced with a package of the same name, to make
adding/removing packages easier. Note that pacman prefers packages over groups
for the same name, so the set of included packages is now listed here
https://packages.msys2.org/package/base-devel

This cleanup can lead to build errors in case your build setup assumes certain
packages being installed with `base-devel`. If that is the case make sure to
install those missing packages explicitly instead.

### 2021-12-21 - Potential Incompatibilities with newer Python setuptools

**tl;dr:** use `export SETUPTOOLS_USE_DISTUTILS=stdlib` if you have problems
building/installing packages with newer versions of setuptools from pypi.

The Python packaging ecosystem is currently in the transition of removing
distutils from CPython and moving it into setuptools. Historically distutils is
patched quite a bit by us to make it work with our directory layout and to build
packages with gcc/clang instead of MSVC. With this move our patches are no
longer used and setuptools will fail in various ways, or install things into
wrong places.

We are working with upstream to include our patches, but this will take some
more time. In the meantime you can force setuptools to use the (still patched)
distutils from the CPython stdlib via `export SETUPTOOLS_USE_DISTUTILS=stdlib`
The setuptools version in our repo however will continue to use the patched
distutils until all issues are resolved and is not affected.

🙏 Many thanks to the distutils and setuptools maintainers for considering our
patches, despite Cygwin/MSYS2 not being officially supported by CPython.

### 2021-10-14 - OpenSSH 8.8 dropped support for old ssh-rsa keys using SHA-1

The recent OpenSSH update disabled support for old ssh-rsa keys using SHA-1 by
default. See https://www.openssh.com/txt/release-8.8
"Potentially-incompatible changes" for details and possible workarounds.


### 2021-07-04 - Some Mirror/Server/Repository Changes

**Primary Pacman Server**: We've switched the main server in the pacman config
to https://mirror.msys2.org. This server will redirect pacman to an up-to-date
mirror [near you](https://mirror.msys2.org/?mirrorstats) for each file. We hope
this will improve the download speed for users further away from Europe. We also
have a new overview of all mirrors [here](./dev/mirrors.md).

**Repo Path Renaming:** We've renamed `mingw/i686/` to `mingw/mingw32/` and
`mingw/x86_86/` to `mingw/mingw64/` and added symlinks for the old paths. This
means 100GB of resyncing for mirrors using rsync (sorry :/). Having the repo
name in the directory path allows us to have one mirrorlist configuration for
all repos in the future.

**Sourceforge**: Due to space constraints we no longer host the source packages
on Sourceforge. They are still available on our main server and on all mirrors.


### 2021-04-21 - R.I.P. [mingwandroid](https://github.com/mingwandroid)

Ray Donnelly is a co-founder and developer of MSYS2 and after a multi year fight
with cancer passed away on 2021-04-20.

![ray](./ray.jpg){: width=589 height=393 style="max-width: 300px; width:100%; border: 2px solid #333; box-shadow: 0px 0px 3px #ccc;" }

If you want to know more about his life and work see his fundraiser
descriptions:

* https://www.gofundme.com/f/help-Ray-fund-a-hospice-bedroom
* https://www.gofundme.com/f/arku72-help-ray-fight-cancer

He was always helpful, knowledgeable, and friendly, and he will be greatly missed.

### 2021-03-25 - Temporarily broken msys2-launcher package

The repo contained a broken msys2-launcher package for a few hours today causing things like
"msys2.exe" to just show an error dialog. You can get back to a working setup this way:

* Start `C:/msys64/msys2_shell.cmd` to get a shell
* Run `pacman -Suy` to get all the fixed packages


### 2021-02-27 - New server for repo.msys2.org and packages.msys2.org

We have moved repo.msys2.org (and package.msys2.org) to a new server.  There was
a short downtime, but everything should be running great now.  Big thanks to
~~appfleet.com~~ jsdelivr.com for sponsoring the new server.

New mirrorlists for Pacman will be published soon.  After you get them, your
package installs and updates should be faster than before and without the
404s and glitches.

With the migration, Christoph (@lazka) will now be updating and signing
the Pacman databases more often.  This should go smoothly as the GPG keys are
already in place and the process has been tested on the new server before it
went live.

By the way, the redirect domain msys2.org (no www.) should work more
reliably now and HTTPS is now available for it.


### 2021-01-31 - ASLR enabled by default

About 5 months ago we started backporting patches to our binutils
2.35 to allow enabling ASLR support via various flags. We also enabled these
flags in our build system, so any package in our repo that was updated in the
last 5 months has ASLR support enabled.

We've now updated to 2.36 which has ASLR enabled by default. Ideally you
shouldn't notice any changes, but in case this leads to problems all of it can
be disabled/reverted via linker flags:

* mingw64: `-Wl,--disable-dynamicbase,--disable-high-entropy-va,--default-image-base-low`
* mingw32: `-Wl,--disable-dynamicbase`

Note that this is only a temporary workaround and some of these flags will not
be available forever, so you should either fix your code or file a bug in case
you suspect a toolchain issue.

Thanks to the binutils developers for improving/fixing ASLR support and to
everyone helping on the MSYS2 side of things, especially [Jeremy
Drake](https://github.com/jeremyd2019) for backporting, upstreaming and fixing
bugs exposed by these changes.

**Known issues:**

* (Fixed now) ~~In case you are seeing errors such as `relocation truncated to fit:
  IMAGE_REL_AMD64_REL32 against undefined symbol` try building with
  `-Wl,--default-image-base-low`. Here is the upstream bug report:
  https://sourceware.org/bugzilla/show_bug.cgi?id=26659~~


### 2020-12-26 - Zstd exemption for core packages removed

Given it's been months since we began the switch to Zstd for compressing
packages, we've now started using it for core packages as well.  This means
older installations without Zstd support won't be able to cleanly upgrade
anymore.

@dmn-star compiled these commands that should update an older installation to
support Zstd and unblock futher upgrades:

```
pacman --noconfirm -U "https://repo.msys2.org/msys/x86_64/libzstd-1.4.4-2-x86_64.pkg.tar.xz"
pacman --noconfirm -U "https://repo.msys2.org/msys/x86_64/zstd-1.4.4-2-x86_64.pkg.tar.xz"
pacman --noconfirm -U "https://repo.msys2.org/msys/x86_64/pacman-5.2.1-6-x86_64.pkg.tar.xz"
```


### 2020-10-08 - main repo pruned

Due to limited space on the new server and SourceForge file hosting, we are
starting to remove older unused packages from the archives.  There should still
be a 1 year's worth of packages available for downgrades.  Mirrors are free to
choose whether they want to keep everything or follow the lead.


### 2020-10-07 - server downtime

From Friday 2nd to Wednesday 10th, the main hosting at repo.msys2.org was down.
The server unfortunately completely died and the hosting had to be moved
elsewhere.  We thank Diablo-D3 for having provided the hardware and hosting.  If
you notice anything wrong with repo.msys2.org since the move, please tell us.


### 2020-06-29 - new packagers

Alexey is stepping down from his role as the main packager and two new packagers
have been appointed in his place:

- David Macek with [signing key 0x9078f532](https://keyserver.ubuntu.com/pks/lookup?search=0x87771331B3F1FF5263856A6D974C8BE49078F532&fingerprint=on&op=vindex)
- Christoph Reiter with [signing key 0xa0aa7f57](https://keyserver.ubuntu.com/pks/lookup?search=0x5F944B027F7FE2091985AA2EFA11531AA0AA7F57&fingerprint=on&op=vindex)

You can see the keys in full without relying on keyservers in the [msys2-keyring
GitHub repository](https://github.com/msys2/MSYS2-keyring/).

We have released a new *msys2-keyring* package from that source (and a new
installer that includes them) and we are waiting for a bit before uploading new
databases and packages to give people time to update.  If you don't update the
keyring in time, you'll see something like this:

```
:: Synchronizing package databases...
downloading mingw32.db...
downloading mingw32.db.sig...
error: mingw32: key "4A6129F4E4B84AE46ED7F635628F528CF3053E04" is unknown
:: Import PGP key 4096R/87771331B3F1FF5263856A6D974C8BE49078F532, "David Macek <david.macek.0@gmail.com>", created: 2018-01-14? [Y/n]
error: mingw32: signature from "David Macek <david.macek.0@gmail.com>" is marginal trust
error: failed to update mingw32 (invalid or corrupted database (PGP signature))

downloading mingw64.db...
downloading mingw64.db.sig...
error: mingw64: signature from "David Macek <david.macek.0@gmail.com>" is marginal trust
error: failed to update mingw64 (invalid or corrupted database (PGP signature))

downloading msys.db...
downloading msys.db.sig...
error: msys: signature from "David Macek <david.macek.0@gmail.com>" is marginal trust
error: failed to update msys (invalid or corrupted database (PGP signature))
error: failed to synchronize all databases

error: mingw32: signature from "David Macek <david.macek.0@gmail.com>" is marginal trust
error: mingw64: signature from "David Macek <david.macek.0@gmail.com>" is marginal trust
error: msys: signature from "David Macek <david.macek.0@gmail.com>" is marginal trust
```

We have prepared the following steps to verify and install the new keyring
manually after which you should be able to use `pacman -Syu` again:

```
$ curl -O https://repo.msys2.org/msys/x86_64/msys2-keyring-r21.b39fb11-1-any.pkg.tar.xz
$ curl -O https://repo.msys2.org/msys/x86_64/msys2-keyring-r21.b39fb11-1-any.pkg.tar.xz.sig

$ pacman-key --verify msys2-keyring-r21.b39fb11-1-any.pkg.tar.xz.sig
==> Checking msys2-keyring-r21.b39fb11-1-any.pkg.tar.xz.sig... (detached)
gpg: Signature made Mon Jun 29 07:36:14 2020 CEST
gpg:                using DSA key AD351C50AE085775EB59333B5F92EFC1A47D45A1
gpg: Good signature from "Alexey Pavlov (Alexpux) <alexpux@gmail.com>" [full]

# pacman -U msys2-keyring-r21.b39fb11-1-any.pkg.tar.xz
```

If you can't even import the key and the above command fails like this:

```
error: msys: key "4A6129F4E4B84AE46ED7F635628F528CF3053E04" is unknown
:: Import PGP key 4A6129F4E4B84AE46ED7F635628F528CF3053E04? [Y/n]
[...]
error: database 'msys' is not valid (invalid or corrupted database (PGP signature))
loading packages...
error: failed to prepare transaction (invalid or corrupted database)
```

... you have to convince pacman to not care about those databases for a while,
for example like this:

```
# pacman -U --config <(echo) msys2-keyring-r21.b39fb11-1-any.pkg.tar.xz
```

If you still see signature errors, resetting your pacman key store might help:

```
# rm -r /etc/pacman.d/gnupg/
# pacman-key --init
# pacman-key --populate msys2
```


### 2020-06-15 - New `base` metapackage; `pacman-contrib` is now separate

Following a similar change in Arch Linux, the `base` group was replaced with
a `base` metapackage.  If you installed your MSYS2 using an installer older than
2020-06-02, please run `pacman -S base` to get up to date.

This also installs the `pacman-contrib` package where `updpkgsums`, `pactree`
etc. now live (previously included in the `pacman` package).

Details at [#1979](https://github.com/msys2/MSYS2-packages/pull/1979),
[#1976](https://github.com/msys2/MSYS2-packages/issues/1976) and
[#1988](https://github.com/msys2/MSYS2-packages/pull/1988).


### 2020-05-31 - Update may fail with "could not open file"

In case your update process errors out with something similar to

> error: could not open file /var/cache/pacman/pkg/zstd-1.4.5-1-x86_64.pkg.tar.zst: Child process exited with status 127

update pacman separately first:

```
pacman -Sydd pacman
```

This issue is caused by a pacman version that is too old and can't handle newer
packages compressed with zstd. In case you are seeing this problem in CI
consider using a newer base which contains a newer pacman which supports zstd:
https://github.com/msys2/msys2-installer/releases


### 2020-05-22 - MSYS2 may fail to start after a msys2-runtime upgrade

MSYS2 programs will fail to start if programs started before the update are
still running in the background (especially sshd, dirmngr, gpg-agent, bash,
pacman and mintty). You can stop them by running the following in a Windows
terminal:

```batch
taskkill /f /fi "MODULES eq msys-2.0.dll"
```

If that fails, try a reboot.

We've improved our update process so this shouldn't happen again with future
updates.


### 2020-05-22 - Pacman may fail to install packages with `Unrecognized archive format`

For a while, the core packages were prematurely packaged using zstd without
giving users time to update to zstd-enabled pacman first.  This should be
resolved now.


### 2020-05-17 - 32-bit MSYS2 no longer actively supported

32-bit mingw-w64 packages are still supported, this is about the POSIX emulation
layer, i.e. the runtime, Bash, MinTTY...

After this date, we don't plan on building updated msys-i686 packages nor
releasing i686 installers anymore.  This is due to increasingly frustrating
difficulties with limited 32-bit address space, high penetration of 64-bit
systems and Cygwin (our upstream) starting their way to drop 32-bit support as
well.


### 2019-06-03 - mingw-w64 Ada and ObjC unsupported until further notice

Pacman may say this when updating:

```
looking for conflicting packages...
error: failed to prepare transaction (could not satisfy dependencies)
:: installing mingw-w64-x86_64-gcc (9.1.0-1) breaks dependency 'mingw-w64-x86_64-gcc=8.3.0-2' required by mingw-w64-x86_64-gcc-ada
:: installing mingw-w64-x86_64-gcc (9.1.0-1) breaks dependency 'mingw-w64-x86_64-gcc=8.3.0-2' required by mingw-w64-x86_64-gcc-objc
:: installing mingw-w64-x86_64-gcc (9.1.0-1) breaks dependency 'mingw-w64-i686-gcc=8.3.0-2' required by mingw-w64-i686-gcc-ada
:: installing mingw-w64-x86_64-gcc (9.1.0-1) breaks dependency 'mingw-w64-i686-gcc=8.3.0-2' required by mingw-w64-i686-gcc-objc
```

Ada and ObjC are currently unsupported in MSYS2 builds due to long-standing
issues with the i686 variant.  Run
`pacman -R mingw-w64-x86_64-gcc-ada mingw-w64-x86_64-gcc-objc` and/or
`pacman -R mingw-w64-i686-gcc-ada mingw-w64-i686-gcc-objc`, then update.


### 2016-07-15 - Core update integrated into Pacman; `update-core` removed

The function of `update-core` is transferred to `pacman -Syuu`.


### 2016-04-05 - Command window may linger after startup

Change the argument `/K` to `/C` in all three Start menu shortcuts.

