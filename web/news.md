---
title: News
summary: Important events happening.
---
# News

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

