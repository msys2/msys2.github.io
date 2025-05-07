---
summary: The MSYS2 software distribution provides binary packages with for `pacman` using
    prefixes according to the target environment.
---

# Package Naming

## Overview

The following table lists the packages according to their environment, see ['Environments'](environments.md) for general information on these.
When installing packages, see  ['Package Management'](package-management.md), you'll commonly use the full name including the package prefix as outlined below.

|                                                          | Name [^1]      | Package prefix [^2]       |
|----------------------------------------------------------|----------------|---------------------------|
| ![msys](msys.png){: style="max-width:25px" }             | **MSYS**       | None                      |
| ![mingw64](mingw64.png){: style="max-width:25px" }       | **MINGW64**    | `mingw-w64-x86_64`        |
| ![ucrt64](ucrt64.png){: style="max-width:25px" }         | **UCRT64**     | `mingw-w64-ucrt-x86_64`   |
| ![clang64](clang64.png){: style="max-width:25px" }       | **CLANG64**    | `mingw-w64-clang-x86_64`  |
| ![mingw32](mingw32.png){: style="max-width:25px" }       | **MINGW32**    | `mingw-w64-i686`          |
| ![clang32](clang32.png){: style="max-width:25px" }       | **CLANG32**    | `mingw-w64-clang-i686`    |
| ![clangarm64](clangarm64.png){: style="max-width:25px" } | **CLANGARM64** | `mingw-w64-clang-aarch64` |

[^1]: environment variable `MSYSTEM` 
[^2]: environment variable `MINGW_PACKAGE_PREFIX`

## Avoiding writing long package names

Use `pacboy` to install **mingw** packages without having to type the long package names (install `pacboy` first using `pacman -S pactoys` if necessary).  Examples:

`pacboy` installs the listed packages for one or more environments. The
selection of environments for each package is controlled by appending
suffixes on the package name.

In particular, adding the `:p` suffix installs the package for the current
environment only.

If no suffix is given, the selection of environments depends on what
environment you're currently in - e.g. in a `mingw64` environment, it
currently defaults to installing the package for both `mingw32` and `mingw64`.

See the output of `pacboy help` for the list of suffixes:
```
$ pacboy help

    Pacboy 2016.6.24
    Copyright (C) 2015, 2016 Renato Silva
    Licensed under BSD

    This is a pacman wrapper for MSYS2 which handles the package prefixes
    automatically, and provides human-friendly commands for common tasks.

    Usage:
        pacboy [command] [arguments]
        Arguments will be passed to pacman after translation:

        For 64-bit MSYS2 shell:
            name:i means i686-only
            name:x means x86_64-only
            name:z means clang-i686-only
            name:c means clang-x86_64-only
            name:u means ucrt-x86_64-only
            name:a means clang-aarch64-only
            name:p means MINGW_PACKAGE_PREFIX-only

        For MSYS shell:
            name:m means mingw-w64
            name:l means mingw-w64-clang

        For all shells:
            name: disables any translation for name
            repository::name means repository/name
```

Here are examples of using the `:x`, `:i` and `:m` suffixes for installing
packages for the `mingw64`, `mingw32` and both environments:
```
$ pacboy -S x265:x
resolving dependencies...
looking for conflicting packages...

Packages (1) mingw-w64-x86_64-x265-2.3-1

Total Download Size:    0.97 MiB
Total Installed Size:  20.72 MiB

:: Proceed with installation? [Y/n]
```
```
$ pacboy -S x265:i
resolving dependencies...
looking for conflicting packages...

Packages (1) mingw-w64-i686-x265-2.3-1

Total Download Size:    0.97 MiB
Total Installed Size:  11.37 MiB

:: Proceed with installation? [Y/n]
```
```
$ pacboy -S x265:m
resolving dependencies...
looking for conflicting packages...

Packages (2) mingw-w64-i686-x265-2.3-1  mingw-w64-x86_64-x265-2.3-1

Total Download Size:    0.97 MiB
Total Installed Size:  32.09 MiB

:: Proceed with installation? [Y/n]
```
