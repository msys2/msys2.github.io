---
title: Windows Terminal Integration 
summary: Explores the use case of running msys2 programs in the Windows terminal for better integration with other systems
---

Windows Shell Integration
-------------------------

Arguably the most common critique of msys2 is lack of shell integration: Quite a few programming tools permit the running of external programs, but only in `PowerShell` even `cmd.exe`- to these tools, the msys2 bash shell is not a benefit but a use barrier. The situation is similar for `PowerShell` or `cmd` users who prefer not to invest time to learn bash, but could still benefit from using msys2 programs.

Fortunately, it works perfectly fine for many non-interactive msys2 programs to be run this way, including the package manager `pacman`. This approach permits using msys2 packages without any knowledge of unix or the msys2 subsystem, looking at msys2 chiefly as another Windows package manager- albeit one that contains mature and up-to-date packages for unix build dependencies both common and esoteric.

Instructions
------------

To set up msys2 to permit running programs in `PowerShell` and `cmd`, first install install msys2 normally. Then, you need to set up your Windows paths to access the msys2 programs, and do something about Windows lack of support for executing shell scripts.

**Install msys2 normally**

This can be done from the msys2 web site using the regular installation instructions.

**Set up paths**

1. press the `Windows`-key and type `Env`. A menu entry called "Environment Variables" will pop up, which you can click.
2. A control panel configuration window opens that has an Environment Variables button. Click that too.
3. The environment editing window pops up. One of the environment variables is the path, which you can double-click to edit it.
4. A list of the path entries pops up. Add an entry for `C:\msys64\usr\bin`.
5. If you installed the mingw64 compiler, add an additional entry for `C:\msys64\mingw64\bin

Note that you can control which program has precedence, in case you installed additional unix programs from other sources. If you place the environment variables at the top of the list, the msys2 version will take precedence, if you place them at the bottom, the other programs will.

**Work around script support**

Unix shells support specifying an arbitrary interpreter to be used when executing shell scripts in the file itself, the so-called "shebang" line. Windows terminal does not support this, and will only run `.bat`, `.cmd` or `.exe` files. This breaks otherwise portable build tools that might run something like `autoreconf` in the system standard shell.

A usable workaround is to place a Windows executable in the path with the same name as the desired script, except the extension, that will then run that script with the correct interpreter. This could be considered an "external shebang". The easiest way is by using a `.bat` file in the same directory as the script.

To make the script `C:\msys64\usr\bin\myshellscript` run with bash, place a file with the following contents in `C:\mys64\usr\bin\myshellscript.bat.

    @echo off
    bash "%~dpn0" %*

This will execute the program `bash` found in the path with the actual script as the first argument, followed by all arguments provided. So the script can be called like so:

    myshellscript --foo=bar fuz buz

And the batch file will execute `bash myshellscript --foo=bar fuz buz` making the batch file completely transparent.

This needs to be done for every script that is needed. If the interpreter is the same, the script can simply be copied- `cp myshellscript.bat myothershellscript.bat`, but need to be adapted if the interpreter is different:

    @echo off
    perl "%~dpn0" %*

Can be placed in a file `C:\msys64\usr\bin\myperlscript.bat` to allow the perl script `C:\msys64\usr\bin\myperlscript` be run from Windows.

Other scripting languages may of course be used. When creating the "shimbang" file (let's call it that), `"%~dpn0"` refers to the full path without extension, which is your script file (include the quotes), and `%*` refers to all arguments passed to the batch file. 

While creating these "shimbang" files does require some manual editing, it is still far preferable to creating a Frankenstein's monster of unix build dependencies from different sources.

**Use it**

Now restart your Windows terminal and install a few packages you need. For example:

`pacman -S git mingw-w64-x86_64-gcc autoconf libtool bash perl ar nasm make`

Will give you everything you need to build a C library that uses inline assembler and autoconf/make from the Windows terminal. Note: run `bash configure` instead of `./configure`.

