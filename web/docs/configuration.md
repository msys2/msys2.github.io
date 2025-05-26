# Configuration Locations

Cygwin packages, like openssh and git, follow the standard Unix conventions and
use your `$HOME` or `$HOME/.config` directory for storing the user configuration
and `/etc` for the system configuration.

For native Windows programs the situation is a bit more complicated. For the
user configuration some programs use the standard Windows paths, such as
`%USERPROFILE%\AppData\Roaming`. In some cases native Windows programs are
minimally ported from Unix and will write to `%USERPROFILE%\.appname` or
`%USERPROFILE%\.config\appname`, or they will prefer the `HOME` environment
variable over `USERPROFILE` and store their configuration in `$HOME\.appname` or
`$HOME\.config\appname` like their Unix variants. For the system configuration
some programs might store them alongside their other data files or in case they
were ported from Unix they might follow the Unix layout and store things in
`$MINGW_PREFIX/etc/appname`

## FAQ

**Can't all programs use the same location for their user configuration?**

While having two locations for configuration can be confusing we want native
programs to follow Windows conventions and be independent from MSYS2. Also we
don't want to change the behavior of programs compared to their upstream
versions unless we have to.

That said, sharing the location for multiple installation of applications is
still possible, in the sense that:

* Packages with different prefixes may share the same configuration \
location (as the default of some native x86/x64 Win32 applications).
* The shared location is not actively checked against by the runtime, so it
is possible to have different path pointing to the same file system location
and the applications *may* actually work.

Shared location can be implemented by setting the value of `HOME` environment
varible (which can be interited from Windows environment) or symbolic link
on directories, for instance. This is not normally supported. Individual
applications may fail because they do not expect the configuration being
shared (e.g. a Unix application may be only compatible to LF as line endings
in its configuration files, and it will fail to parse CR+LF line endings
written by a Win32 native application). Some applications (like
[Mercurial](https://www.mercurial-scm.org/doc/hgrc.5.html)) have different
search paths for Win32/Unix environments. However, such layout may be useful
for testing. Use with your own risks when you really know the consequences.
