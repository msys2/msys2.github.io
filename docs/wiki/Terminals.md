This is a basic explanation of how [console programs](https://en.wikipedia.org/wiki/Console_application) work in Cygwin and MSYS2. [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface) (graphical, windowed) programs fall outside of the scope of this text.

Note that this topic is not simple and there are many factors that can cause differences in observed behavior (`TERM`, `LANG`, `LC_*`...). The following information is our best understanding and our best attempt at explaining it. If the reader has any corrections or clarifications, please post to the mailing list. Note that where we say MSYS2 below, it usually denotes Cygwin as well.

MSYS2 (more generally POSIX) and regular Windows (i.e. non-MSYS2 ones) console programs both use character streams to read data from the user and to display data to the user. If reading and writing simple text is the only thing a program does (i.e. it's not interactive), then the program's I/O should be easily portable between Windows, MSYS2 and other platforms.

On a more advanced level, e.g. when a program employs a [REPL](https://en.wikipedia.org/wiki/Read–eval–print_loop) or uses colored output or draws [TUIs](https://en.wikipedia.org/wiki/Text-based_user_interface), the two systems are fundamentally different. MSYS2/POSIX programs use [in-band terminal sequences](https://en.wikipedia.org/wiki/ANSI_escape_code), while Windows programs use out-of-band calls to the [Windows Console API](https://en.wikipedia.org/wiki/Win32_console). In the POSIX world, REPLs are often programmed using the *readline* library and TUIs using the *ncurses* library.

Terminals
---

[Terminals](https://en.wikipedia.org/wiki/Terminal#Electronics.2C_telecommunication.2C_and_computers) are programs that interface with console programs and facilitate their input (e.g. accept keypresses from the user and send corresponding characters to the program) and output (e.g. draw the characters from the programs as corresponding glyphs on the screen).

**Mintty** is a terminal emulator built for MSYS2 programs. It provides the necessary POSIX interfaces to MSYS2 programs. There are other terminal emulators in Cygwin, but they're not provided in MSYS2.

The Windows console (*conhost*) does the same for Windows programs. It provides the back-end to the Windows Console API.

Shells
---

A distinct category of programs are [shells](https://en.wikipedia.org/wiki/Shell#Computing). A shell is the actual program that reads commands from the user and runs them.

The "DOS window" in Windows is actually a combination of a Windows console and the Windows shell (**cmd**, command line). Likewise, when you open a mintty window, you'll probably see the **bash** shell running inside and waiting for your commands. This matching is not mandatory though, as bash can be run in a Windows console and cmd can be run in mintty.

Mixing MSYS2 and Windows
---

MSYS2 allows some inter-operation between a MSYS2 program and Windows console and between a Windows program and MSYS2 terminal emulators. For basic stuff, it works fine. Anything more complicated, like colored text, [TUIs](https://en.wikipedia.org/wiki/Text-based_user_interface) and [line editing](https://en.wikipedia.org/wiki/Line_editor), is a lottery -- it can work, it can break.

**Winpty** is a wrapper program that works as a translator between Windows programs and MSYS2 terminals. It opens an invisible Windows console window and runs the wrapped program in it. It then relays input from the terminal to the program and output from the program to the terminal. This solves a lot of the issues of running Windows programs in a MSYS2 terminal.
