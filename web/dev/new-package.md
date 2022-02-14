# Creating a new Package

A package consists of a package recipe in the form of a `PKGBUILD` file. See the
[PKGBUILD file for
glib](https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-glib2/PKGBUILD)
as an example. To have your package included in the official repository it has
to end up in the package git repository via a pull request →
https://github.com/msys2/MINGW-packages/pulls

## Things to consider before creating a PKGBUILD file

* Does the project you'd like to package support Windows and does it support
  other compilers than MSVC?
* Is the project you'd like to package already in the repo?
* Are all the runtime and build dependencies of that project already in the
  repo?
* Does building the project work in an MSYS2 environment?
* Is the project packaged in [Arch Linux](https://archlinux.org/packages/) or in
  the [AUR](https://aur.archlinux.org/), to help you as a reference for both the
  build process and finding a package name?

## Creating a new PKGBUILD file

Many projects are similar to build and package, so it's easiest to just copy an
existing PKGBUILD file as a starting point. You can either look for a package
with a similar build system and dependencies in our repository or use one of our
`PKGBUILD` templates:

* CMake - git: [PKGBUILD.CMake-git](https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-PKGBUILD-templates/PKGBUILD.CMake-git.sh)
* CMake - tarball: [PKGBUILD.CMake-tarball](https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-PKGBUILD-templates/PKGBUILD.CMake-tarball.sh)
* Autotools - tarball: [PKGBUILD.autotools-tarball](https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-PKGBUILD-templates/PKGBUILD.autotools-tarball.sh)
* Rust/Cargo - tarball: [PKGBUILD.cargo-tarball](https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-PKGBUILD-templates/PKGBUILD.cargo-tarball.sh)
* Meson - tarball: [PKGBUILD.meson-tarball](https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-PKGBUILD-templates/PKGBUILD.meson-tarball.sh)
* Python/Setuptools - tarball: [PKGBUILD.python-setuptools](https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-PKGBUILD-templates/PKGBUILD.python-setuptools.sh)
* Python/pyproject.toml - tarball: [PKGBUILD.python-pyproject](https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-PKGBUILD-templates/PKGBUILD.python-pyproject.sh)

After you have decided on a good starting point:

1. Decide on a package name. If the project is already packaged in Arch Linux or
   the AUR then we prefer the same name.
2. Create a directory called `mingw-w64-<package-name>`
3. Move your `PKGBUILD` file into that directory.
4. Fill out your `PKGBUILD` file
    * See https://wiki.archlinux.org/title/PKGBUILD for details on the format and
      the meaning of variables and functions.
    * See our [Package Guidelines](./package-guidelines.md) for how we expect
      `PKGBUILD` files to be structured and how they should behave.
5. Run `updpkgsums` to update the source checksums in the `PKGBUILD` file.
6. Build the package...

## Building the package

Building a package requires a base set of build related packages to be installed
first. This only needs to be done once:

```bash
pacman -S --needed base-devel
```

To build the package, start a shell in an environment you want to build for,
change the working directory to the directory of the `PKGBUILD`, and run:

```bash
makepkg-mingw --cleanbuild --syncdeps --force --noconfirm
```

This will download all required build dependencies, build your package, and will
result in a `*.pkg.tar.zst` package in the same directory, if nothing goes
wrong.

To install the package you can run:

```bash
pacman -U *.pkg.tar.zst
```

`makepkg-mingw` has various other helpful options you can add:

* `--install` - to install the built package right away
* `--rmdeps` - to remove all packages again that it installed for building
* `--help` - to see more options

## Proposing the package to be included in our official repository

Once you are pleased with your package and have tested it sufficiently you can
create a pull request against our package repository →
https://github.com/msys2/MINGW-packages/pulls

Once the PR is opened, our CI system will try to build your package in a fresh
and clean build environment and will also try to build it for all our supported
target environments (mingw64, clang64, etc).

There is a chance that this will uncover some issues in your package, such as
unspecified build dependencies, or uncover errors in projects that build with
gcc but not with clang for example. If that is the case you can try to fix the
found issues or ask us for assistance.

## Differences compared to Arch Linux

If you are already accustomed to building packages for Arch Linux, you might
notice some differences despite us using the same tools:

* Our `PKGBUILD` files use environment variables such as `MINGW_PACKAGE_PREFIX`
  and `MINGW_PREFIX` in various places so they can be used to build packages for
  difference environments using the same `PKGBUILD` file.
* We use `makepkg-mingw` instead of `makepkg`. `makepkg-mingw` is just a small
  wrapper around `makepkg` which sets up the right environment and also allows
  building the same package multiple times for different environments in one go.
