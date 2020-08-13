# News

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
$ curl -O http://repo.msys2.org/msys/x86_64/msys2-keyring-r21.b39fb11-1-any.pkg.tar.xz
$ curl -O http://repo.msys2.org/msys/x86_64/msys2-keyring-r21.b39fb11-1-any.pkg.tar.xz.sig

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

You may need to backup a copy of `C:\msys64\usr\bin\pacman.exe` then overwrite it with `msys2-base-x86_64-20******.tar.xz/msys64/usr/bin/pacman.exe`.

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

