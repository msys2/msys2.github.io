Original answer: http://stackoverflow.com/a/21389480/2419207

---

Based on information found in ..:

- https://ghc.haskell.org/trac/ghc/wiki/Building/Preparation/Windows/MSYS2
- https://wiki.archlinux.org/index.php/pacman

.. I created huge zip file containing most of 32-bit packages and libraries.

---

From:
https://github.com/iljau/msys2_zip/releases/tag/v0.3

1. Download: https://github.com/iljau/msys2_zip/releases/download/v0.3/msys32.exe
2. Let it run.
3. Launch `mingw32_shell.bat`

```
$ clang++ --version
clang version 3.4 (tags/RELEASE_34/final)
Target: i686-w64-mingw32
Thread model: posix
```
    
I got my [`hello_world.cpp`](https://en.wikibooks.org/wiki/C%2B%2B_Programming/Examples/Hello_world#Hello_World_-_Writing.2C_Compiling_and_Running_a_C.2B.2B_Program) compiled. It didn't print anything, though. ;-D

But good for a start.

---

*References*:
- https://ghc.haskell.org/trac/ghc/wiki/Building/Preparation/Windows/MSYS2
- http://sourceforge.net/projects/s-zipsfxbuilder/
- https://github.com/bliker/cmder
- https://github.com/cbucher/console
- https://github.com/bmatzelle/gow
- https://github.com/fish-shell/fish-shell/issues/810
- https://github.com/fish-shell/fish-shell/issues/319
- http://sourceforge.net/mailarchive/message.php?msg_id=30882322
- https://github.com/kripken/emscripten/issues/2029
- http://cygwin.1069669.n5.nabble.com/Cygwin-installer-could-be-much-more-better-td105775.html
