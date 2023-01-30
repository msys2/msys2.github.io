# Repositories and Mirrors

## Active environments

The package manager uses only environments that are configured under `/etc/pacman.conf`.
You may add/uncomment/remove/comment those as needed:

```pkgconf
# always include msys!
[msys]
Include = /etc/pacman.d/mirrorlist.msys

[mingw32]
Include = /etc/pacman.d/mirrorlist.mingw

[mingw64]
Include = /etc/pacman.d/mirrorlist.mingw

[ucrt64]
Include = /etc/pacman.d/mirrorlist.mingw

[clang64]
Include = /etc/pacman.d/mirrorlist.mingw

[clang32]
Include = /etc/pacman.d/mirrorlist.mingw

[clangarm64]
Include = /etc/pacman.d/mirrorlist.mingw
```

For more details about how to install packages see ['Package Management'](package-management.md).

To launch an environment either use the wrapper executables like `ucrt64.exe` or
call `msys2_shell.cmd` with either the matching parameter like `msys2_shell.cmd -clang64`
or by setting `MSYSTEM`.
