---
title: Environments
summary: The differences between the environments is
    mainly between environment variables, default compilers/linkers, architecture,
    system libraries used etc.
---

# Environments

MSYS2 comes with different environments/subsystems and the first thing you have
to decide is which one to use. The differences between the environments is
mainly between environment variables, default compilers/linkers, architecture,
system libraries used etc. If you are unsure, go with **MINGW64**.

The **MSYS** environment contains the unixy/cygwin based tools, lives under
`/usr` and is special in that it is always active. All the other environments
inherit from the **MSYS** one and add various things on top of it.

For example in the **MINGW64** environment your `$PATH` starts with
`/mingw64/bin:/usr/bin` so you get all mingw64 based tools as well as all msys
tools.

## Overview

|| Name | Prefix | Toolchain | Architecture | C Library | C++ Library |
| - |-  |-       |-|-|-|-|
| ![msys](msys.png){: style="max-width:25px" } | **MSYS** | `/usr` | gcc | x86_64 | cygwin | libstdc++ |
| ![mingw64](mingw64.png){: style="max-width:25px" } | **MINGW64** | `/mingw64` | gcc | x86_64 | msvcrt | libstdc++ |
| ![ucrt64](ucrt64.png){: style="max-width:25px" } | **UCRT64** | `/ucrt64` | gcc | x86_64 | ucrt | libstdc++ |
| ![clang64](clang64.png){: style="max-width:25px" } | **CLANG64** | `/clang64` | llvm | x86_64 | ucrt | libc++ |
| ![mingw32](mingw32.png){: style="max-width:25px" } | **MINGW32** | `/mingw32` |  gcc | i686  | msvcrt | libstdc++ |

## GCC vs LLVM/Clang

These are the default compilers/toolchains used for building all packages in the
respective repositories.

**GCC** based environments:

* Widely tested/used at this point
* Fortran support
* While there also exists a Clang package in the MINGW environments, that one
  still uses the GNU linker and the GNU C++ library. In some cases Clang is used
  to build packages as well there, in case upstream prefers Clang over gcc for
  example.

**LLVM/Clang** based environments:

* Only uses LLVM tools, LLD as a linker, LIBC++ as a C++ standard library
* Clang provides ASAN support
* Native TLS support
* LLD is faster than LD, but does not support all the features LD supports
* Some tools lack feature parity with equivalent GNU tools
* Supports ARM64 on Windows

## MSVCRT vs UCRT

These are two variants of the C standard library on Windows.

**MSVCRT** is available by default on all Windows versions, but due to backwards
compatibility issues is stuck in the past, not C99 compatible and is missing
some features.

* It isn't C99 compatible, for example the printf() function family, but...
* mingw-w64 provides replacement functions to make things C99 compatible in many
  cases
* It doesn't support the UTF-8 locale
* Because MSVC uses UCRT, and CRTs shouldn't be mixed, you can't mix it with
  libraries built with MSVC.
* Works out of the box on every Windows machine.

**UCRT** is a newer version which is also used by Visual Studio by default. It
should work and behave as if the code was compiled with MSVC.

* Better compatibility with MSVC, both at build time and at run time.
* It only ships by default on Windows 10 and for older versions you have to
  provide it yourself or depend on the user having it installed.
