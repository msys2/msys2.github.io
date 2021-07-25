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
reproducible package building. Our package repository contains [more than 2000
pre-built packages](https://packages.msys2.org/base) ready to install.

For more details see ['What is MSYS2?'](docs/what-is-msys2.md) which also
compares MSYS2 to other software distributions and development environments like
[Cygwin](https://cygwin.com),
[WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux),
[Chocolatey](https://chocolatey.org/), [Scoop](https://scoop.sh/), ... and ['Who
Is Using MSYS2?'](docs/who-is-using-msys2.md) to see which projects are using
MSYS2 and what for.


## Installation

1. Download the installer: <a href="https://github.com/msys2/msys2-installer/releases/download/2021-07-25/msys2-x86_64-20210725.exe" class="button">msys2-x86_64-20210725.exe</a>

    <span style="opacity: 0.6;">Verify with SHA256 checksum `7e055b71306e64192e2612f959f54ae99a5cf57186206ac702d113ef00ba35c0`
    or [GPG signature](https://github.com/msys2/msys2-installer/releases/download/2021-07-25/msys2-x86_64-20210725.exe.sig)
    by [0xf7a49b0ec](http://keyserver.ubuntu.com/pks/lookup?search=0x0ebf782c5d53f7e5fb02a66746bd761f7a49b0ec&fingerprint=on&op=vindex).</span>

2. Run the installer. MSYS2 requires 64 bit Windows 7 or newer.

3. Enter your desired **Installation Folder** (short ASCII-only path on a NTFS volume, no accents, no spaces, no symlinks, no subst or network drives, no FAT).

    ![Second screen of MSYS2 installation](images/install-2-path.png)

4. When done, tick **Run MSYS2 now**.

    ![Third screen of MSYS2 installation](images/install-3-finish.png)

5. Update the package database and base packages.  Unless your setup file is very recent, it will take two steps.  First run `pacman -Syu`:

    ```
    $ pacman -Syu
    :: Synchronizing package databases...
     mingw32                        805.0 KiB
     mingw32.sig                    438.0   B
     mingw64                        807.9 KiB
     mingw64.sig                    438.0   B
     msys                           289.3 KiB
     msys.sig                       438.0   B
    :: Starting core system upgrade...
    warning: terminate other MSYS2 programs before proceeding
    resolving dependencies...
    looking for conflicting packages...
    
    Packages (6) bash-5.1.004-1  filesystem-2021.01-1
                 mintty-1~3.4.4-1  msys2-runtime-3.1.7-4
                 pacman-5.2.2-9  pacman-mirrors-20201208-1
    
    Total Download Size:   11.05 MiB
    Total Installed Size:  53.92 MiB
    Net Upgrade Size:      -1.24 MiB
    
    :: Proceed with installation? [Y/n]
    :: Retrieving packages...
     bash-5.1.004-1-x86_64            2.3 MiB
     filesystem-2021.01-1-any        33.2 KiB
     mintty-1~3.4.4-1-x86_64        767.2 KiB
     msys2-runtime-3.1.7-4-x86_64     2.6 MiB
     pacman-mirrors-20201208-1-any    3.8 KiB
     pacman-5.2.2-9-x86_64            5.4 MiB
    (6/6) checking keys in keyring       100%
    (6/6) checking package integrity     100%
    (6/6) loading package files          100%
    (6/6) checking for file conflicts    100%
    (6/6) checking available disk space  100%
    :: Processing package changes...
    (1/6) upgrading bash                 100%
    (2/6) upgrading filesystem           100%
    (3/6) upgrading mintty               100%
    (4/6) upgrading msys2-runtime        100%
    (5/6) upgrading pacman-mirrors       100%
    (6/6) upgrading pacman               100%
    :: To complete this update all MSYS2 processes including this terminal will be closed. Confirm to proceed [Y/n]
    ```

6. Run "MSYS2 MSYS" from Start menu.  Update the rest of the base packages with `pacman -Su`:

    ```
    $ pacman -Su
    :: Starting core system upgrade...
     there is nothing to do
    :: Starting full system upgrade...
    resolving dependencies...
    looking for conflicting packages...
    
    Packages (20) base-2020.12-1  bsdtar-3.5.0-1
                  [... more packages listed ...]
    
    Total Download Size:   12.82 MiB
    Total Installed Size:  44.25 MiB
    Net Upgrade Size:       3.01 MiB
    
    :: Proceed with installation? [Y/n]
    [... downloading and installation continues ...]
    ```

7. Now MSYS2 is ready for you.  You will probably want to install some tools and the mingw-w64 GCC to start compiling:

    ````
    $ pacman -S --needed base-devel mingw-w64-x86_64-toolchain
    warning: file-5.39-2 is up to date -- skipping
    [... more warnings ...]
    :: There are 48 members in group base-devel:
    :: Repository msys
       1) asciidoc  2) autoconf  3) autoconf2.13  4) autogen
       [... more packages listed ...]
    
    Enter a selection (default=all):
    :: There are 19 members in group mingw-w64-x86_64-toolchain:
    :: Repository mingw64
       1) mingw-w64-x86_64-binutils  2) mingw-w64-x86_64-crt-git
       [... more packages listed ...]
    
    Enter a selection (default=all):
    resolving dependencies...
    looking for conflicting packages...
    
    Packages (123) docbook-xml-4.5-2  docbook-xsl-1.79.2-1
                   [... more packages listed ...]
                   m4-1.4.18-2  make-4.3-1  man-db-2.9.3-1
                   mingw-w64-x86_64-binutils-2.35.1-3
                   mingw-w64-x86_64-crt-git-9.0.0.6090.ad98746a-1
                   mingw-w64-x86_64-gcc-10.2.0-6
                   mingw-w64-x86_64-gcc-ada-10.2.0-6
                   mingw-w64-x86_64-gcc-fortran-10.2.0-6
                   mingw-w64-x86_64-gcc-libgfortran-10.2.0-6
                   mingw-w64-x86_64-gcc-libs-10.2.0-6
                   mingw-w64-x86_64-gcc-objc-10.2.0-6
                   mingw-w64-x86_64-gdb-10.1-2
                   mingw-w64-x86_64-gdb-multiarch-10.1-2
                  [... more packages listed ...]
    
    Total Download Size:    196.15 MiB
    Total Installed Size:  1254.96 MiB
    
    :: Proceed with installation? [Y/n]
    [... downloading and installation continues ...]
    ````

