---
title: Creating a Mirror
---

## Available Mirrors

The mirrors are defined in the [pacman-mirrors](https://github.com/msys2/MSYS2-packages/tree/master/pacman-mirrors) package.

## Creating a New Mirror

The repository size is ~150 GiB (as of 2021/01) with the distribution of sizes like this:

```
-100B:  ~1000 files
  -1K: ~13000 files
 -10K:   ~200 files
-100K:  ~3000 files
  -1M:  ~5000 files
 -10M:  ~4000 files
-100M:  ~1000 files
  -1G:   ~200 files
 -10G:    ~20 files
```

* You can use rsync to update your mirror using `rsync -rtlvH --delete-after --delay-updates --safe-links`
* If you want to add your mirror to the main mirror list please open a PR against the [pacman-mirrors](https://github.com/msys2/MSYS2-packages/tree/master/pacman-mirrors) package

Our main repository supports rsync: `rsync://repo.msys2.org/builds`

Some of the existing mirrors also support rsync:

* `rsync://mirror.yandex.ru/mirrors/msys2`
* `rsync://mirror.selfnet.de/msys2`

