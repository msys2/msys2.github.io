While in our humble opinions, MSYS2 makes collaborative, organised development of open-source software on Windows a workable proposition, there are a few things to be aware of that we commonly run into, mostly due to the design decisions made by Microsoft, our preference for using native tools and compilers rather than cross msys2-to-native ones and our wish to be as flexible as we can be.

mingw32-make
------------
MSYS2 provides two versions of make, one in the `make` package and one in the `mingw-w64-{i686,x86_64}-make` packages. The latter one is called `mingw32-make` on command line, is fully native and doesn't depend on `msys2` shells. The downside is that it doesn't work with many `Makefile`s. Unless you know what you're doing, use the regular `make`.

Detecting version of MSYS from GNU make
---------------------------------------
You can use the following `Makefile` snippet to detect whether you are running GNU make from an MSYS or an MSYS2 shell. If you run it through `mingw32-make.exe` from `cmd.exe` you will likely get an error since `uname` will not be found on your `PATH`. If you run it through `mingw32-make.exe` from one of the MSYS shells, it will set `msys_version` to 1 or 2 as appropriate. On any other system with `uname` present, it will set it to 0.

~~~~
msys_version := $(if $(findstring Msys, $(shell uname -o)),$(word 1, $(subst ., ,$(shell uname -r))),0)
$(info The version of MSYS you are running is $(msys_version) (0 meaning not MSYS at all))
~~~~


Platform checks
---------------

You may need to use platform checks to switch between behaviour suited for MSYS2 and the default one. Some useful identifiers:

Identifier           | Platform(s)                | Usage
---------------------|----------------------------|----------------------------
`_WIN32`             | mingw, msvc                | C code (`#ifdef ...`)
`_WIN64`             | 64-bit mingw, 64-bit msvc  | C code (`#ifdef ...`)
`__CYGWIN__`         | msys2, cygwin              | C code (`#ifdef ...`)
`__MSYS__`           | msys2                      | C code (`#ifdef ...`)
`x86_64-pc-msys2`    | 64-bit msys2               | Build scripts (`if [ $host = '...' ]`)
`i686-pc-msys2`      | 32-bit msys2               | Build scripts (`if [ $host = '...' ]`)
`x86_64-w64-mingw32` | 64-bit mingw               | Build scripts (`if [ $host = '...' ]`)
`i686-w64-mingw32`   | 32-bit mingw               | Build scripts (`if [ $host = '...' ]`)
`msys`               | msys2                      | Python (`sys.platform`)
`win32`              | mingw                      | Python (`sys.platform`)

Filesystem namespaces
---------------------

In MSYS2 there are two different filesystem namespaces in play. If you are building purely `msys2` software, you can ignore the Windows filesystem namespace entirely, however, when building native software using MSYS2's tools, you must be mindful that when `msys2` executes a native program, it will translate environment variables and command arguments from msys2-form to native-form. To do this, it converts things that _look_ like `msys2` paths. Sometimes it gets this wrong, e.g.:

    command.exe /switch
Explanation: `/switch` is a Windows style switch. Note that Windows programs commonly accept unambiguous dash-prefixed switches (`-switch`) as well.

    adb push readme.txt /sdcard/0/
Explanation: `/sdcard/0/` is a path on a foreign system.

    ./configure --root=/
Explanation: The value of root (`/`) is emitted to a text file via echo (which is an `msys2` program and hence not mangled) and also to a `Makefile` (through autotools) which passes it to a native program, which reads the text file replacing each instance of `/` with "some-other-path". This will go wrong as `/` passed to the native program was converted to e.g. `C:/msys64/` and therefore the necessary substitutions did not happen. [last sentence needs review or rewording]

To work around this, path conversion can be selectively disabled. MSYS2 reads an environment variable called `MSYS2_ARG_CONV_EXCL`. This is a `;` delimited string each part of which is compared against the front part of each argument and if a match is found, that conversion is skipped. An example of a value for `MSYS2_ARG_CONV_EXCL` that would inhibit path transformations of the 3 cases above is `/switch;/sdcard;--root=`.

The development repository for this path conversion code is <https://github.com/Alexpux/path_convert>. If you find a case that you think is unambiguously being converted incorrectly, please raise an issue there and/or a pull request with the broken test-case.


Hard-coded paths and relocation
-------------------------------

