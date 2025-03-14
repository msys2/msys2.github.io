# C/C++

## Expanding wildcard arguments

For making your program accept wildcard arguments, the official MSVC way is to
link [w]setargv.obj to your program. By default it is not enabled. For more
details see
https://learn.microsoft.com/en-us/cpp/c-language/expanding-wildcard-arguments

Note that enabling wildcard expansion can have usability and security
implications:

* The program might transform the arguments you passed in, depending on the
  current directory, leading to user confusion.
* The program might leak information about the existence and names of files on
  the filesystem.
* Input validation might be bypassed if wildcard expansions is not taken into
  account.

With mingw-w64, there are three ways wildcard expansion can be configured:

1. You can set `_dowildcard` in your source code to either `0` or `-1` to disable or enable wildcard expansion.

    ```c
    // To force-enable wildcard expansion
    int _dowildcard = -1;
    // To force-disable wildcard expansion
    int _dowildcard = 0;
    ```

2. You can link in `CRT_noglob.o` or `CRT_glob.o` to disable or enable wildcard expansion, respectively. This will error out if `_dowildcard` is already set in the source.

    ```bash
    # To force-enable wildcard expansion
    cc main.c "$(cc -print-file-name=CRT_glob.o)"
    # To force-disable wildcard expansion
    cc main.c "$(cc -print-file-name=CRT_noglob.o)"
    ```

3. mingw-w64 can be configured at build time to either enable or disable wildcard expansion by default via the `--enable-wildcard` configure flags. This can to be overridden on a per .exe basis by the user.

    Wildcard expansion is disabled by default in MSYS2.

### Changelog

* Starting with 2024-11-03 we have changed mingw-w64 to to disable wildcard
handling by default. You can still enable it on a per application basis as
described above. For more info on the change see [the news
entry](../news.md#2024-11-03-disabling-mingw-w64-wildcard-support-by-default).
