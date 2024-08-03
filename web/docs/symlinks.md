# Symlinks

[Symlinks](https://en.wikipedia.org/wiki/Symbolic_link) are a way to create a
reference to a file or directory in another location. They are quite common on
Linux/Unix systems, and many Unix tools are using/depending on them. While
symlinks also exist on Windows, they are not available to normal Windows users
by default, which makes them less common on Windows.

In MSYS2 symlinks are by default avoided, and creating a symlink with Cygwin
tools instead creates a deep-copy of the target. This makes sure that symlinking
works on every Windows installation and for every Windows user and the result is
readable by native Windows software.

The deep-copying has the downside that the symlink and the target are not
actually linked, and due to the duplication it also takes up double the disk
space. Another downside is that the target always needs to exist, otherwise it
couldn't be copied.

We are planning to improve this in the future, see
https://github.com/msys2/msys2-runtime/pull/114 for more information.

## Cygwin Symlink Modes

While MSYS2 is based on Cygwin, Cygwin has different default behavior for
symlinks and tries to create "real" symlinks if possible, with the potential
downside that they are not readable by native Windows applications.

See https://cygwin.com/cygwin-ug-net/using.html#pathnames-symlinks for details
on the default behavior and all the different symlink modes that are available
in Cygwin.

All these modes can also be enabled in MSYS2 by setting the `MSYS` environment
variable instead of `CYGWIN`. For example `MSYS=winsymlinks:nativestrict` can be
used to enable native Windows symlinks.

* `ln -s target link` - create a symlink to a file or directory

The default mode in MSYS2 is called `winsymlinks:deepcopy` and is only available
in MSYS2 and not in Cygwin.

## Native Windows Symlinks

This is a short primer for native Windows symlinks in case you haven't used them
before or are only familiar with them on Unix systems.

Symlink support in Windows existed for a long time, but creating them was
initially only possible with administrator accounts. Starting with Windows 10
(~2016) it is now possible to create symlinks with your normal user account if
you have the ["Developer Mode"
enabled](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development).
Existing symlinks that were created by an administrator account, or with the
"Developer Mode" enabled, can be used and deleted by normal users without rights
to create symlinks themselves.

Compare to Unix symlinks, the Windows symlinks come in a "directory" and a
"file" type. If you create a file symlink to a directory, or vice versa, or if
the target type changes after the symlink is created, the symlink will be
broken.

Symlinks also only work on NTFS/ReFS filesystems, and not on FAT32 or exFAT.

To create a symlink on Windows in cmd you can use "mklink":

* `mklink link target` - create a symlink called "link" to a file called "target"
* `mklink /d link target` - create a symlink called "link" to a directory called "target"

mklink ignores the type of any existing target and always creates a file
symlink if not specified otherwise.

* When on an unsupported filesystem you will get: "The device does not support symbolic links".
* Without developer mode enabled or administrative privileges you will get: "You do not have sufficient privilege to perform this operation."

Under PowerShell you can use "New-Item":

* `New-Item -ItemType SymbolicLink -Path link -Target target` - create a symlink called "link" to a file or directory called "target"

Unlike "mklink", "New-Item" will automatically create a directory symlink if the
target is a directory and a file symlink if the target is a file. In case the
target doesn't exist yet, the symlink will be a file symlink by default and, as
far as I'm aware (??), there is no way to create a directory symlink to a
non-existing target with "New-Item".

* When on an unsupported filesystem you will get: "Symbolic links are not supported for the specified path."
* Without developer mode enabled or administrative privileges: "Administrator privilege required for this operation."

If you get the "Administrator privilege required" error despite having Developer
Mode enabled, you might be using a too old version of Powershell, like the
version included in Windows by default. You either need to [install a newer
version of Powershell](https://winget.run/pkg/Microsoft/PowerShell), use mklink
via `cmd /c mklink`, or use an elevated prompt. You can check your Powershell
version with `$PSVersionTable.PSVersion`.

## Known Issues

As stated above, for the deep-copy to work the target needs to exist for the
symlinking to work. While dangling symlinks are not that common, they can happen
easily when unpacking a tar file that contains symlinks. If the symlinks is
unpacked before the target, then creating the symlink will fail. A workaround
for this is to unpack the tar file twice, first to create the target while
ignoring any symlink creation errors and then to create the symlinks:

```bash
bsdtar -xf "archive.tar.bz2" 2>/dev/null || bsdtar -xf "archive.tar.bz2"
```
