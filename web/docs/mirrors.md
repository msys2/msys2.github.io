# Package Mirrors

MSYS2 uses multiple mirror servers around the world to distribute packages. By default, when you install or update packages, pacman automatically selects the best available mirror to download from.

## How Mirrors Work

By default, pacman tries mirrors in the order listed in these files:

- `/etc/pacman.d/mirrorlist.mingw` (for mingw packages)
- `/etc/pacman.d/mirrorlist.msys` (for msys packages)

The first entry `mirror.msys2.org` is a special geo-redirector that automatically sends you to the nearest tier 1 mirror. The second entry is `repo.msys2.org`, which is the main package server. Everything else in the lists are [third-party mirrors](../dev/mirrors.md).

## Changing Your Mirror

To use a specific mirror:

1. Edit `/etc/pacman.d/mirrorlist.mingw` and `/etc/pacman.d/mirrorlist.msys`
2. Move your preferred mirror to the top of the list
3. Or comment out unwanted mirrors with `#`

## Corporate Firewalls and Restricted Networks

If you're behind a firewall that blocks most internet access:

1. Ask your IT team to allowlist `repo.msys2.org` or any other specific mirrors you want to use.
2. Edit your mirrorlist files to use only that mirror:

   ```
   Server = https://repo.msys2.org/mingw/$arch/
   Server = https://repo.msys2.org/msys/$arch/
   ```

`mirror.msys2.org` is not suitable for firewalls because it redirects to various mirrors, which may not be allowlisted.

## Privacy and Logging

Information about what data is transmitted to mirrors and how it's used can be found on the [Privacy page](../privacy.md).
