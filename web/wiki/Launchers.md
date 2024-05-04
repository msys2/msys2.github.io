---
summary: How to start MSYS2?
---

# Launchers

You should *not* launch sh.exe directly as that doesn't start a login shell or set the correct environment variables for the type of shell that you want to use. Instead, your best choices are:

[**msys2_shell.cmd**](https://github.com/Alexpux/MSYS2-packages/blob/master/filesystem/msys2_shell.cmd), the improved multi-purpose batch file from the [`filesystem` package](https://github.com/Alexpux/MSYS2-packages/tree/master/filesystem).  Run `msys2_shell.cmd --help` for usage.

**msys2.exe**, **mingw64.exe**, **mingw32.exe**, the new pinnable launchers from the `msys2-launcher` package from @Elieux. [GitHub](https://github.com/elieux/msys2-launcher), [discussion](https://github.com/Alexpux/MSYS2-packages/issues/370#issuecomment-152021427), [discussion](https://sourceforge.net/p/msys2/mailman/message/34599465/)

A nice explanation how to [set up ConEmu](https://superuser.com/a/1297072) to run MSYS2 inside it by jstine.

Configuration for [an MSYS2 shell in Visual Studio Code](https://stackoverflow.com/a/48016561).

**msys2_env.bat** from @DavidEGrayson. [Gist](https://gist.github.com/DavidEGrayson/2e5923b9c0d8acb3f7a7), [discussion](https://github.com/Alexpux/MSYS2-packages/issues/370#issuecomment-151658726)

**msys2.cmd**, **mingw64.cmd**, **mingw32.cmd** from @Elieux. [Gist](https://gist.github.com/elieux/dd6d0c15cc0ae503f830)

**smart_msys** from @jhasse. [GitHub](https://github.com/jhasse/smart_cmd), [discussion](https://sourceforge.net/p/msys2/mailman/message/34639135/)

**MSYS2 here**, **MINGW64 here** and **MINGW32 here** Explorer context menu items from @Elieux. [Gist](https://gist.github.com/elieux/ef044468d067d68040c7)

**msystem.bat** and cmd/clink integration in the `filesystem-cmd` package from @userzimmermann. [PR](https://github.com/Alexpux/MSYS2-packages/pull/350), [commits](https://github.com/userzimmermann/MSYS2-packages/commits/ed54eccce9716b9471c63bc1738ebbab637ed552)

**git-bash.exe** and **start-ssh-agent.cmd** as part of the Git for Windows project from @dscho. [GitHub](https://github.com/git-for-windows/MINGW-packages/blob/main/mingw-w64-git/git-wrapper.c), [GitHub](https://github.com/git-for-windows/MINGW-packages/tree/master/mingw-w64-git)

**Open MSYS2 here** from @magthe, with contributions from @sushovan-dw and @ryanpfeeley. [Gist+discussion](https://gist.github.com/magthe/a60293fe395af7245a9e)

[**msys2_shell.bat**](https://github.com/Alexpux/MSYS2-packages/blob/b827a678b1793571968a4d27f72f981d99c305ef/filesystem/msys2_shell.bat), [**mingw64_shell.bat**](https://github.com/Alexpux/MSYS2-packages/blob/b827a678b1793571968a4d27f72f981d99c305ef/filesystem/mingw64_shell.bat) and [**mingw32_shell.bat**](https://github.com/Alexpux/MSYS2-packages/blob/b827a678b1793571968a4d27f72f981d99c305ef/filesystem/mingw32_shell.bat), the old-school batch files from [old versions of the `filesystem` package](https://github.com/Alexpux/MSYS2-packages/tree/b827a678b1793571968a4d27f72f981d99c305ef/filesystem).

### The idea

If you need to start a shell correctly, but none of the ways above suit you, devise your own way based on this knowledge:

- set `MSYSTEM=...` into the environment, with the value of either `MSYS`, `MINGW32`, or `MINGW64`
- then run a *login* shell

The typical one-liner if your options are limited is `C:\\msys64\\usr\\bin\\env MSYSTEM=MSYS /usr/bin/bash -li`.

Caveats:

- MSYS2 inherits multi-user capabilities from Cygwin and there is a notion of user's default shell.  Not everyone's default shell is *bash*.  To correctly figure out the default shell from outside (i.e. without directly calling the POSIX APIs), you can use this shell one-liner or an equivalent: `getent passwd $(whoami) | cut -d: -f7`
- There are other environment variables that control MSYS2 at runtime or initialization.  See the source of launchers above to figure them out if needed.
- You might need to set `CHERE_INVOKING=1` for the shell to stay in the current working directory.
- If you need to run a specific command instead of an interactive shell, you still need to go through a login shell, e.g. `... /usr/bin/bash -lc python`.
