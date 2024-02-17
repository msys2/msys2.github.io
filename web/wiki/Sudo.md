---
summary: In regular GNU/Linux environments, people use `sudo` to perform administrative tasks on their system
---

# Do you need Sudo?

## Do you need Sudo?

In regular GNU/Linux environments, people use `sudo` to perform administrative tasks on their system, e.g. installing and removing packages, editing system configuration.  Since the most common way of installing MSYS2 results in the MSYS2 root directory being writable by the user, these tasks can be performed without doing anything special.  If you made your MSYS2 root read only for users or want to run Windows administrative tasks from MSYS2, continue reading.

## How to get Sudo

There are several `sudo` alternatives to choose from.  Check the difference sheet below and pick the one you like to download.  For general users, we recommand `gsudo` as it is powerful and modern.  To have it installed, run `winget install gsudo` and reboot your system if you have winget.  Run `echo 'alias sudo=gsudo' > ~/.bashrc` if you are used to typing `sudo`.  If you can't invoke `gsudo` as your shell doesn't inherit Windows PATH, please append `alias sudo='"$PROGRAMFILES/gsudo/Current/gsudo.exe"'`to your bashrc.  Click the links below to learn more advanced features.

## Difference between various Sudo

* [gsudo](https://github.com/gerardog/gsudo): Universal implementation in C#, support a wide range of features including `-u`, multiple shells, job control, etc. Installation needed.
* [win-sudo](https://github.com/purplesyringa/win-sudo): Compact implementation in shell script, lacks some features like job control.
* [Sudo for Windows](https://github.com/microsoft/sudo): Official implementaion from Microsoft. Coming soon.
* [NSudo](https://github.com/M2TeamArchived/NSudo)/[MinSudo](https://github.com/M2Team/NanaRun): Poor support for MSYS2, don't choose it.

