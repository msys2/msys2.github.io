When creating packages for msys2 we create a script called PKGBUILD and run it through the bash program makepkg.
Typically you would have each PKGBUILD in it's own folder as it downloads sources and uses patches when building.

In msys2 there are 2 types of packages
* msys2 packages - these run in the emulation layer and are typically linux only programs
* mingw packages - these are native mingw-w64 packages that create native programs for windows