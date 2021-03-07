---
title: Signing Packages
summary: Create a GPG key and import it into pacman.
---
[ rough draft ]

Have a GPG key
--------------

Create your new key:
`gpg --gen-key`
[more...](https://fedoraproject.org/wiki/Creating_GPG_Keys#Creating_GPG_Keys_Using_the_Command_Line) [ TBD: how strong should the key be? ]

Back it up:
`gpg --export-secret-keys --armor <keyid> > my_key_backup.asc`
[more...](https://fedoraproject.org/wiki/Creating_GPG_Keys#Making_a_Key_Backup_Using_the_Command_Line)

In case you need to import the backup later:
`gpg --import <backup_file>`, `gpg --edit-key <keyid>` and `trust` it ultimately.

Export the public key:
`gpg --export --armor <keyid> > my_pub_key.asc`

If you're going to use the key for GPG/MIME or share your signed packages with other people, you probably need publish your key:
`gpg --send-key <keyid>`
[more...](https://fedoraproject.org/wiki/Creating_GPG_Keys#Exporting_a_GPG_Key_Using_the_Command_Line)


Import into pacman
---------------------

This is needed because pacman has its own keystore and own rules for trusting keys. Either you get approved as a packager for the MSYS2 project, or you have to import your key manually.

To import and sign your key with `pacman-key`:

1. `pacman-key --add <pubkeyfile>`, or if it's published `pacman-key --recv-keys <keyid>`
2. `pacman-key --lsign-key <keyid>`
[more...](https://wiki.archlinux.org/index.php/pacman-key#Adding_unofficial_keys)

To make your key a trusted developer key for signing official packages, you have to get your key included in the respective keyring and get it signed by at least 3 master keys. The package and repository is `msys2-keyring` for MSYS2, see [Alexpux/msys2-keyring](https://github.com/Alexpux/MSYS2-keyring/). The package and repository for Arch Linux is `archlinux-keyring`, see https://projects.archlinux.org/archlinux-keyring.git/. These packages install keyring files into `/usr/share/pacman/keyrings` which then can be imported and locally signed in one batch using `pacman-key --populate <keyringname>`.


Actually sign stuff
-------------------

- Old packages: `gpg --detach-sign --no-armor <pkg>` for each package (all such packages need to be re-`repo-add`ed to make the database aware of the new signatures)
- New packages: just add `--sign` to makepkg command line or set the related `makepkg.conf` option
- Databases: `repo-add -s -v <db> <pkg>`

