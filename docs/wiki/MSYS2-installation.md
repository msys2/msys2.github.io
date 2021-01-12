---
title: MSYS2-Installation
summary: MSYS2 ships in the form of installers and base archives.
---
I. Downloading
==============
**MSYS2** ships in the form of installers and base archives. They can be installed or extracted to any place on your computer, but you **MUST** use folder names that consist of only ascii characters and no spaces (also it makes good sense to put it in a path that doesn't use many characters due to PATH_MAX being 260; C:\msys32 or C:\msys64 is ideal).
  You can download the installers or base MSYS2 archives from the links below:

  1. [**32-bit**](http://repo.msys2.org/distrib/i686/)

  2. [**64-bit**](http://repo.msys2.org/distrib/x86_64/)

Note: if you are using 64-bit Windows, there is *no* reason to use 32-bit MSYS2. Well, to be honest, there is one reason: you want to develop MSYS2 software (or contribute to MSYS2-packages) and want to test that the software/package also works on 32-bit MSYS2. When it comes to native software, 64-bit MSYS2 can be used to build, install and run both 32-bit and 64-bit variants. 64-bit MSYS2 software (practically speaking) never needs to be "re-based", giving a better user experience.

II. Installation
================
The installers and base archives only contain the tools necessary to 1) start **MSYS2** 2) update the pre-installed packages and 3) install new packages.

 * After installing or extracting MSYS2 you should start MSYS2 by executing **msys2_shell.cmd**.
  (if you did not use an installer and this is first time running of MSYS2 after unpacking, then at this point it will create the files and settings necessary for it to function properly. After this initial run you **MUST** restart MSYS2 so that the settings are correct)

 * Now you can update the base MSYS2 packages to their latest versions. MSYS2 comes with a ported version of the **[Pacman][1]** package manager (known from Arch Linux).

III. Updating packages
======================
  Partial upgrades (e.g. updating just `pacman` while not updating `msys2-runtime`) are not supported and are expected to break stuff.

  1. Since pacman 5.0.1.6403, you can just:
    - Run **`pacman -Syuu`**. Follow the instructions. Repeat this step until it says there are no packages to update.

  2. Since pacman 4.2.1.6187, there's an `update-core` script that helps you to update MSYS2 in the right way. To update your MSYS2 installation you need:
    - Run **`update-core`**. If one of the packages is updated during script run you ***MUST*** restart MSYS2
    - Run **`pacman -Suu`** to update the rest of the packages (allowing downgrades).

  3. In older MSYS2 installations, follow these steps:
    - Before updating you should synchronize your local package databases with the latest repositories:
    **`pacman -Sy`**
     This command connects to the remote repositories and downloads the package databases.
    - The next step is to update the installed packages (do this initially and as often as you want thereafter):
     The 'normal' way (**don't do this**) would be to simply issue:
    **`pacman -Suu`**
     ... however, because all MSYS2 programs share the same address space for DLLs due to how MSYS2 (well, Cygwin) implements 'fork', updating bash, MSYS2 or Pacman itself can cause subsequent package updates to fail. For this reason, the safest procedure for updating MSYS2 is to do it in two stages; first those 'core' MSYS2 packages:
    **`pacman --needed -S bash pacman pacman-mirrors msys2-runtime`**
    ... if any packages got updated during this then you **MUST** restart MSYS2 because files that are provided by these packages will be in use and after update you can get fork errors - you need to exit all MSYS2 shells (and if using MSYS2 32bit, run autorebase.bat) then re-launch **`msys2_shell.bat`**
    - Finally you can do an update of the remaining packages by issuing:
    **`pacman -Suu`**

IV. General Package Management
==============================
  1. Installing new packages:
    **`pacman -S <package_names|package_groups>`**
     For example, `pacman -S make gettext base-devel`
     In this example <base-devel> is a package group which contains many packages. If you try to install a package group, Pacman will ask you whether you want to install one package from the group or all of the packages from the group.
  2. Removing packages:
    **`pacman -R <package_names|package_groups>`**
  3. Searching for packages:
    **`pacman -Ss <name_pattern>`**

More on our [Using packages wikipage](Using-packages.md).

V. Issues and workarounds
=========================
  1. Please read "III." above, carefully :-) We will continue working towards trouble-free updates.
  2. If you do run into failures to run post-install scripts, it's really *nothing* to panic about. Simply make a list of the packages that failed to install correctly, exit all your MSYS2 shells (make sure that they fully exit and no mintty/bash processes are running). Then launch a new MSYS2 shell, and issue: `pacman -S <list-of-packages-that-failed-to-install>`
  3. If you get `error: failed to prepare transaction (could not satisfy dependencies)` complaining about `msys2-runtime-devel` when you try to update the core, you need to update this package alongside `msys2-runtime` and the other core packages.
  4. Sometimes a package upgrade fails with `failed to commit transaction (conflicting files)` and `some-pkg: /path/to/some/file exists in filesystem`. If you're sure you didn't put the offending files there manually, move or delete the files and start the upgrade again.
  5. If your MSYS2 is unable to start after an upgrade, it's possible you just have some lingering MSYS2 processes (loaded with an older version of the runtime) that are conflicting with the processes you're trying to start. Hunt down these processes in your favorite task manager and kill them, or just reboot your system.
  6. After an update, you get `error: GPGME error: No data` then you were unlucky and caught SourceForge at a bad time. Check `/var/lib/pacman/sync` and if the files in there contain an HTML formatted error page, then delete those files and try again.
