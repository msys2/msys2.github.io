# PKGBUILD

PKGBUILD is the Arch Linux package build description file, which we inherit by
using pacman. See https://man.archlinux.org/man/PKGBUILD.5 for details on the
format. We have some minor extensions to the format, which are documented here.

## Extra Metadata

Variables starting with `msys2_` and `mingw_` can be used to add additional metadata to a package, which will be read and used by our tools.
The following variables are recognized:

| Variable                   | Type    | Description |
|--------------------------- |---------|-------------|
| `mingw_arch`               | array   | A list of MSYS2 environments the package is built for. Defaults to an empty list. |
| `msys2_internal`           | boolean | Whether the package is an internal or meta package and shouldn't be linked to external sources. Defaults to `false`. |
| `msys2_references`         | mapping | Maps the package to external resources, such as other package repositories. |
| `msys2_changelog_url`      | string  | NEWS file in git or the GitHub releases page. In case there are multiple, the one that is more useful for packagers. |
| `msys2_documentation_url`  | string  | URL to the documentation for the API, tools, etc., in case it's a different website than the homepage. |
| `msys2_repository_url`     | string  | URL to the web view of the repository, e.g., on GitHub or GitLab. |
| `msys2_issue_tracker_url`  | string  | URL to the bug tracker, mailing list archive, etc. |
| `msys2_pgp_keys_url`       | string  | URL to a website containing which keys are used to sign releases. |

For `msys2_references` the following keys are recognized:

* `archlinux` - the Arch Linux package name: https://archlinux.org/packages/
* `aur` - the AUR package name: https://aur.archlinux.org/packages
* `cygwin` - the cygwin package name: https://cygwin.com/packages/src_package_list.html
* `cygwin-mingw64` -
  the cygwin package name for all packages starting with "mingw64-x86_64-",
  minus that prefix: https://cygwin.com/packages/src_package_list.html
* `pypi` - the PyPI project name: https://pypi.org/search/
* `gentoo` - the full Gentoo package name e.g. `dev-python/pyasn1`

Defining a key without a value means there is no mapping and the package shouldn't be linked.

The following datatypes are supported:

* **string:** `msys2_myvar="example"` 🠆 `{"myvar": "example"}`
* **array:** Arrays of strings: `msys2_myvar=("example1" "example2")` 🠆 `{"myvar": ["example1", "example2"]}`
* **mapping:** Mappings of strings to an optional string, separated by `":"`, values are
  stripped: `msys2_myvar=("example1: value1" "example2")` 🠆 `{"myvar": {"example1": "value1", "example2": null}}`
* **boolean:** either `true` or `false`: `msys2_myvar=true` 🠆 `{"myvar": true}`
