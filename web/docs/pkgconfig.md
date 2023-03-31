# pkg-config

We default to [pkgconf](https://github.com/pkgconf/pkgconf) as our pkg-config
implementation. This page lists some Windows specific topics/issues/challenges
for working with pkg-config on Windows.

## Environment Variables

By default, the MSYS2 shells set the following environment variables with paths for the active environment to support pkgconf:

* `PKG_CONFIG_PATH` - e.g. `/ucrt64/lib/pkgconfig:/ucrt64/share/pkgconfig`
* `PKG_CONFIG_SYSTEM_INCLUDE_PATH` - e.g. `/ucrt64/include`
* `PKG_CONFIG_SYSTEM_LIBRARY_PATH` - e.g. `/ucrt64/lib`

## Prefix / Relocation

The first few lines of a .pc file usually look something like this:

```bash
prefix=/ucrt64
includedir=${prefix}/include
libdir=${prefix}/lib
```

As you can see `/ucrt64` is not a proper Windows path, but that's not a problem
because by default `prefix` will be ignored, or rather re-defined by
pkgconf/pkg-config based on the location of the .pc file itself. It will strip
of `/<...>/pkgconfig` from the directory of the `.pc` file and use the resulting
path as the new `prefix` (as documented
[here](https://gitlab.freedesktop.org/pkg-config/pkg-config/-/blob/d97db4fae4c1cd099b506970b285dc2afd818ea2/README.win32#L17-22),
which is sightly outdated as the second parent doesn't have to be `(lib|share)`
but can be anything)

So if the file is at `C:/msys64/ucrt64/lib/pkgconfig/glib-2.0.pc` it will take
the directory `C:/msys64/ucrt64/lib/pkgconfig`, then strip of the last two
parts, leading to `C:/msys64/ucrt64` and use that as the new prefix. This way
you will get the right output independent of where MSYS2 is installed. You can
disable this feature by passing `--dont-define-prefix` to pkgconf if wanted.

Relocation depends on all other variables being relative to `prefix` by using
`${prefix}` like in the example above. But some projects use absolute paths and
in theory don't support relocation, which looks something like:

```bash
prefix=/ucrt64
includedir=/ucrt64/include
libdir=/ucrt64/lib
```

Luckily both pkg-config and pkgconf include a hack which replace all values that
start with the value of `prefix` with `${prefix}`, so `/ucrt64/include` becomes
`${prefix}/include`, making them relocatable anyway. So, despite `prefix`
normally being ignored it might still be useful for such broken `.pc` files.
Ideally all projects would only use relative paths, as absolute paths can also
lead to problems on other platforms, see
https://www.bassi.io/articles/2018/03/15/pkg-config-and-paths/.

The above relocation logic sadly breaks down when you install the `.pc` into a
different custom location, like `/lib/mylib-1.2/pkgconfig` as it will derive the
wrong `prefix` value for them. See https://github.com/pkgconf/pkgconf/issues/286
for a more detailed summary of the problem. The only workaround there is to
patch the `.pc` file with the wrong prefix in mind, like in this example:
https://github.com/msys2/MINGW-packages/blob/9d4a713ce27c363a0ec63877775e229e7e4f36cb/mingw-w64-ffmpeg4.4/PKGBUILD#L215-L217

## Syntax, Paths & Escaping

pkg-config values can be dumped as is into a Unix shell, so if you want to use
backslashes or spaces you need to escape them with `\`.  So for example:

```bash
mypath=C:\\my\ path\ with\ spaces\\file.txt
```

Since this is rather uncommon on Unix systems and tools might not expect it,
it's recommended to avoid spaces in paths and use forward slashes instead of
backslashes instead. Ideally both should work though.

## Cflags.private / Static Libraries

[pkgconf](https://github.com/pkgconf/pkgconf), unlike
[pkg-config](https://gitlab.freedesktop.org/pkg-config/pkg-config), supports an
additional field called `Cflags.private` which is especially relevant on
Windows.

Many projects require that you define a specific C macro when statically linking
against it on Windows, something like `-DMYLIB_STATIC`, or they define a macro
via `Cflags` and require that you unset it when linking statically like
`-UMYLIB_DLL`.

`Cflags.private` allows you to add extra CFLAGS that are only emitted via
`--cflags` when `--static` is passed, making static builds work automatically.

```console
$ pkgconf --cflags libxml-2.0
-IC:/msys64/ucrt64/include/libxml2
$ pkgconf --cflags --static libxml-2.0
-IC:/msys64/ucrt64/include/libxml2 -DLIBXML_STATIC
$ pkgconf --cflags x264
-DX264_API_IMPORTS
$ pkgconf --cflags --static x264
-DX264_API_IMPORTS -UX264_API_IMPORTS
```
