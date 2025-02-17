# PKGBUILD

PKGBUILD is the Arch Linux package build description file, which we inherit by
using pacman. See https://man.archlinux.org/man/PKGBUILD.5 for details on the
format. We have some minor extensions to the format, which are documented here.

## Extra Metadata

Variables starting with `msys2_` and `mingw_` can be used to add additional metadata to a package, which will be read and used by our tools.
The following variables are recognized:

| Variable                       | Type    | Description                                                                                                          |
|--------------------------------|---------|----------------------------------------------------------------------------------------------------------------------|
| `mingw_arch`                   | array   | A list of MSYS2 environments the package is built for. Defaults to an empty list.                                    |
| `msys2_references`             | mapping | Maps the package to external resources, such as other package repositories.                                          |
| `msys2_changelog_url`          | string  | NEWS file in git or the GitHub releases page. In case there are multiple, the one that is more useful for packagers. |
| `msys2_documentation_url`      | string  | URL to the documentation for the API, tools, etc., in case it's a different website than the homepage.               |
| `msys2_repository_url`         | string  | URL to the web view of the repository, e.g., on GitHub or GitLab.                                                    |
| `msys2_issue_tracker_url`      | string  | URL to the bug tracker, mailing list archive, etc.                                                                   |
| `msys2_pgp_keys_url`           | string  | URL to a website containing which keys are used to sign releases.                                                    |
| `msys2_ignore_vulnerabilities` | array   | A list of CVE and/or GHSA IDs which should be ignored.                                                               |

For `msys2_references` the following keys are recognized:

* `archlinux` - the Arch Linux package name: https://archlinux.org/packages/
* `aur` - the AUR package name: https://aur.archlinux.org/packages
* `cygwin` - the cygwin package name: https://cygwin.com/packages/src_package_list.html
* `cygwin-mingw64` -
  the cygwin package name for all packages starting with "mingw64-x86_64-",
  minus that prefix: https://cygwin.com/packages/src_package_list.html
* `gentoo` - the full Gentoo package name e.g. `dev-python/pyasn1`
* `internal` - special key, which if it exists marks the package as internal and doesn't link it to any external sources
* `purl` - a [package URL](https://github.com/package-url/purl-spec). Multiple PURLs supported. Versions are optionally supported, and useful in case the upstream version is different from the package version. Some common PURL types:
  * [pypi](https://github.com/package-url/purl-spec/blob/master/PURL-TYPES.rst#pypi) - example: `pkg:pypi/jinja2` or `pkg:pypi/@3.1.5` - make sure to [normalize](https://packaging.python.org/en/latest/specifications/name-normalization) the package name
  * [cargo](https://github.com/package-url/purl-spec/blob/master/PURL-TYPES.rst#cargo) - example: `pkg:cargo/ripgrep` or `pkg:cargo/ripgrep@14.1.1`
  * [gem](https://github.com/package-url/purl-spec/blob/master/PURL-TYPES.rst#gem) - example: `pkg:gem/asciidoctor`
  * [github](https://github.com/package-url/purl-spec/blob/master/PURL-TYPES.rst#github) - example: `pkg:github/curl/curl` or `pkg:github/curl/curl@curl-8_12_1`
  * ...
* `cpe` - a [CPE](https://en.wikipedia.org/wiki/Common_Platform_Enumeration) prefix, either in the 2.2 format (`cpe: cpe:/a:gnu:gcc`) or the 2.3 format (`cpe:2.3:a:gnu:gcc`). `version`, `target_sw` etc are currently not supported. Multiple CPEs supported.

Defining a key without a value means there is no mapping and the package shouldn't be linked.

The following datatypes are supported:

* **string:** `msys2_myvar="example"` 🠆 `{"myvar": "example"}`
* **array:** Arrays of strings: `msys2_myvar=("example1" "example2")` 🠆 `{"myvar": ["example1", "example2"]}`
* **mapping:** Mappings of strings to optional other strings, separated by `":"`, values are
  stripped: `msys2_myvar=("example1: value1" "example2")` 🠆 `{"myvar": {"example1": ["value1"], "example2": [null]}}`
* **boolean:** either `true` or `false`: `msys2_myvar=true` 🠆 `{"myvar": true}`

## Changelog

**2025-02-17:** Added support for the `version` component in `purl` entries, for example `purl: pkg:pypi/jinja2@3.1.5`.

**2025-02-17:** Removed support for `pypi` in `msys2_references`, use `purl` with the `pypi` type instead, for example `purl: pkg:pypi/jinja2` instead of `pypi: jinja2`.