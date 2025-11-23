# Package Guidelines

## Applying git patches

Git patches should be applied in `prepare()`. Since the build system doesn't have a committer configured and we generally try to avoid changing the git history because that distorts the input for a later `pkgver()` call, we apply patches without committing:

* Use `git apply` to apply a git patch without creating a commit
* In case of a git checkout use `git cherry-pick --no-commit` to backport a commit without creating a commit.

## Release Signing Keys

### What to do when a new release is signed with a new key?

Visit the upstream website or other official communication channels and verify that the new key is an official release signing key.

While at it you can also verify that `validpgpkeys` does not contain inactive signing keys. If a key in `validpgpkeys` seems unused, either because the person upstream switched to a new key, or if the key isn't listed upstream anymore please remove it from `validpgpkeys`.

## Python Packages

If possible we include ".pyc" and ".opt-1.pyc" for all .py files in all packages because:

* In case the package directory isn't writable to speed up the Python startup
* To avoid file conflicts when a package starts do create their own .pyc files while for the older version the user's Python created them at runtime.

.pyc files contain the absolute path of their respective Python source file for things like stack traces. Since our packages are relocatable there is no "right" path to store, so we just use the "unix" path, so something like `/ucrt64/lib/python3.10/site-packages/foo.py`.

To create such .pyc files in a PKGBUILD for packages which don't do it themselves you can use the following snippet:

```bash
MSYS2_ARG_CONV_EXCL="-p" \
  python -m compileall -o 0 -o 1 -q -s"${pkgdir}" -p"/" "${pkgdir}${MINGW_PREFIX}"
```

## The package prefix (hack)

When looking at some of our package recipes you might have seen something like:

```bash
MSYS2_ARG_CONV_EXCL="--prefix=" \
  meson \
    --prefix="${MINGW_PREFIX}" \
    ...
```

which results in `meson --prefix=/mingw64 ...` being executed.

`/mingw64` in this case is the UNIX prefix where the package will be installed
to and in addition is a valid Windows path (a drive relative path, so
`C:\mingw64`), so the native build tools will concatenate it with DESTDIR and
copy things to the right place.

In the native Windows world this path doesn't make much sense, as `C:\mingw64`
likely doesn't match where the software lives, but ideally all native Windows
tools are relocatable and won't use the prefix at runtime anyway. And if they do
and happen to call Cygwin tools then the prefix resolves to the correct path
because the Cygwin root path is relocatable.

## Why are some packages split up, while others are not?

In general, we try to avoid splitting packages unless there is a good reason to do so, in order to keep maintenance overhead low.

Reasons to split packages include:

- Large optional dependencies that most users do not need
- Large packages where users often only need a small subset of the functionality
- Development files that are not needed at runtime

We also try to avoid splitting packages into development ('\*-dev' or '\*-devel' packages in other distributions) and runtime parts, except for our Cygwin packages. All Cygwin packages that are part of the base installation are split to minimize the size of the installer. For consistency reasons, many other Cygwin packages are also split, but this is not strictly required.