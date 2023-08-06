# Python

Since the official CPython implementation doesn't support building with GCC/Clang on Windows and has its own Windows specific directory layout, we maintain a friendly fork of CPython at https://github.com/msys2-contrib/cpython-mingw/

Some differences/features compared to the official Windows CPython:

* In an active MSYS2 environment `os.sep` and `os.altsep` are switched to make relative paths more compatible with Unix tools that don't understand Windows paths. Outside of an active MSYS2 environment it behaves normally though.
* `sys.path` uses the Unix directory layout, see `python -m site`
* Virtual environments also work with bash: `python -m venv _venv`, `source _venv/bin/activate` and so on.

### Portability

As long as you don't hardcode/assume platform specific values and paths and always use things like `os.sep`, do path operations with `os.path` or `pathlib` and derive Python installation related paths and configuration from the `sysconfig` module then your Python code should work just like with the official Windows CPython installation.

If for some reason you still need to detect our fork you can check for it as follows:

```python
import os
import sysconfig

if os.name == "nt" and sysconfig.get_platform().startswith("mingw"):
    print("cpython-mingw detected!")
```

Unlike many other Windows packages in MSYS2, Python will not look for DLL dependencies in PATH by default, but requires directories to be explicitly added via `os.add_dll_directory()` at runtime. You can disable this behavior, and make it look in PATH, by setting the `PYTHONLEGACYWINDOWSDLLLOADING` environment variable to `1`.

### Known issues

* C extensions are not compatible with the official CPython, which means pip can't use binary wheels from PyPI and packages have to be build when installing them.
* Some C extensions don't build out of the box since they don't expect non-MSVC on Windows. In some cases we provide patched versions in our repo.
* [setuptools](https://github.com/pypa/setuptools) >= 60.0 is currently incompatible with MSYS2. You can set `export SETUPTOOLS_USE_DISTUTILS=stdlib` to work around the issue. We are currently working on restoring compatibility.