When installing MSYS2, the user selects the root folder. POSIX software has a habit of baking the installation paths into the packages at build time, which is okay for `msys2` software (which only sees the single-root virtual filesystem), but usually causes failures in native software. When a program tries to load its data files using these absolute paths on another MSYS2 installed to a different root folder, it won't find them. For this reason, adding path relocation patches is a common necessity for `mingw` packages (but never for `msys2` packages). The point is to find the path where the program's executable resides, cutting off the `/bin` from the end and finding all necessary files using paths relative to that. Since this is a pretty common task and is not exactly trivial to get it right for all cases, we wrote some re-usable C code for that, available at <https://github.com/Alexpux/MINGW-packages/tree/master/mingw-w64-pathtools>.

Sometimes these paths are baked into shell scripts or pkg-config's `.pc` files. In that case, you should use sed in the `PKGBUILD` `package()` function to correct this back to the `msys2` version of the path. [please review last sentence] An example of this can be seen at <https://github.com/Alexpux/MINGW-packages/blob/master/mingw-w64-libtool/PKGBUILD#L55>.


C *printf Format Specifier issues
---------------------------------

The vc6.0 msvcrt.dll that MinGW-w64 targets doesn't implement support for the ANSI standard format specifiers. MinGW-w64 works around this by providing their own implementation. To enable this you should pass -D__USE_MINGW_ANSI_STDIO=1 to the MinGW-w64 C and C++ compilers. All of our C/C++ packages are built with this flag.


Different size of struct timeval
--------------------------------

The Windows (and thus mingw-w64) `struct timeval` is defined as having two `long` members, while the POSIX specs say it's supposed to have one `time_t` and one `suseconds_t` member. This means that on 64-bit, the size of the struct will be different from what you would expect on Linux/Cygwin/MSYS2.

