# PKGBUILD

PKGBUILD is the Arch Linux package build description file, which we inherit by
using pacman. See https://man.archlinux.org/man/PKGBUILD.5 for details on the
format.

We have some minor extensions to the format, which are documented here.

## Extra Metadata

Variables starting with `msys2_` and `mingw_` can be used to add additional metadata to a package, which will be read and used by our tools. The following datatypes are supported:

* Strings: `msys2_myvar="example"` 🠆 `{"myvar": "example"}`
* Arrays of strings: `msys2_myvar=("example1" "example2")` 🠆 `{"myvar": ["example1", "example2"]}`
* Mappings of strings to an optional string, separated by `":"`, values are
  stripped: `msys2_myvar=("example1: value1" "example2")` 🠆 `{"myvar": {"example1": "value1", "example2": null}}`
* Booleans (either `true` or `false`): `msys2_myvar=true` 🠆 `{"myvar": true}`

The following variables are recognized:

* `mingw_arch` - array - a list of MSYS2 environments the package is built
  for. Defaults to an empty list.
* `msys2_internal` - boolean - whether the package is an internal or meta
  package, and shouldn't be linked to external sources. Defaults to `false`.
* `msys2_references` - mapping - maps the package to external resources, for
  example other package repositories. Defining a key without a value means there
  is no mapping. The following keys exist:
    * `archlinux` - the Arch Linux package name: https://archlinux.org/packages/
    * `aur` - the AUR package name: https://aur.archlinux.org/packages
    * `cygwin` - the cygwin package name: https://cygwin.com/packages/src_package_list.html
    * `cygwin-mingw64` -
      the cygwin package name for all packages starting with "mingw64-x86_64-",
      minus that prefix: https://cygwin.com/packages/src_package_list.html
    * `pypi` - the PyPI project name: https://pypi.org/search/
* `msys2_changelog_url` - string -  NEWS file in git or the github releases page. In
  case there are multiple, the one that is more useful for packagers
* `msys2_documentation_url` - string - Documentation for the API, tools, etc. provided,
  in case it's a different website than the homepage.
* `msys2_repository_url` - string - Web view of the repository, e.g. on github or gitlab
* `msys2_issue_tracker_url` - string - The bug tracker, mailing list, etc.
* `msys2_pgp_keys_url` - string - A website containing which keys are used to sign releases
