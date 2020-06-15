# News

### 2020-06-15 - `base` metapackage; separate `pacman-contrib`

Following a similar change in Arch Linux, the `base` group was replaced with
a `base` metapackage.  If you installed your MSYS2 using an installer older than
2020-06-02, please run `pacman -S base` to get up to date.

This also installs the `pacman-contrib` package where `updpkgsums`, `pactree`
etc. now live (previously included in the `pacman` package).

Details at [#1979](https://github.com/msys2/MSYS2-packages/pull/1979),
[#1976](https://github.com/msys2/MSYS2-packages/issues/1976) and
[#1988](https://github.com/msys2/MSYS2-packages/pull/1988).


### 2020-05-31 - Update fails with "could not open file"

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


### 2020-05-22 - MSYS2 fails to start after a msys2-runtime upgrade

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