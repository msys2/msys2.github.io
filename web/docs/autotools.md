# Autotools

MSYS2 ships with multiple versions of autotools related tools such as autoconf and automake. To make things easier for developers we provide meta packages which depend on all the usual packages needed to re-configure an autotools based project:

```bash
pacman -S "${MINGW_PACKAGE_PREFIX}-autotools" # for mingw
pacman -S autotools # for msys
```

Since some projects depend on specific versions of automake and, in some cases, autoconf, we provide two wrappers which dynamically provide different versions using the same script:

### automake wrapper

By default the [automake wrapper](https://packages.msys2.org/package/automake-wrapper) will detect the version to use based on existing generated files and things will just work. If there are no generated files, or if the detected version isn't available it will fall back to the newest available version. You can also force a different version via the `WANT_AUTOMAKE` env var, and the newest available version via `WANT_AUTOMAKE=latest`.

```shell
WANT_AUTOMAKE='1.15' autoreconf -fvi
```

### autoconf wrapper

By default the [autoconf wrapper](https://packages.msys2.org/package/autoconf-wrapper) will detect the version to use based on existing generated files and things will just work. If there are no generated files, or if the detected version isn't available it will fall back to the newest available version. You can also force a different version via the `WANT_AUTOCONF` env var, and the newest available version via `WANT_AUTOCONF=latest`.

```bash
WANT_AUTOCONF='2.69' autoreconf -fvi
```

These wrappers are developed by [Gentoo Linux](https://devmanual.gentoo.org/general-concepts/autotools/index.html) and are also used in Cygwin.

### Known Issues

Some projects require their configure scripts to be updated to make them build successfully:

```console
$ pacman -S "${MINGW_PACKAGE_PREFIX}-autotools"
$ autoreconf -fvi
$ ./configure
$ make
...
```

This is due to some MSYS2 specific patches that have not been upstreamed yet or have not made it into upstream projects.
