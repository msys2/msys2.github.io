---
title: Package Naming
summary: The MSYS2 software distribution provides binary packages with for `pacman` using
    prefixes according to the target environment.
---

## Overview

Tha following table lists the packages according to their environment, see ['Environments'](environments.md) for general information on these.
When installing packages, see  ['Package Management'](package-,anagement.md), you'll commonly use the full name including the pacakge prefix as outlined below.

|                                                          | Name [^1]      | Package prefix [^2]        |
|----------------------------------------------------------|----------------|----------------------------|
| ![msys](msys.png){: style="max-width:25px" }             | **MSYS**       | None                       |
| ![mingw64](mingw64.png){: style="max-width:25px" }       | **MINGW64**    | `mingw-w64-x86_64-`        |
| ![ucrt64](ucrt64.png){: style="max-width:25px" }         | **UCRT64**     | `mingw-w64-ucrt-x86_64-`   |
| ![clang64](clang64.png){: style="max-width:25px" }       | **CLANG64**    | `mingw-w64-clang-x86_64-`  |
| ![mingw32](mingw32.png){: style="max-width:25px" }       | **MINGW32**    | `mingw-w64-i686-`          |
| ![clang32](clang32.png){: style="max-width:25px" }       | **CLANG32**    | `mingw-w64-clang-i686-`    |
| ![clangarm64](clangarm64.png){: style="max-width:25px" } | **CLANGARM64** | `mingw-w64-clang-aarch64-` |

[^1]: environment variable `MSYSTEM` 
[^2]: environment variable `MINGW_PACKAGE_PREFIX`

## Avoiding writing long package names

Use `pacboy` to install **mingw** packages without having to type the long package names (install `pacboy` first using `pacman -S pactoys` if necessary).  Examples:

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