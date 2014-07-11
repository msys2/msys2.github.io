Msys2 uses Arch's pacman as the package manager.
When creating packages for pacman we typically create a PKGBUILD script.

Typically you would have each PKGBUILD in it's own folder as it downloads sources and uses patches when building.

In msys2 there are 2 types of packages:
* **[msys2 packages](http://github.com/msys2/MSYS2-packages)** - these run in the emulation layer and are typically linux only programs
* **[mingw packages](http://github.com/msys2/MINGW-packages)** - these run natively just like any other windows program

You should think of these two systems as separate where msys2 packages should only be makedepends of mingw-packages. What this means is that you can't link a mingw program against a msys2 library.

When building out PKGBUILD scripts we have two tools available to us.
* **makepkg** - these is used to build msys2-packages
* **makepkg-mingw** - this iteration of the tool is used to build mingw packages

 
