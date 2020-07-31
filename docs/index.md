!!! hint

    In case you are experiencing **signature errors** when using pacman you will
    have to manually install a new keyring package. Please follow [the instructions
    in our news section](./news.md#2020-06-29-new-packagers).

<header>
<h1>MSYS2</h1>
<h2>Software Distribution and Building Platform for Windows</h2>
</header>

**MSYS2** is a collection of tools and libraries providing you with an
easy-to-use environment for building, installing and running native Windows
software.

It consists of a command line terminal called
[mintty](https://mintty.github.io/), bash, version control systems like git and
subversion, tools like tar and awk and even build systems like autotools, all
based on a modified version of [Cygwin](https://cygwin.com). Despite some of
these central parts being based on Cygwin, the main focus of MSYS2 is to provide
a build environment for native Windows software and the Cygwin-using parts are
kept at a minimum. MSYS2 provides up-to-date native builds for GCC, mingw-w64,
CPython, CMake, Meson, OpenSSL, FFmpeg, Rust, Ruby, just to name a few.

To provide easy installation of packages and a way to keep them updated it
features a package management system called
[Pacman](https://wiki.archlinux.org/index.php/pacman), which should be familiar
to Arch Linux users. It brings many powerful features such as dependency
resolution and simple complete system upgrades, as well as straight-forward and
reproducible package building. Our package repository contains [more than 1800
pre-built packages](https://packages.msys2.org/base) ready to install.

For more details see ['What is MSYS2?'](docs/what-is-msys2.md) which also
compares MSYS2 to other software distributions and development environments like
[Cygwin](https://cygwin.com),
[WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux),
[Chololatey](https://chocolatey.org/), [Scoop](https://scoop.sh/), ... and ['Who
Is Using MSYS2?'](docs/who-is-using-msys2.md) to see which projects are using
MSYS2 and what for.


## Installation

1. Download the installer: <a href="https://repo.msys2.org/distrib/x86_64/msys2-x86_64-20200720.exe" class="button">msys2-x86_64-20200720.exe</a>

    <span style="opacity: 0.6;">SHA256 checksum: `ad6b58b355a852d9df7c6dc2722d0eca139042cf262ae7363e0a5e7dd2a6c5c9`</span>

2. Run the installer. MSYS2 requires 64 bit Windows 7 or newer.
3. Click **"Next"**

    ![First screen of MSYS2 installation](images/1_msys32-start.png)

4. Enter **Installation Folder** (ASCII, no accents, spaces nor symlinks, short path)

    ![Second screen of MSYS2 installation](images/2_msys32-install_path.png)

5. Tick **Run MSYS2 now**

    ![Third screen of MSYS2 installation](images/5_msys2-finish_install.png)

6. Update the package database and core system packages with:

    ```
    pacman -Syu
    ```

    ![MSYS2 shell with pacman's output about system upgrade](images/6_msys2-update-system.png)

7. If needed, close MSYS2, run it again from Start menu. Update the rest with:

    ```
    pacman -Su
    ```

8. Now **Pacman** is fully committed to the Windows cause :)

    ![MSYS2 shell with pacman's output about package installation](images/7_msys2-install-freely.png)

9. Take look at [Detailed MSYS2 install guide](wiki/MSYS2-installation.md) for
   troubleshooting and additional details on how to keep your MSYS2 up-to-date.

##  Authors and Contributors

* [Alexpux (Алексей)](https://github.com/Alexpux)
* [martell (Martell Malone)](https://github.com/martell)
* [mingwandroid (Ray Donnelly)](https://github.com/mingwandroid)
* [Elieux (David Macek)](https://github.com/elieux)
* [lazka (Christoph Reiter)](https://github.com/lazka)
* [Renato Silva](https://github.com/renatosilva)
* [niXman](https://github.com/niXman)

## Support and Contact

*   read our [wiki](https://www.msys2.org/wiki/Home/)
*   browse our [package lists](https://packages.msys2.org/)
*   search for and file [issues for msys2 packages on GitHub](https://github.com/msys2/msys2-packages/issues)
*   search for and file [issues for mingw-w64 packages on GitHub](https://github.com/msys2/mingw-packages/issues)
*   search for very old [tickets on SourceForge](https://sourceforge.net/p/msys2/tickets/)
*   read and post to our [mailing list](https://sourceforge.net/p/msys2/mailman/msys2-users/)
*   talk on our [IRC channel](irc://irc.oftc.net:6667/msys2)
*   talk in our [Gitter room](https://gitter.im/msys2/msys2)
*   read older [discussion on SourceForge](https://sourceforge.net/p/msys2/discussion/general/)
*   more links on our [developer homepage on GitHub](https://github.com/msys2/msys2)

## Donations

#### Alexey Pavlov ([@alexpux](https://github.com/alexpux))

Webmoney transfer to the following webmoney wallets:

* E271473533800
* R691797957081
* Z110171850957

To Paypal account: alexpux@gmail.com

To yandex.money: 41001429355429

#### Ray Donnelly ([@mingwandroid](https://github.com/mingwandroid))

PayPal:

<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
              <input type="hidden" name="cmd" value="_s-xclick">
              <input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----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-----END PKCS7-----
                ">
              <input type="image" src="https://www.paypalobjects.com/en_US/GB/i/btn/btn_donateCC_LG.gif" name="submit" alt="PayPal – The safer, easier way to pay online." border="0">
              <img alt="" src="https://www.paypalobjects.com/en_GB/i/scr/pixel.gif" style="display: none !important;" width="1" hidden="" height="1" border="0">
</form>
