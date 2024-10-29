# C/C++

## Expanding wildcard arguments

For making your program accept wildcard arguments, the official MSVC way is to
link [w]setargv.obj to your program. By default it is not enabled. For more
details see
https://learn.microsoft.com/en-us/cpp/c-language/expanding-wildcard-arguments

With mingw-w64, there are three ways wildcard expansion can be configured:

1. mingw-w64 can be configured at build time to either enable or disable wildcard expansion by default via the `--enable-wildcard` configure flags. This can to be overridden on a per .exe basis by the user.

    Currently wildcard expansion is enabled by default in MSYS2.

2. You can set `_dowildcard` in your source code to either `0` or `-1` to disable or enable wildcard expansion.

    ```c
    // To force-enable wildcard expansion
    int _dowildcard = -1;
    // To force-disable wildcard expansion
    int _dowildcard = 0;
    ```

3. You can link in `CRT_noglob.o` or `CRT_glob.o` to disable or enable wildcard expansion, respectively. This will error out if `_dowildcard` is already set in the source.

    ```bash
    # To enable force-enable wildcard expansion
    cc main.c $(cc -print-file-name=CRT_glob.o)
    # To force-disable wildcard expansion
    cc main.c $(cc -print-file-name=CRT_noglob.o)
    ```
