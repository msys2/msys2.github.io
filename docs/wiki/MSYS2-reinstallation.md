---
title: Re-installing MSYS2
summary: When we release new installers and new base tar.xz packages
---
Introduction
------------

When we release new installers and new base tar.xz packages, we'd appreciate it if people can help out by testing complete re-installs of their entire MSYS2. The procedure is safe as it is fully reversible. Also, if your system gets messed up, this procedure could help to get you running again.

Re-installing
-------------

1. Run your existing MSYS2 installation via `msys2_shell.cmd`.

2. Make a list of installed packages:

        pacman -Qqe | xargs echo > /c/packages.txt ; exit

3. Rename your `msys??` folder to `msys??.old`.

4. Run the installer (or untar the base package, run `msys2_shell.cmd`, then exit it).

5. To save server bandwidth and your time, move your old cached packages directory to the new installation. In Explorer, remove the empty `msys??\var\cache\pacman\pkg` folder, then replace it with `msys??.old\var\cache\pacman\pkg`.

6. Run the new MSYS2 installation via `msys2_shell.cmd`.

7. Update the package databases:

        pacman -Sy

8. Update the core packages:

        pacman --needed -S bash pacman pacman-mirrors msys2-runtime

9. If any packages got updated during step 8, you MUST restart MSYS2, otherwise you can get fork errors in the next step. You need to exit all MSYS2 shells (and if using MSYS2 32bit, run `autorebase.bat`) then re-launch `msys2_shell.cmd`.

10. Re-install your old packages, by entering:

        pacman -S --needed $(cat /c/packages.txt)

You may also want to compare your new $HOME folder with your old one and merge across your dotfiles and other files.

Reversing the procedure
-----------------------

1. Move the pkg folder back from `msys??\var\cache\pacman\pkg` to `msys??.old\var\cache\pacman\pkg`.
2. Delete the new `msys??` folder.
3. Rename `msys??.old` to `msys??`.

Finally
-------

It would be good if you can try working with the new installation to see if everything's OK, and if not, please report a bug (try to use e.g. strace or procmon to figure out what goes wrong and meld3 or Beyond Compare to help track down which files are different).
