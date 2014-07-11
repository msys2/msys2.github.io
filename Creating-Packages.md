Msys2 uses Arch's pacman as the package manager.
When creating packages for pacman we typically create a PKGBUILD script.

Typically you would have each PKGBUILD in it's own folder as it downloads sources and uses patches when building.

Listed here are the types of packages and examples are in the respective repos

In msys2 there are 2 types of packages:
* **[msys2 packages](http://github.com/msys2/MSYS2-packages)** - these run in the emulation layer and are typically linux only programs
* **[mingw packages](http://github.com/msys2/MINGW-packages)** - these run natively just like any other windows program