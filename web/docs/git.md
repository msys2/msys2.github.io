# Git

We currently only provide a [cygwin based git](https://packages.msys2.org/base/git), which only understands and outputs Unix paths and thus behaves slightly differently compared to ["Git for Windows"](https://gitforwindows.org/). It also is quite a bit slower, which is especially noticeable on larger repositories.

```bash
pacman -S git
```

## FAQ

### Why is there no MinGW based Git in MSYS2 despite "Git for Windows" being based on MSYS2?

The [git-for-windows](https://github.com/git-for-windows) project maintains various patches on top of git itself as well as patches various MSYS2 packages to get the git test suite to pass on Windows and provide a complete and bug-free git experience. Our long term goal is to include their git build, but no one has started working on this yet.

There exists a guide to install the official build into MSYS2: https://github.com/git-for-windows/git/wiki/Install-inside-MSYS2-proper but note that this setup is only supported on a best effort basis and any issues should be verified with the official git build before reporting them upstream.

### Why are "gitk" and "git gui" not working in the MSYS environment?

They depend on Tcl/Tk and we only provide mingw builds for those. In all environments besides MSYS they should work fine though.

### Some tool I use fails to work with the git in MSYS2, but works fine with the official one

One common issue with external tools integrating git, is that they get confused by Unix paths, for example when figuring out the project root path via `git rev-parse --show-toplevel`. This can be worked around by using `git rev-parse --show-prefix` instead which outputs a relative path from the root to the current working directory, which is both a valid Unix and Windows path.
