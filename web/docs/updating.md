# Updating MSYS2

After you have installed MSYS2 via the installer or other means, you need to
continue updating it with the built-in `pacman` tool. MSYS2 is a [rolling
release](https://en.wikipedia.org/wiki/Rolling_release) distribution and only
supports full system upgrades, which means there are frequent minor and major
updates to various packages and you can only update all packages at once.

To update all packages you should run the following command:

```shell
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

```shell
:: To complete this update all MSYS2 processes including this terminal will be closed. Confirm to proceed [Y/n]
```

After confirming you need to start a new terminal and run the update (`pacman -Suy`) again to update the remaining non-core packages.

## Cleaning the package cache

`pacman` keeps all packages it downloads under `/var/cache/pacman/pkg/`. To free up some space by removing old packages run:

```shell
$ paccache -r
==> finished: 5 packages removed (disk space saved: 49.05 MiB)
```

## Configuration file backups during updates

When you have modified a global configuration file of a package (under `/etc` for example) and the content of the file would changed due to an update or the package being remove then pacman will create a backup of the changed file instead of discarding your changes. If you don't change any global configuration files then you can ignore this section.

1) In case a new package version gets installed which changes the file content, then pacman will leave the existing file alone and create a `<filename>.pacnew` instead:

```shell
warning: /etc/myconfig.conf installed as /etc/pacman.d/myconfig.conf.pacnew
```

You can run `pacdiff` which searches for such `.pacnew` files and will ask you how to deal with them:

```shell
$ pacdiff
==> pacnew file found for /etc/myconfig.conf
:: (V)iew, (M)erge, (S)kip, (R)emove pacnew, (O)verwrite with pacnew, (Q)uit: [v/m/s/r/o/q]
```

2) In case the package which owns the config file you changed gets uninstalled it will save a copy as `<filename>.pacsave`:

```shell
warning: /etc/myconfig.conf saved as /etc/myconfig.conf.pacsave
```

If you install the package again you can run `pacdiff` to restore/merge your original changes:

```shell
$ pacdiff
==> pacsave file found for /etc/myconfig.conf
:: (V)iew, (M)erge, (S)kip, (R)emove pacsave, (O)verwrite with pacsave, (Q)uit: [v/m/s/r/o/q]
```
