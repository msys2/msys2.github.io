# Tips and Tricks

A list of useful small guides related to package management. See lots more on the [Arch
Linux wiki](https://wiki.archlinux.org/title/Pacman/Tips_and_tricks).


#### Show the license information of a package

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