8. To start building using the mingw-w64 GCC, close this window and run "MSYS MinGW 64-bit" from Start menu.  Now you can call `make` or `gcc` to build software for Windows.

9. Check out [the introduction page](wiki/MSYS2-introduction/) to learn which
   Start menu item to use when and which packages to install.  Take look at
   [Detailed MSYS2 install guide](wiki/MSYS2-installation/) for troubleshooting
   and additional details on how to keep your MSYS2 up-to-date.


## Sponsors

Our main server is sponsored by [appfleet.com](https://appfleet.com)

[![appfleet.com](appfleet.svg){: width=250px}](https://appfleet.com)


##  Authors and Contributors

* [Alexpux (Alexey Pavlov)](https://github.com/Alexpux)
* [martell (Martell Malone)](https://github.com/martell)
* [mingwandroid (Ray Donnelly)](https://github.com/mingwandroid)
* [Elieux (David Macek)](https://github.com/elieux)
* [lazka (Christoph Reiter)](https://github.com/lazka)
* [Renato Silva](https://github.com/renatosilva)
* [niXman](https://github.com/niXman)
* [naveen521kk (Naveen M K)](https://github.com/naveen521kk)
* [Biswa96 (Biswapriyo Nath)](https://github.com/Biswa96)
* [jeremyd2019 (Jeremy Drake)](https://github.com/jeremyd2019)
* [mati865 (Mateusz Mikuła)](https://github.com/mati865)

## Donations

#### Alexey Pavlov ([@alexpux](https://github.com/alexpux))

* WebMoney transfer to the following WebMoney wallets:
    * `E271473533800`
    * `R691797957081`
    * `Z110171850957`
* PayPal: [alexpux@gmail.com](https://www.paypal.com/donate/?business=alexpux%40gmail.com)
* Yandex.Money: `41001429355429`

#### Ray Donnelly ([@mingwandroid](https://github.com/mingwandroid))

See <https://www.msys2.org/news/#2021-04-21-rip-mingwandroid>

#### Christoph Reiter ([@lazka](https://github.com/lazka))

* GitHub Sponsors: https://github.com/sponsors/lazka
* PayPal: [reiter.christoph@gmail.com](https://www.paypal.com/donate?hosted_button_id=LDTZEZT6EXVEC)
