# Updating MSYS2

After you have installed MSYS2 via the installer or other means, you need to continue updating it with the built-in `pacman` tool. MSYS2 is a [rolling release](https://en.wikipedia.org/wiki/Rolling_release) distribution and only supports full system upgrades, which means there are frequent minor and major updates to various packages and you can only update all packages at once.

To update all packages run the following command:

```console
$ pacman -Suy
:: Synchronizing package databases...
 mingw32 is up to date
 mingw64 is up to date
 ucrt64 is up to date
 clang32 is up to date
 clang64 is up to date
 msys is up to date
:: Starting core system upgrade...
 there is nothing to do
:: Starting full system upgrade...
 there is nothing to do
```

In some cases, certain core packages will get updated and pacman will prompt you to close all terminals:

```console
:: To complete this update all MSYS2 processes including this terminal will be closed.
   Confirm to proceed [Y/n]
```

After confirming you need to start a new terminal and run the update again (`pacman -Suy`) to update the remaining non-core packages.

## Pruning the package cache

`pacman` keeps all packages it downloads under `/var/cache/pacman/pkg/`. To free up some space by removing old packages run:

```console
$ paccache -r
==> finished: 5 packages removed (disk space saved: 49.05 MiB)
```

## Managing configuration file backups

When you have modified a global configuration file of a package (under `/etc` for example) and the package is about to be removed or updated then pacman will avoid deleting your changes. The `pacdiff` tool can then be used to merge your configuration file with the default state again.

1) In case a new package version with some changed configuration gets installed, which would discard your changes, pacman will leave the existing file alone and create a `<filename>.pacnew` with the new configuration instead:

```console
warning: /etc/myconfig.conf installed as /etc/pacman.d/myconfig.conf.pacnew
```

You can run `pacdiff` which searches for such `.pacnew` files and will ask you how it should deal with them:

```console
$ pacdiff
==> pacnew file found for /etc/myconfig.conf
:: (V)iew, (M)erge, (S)kip, (R)emove pacnew, (O)verwrite with pacnew, (Q)uit: [v/m/s/r/o/q]
```

2) In case the configuration file is part of a package which gets uninstalled it will save a copy as `<filename>.pacsave` instead of deleting it:

```console
warning: /etc/myconfig.conf saved as /etc/myconfig.conf.pacsave
```

If you later on install the package again you can run `pacdiff` to restore your original changes:

```console
$ pacdiff
==> pacsave file found for /etc/myconfig.conf
:: (V)iew, (M)erge, (S)kip, (R)emove pacsave, (O)verwrite with pacsave, (Q)uit: [v/m/s/r/o/q]
```
