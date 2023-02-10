---
summary: Important events happening.
---
# News

This page lists important changes or issues affecting MSYS2 users. We also post them to [Twitter](https://twitter.com/msys2org) and [Mastodon](https://fosstodon.org/@msys2org), including some not-so-important things :)

### 2023-02-10 - Server maintenance on 2023-02-18/19

There will be a short server maintenance around the weekend of 2023-02-18/19 which will affect repo.msys2.org, mirror.msys2.org, packages.msys2.org, and some subdomain redirects of our website.

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

* https://uk.gofundme.com/f/help-Ray-fund-a-hospice-bedroom
* https://uk.gofundme.com/f/arku72-help-ray-fight-cancer

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

- David Macek with [signing key 0x9078f532](http://keys.gnupg.net/pks/lookup?search=0x87771331B3F1FF5263856A6D974C8BE49078F532&fingerprint=on&op=vindex)
- Christoph Reiter with [signing key 0xa0aa7f57](http://keys.gnupg.net/pks/lookup?search=0x5F944B027F7FE2091985AA2EFA11531AA0AA7F57&fingerprint=on&op=vindex)

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


### 2016 - Core update integrated into Pacman; `update-core` removed

The function of `update-core` is transferred to `pacman -Syuu`.


### 2016 - Command window may linger after startup

Change the argument `/K` to `/C` in all three Start menu shortcuts.

