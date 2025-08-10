# Updating an existing Package

In case you are looking for packages which need to be updated have a look at our
[Outdated Packages](https://packages.msys2.org/outofdate) page.

## Updating a Package

* Fork the [packages repository](https://github.com/msys2/MINGW-packages) if you
  haven't already and create a new branch for your update
* Look at the upstream changelog for potential update related information like
  new dependencies, changes to build options, changes to the build system, etc.
* Update pkgver in the PKGBUILD and reset pkgrel back to 1
* Run `updpkgsums` in the PKGBUILD directory for updating the checksums of the
  source files
* Run `makepkg-mingw --cleanbuild --syncdeps --force --install --noconfirm` to
  build and install the new version
* Test the new version, if possible
* Commit and push your changes and open a pull request. Try to include some
  brief information of your changes like why you added/removed patches, why you
  added/removed new dependencies, why you changed the build options etc.

If your lucky then this is all that's needed, but in some cases the new version
might need some additional work:

* In case there are patches that no longer apply they have to be refreshed
* In case some patches are no longer needed in the new version they have to be
  removed
* In case the release is signed by a new signing key the key has to be added to
  the `validpgpkeys` array
* In case of major changes, like a build system switch, consider comparing the
  old build result and the new build result for differences to avoid any
  regressions. [meld](https://packages.msys2.org/base/mingw-w64-meld3) can be a
  helpful tool for this.
* In case there are incompatible changes that might break reverse-dependencies
  (DLL name changes, ABI breaks, etc.) bump the pkgrel of all reverse
  dependencies and include them in your PR.

After you have submitted your pull request, our CI system will try to build the
package for all environments and do so some simple checks on it. After the
update is reviewed and merged you can follow the build process on our [Pending
Updates](https://packages.msys2.org/queue) status page.
