# C++

## Known Issues

The exception handling implementation used in the MINGW32 environment only works with a dynamically linked libgcc, so using `-static-libgcc` anywhere in your build will lead to broken exception handling (see https://gcc.gnu.org/bugzilla/show_bug.cgi?id=105507#c5). Other environments are not affected.