# Tips and Tricks

A list of useful small guides related to package management. See lots more on the [Arch
Linux wiki](https://wiki.archlinux.org/title/Pacman/Tips_and_tricks).


### Show the license information of a package

To list the license of an installed package you can run:

```bash
$ pacman -Qi meson | grep '^Licenses'
Licenses        : Apache 2
```

To list the license of a package in the sync database you can run:

```bash
$ pacman -Si meson | grep '^Licenses'
Licenses        : Apache 2
```

For the exact meaning of the license string see [License Metadata](../dev/package-licensing.md).

To list all license files installed by a package in the recommended location:

```bash
$ pacman -Ql meson | grep -E "/share/licenses/.+/.+"
meson /usr/share/licenses/meson/COPYING
```

Note that not every package includes the license text as a file, nor puts it
in this specific recommended location.


### Listing the content of a package

If you would like to know what has been installed as a part of a specific package use the following command:

`pacman -Ql <name of the package>`

Example:

`$ pacman -Ql mingw-w64-x86_64-pugixml`

```
mingw-w64-x86_64-pugixml /mingw64/
mingw-w64-x86_64-pugixml /mingw64/bin/
mingw-w64-x86_64-pugixml /mingw64/bin/libpugixml.dll
mingw-w64-x86_64-pugixml /mingw64/include/
mingw-w64-x86_64-pugixml /mingw64/include/pugixml-1.8/
mingw-w64-x86_64-pugixml /mingw64/include/pugixml-1.8/pugiconfig.hpp
mingw-w64-x86_64-pugixml /mingw64/include/pugixml-1.8/pugixml.hpp
mingw-w64-x86_64-pugixml /mingw64/lib/
mingw-w64-x86_64-pugixml /mingw64/lib/cmake/
mingw-w64-x86_64-pugixml /mingw64/lib/cmake/pugixml/
mingw-w64-x86_64-pugixml /mingw64/lib/cmake/pugixml/pugixml-config-noconfig.cmake
mingw-w64-x86_64-pugixml /mingw64/lib/cmake/pugixml/pugixml-config.cmake
mingw-w64-x86_64-pugixml /mingw64/lib/pkgconfig/
mingw-w64-x86_64-pugixml /mingw64/lib/pkgconfig/pugixml.pc
mingw-w64-x86_64-pugixml /mingw64/lib/pugixml-1.8/
mingw-w64-x86_64-pugixml /mingw64/lib/pugixml-1.8/libpugixml.dll.a
```

As you can see the package contains:

* a binary executable library file (libpugixml.dll),
* a static library (libpugixml.dll.a),
* 2 header files (pugixml.hpp, pugiconfig.hpp),
* 2 cmake files,
* and a PKGCONFIG file (pugixml.pc).
