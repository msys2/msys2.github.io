# Supported Windows Versions and Hardware

We try to cater to two different types of users for our pre-built packages:

* Developers using MSYS2 directly, who usually want the latest software and tend to use newer hardware and keep their Windows up to date.
* End users, who use bundled applications containing pre-built packages from the MSYS2 repository. They can use [very outdated Windows versions on very outdated hardware](https://data.firefox.com/dashboard/hardware).

In some cases we can't please both groups at the same time, so we have to find compromises.

## Msys Packages & the Installer

This includes the unixy environment and the GUI installer.

**Required Windows version:** 64bit Windows 8.1 / Windows Server 2012 R2

## Mingw Packages

This includes all packages that don't depend on Cygwin.

**Targeted Windows version (*):** Windows 8.1+

(*) If possible, depending on the upstream support. In some cases we can delay dropping support by staying on older versions/branches longer, or patching them, but that is not always practical or desirable.

## Supported Hardware

We try to follow the minimum hardware requirements of the Windows versions we support.

## Additional Resources

* [Windows 7 Support Dates](https://docs.microsoft.com/en-us/lifecycle/products/windows-7)
* [Windows 8 Support Dates](https://docs.microsoft.com/en-us/lifecycle/products/windows-8)
* [Windows 8.1 Support Dates](https://docs.microsoft.com/en-us/lifecycle/products/windows-81)
* [Windows 10 Support Dates](https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro)
* [Windows 11 Support Dates](https://learn.microsoft.com/en-us/lifecycle/products/windows-11-home-and-pro)
