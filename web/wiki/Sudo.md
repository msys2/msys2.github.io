---
summary: In regular GNU/Linux environments, people use `sudo` to perform administrative tasks on their system
---

# Do you need Sudo?

## Do you need Sudo?

In regular GNU/Linux environments, people use `sudo` to perform administrative tasks on their system, e.g. installing and removing packages, editing system configuration.  Since the most common way of installing MSYS2 results in the MSYS2 root directory being writable by the user, these tasks can be performed without doing anything special.  If you made your MSYS2 root read only for users or want to run Windows administrative tasks from MSYS2, continue reading.

## How to get Sudo

Since MSYS2 doesn't support all the things a classic Sudo needs (setuid? PAM?), we need a replacement.  One such replacement that doesn't seem to suffer from horrible security flaws is [*win-sudo*](https://github.com/imachug/win-sudo).  It doesn't support (as of May 2020) the various different arguments (`-H`, `-u` etc.), but it does work in the most common use case of `sudo foo` running `foo` with elevated privileges.  The authorization is handled by UAC, same as any other Windows program.
