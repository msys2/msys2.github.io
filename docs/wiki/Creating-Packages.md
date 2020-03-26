The MSYS2 software distribution uses a port of Pacman (known from Arch Linux) to safely install, remove and update binary packages and also to build those packages in the first place.

## General information

There are 3 package repositories, **msys**, **mingw32**, and **mingw64**. **msys** software (from the **msys** repository) is software that depends on `msys-2.0.dll` and is very similar to Cygwin software (which is a POSIX emulation layer for Windows). Native Windows software (from this project's perspective) is software that doesn't depend on `msys-2.0.dll`, and links dynamically to the highly compatible `msvcrt.dll`.

In this document, to attempt to avoid confusion, MSYS2 refers to the software distribution while **msys** refers to the repository, the packages in that repository and the software in those packages that link to `msys-2.0.dll`.

### Package recipes

Packages are built from programmatic recipes to ensure builds are reproducible. A recipe is a set of files which describe how to build, package and install a given piece of software; these are often specific to MSYS2.

In the simplest form it is a single file named `PKGBUILD`, which contains metadata for the package, a specification where the source for the given software can be found, and a few lines of code which that takes the source and builds the final software from it. For more complex cases it also contains install scripts or a number of patch files which are needed to be applied on the released version of the upstream software in order to be able to compile and work in the given environment.

Typically, each recipe is in its own directory. The directory is also used when building as a working place by default.

### PKGBUILD

Use 2 spaces for indentation: `expand -t 2 PKGBUILD > PKGBUILD.new && mv PKGBUILD.new PKGBUILD`

A PKGBUILD is a bash script defining variables and functions that are then used by the build system to create the package. The [PKGBUILD manpage](https://www.archlinux.org/pacman/PKGBUILD.5.html) and the [PKGBUILD wikipage on ArchWiki](https://wiki.archlinux.org/index.php/PKGBUILD) are good sources to read about all the details of PKGBUILDs. The **mingw** PKGBUILDs are loosely based on the [mingw-w64 cross-compilation packages guidelines in Arch Linux](https://wiki.archlinux.org/index.php/MinGW_package_guidelines). If you don't want to read all that just yet, just read some existing PKGBUILDs; the purpose of most parts should be obvious.

### Patch files

When creating a patch file, you can use the following naming convention for its name: `###-target-Purpose.patch`

Where

* `###` a sequence number, starting from 001
* `target`, is the package name and version (separated by a hyphen) for which the patch was first created
* `[Purpose]` describes what the patch is fixing or improving

### Building

The actual build and packaging is done by running `makepkg` or `makepkg-mingw`. The former is used to build **msys** packages and the latter for **mingw** packages. To learn more, read the [makepkg manpage](https://www.archlinux.org/pacman/makepkg.8.html) and the [makepkg wikipage on ArchWiki](https://wiki.archlinux.org/index.php/makepkg). When building *either* **msys** or native software, you should use the MSYS shell, not the MINGW{32,64} shells.

The process happens in multiple phases:

* download, verify and extract - the package sources are downloaded if necessary, checked against checksums and PGP signatures if specified, and extracted into a working directory (`src` by default)
* `prepare()` - using this function, the packager can specify what should happen with the sources before the actual build; apply patches and source modifications here
* `build()` - this function contains commands to run the build tool(s), e.g. `./configure` and `make`
* `check()` - an optional step to check the build products by e.g. running the software's test suite
* `package()` - this function is provided with a temporary directory, where it should put the final contents of the package using e.g. `make install`
* tidy, archive and sign - the package contents are scanned for some issues, tidied up and packaged into the final `.tar.xz` with an optional signature in `.tar.xz.sig`

The makepkg tool takes arguments allowing you to turn off some phases or some checks. The typical usage is `makepkg -sCLf` for a full build and `makepkg -RdLf` for a "re-package". Re-packaging is useful when the process failed in `package()` and you don't want to run the long build part again. `makepkg-mingw` takes the same arguments.

## Re-building a package

To get you started, you can try just re-building an existing package. This may also be helpful if you need to diagnose an issue and need the debugging symbols.

An example of fetching the **msys** repository source, building and then installing a package from it is:

    git clone "https://github.com/Alexpux/MSYS2-packages"
    cd MSYS2-packages/flex
    makepkg -sCLf
    pacman -U flex-*.pkg.tar.xz

An example of fetching the **mingw** repository source, building and then installing a package from it is:

    git clone "https://github.com/Alexpux/MINGW-packages"
    cd MINGW-packages/mingw-w64-python3
    makepkg-mingw -sCLf
    pacman -U mingw-w64-*-python3-*-any.pkg.tar.xz

## A new package from start to finish

Please do *not* create pull requests for PKGBUILDs that just repackage binary releases from other projects. This is contrary to the goals of MSYS2. If the software cannot be built for some reason then try to fix the cause of that.

1. Decide which subsystem to target (**msys** or **mingw**)
2. Build the software in the target subsystem
3. Test the functionality
4. Create patches if necessary and repeat
5. Prepare a recipe
6. Build the package
7. Install the package locally
8. Test the installed package
9. Modify the recipe if necessary and repeat
10. Commit the new package to the target repository (on your own GitHub account)
11. Send a pull request to merge the new recipe into the official repository
12. Check CI results, reviews and comments
13. Fix issues if necessary and repeat
14. Offer your fixes to the software's developers (upstream)

The steps above describe an intuitive process of going from the idea of creating a package to making it available to you and others using `pacman`. You can of course customize the process to suit you and your situation.

Once you are familiar with the process, we recommend creating recipes and using `makepkg` straight away for all packages. It's a great way to record your build steps in a reproducible way, which is not only useful for you, but also for other people when asked for help with the builds.

### Which subsystem?

In MSYS2 there are 2 types of packages:
* **msys packages** - these run on the emulation layer and are typically POSIX-only programs
* **mingw packages** - these run natively just like any other Windows program

You should think of these two systems as separate where **msys** packages should generally only be build dependencies of **mingw** packages. You also can't link a **mingw** program against an **msys** library.

This means you first need to decide which subsystem (and which repository) is the right one for your new package. The set of things that belong to the **msys** subsystem is pretty small:

- essential POSIX stuff: `filesystem`, `msys2-runtime`, ...
- the native toolchain: `gcc`, `binutils`, `gdb`, ...
- supporting programs that are hard to port to Windows: `pacman`, `bash`, `automake`, `make`, ...
- programs for bridging the gap: `mintty`, `winpty`, ...
- supporting programs, even though they're portable: `python`, `man`, `vim`, `git`, ...
- carefully chosen useful tools: `mc`, `ssh`, `rsync`, `lftp`, ...
- dependencies of these packages

In other words, if a program is needed to build native software, but is itself hard to port, it can be made into an **msys** package. Anything else needs to be done as a **mingw** package or vetted individually.

### Build software

In order to be able to compile a software or build a package you need to install basic packages, as the MSYS2 install does not contain build tools.

The core packages groups you need to install if you wish to build from PKGBUILDs are:

- `base-devel` for any building
- `msys2-devel` for building **msys** packages
- `mingw-w64-i686-toolchain` for building **mingw32** packages
- `mingw-w64-x86_64-toolchain` for building **mingw64** packages

If you don't install the required package group, building might fail with unexpected errors. Note that -- contrary to what you might expect -- `base-devel` doesn't contain `gcc` nor `binutils`.

### Test software

Check that the software does what it should. Try its test suite.

### Patch software

If the software doesn't work straight away or doesn't even build, you'll probably need to pass some arguments to the build scripts or modify (patch) its build system, its source code, its definitions files etc. Such patches will be stored as files alongside the PKGBUILD.

This part is very specific to each software and may require searching the Internet, talking to the software's developers or support team, talking to us etc. The [Porting wikipage](Porting.md) may help with some common issues. While it is probably okay to make quick (monkey-)patches that fix the software for our use case (and possibly break it for every other), is it better to make proper surgical-precision patches and attempt to have them accepted by the software developer ("upstream").

### Recipe

Create a `PKGBUILD` describing all the steps necessary to build and package the software, including any patches or additional files. Make sure the follow the style and ideas of other recipes if applicable. A good strategy is to find some existing working recipes that use the same build system as your software does and use them as a template for your recipe. You can also take inspiration from an official Arch Linux (or unofficial AUR) recipe for your software.

### Build package

Run the makepkg command (`makepkg` or `makepkg-mingw`) on your recipe.

`makepkg-mingw` is essentially a wrapper that does a few checks, sets up the correct environments and runs `makepkg` twice, once for **mingw32** and once for **mingw64**. If you want to build just for one architecture (e.g. if you're on 32-bit Windows), you'll need to define `MINGW_INSTALLS` in the environment, with either `mingw32` or `mingw64` as the value, for example:

    MINGW_INSTALLS=mingw32 makepkg-mingw -sCLf

... or you could export it from `~/.profile` so it's set up automatically:

    export MINGW_INSTALLS=mingw32

Note that if you want to contribute, we'd appreciate it if you test your packages on both architectures (32 and 64 bits), which is only possible on a 64-bit Windows system. If you can't do that for some reason, we can test your pull requests on a 64-bit system.

### Install package

If the package build successfully, it's good to check its contents first before installing to see if it contains what you intended. When installing (using `pacman -U pkgname-pkgver-arch.tar.xz`), pacman checks for any filesystem conflicts and then places the package contents into your MSYS2 root as it would do with any other package. You can also remove the package using `pacman -R pkgname`.

### Test package

Make sure the package installed all the files which it's supposed to distribute: executables, shared and static libraries, configuration files, header files, licenses, documentation etc.

Pay special attention to the configuration files and make sure they are not containing hard-coded path elements and are pointing to the right location. Typical config files:

* `*-config` files in the `${prefix}/bin` directory
* `*.pc` files for `pkg-config` in the `${prefix}/lib/pkgconfig` directory
* `*.cmake` files in the `${prefix}/lib/cmake` directory

Verify that the package works even if installed into a clean updated MSYS2 installation, preferably not in the default `C:\msys{32,64}` location (and maybe even temporarily rename your primary MSYS2 installation root). This checks that you specified the runtime dependencies correctly and that the software doesn't try to use hard-coded paths from your build.

### Modify package

If there are issues, fix them in your PKGBUILD and re-build or re-package as necessary. Make sure you're not using stale build products or source files from a previous build (use the `-C` flag for makepkg).

### Commit

Integrate your recipe into your local clone of the **msys2-packages** or **mingw-packages** repository. In order to help us avoid accumulating useless commits in the repository, please follow these guidelines:

- create a new branch for your work
- put all your work into it, preferably in just 1 commit
- if you want to pull changes from our repository, use the rebasing strategy (`git pull --rebase`) to place your commits above ours, do not just merge
- if you need to change something in your recipe, amend your existing commit (`git commit --amend`)
- push your new branch onto your repository "fork" on your GitHub account, using `git push --force-with-lease` if necessary

Although these guidelines (which rely heavily on rewriting history) are not suitable for public development on main branches (`master` etc.), they're an excellent match for this kind the iterative work-in-progress development that happens when contributing new packages.

### Send PR

Open and send a pull request against the master branch of the official repositories on GitHub ([links here](https://github.com/msys2/msys2)). Please include a short description of what you're submitting and why. In case your recipe is not final yet, add "[do not merge]" to the title and explain in the description.

### Check

Our CI systems will automatically try to build your package. If it fails, try to figure out why. However, the CI systems are not perfect and unfortunately may fail even if your package is fine.

The project maintainers will try to look at your PR and review it. This may take some time and sometimes happens in bursts, so don't be discouraged if you get no response for a few days, but don't be afraid to explicitly ask for help or a review on our IRC channel.

### Fix

If there are any issues pointed out, try to fix them and update your pull request. GitHub will automatically refresh the pull request when you push to your branch, there is no need to create a new PR. After pushing, add a comment to the PR to notify the reviewers.

If there are no issues with the package, it will be merged. Please note that this doesn't make the package immediately available through pacman. The binary repositories are updated in bursts.

### Upstream

In case you had to made changes in order to be able to compile and run properly (and hence created patches), please make an effort to submit proper patches and PRs to the upstream project so that the patches can be removed from our repositories and can be of use to other Windows developers.

## Resources

Read through our wiki, especially about [pacman](Using-packages.md) and the [Porting section](Porting.md).

### Useful packages and tools

Package                                | Purpose
---------------------------------------|------------------------------------------------------------
`mingw-w64-{i686,x86_64}-qt-creator`   | to build/debug qmake, qbs, autotools and cmake based packages
`mingw-w64-{i686,x86_64}-codelite-git` | if you dislike qt-creator
`mingw-w64-{i686,x86_64}-gedit`        | to avoid notepad and notepad++
`mingw-w64-{i686,x86_64}-meld3`        | to compare files and directories
`perl-ack`                             | Faster, better replacement for `grep`
`mingw-w64-{i686,x86_64}-ag`           | Very fast replacement for `grep` or `perl-ack`

### Various links

- [bash on ArchWiki](https://wiki.archlinux.org/index.php/bash)
