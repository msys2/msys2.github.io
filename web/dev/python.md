# Python

* PKGBUILD: https://github.com/msys2/MINGW-packages/tree/master/mingw-w64-python
* Source: https://github.com/msys2-contrib/cpython-mingw

## Major Version Upgrade Workflow

* Create a new branch at https://github.com/msys2-contrib/cpython-mingw for the new version
* Copy the existing PKGBUILD to a "python3.x" and set `_primary_python=no`
* Test the new version (Windows 7 support?)
* Maybe wait for 3.x.1 / 2 for the initial issues to be ironed out
* Figure out which packages need to be rebuild:
    * Use https://github.com/jeremyd2019/package-grokker to detect dependencies on
      the .dll
    * `pacman -Fyqx '/python3\.9/' '.*\.pyc'` to detect the remaining packages
* Try to update packages that need to be rebuild to get potential Python related
  fixes.
* Move the PKGBUILD over to `mingw-w64-python` and make it the default one and
  rebuild all relevant packages
* Let autobuild handle the rest
