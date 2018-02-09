You should *not* launch sh.exe directly as that doesn't start a login shell or set the correct environment variables for the type of shell that you want to use. Instead, your choices are:

**msys2_shell.cmd**, the improved multi-purpose batch file from the `filesystem` package.

**msys2.exe**, **mingw64.exe**, **mingw32.exe**, the new pinnable launchers from the `msys2-launcher` package from @Elieux. [GitHub](https://github.com/elieux/msys2-launcher), [discussion](https://github.com/Alexpux/MSYS2-packages/issues/370#issuecomment-152021427), [discussion](https://sourceforge.net/p/msys2/mailman/message/34599465/)

**msys2_env.bat** from @DavidEGrayson. [Gist](https://gist.github.com/DavidEGrayson/2e5923b9c0d8acb3f7a7), [discussion](https://github.com/Alexpux/MSYS2-packages/issues/370#issuecomment-151658726)

**msys2.cmd**, **mingw64.cmd**, **mingw32.cmd** from @Elieux. [Gist](https://gist.github.com/elieux/dd6d0c15cc0ae503f830)

**smart_msys** from @jhasse. [GitHub](https://github.com/jhasse/smart_cmd), [discussion](https://sourceforge.net/p/msys2/mailman/message/34639135/)

**MSYS2 here**, **MINGW64 here** and **MINGW32 here** Explorer context menu items from @Elieux. [Gist](https://gist.github.com/elieux/ef044468d067d68040c7)

**msystem.bat** and cmd/clink integration in the `filesystem-cmd` package from @userzimmermann. [PR](https://github.com/Alexpux/MSYS2-packages/pull/350), [commits](https://github.com/userzimmermann/MSYS2-packages/commits/ed54eccce9716b9471c63bc1738ebbab637ed552)

**git-bash.exe** and **start-ssh-agent.cmd** as part of the Git for Windows project from @dscho. [GitHub](https://github.com/git-for-windows/git/blob/master/compat/win32/git-wrapper.c), [GitHub](https://github.com/git-for-windows/MINGW-packages/tree/master/mingw-w64-git)

**Open MSYS2 here** from @magthe, with contributions from @sushovan-dw and @ryanpfeeley. [Gist+discussion](https://gist.github.com/magthe/a60293fe395af7245a9e)

**msys2_shell.bat**, **mingw64_shell.bat** and **mingw32_shell.bat**, the old-school batch files from old versions of the `filesystem` package.
