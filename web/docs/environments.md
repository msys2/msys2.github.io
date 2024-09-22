---
summary: The differences between the environments is
    mainly between environment variables, default compilers/linkers, architecture,
    system libraries used etc.
---

# Environments

MSYS2 comes with different environments and the first thing you have
to decide is which one to use. The differences among the environments are
mainly environment variables, default compilers/linkers, architecture,
system libraries used etc. If you are unsure, go with **UCRT64**.

The **MSYS** environment contains the unix-like/cygwin based tools, lives under
`/usr` and is special in that it is always active. All the other environments
inherit from the **MSYS** environment and add various things on top of it.

For example, in the **UCRT64** environment the `$PATH` variable starts with
`/ucrt64/bin:/usr/bin` so you get all ucrt64 based tools as well as all msys
tools.

## Overview

=== "Environments"

    |                                                          | Name           | Prefix        | Toolchain | Architecture | C Library | C++ Library |
    |----------------------------------------------------------|----------------|---------------|-----------|--------------|-----------|-------------|
    | ![msys](msys.png){: style="max-width:25px" }             | **MSYS**       | `/usr`        | gcc       | x86_64       | cygwin    | libstdc++   |
    | ![ucrt64](ucrt64.png){: style="max-width:25px" }         | **UCRT64**     | `/ucrt64`     | gcc       | x86_64       | ucrt      | libstdc++   |
    | ![clang64](clang64.png){: style="max-width:25px" }       | **CLANG64**    | `/clang64`    | llvm      | x86_64       | ucrt      | libc++      |
    | ![clangarm64](clangarm64.png){: style="max-width:25px" } | **CLANGARM64** | `/clangarm64` | llvm      | aarch64      | ucrt      | libc++      |
    | ![mingw64](mingw64.png){: style="max-width:25px" }       | **MINGW64**    | `/mingw64`    | gcc       | x86_64       | msvcrt    | libstdc++   |

=== "Legacy Environments"

    |                                                          | Name           | Prefix        | Toolchain | Architecture | C Library | C++ Library |
    |----------------------------------------------------------|----------------|---------------|-----------|--------------|-----------|-------------|
    | ![clang32](clang32.png){: style="max-width:25px" }       | **CLANG32**    | `/clang32`    | llvm      | i686         | ucrt      | libc++      |
    | ![mingw32](mingw32.png){: style="max-width:25px" }       | **MINGW32**    | `/mingw32`    | gcc       | i686         | msvcrt    | libstdc++   |

The active environment is selected via the `MSYSTEM` environment variable.
Setting `MSYSTEM` to `UCRT64` and starting a login shell will put you in that
environment.

## GCC vs LLVM/Clang

These are the default compilers/toolchains used for building all packages in the
respective repositories.

**GCC** based environments:

* Widely tested/used at this point
* Fortran support
* While there also exists a Clang package in the MINGW environments, that one
  still uses the GNU linker and the GNU C++ library. In some cases Clang is used
  to build packages as well there, in case upstream prefers Clang over GCC for
  example.

**LLVM/Clang** based environments:

* Only uses LLVM tools, LLD as a linker, LIBC++ as a C++ standard library
* Clang provides ASAN support
* Native support for TLS (Thread-local storage)
* LLD is faster than LD, but does not support all the features LD supports
* Some tools lack feature parity with equivalent GNU tools
* Supports ARM64/AArch64 architecture on Microsoft Windows 10

## MSVCRT vs UCRT

These are two variants of the C standard library on Microsoft Windows.

**MSVCRT** (Microsoft Visual C++ Runtime) is available by default on all
Microsoft Windows versions, but due to backwards compatibility issues is
stuck in the past, not C99 compatible and is missing some features.

* It isn't C99 compatible, for example the printf() function family, but...
* mingw-w64 provides replacement functions to make things C99 compatible in many
  cases
* It doesn't support the UTF-8 locale
* Binaries linked with MSVCRT should not be mixed with UCRT ones because the
  internal structures and data types are different. (More strictly, object
  files or static libraries built for different targets shouldn't be mixed.
  DLLs built for different CRTs can be mixed as long as they don't share
  CRT objects, e.g. `FILE*`, across DLL boundaries.) Same rule is applied for
  MSVC compiled binaries because MSVC uses UCRT by default (if not changed).
* Works out of the box on every version of Microsoft Windows.

**UCRT** (Universal C Runtime) is a newer version which is also used by
Microsoft Visual Studio by default. It should work and behave as if the
code was compiled with MSVC.

* Better compatibility with MSVC, both at build time and at run time.
* It is included as part of the operating system in Windows 10 or later,
  and Windows Server 2016 or later. For older Windows versions, you have to
  provide it explicitly or depend on the user having it installed. More
  information about that can be found in [UCRT deployment](https://learn.microsoft.com/en-us/cpp/windows/universal-crt-deployment).

## Changelog

**2023-12-13:** Start of phase out for 32-bit environments, MINGW32 and CLANG32. See [NEWS](../news.md#2023-12-13-starting-to-drop-some-32-bit-packages) for more information.

**2022-12-30:** Added CLANGARM64 environment.

**2022-10-29:** Changed the default environment from MINGW64 to UCRT64. See [NEWS](../news.md#2022-10-29-changing-the-default-environment-from-mingw64-to-ucrt64) for more information.

**2022-05-01:** Added CLANG32 environment.

**2021-03-26:** Added UCRT64 environment.

**2020-05-17:** Dropped 32-bit variant of the MSYS environment. See [NEWS](../news.md#2020-05-17-32-bit-msys2-no-longer-actively-supported) for more information.
