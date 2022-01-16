# Package Naming

|                                                          | Package prefix             |
|----------------------------------------------------------|----------------------------|
| ![msys](msys.png){: style="max-width:25px" }             | None                       |
| ![mingw64](mingw64.png){: style="max-width:25px" }       | `mingw-w64-x86_64-`        |
| ![ucrt64](ucrt64.png){: style="max-width:25px" }         | `mingw-w64-ucrt-x86_64-`   |
| ![clang64](clang64.png){: style="max-width:25px" }       | `mingw-w64-clang-x86_64-`  |
| ![mingw32](mingw32.png){: style="max-width:25px" }       | `mingw-w64-i686-`          |
| ![clang32](clang32.png){: style="max-width:25px" }       | `mingw-w64-clang-i686-`    |
| ![clangarm64](clangarm64.png){: style="max-width:25px" } | `mingw-w64-clang-aarch64-` |

### Avoiding writing long package names

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