[struct timeval on MSDN](https://msdn.microsoft.com/en-us/library/windows/desktop/ms740560(v=vs.85).aspx)
[struct timeval on OpenGroup.org](http://pubs.opengroup.org/onlinepubs/007908775/xsh/systime.h.html)


More 32/64 bit peculiarities
----------------------------

Sorting out the stat thing by LRN:
https://gnunet.org/sorting-out-stat-thing


Calling conventions, stdcall, and autotools
-------------------------------------------

Details about Windows' 32bit calling conventions:
http://www.willus.com/mingw/yongweiwu_stdcall.html

Problems stdcall causes with autotool's AC_CHECK_FUNC and AC_SEARCH_LIBS:
http://lists.gnu.org/archive/html/autoconf/2013-05/msg00090.html


Macro/inline function and autotools
-----------------------------------

`AC_CHECK_FUNCS` and friends can't deal with function macros and static inline functions (because the checking code tries to `#undef` the symbol, doesn't include any headers and declares the symbol as extern instead). Possible solution is replacing them with more elaborate checks using `AC_LINK_IFELSE` or `AC_COMPILE_IFELSE`. For example this:

    AC_CHECK_FUNCS([localtime_r],
    [AM_CONDITIONAL([HAVE_LOCALTIME_R], true)],
    [AM_CONDITIONAL([HAVE_LOCALTIME_R], false)])

... can be replaced with this:

    AC_MSG_CHECKING([for localtime_r])
    AC_LINK_IFELSE([AC_LANG_PROGRAM([[
      #include <time.h>
    ]], [[
      time_t t; struct tm r;
      localtime_r(&t, &r);
    ]])],
    [AC_MSG_RESULT([yes])
     AM_CONDITIONAL([HAVE_LOCALTIME_R], true)
     AC_DEFINE([HAVE_LOCALTIME_R], [1], [Define to 1 if you have the `localtime_r' function or macro.])],
    [AC_MSG_RESULT([no])
     AM_CONDITIONAL([HAVE_LOCALTIME_R], false)])

Don't forget to `autoreconf -fi` after patching `configure.ac`.

A tidy workaround from flameeyes for asprintf/vasprintf (but generally applicable):
https://mailman.videolan.org/pipermail/vlc-devel/2015-March/101802.html


Guarded time functions, ANSI format specifiers
----------------------------------------------

Some things in mingw-w64 are (maybe unexpectedly) guarded by `#ifdef`s. Check out `_POSIX_C_SOURCE`, `__USE_MINGW_ANSI_STDIO`, the `time.h` file. Note that (at the time of writing) `pthread.h` contains some defines that affect the definitions in `time.h`.


Undefined references and linking to DLLs/SOs
--------------------------------------------
[this section may contain misinformations; it needs review from a knowledgeable person]

Linux/ELF platforms generally don't do anything special to link to shared objects, they just leave the undefined references in the binary. Windows however requires all references to be resolved at link time. In case of DLLs, this is solved by the .dll.a import libraries that add the relevant .dll to the binary's import table and insert correct calls into the code, but it needs that correct linker flags be passed when linking binaries. Note that the linker is aware of these files and will use them automatically when using the standard `-l` arguments, for example `-lfoo` will make the linker check for `libfoo.dll.a` and `libfoo.a`, in this order (unless specified otherwise).

Libtool generally refuses to create DLLs unless `-no-undefined` is passed to the linker invocation (`library_la_LDFLAGS = -no-undefined`).
See: https://lists.gnu.org/archive/html/libtool/2007-04/msg00066.html


Library prefixes
----------------

`mingw` DLLs follow the convention of prefixing libraries with `lib`. This affects shared libraries (`.dll`), static object archives (`.a`), and DLL import libraries (`.dll.a`). Because `msys2` DLLs are generally ABI-incompatible with everything from outside of `msys2`, they are prefixed with `msys2-` instead. For completeness, we note that Cygwin DLLs are prefixed with `cyg`.

[does libtool or the linker handle this automatically?]


Standard streams in mintty
--------------------------

mintty is primarily designed to be a good terminal emulator (in the POSIX sense of the word) and it works well with bash, ssh and other Cygwin/MSYS2 programs. Because native Windows console programs use a fundamentally different way of handling console input/output, mintty uses pipes to connect to their standard streams (stdin, stdout, stderr). Unfortunately, this has the effect that `isatty` and similar APIs (used to check whether a stream is attached to an interactive console or a pipe/file) will return incorrect values for native programs running under mintty.

One way of fixing this problem is to run native programs inside a real Windows console, hide the console and use the console API to communicate with the program. This approach has obvious disadvantages, but it's good enough. Actually, this is the way most Windows console emulators work (e.g. ConsoleZ, ConEmu). There is also a wrapper program called winpty that does exactly this and translates the I/O to/from standard terminal sequences which mintty understands.

Running a program under winpty (by prefixing the command line with `winpty`) will make the program think it is running interactively, but it will also break any special features depending on terminal sequences, possibly including colored text output and TUIs.

MSYS2 includes wrappers for some affected programs, so that they will work correctly most of the time. Examples can be seen in packages containing REPLs (python3, lua, nodejs, ...).

[mintty issue #56](https://github.com/mintty/mintty/issues/56), original [on Google Code](http://code.google.com/p/mintty/issues/detail?id=56)

[winpty on GitHub](https://github.com/rprichard/winpty)

Signals in mintty
-----------------
When running a native Windows program in mintty (or urxvt, apparently), Ctrl+C will not be correctly passed to the process. Instead, it seems to be eaten by the terminal and the running process is terminated.

[ticket #135](https://sourceforge.net/p/msys2/tickets/135/)

Paths in mingw Python
---------------------

The mingw python provided by MSYS2 will try to produce paths that are right for the environment it's running in. According to the value of `MSYSTEM`, it will use either forward or backward slashes as `os.path.sep`.


Response files
--------------

When passing arguments with absolute paths to native Windows programs (such as `/mingw64/bin/gcc`), these paths  get (in most cases) automatically converted by MSYS2 if they're in POSIX format. However, if you're passing these paths inside a file (e.g. a response file for GCC -- `gcc @somefile`), they need to be pre-converted to Windows native format.

[discussion topic: gcc -I (eye) uses msys2 path or windows path?](https://sourceforge.net/p/msys2/discussion/general/thread/b82485a3/)

Setting floating point precision
--------------------------------

Floating point precision issues with multiple threads:
gfortran, open mp and floating point precision by Carl Kleffner:
- https://sourceforge.net/p/mingw-w64/mailman/message/33332276/
- https://gcc.gnu.org/wiki/FloatingPointMath
- https://gcc.gnu.org/wiki/x87note


Command line parsing
--------------------

Windows programs parse the command line themselves, it isn't parsed for them by the calling process, as on Linux. This means that if wildcards (glob patterns) are to be accepted by the program, it has to be able to expand them somehow. MinGW-w64 supplies the correct start-up code, so it happens automatically, in a manner compatible with MSVC-compiled programs. If undesirable, the behavior can be disabled at program build.

Cygwin/MSYS2 programs have to deal with a mix of both approaches, but they can apparently deal with it. Note that they don't behave exactly like native programs, for example they understand single-quoted arguments.

["How Command Line Parameters Are Parsed" by David Deley](http://www.daviddeley.com/autohotkey/parameters/parameters.htm)

["Everyone quotes command line arguments the wrong way" by Daniel Colascione](http://blogs.msdn.com/b/twistylittlepassagesallalike/archive/2011/04/23/everyone-quotes-arguments-the-wrong-way.aspx)

Other resources
---------------

A collection of articles on general C and C++ topics.
http://locklessinc.com/articles/

The MinGW-w64 project's wiki.
http://sourceforge.net/p/mingw-w64/wiki2/browse_pages/
