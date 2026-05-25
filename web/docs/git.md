# Git

```bash
pacman -S "$MINGW_PACKAGE_PREFIX-git"  # native Windows build of git
pacman -S git  # cygwin based git
```

## FAQ

### Why are "gitk" and "git gui" not working in the MSYS environment?

They depend on Tcl/Tk and we only provide mingw builds for those. In all environments besides MSYS they should work fine though.

### Some tool I use fails to work with the Cygwin git in MSYS2, but works fine with the official one

One common issue with external tools integrating git, is that they get confused by Unix paths, for example when figuring out the project root path via `git rev-parse --show-toplevel`. This can be worked around by using `git rev-parse --show-prefix` instead which outputs a relative path from the root to the current working directory, which is both a valid Unix and Windows path. Or `git rev-parse --show-cdup` which outputs a relative path from the current working directory to the root, which is also a valid Unix and Windows path.

If all fails you can `export GIT_DIR=/dev/null` to make git not find any repository at all, which usually makes tools skip any git related logic.


## Changelog

* 2026-02-28: We now provide a native Windows build of git:
  https://packages.msys2.org/base/mingw-w64-git. Workarounds such as
  https://gitforwindows.org/install-inside-msys2-proper are no longer necessary.
