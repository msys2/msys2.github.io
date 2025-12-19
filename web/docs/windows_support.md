# Supported Windows Versions and Hardware

We try to cater to two different types of users for our pre-built packages:

* **Developers using MSYS2 directly:** These users generally prefer the latest software and updates, typically using newer hardware and keeping their Windows operating system updated.
* **End-users of bundled applications:** These applications include pre-built packages from the MSYS2 repository, and the users may run [very outdated versions of Windows on equally outdated hardware](https://data.firefox.com/dashboard/hardware).

In some cases we can't please both groups at the same time, so we have to find compromises.

## Current Policy

**The GUI Installer:** Requires 64-bit Windows 10 (1809+) / Windows Server 2019.

**Msys/Cygwin Packages**: Requires 64-bit Windows 8.1 / Windows Server 2012 R2.

**Mingw Packages**: Requires 64-bit Windows 8.1 / Windows Server 2012 R2.
Upstream software may impose additional requirements.

**Mingw Toolchains**: MINGW32/MINGW64 environments allow targeting Windows 7+ still. All others allow targeting Windows 8.1+.

**Hardware Requirements**: We try to follow the minimum hardware requirements of the oldest Windows versions we support. Upstream software may impose additional requirements.

## Resources for Unsupported Windows Versions

We no longer support these configurations, but here's a list of resources that might help you get things running either way.

**GUI Installer on Windows Server 2016 / Windows 10 (1607)**: The last GUI installer version that worked on Windows Server 2016 and Windows 10 (1607) is
[2024-12-08](https://github.com/msys2/msys2-installer/releases/tag/2024-12-08). Use the old installer and then use [pacman to update](./updating.md).

**GUI Installer on Windows 8.1**: The last GUI installer version that worked on Windows 8.1 is
[2024-01-13](https://github.com/msys2/msys2-installer/releases/tag/2024-01-13). Use the old installer and then use [pacman to update](./updating.md).

**Windows 7 and 8.0**: The last installer version that worked on Windows 7 and 8.0 is [2022-10-28](https://github.com/msys2/msys2-installer/releases/tag/2022-10-28). Switching to [msys2-runtime-3.4](https://packages.msys2.org/base/msys2-runtime-3.4) should keep the Cygwin parts working. Many Mingw packages will no longer work though (Python for example).

**32-bit Windows**: The last working archive is available at https://repo.msys2.org/distrib/i686 and there is a community maintained repo at https://github.com/jeremyd2019/msys2-build32 (no longer updated since 2025-11)

## Changelog

Various changes affecting the supported Windows versions and hardware for both pre-built packages and programs built using our toolchains.

**2025-11-18**: The community maintained 32-bit MSYS2 repo at
https://github.com/jeremyd2019/msys2-build32 is [no longer
updated](https://github.com/jeremyd2019/msys2-build32/commit/82d133b596146ecddb89d5af8c3560b31e13f726).

**2025-02-21**: The GUI installer dropped support for running on Windows Server 2016 and Windows 10 versions older than 1809.

**2024-05-07**: The GUI installer dropped support for running on Windows 8.1.

**2024-05-03:** [msys2-runtime](https://packages.msys2.org/base/msys2-runtime)
was updated to Cygwin 3.5 which dropped support for Windows 7 and 8.0 and will no longer run there.

**2023-12-13:** We will no longer add new 32-bit Mingw packages to the repo unless needed, and will start dropping 32-bit packages without users.

**2023-01-15:** Dropped active support for Windows 7 and 8.0 in general.

**2022-12-26:** Default _WIN32_WINNT bumped to Windows 8.1 for UCRT environments. MINGW32/MINGW64 environments still default to Windows 7.

**2022-12-16:** The GUI installer dropped support for running on Windows 7 and 8.0.

**2022-10-18:** New minimum hardware requirements for pre-built packages matching the minimum requirements of Windows 8.1 (CPUs from ~2006/7+).

**2020-05-17:** 32-bit MSYS2 no longer actively supported. Both packages and the installer will no longer be updated.
