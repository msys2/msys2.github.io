---
title: Creating a Mirror
---

## Available Mirrors

The mirrors are defined in the [pacman-mirrors](https://github.com/msys2/MSYS2-packages/tree/master/pacman-mirrors) package.

## Creating a New Mirror

* The repository size is ~150 GiB (as of 2020/10)
* You can use rsync to update your mirror using `rsync -rtlvH --delete-after --delay-updates --safe-links`
* If you want to add your mirror to the main mirror list please open a PR against the [pacman-mirrors](https://github.com/msys2/MSYS2-packages/tree/master/pacman-mirrors) package

Our main repository supports rsync: `rsync://repo.msys2.org`

Some of the existing mirrors also support rsync:

* `rsync://mirror.yandex.ru/mirrors/msys2`
* `rsync://mirror.selfnet.de/msys2`
