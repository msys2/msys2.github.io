Original answer: http://stackoverflow.com/a/21389480/2419207

---

Based on information found in ..:

- https://ghc.haskell.org/trac/ghc/wiki/Building/Preparation/Windows/MSYS2
- https://wiki.archlinux.org/index.php/pacman

.. I created huge zip file containing most of 32-bit packages and libraries.

---

From:
https://github.com/iljau/msys2_zipped/releases/tag/v0.1

1. Download: https://github.com/iljau/msys2_zipped/releases/download/v0.1/msys32.zip
2. Unzip it using [`7-Zip`](http://www.7-zip.org/) (_because at least in Windows 7 `"Extract all..."` context menu option will hang your `explorer.exe`_)
3. Launch `mingw32_shell.bat`

```
$ clang++ --version
clang version 3.4 (tags/RELEASE_34/final)
Target: i686-w64-mingw32
Thread model: posix
```
    
I got my [`hello_world.cpp`](https://en.wikibooks.org/wiki/C%2B%2B_Programming/Examples/Hello_world#Hello_World_-_Writing.2C_Compiling_and_Running_a_C.2B.2B_Program) compiled. It didn't print anything, though. ;-D

But good for a start.
