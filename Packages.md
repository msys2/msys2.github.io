#!/bin/sh

###### This is a pacman dump of all the packages we provide as of _-_. The commands used to re-generate this list are listed below.

    LANG=C
    {
      cat "$0" | sed -r \
        -e "s/_([0-9-]+)_/_$(date +%Y-%m-%d)_/" \
        -e '/^## /q'
      echo
      {
        pacman -Ss | grep '^mingw64/' -A 1
        pacman -Ss | grep '^msys/' -A 1
      } | sed -r \
         -e 's/ \[installed.*\]//' \
         -e 's#^mingw64/([^ ]+)#<br/>mingw/<b>\1</b>#' \
         -e 's#^msys/([^ ]+)#<br/>msys/<b>\1</b>#' \
         -e 's/-x86_64//' \
         -e 's/$/<br\/>/' \
         -e 's/~/:/'
    } > "$0_"
    mv "$0_" "$0"
    exit

## The list

There is [a nicer package list on packages.msys2.org](https://packages.msys2.org/base).
