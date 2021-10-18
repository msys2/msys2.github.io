---
title: Using CMake in MSYS2
summary: There are a few gotchas regarding how to use CMake in MSYS2.
---
# Using CMake in MSYS2

## Installing

When building projects for Windows with CMake (as opposed to
building projects that are going to run in MSYS2 posix emulation runtime)
make sure to install the MinGW version of CMake, i.e. installing
e.g. `mingw-w64-x86_64-cmake`.

You also want to install a tool for actually doing the build. The
current recommended default is Ninja, which you can install from the
`mingw-w64-x86_64-ninja` package.

(Other alternatives are `make` or `mingw-w64-x86_64-make`, for building
with GNU Make running either as a MSYS2 or MinGW process.)

## Building

When running the CMake configuration command, it's recommended to explicitly
specify the desired build file generator with the `-G` option. MSYS2
provided CMake defaults to Ninja (but this is not the default in upstream
CMake, so it's safest to explicitly specify it).

Thus, to configure and build a CMake based project, you can run the
following commands:

```shell
$ cmake -G Ninja <path-to-source> -DCMAKE_BUILD_TYPE=Release
$ cmake --build .
```

The relevant generator alternatives are:

* `-G Ninja`
* `-G "MSYS Makefiles"`
* `-G "MinGW Makefiles"`

If building by invoking `cmake --build`, the same command works for all
generator choices. Alternatively, to build by directly invoking the
build tool, you can call `ninja`, `make` or `mingw32-make` respectively
for those three alternatives.

## Examples

For building projects with CMake in MSYS2 in Github Actions, see the
[CMake Example](https://github.com/msys2/setup-msys2/blob/master/examples/cmake.yml).
