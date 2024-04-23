# Mirrors

Our [main repo server](https://repo.msys2.org/) is located in Germany and
contains the pacman databases and packages, matching source packages and
installers. The whole content of the mirror is regularly synced to multiple
mirrors across the world.

All these servers are registered with pacman under `/etc/pacman.d/mirrorlist.*`.
The first URL in those lists is the primary mirror, all others will be used as a
fallback. You can make another mirror the primary one by moving it to the top.

In case you have problems with a particular mirror please let us know by filing
an issue: https://github.com/msys2/msys2.github.io/issues

## Primary Server

| Name | URL | Note |
| -    | -   | -    |
| repo.msys2.org | [HTTPS](https://repo.msys2.org/) \| [RSYNC](rsync://repo.msys2.org/builds/) | primary |
| mirror.msys2.org | [HTTPS](https://mirror.msys2.org/) | geo redirection service for Tier 1 mirrors |

## Tier 1 Mirrors

**Requirements:** Reliable, 1GBit/s+ with enough free bandwidth, rsync server
support (\*), HTTPS support, synced at least once per day from the primary server.

**Map**: <https://mirror.msys2.org/?mirrorstats>

| Name | URLs  |  Note |
| -    | -     | -     |
| mirror.umd.edu | [HTTPS](https://mirror.umd.edu/msys2/) \| [RSYNC](rsync://mirror.umd.edu/msys2/) | [website](https://mirror.umd.edu/)|
| ftp.acc.umu.se | [HTTPS](https://ftp.acc.umu.se/mirror/msys2.org/) \| [RSYNC](rsync://ftp.acc.umu.se/mirror/msys2.org/) | <ftp-adm@acc.umu.se> |
| ftp.nluug.nl | [HTTPS](https://ftp.nluug.nl/pub/os/windows/msys2/builds/) \| [RSYNC](rsync://ftp.nluug.nl/msys2/builds/) | <ftp-admin@nluug.nl> |
| ftp.osuosl.org | [HTTPS](https://ftp.osuosl.org/pub/msys2/) \| [RSYNC](rsync://rsync.osuosl.org/msys2/) | <hosting-request@osuosl.org> | |
| mirror.internet.asn.au | [HTTPS](https://mirror.internet.asn.au/pub/msys2/) \| [RSYNC](rsync://mirror.internet.asn.au/msys2/) |  <peering@ix.asn.au> |
| mirror.selfnet.de | [HTTPS](https://mirror.selfnet.de/msys2/) \| [RSYNC](rsync://mirror.selfnet.de/msys2/) | [admin](https://github.com/carrotIndustries) |
| mirror.yandex.ru | [HTTPS](https://mirror.yandex.ru/mirrors/msys2/) \| [RSYNC](rsync://mirror.yandex.ru/mirrors/msys2/) | - |
| mirrors.dotsrc.org | [HTTPS](https://mirrors.dotsrc.org/msys2/) \| [RSYNC](rsync://mirrors.dotsrc.org/msys2/) | <staff@dotsrc.org> |
| mirrors.tuna.tsinghua.edu.cn | [HTTPS](https://mirrors.tuna.tsinghua.edu.cn/msys2/) \| [RSYNC](rsync://mirrors.tuna.tsinghua.edu.cn/msys2/) | - |
| mirrors.ustc.edu.cn | [HTTPS](https://mirrors.ustc.edu.cn/msys2/) \| [RSYNC](rsync://rsync.mirrors.ustc.edu.cn/repo/msys2/) | <lug@ustc.edu.cn> |
| mirror.nju.edu.cn | [HTTPS](https://mirror.nju.edu.cn/msys2/) \| [RSYNC](rsync://mirror.nju.edu.cn/msys2/) | [issue](https://github.com/msys2/msys2.github.io/issues/155) |
| mirrors.bfsu.edu.cn | [HTTPS](https://mirrors.bfsu.edu.cn/msys2/) \| [RSYNC](rsync://mirrors.bfsu.edu.cn/msys2/) | [issue](https://github.com/msys2/MSYS2-packages/issues/2775) |
| mirror.clarkson.edu | [HTTPS](https://mirror.clarkson.edu/msys2/) \| [RSYNC](rsync://mirror.clarkson.edu/msys2/) | [issue](https://github.com/msys2/msys2.github.io/issues/185) |
| quantum-mirror.hu | [HTTPS](https://quantum-mirror.hu/mirrors/pub/msys2/) \| [RSYNC](rsync://quantum-mirror.hu/msys2/) | [website](https://quantum-mirror.hu/web/contact_en.html) |
| fastmirror.pp.ua | [HTTPS](https://fastmirror.pp.ua/msys2/) \| [RSYNC](rsync://fastmirror.pp.ua/msys2/) | [website](https://fastmirror.pp.ua) |
| mirror.archlinux.tw | [HTTPS](https://mirror.archlinux.tw/MSYS2/) \| [RSYNC](rsync://mirror.archlinux.tw/msys2/) | [issue](https://github.com/msys2/msys2.github.io/issues/206) |

(\*) rsync is required by [mirrorbits](https://github.com/etix/mirrorbits), which we use to auto-redirect users to a local mirror via [mirror.msys2.org](https://mirror.msys2.org)

## Tier 2 Mirrors

**Requirements:** Synced regularly.

| Name | URLs  | Note    |
| -    | -     | -       |
| ftp.cc.uoc.gr | [HTTPS](https://ftp.cc.uoc.gr/mirrors/msys2/) | <mirrors@cc.uoc.gr> |
| mirrors.bit.edu.cn | [HTTPS](https://mirrors.bit.edu.cn/msys2/) | <webmaster@bitnp.net> |
| mirror.jmu.edu | [HTTPS](https://mirror.jmu.edu/pub/msys2/) | <mirrormaster@jmu.edu> |
| mirrors.piconets.webwerks.in | [HTTPS](https://mirrors.piconets.webwerks.in/msys2-mirror/) | <mirrors@piconets.com> |
| mirrors.sjtug.sjtu.edu.cn | [HTTPS](https://mirrors.sjtug.sjtu.edu.cn/msys2/) | |
| www2.futureware.at | [HTTPS](https://www2.futureware.at/~nickoe/msys2-mirror/) | [Nick Østergaard](mailto:oe.nick@gmail.com) |
| mirrors.aliyun.com | [HTTPS](https://mirrors.aliyun.com/msys2/) | <ali-yum@alibaba-inc.com> |
| mirror.iscas.ac.cn | [HTTPS](https://mirror.iscas.ac.cn/msys2/) | |
| mirrors.cloud.tencent.com | [HTTPS](https://mirrors.cloud.tencent.com/msys2/) | <petzhou@tencent.com> |
| mirror.ufro.cl | [HTTPS](https://mirror.ufro.cl/msys2/) | [Jonathan Gutiérrez](mailto:jonathan.gutierrez@ufrontera.cl) |
| download.nus.edu.sg | [HTTPS](https://download.nus.edu.sg/mirror/msys2/) | <download@nus.edu.sg> |

## Adding a New Mirror

The repository size is ~725 GiB (see https://mirror.jmu.edu/ for current stats)
with the distribution of sizes like this:

```
  -1K: ~14000 files
-100K:  ~3200 files
  -1M:  ~5000 files
 -10M:  ~4000 files
-100M:  ~1000 files
  -1G:   ~200 files
 -10G:    ~20 files
```

You can use rsync to update your mirror using

```shell
rsync-ssl -rlptH --safe-links --delete-delay --delay-updates \
    rsync://repo.msys2.org/builds/ ./msys2
```

Our repository layout is compatible with Arch Linux, which means you can use the
following script to sync everything more frequently and efficiently:

https://gitlab.archlinux.org/archlinux/infrastructure/-/blob/master/roles/syncrepo/files/syncrepo-template.sh

```shell
source_url='rsync://repo.msys2.org/builds/'
lastupdate_url='https://repo.msys2.org/lastupdate'
```

Since our server has TLS/SSL support, you can replace the `rsync` command in the
script with `rsync-ssl`.

To register your mirror please open an issue here:
https://github.com/msys2/msys2.github.io/issues

## Admin TODO List

When adding/removing/updating mirrors:

* List all mirrors in https://github.com/msys2/MSYS2-packages/tree/master/pacman-mirrors
* List tier 1 mirrors in https://github.com/msys2/msys2-main-server/blob/main/services/mirrorbits/add_mirrors.sh
* Keep this page up-to-date
