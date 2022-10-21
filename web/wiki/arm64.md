# ARM64 Support

MSYS2 has preliminary ARM64/AArch64 support. [Lots of MSYS2 packages](https://packages.msys2.org/package/?repo=clangarm64) have native ARM64 builds available and you can build your own programs for ARM64 Windows. Give it a try and let us know if there are any issues.

Requirements:

* Windows 11 ARM64

Installation:

* [Download/Install MSYS2 as usual](../index.md#installation)
* Execute `clangarm64.exe` in the MSYS2 install directory
* Uncomment the `clangarm64` config in `/etc/pacman.conf`
* Run `pacman -Suy`
* Install clang for example: `pacman -S mingw-w64-clang-aarch64-clang`

## Known Issues

* Not all packages in the repo have native builds yet, let us know if any you need are missing.
* All unixy tools, like bash, will go through x64 emulation, so they might run slower than expected.
* Windows 10 ARM64 isn't supported since we require x64 emulation, which was added in Windows 11. The MinGW packages and anything you build yourself should support Windows 10 ARM64 though.
