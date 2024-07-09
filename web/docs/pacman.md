# pacman

pacman is developed at https://gitlab.archlinux.org/pacman/pacman and we
maintain a fork at https://github.com/msys2/msys2-pacman. The main difference
is support for Windows/Cygwin specifics.

Behaviour differences compared to Arch Linux pacman:

* Due to performance reasons our makepkg does not lint PKGBUILD files by
  default. This can be enabled by setting the env var `MAKEPKG_LINT_PKGBUILD=1`
* When pacman asks for confirmation to remove a package, it will always default
  to "yes", instead of "no" like on Arch Linux. This allows the `--noconfirm`
  option to be used to continue without user interaction, similar to `--yes`
  with `apt-get` (upstream issue: https://bugs.archlinux.org/task/32886)
