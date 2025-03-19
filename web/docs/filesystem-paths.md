---
summary: Many of our build processes are made up of a mix of Cygwin tools (makepkg/bash for starters) 
    and native Windows tools.
---
# Filesystem Paths

Many of our build processes are made up of a mix of Cygwin tools (makepkg/bash for
starters) and native Windows tools. When building things the paths of input and
output files and directories are often communicated between them via process
arguments or environment variables. The problem here is that those are in many
cases not compatible:

* `C:\nope` is not a valid Unix path and `\n` might make problems when being
  interpreted as an escape sequence.
* `C:/nope` is slightly better, because, while it's not a valid Unix path, if
  it's just forwarded to some other Windows tools things might work out fine.
* `/foo` is both a valid Windows path (drive relative path evaluating to
  `C:\foo` for example) and a valid Unix path, but resolves to a different path.
  Again, if it's just forwarded to some other Unix tool then things might work
  out fine.
* `foo/bar.txt` just works, relative to the current working directory, while
  `foo\bar.txt` is only OK with native tools.
* Path lists, commonly used in environment variables like `FOO=/foo:/bar` also
  will never work, since paths are separated by `;` on Windows and not `:`,
  similarly `c:/foo` could be interpreted as a Unix path list containing `c` and
  `/foo` when a path list is expected.

The only solution here is to avoid mixing Unix/Cygwin and native tools outside
of makepkg (preferred) or convert them when they get passed between the
different programs. For the latter MSYS2 provides an automatic conversion that
just works automatically in many cases.

## Manual Unix ⟷ Windows Path Conversion

MSYS2 ships the Cygwin tool `cygpath` by default which allows converting paths
between the Unix format, Windows format, and mixed format, see `cygpath --help`
for details.

```shell
$ cygpath -u C:\\foo
/c/foo
$ cygpath -m /mingw64/bin
C:/msys64/mingw64/bin
$ cygpath -w /mingw64/bin
C:\msys64\mingw64\bin
```

## Automatic Unix ⟶ Windows Path Conversion

### Process Arguments

When calling native executables from the context of Cygwin then all the
arguments that look like Unix paths will get auto converted to Windows. For
example when calling native Python from the context of bash:

```shell
$ python3 -c "import sys; print(sys.argv)" --dir=/foo
['-c', '--dir=C:/msys64/foo']
$ python3 -c "import sys; print(sys.argv)" --dir=/foo:/bla
['-c', '--dir=C:\\msys64\\foo;C:\\msys64\\bla']
```

While this is helpful in many cases it's also not perfect and in corner cases
converts arguments that look like Unix paths while they are not, or detects
lists of Unix paths where there are none. For these cases you can exclude
certain arguments via the `MSYS2_ARG_CONV_EXCL` environment variable:

```shell
$ MSYS2_ARG_CONV_EXCL='--dir=' python3 -c "import sys; print(sys.argv)" --dir=/foo
['-c', '--dir=/foo']
```

`MSYS2_ARG_CONV_EXCL` can either be `*` to mean exclude everything, or a list of
one or more arguments prefixes separated by `;`, like
`MSYS2_ARG_CONV_EXCL=--dir=;--bla=;/test`. It matches the prefix against the
whole argument string.

### Environment Variables

Similar to process arguments, paths in environment variables get converted too:

```shell
$ MYVAR=/foo python3 -c "import os; print(os.environ['MYVAR'])"
C:/msys64/foo
$ MYVAR=/foo:/bar python3 -c "import os; print(os.environ['MYVAR'])"
C:\msys64\foo;C:\msys64\bar
```

You can disable the conversion with `MSYS2_ENV_CONV_EXCL`:

```
$ MSYS2_ENV_CONV_EXCL='MYVAR' MYVAR=/foo python3 -c "import os; print(os.environ['MYVAR'])"
/foo
```

`MSYS2_ENV_CONV_EXCL` can either be `*` to mean exclude everything, or a list of
one or more environment variable prefixes separated by `;`, like
`MSYS2_ENV_CONV_EXCL=FOO;BAR;/test`. It matches the prefix against the following
string `KEY=VALUE`.

Cygwin special cases some environment variables that are known to be paths or
path lists and does less guessing with them. For example `HOME` will never be
interpreted as a path list even if it contains `:`.

## Windows ⟶ Unix Path Conversion

You might wonder why calling things like `ls C:/` might work and suspect that
again auto conversion is used, but that's not the case:

```shell
$ /usr/bin/python3 -c "import sys, os; print(sys.argv, os.listdir(sys.argv[1]))" C:/
['-c', 'C:/'] ['$Recycle.Bin', '$SysReset', ...]
```

Cygwin which provides the POSIX API will just forward the paths to the Windows
API as is. This works as long as the tool does not try to interpret the path too
much and just forwards it to the system API. If that doesn't work in your case
you can use `cygpath`:

```shell
$ /usr/bin/python3 -c "import sys, os; print(sys.argv, os.listdir(sys.argv[1]))" "$(cygpath -u C:/)"
['-c', '/c/'] ['$Recycle.Bin', '$SysReset', ...]
```
