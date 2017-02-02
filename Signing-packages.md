[ draft ]

1) have a GPG key
Essentially you do gpg --gen-key: https://fedoraproject.org/wiki/Creating_GPG_Keys#Creating_GPG_Keys_Using_the_Command_Line
It's probably good to back it up: https://fedoraproject.org/wiki/Creating_GPG_Keys#Making_a_Key_Backup_Using_the_Command_Line
If you're going to use the key for GPG/MIME or share your signed packages with other people, you probably need to do this: https://fedoraproject.org/wiki/Creating_GPG_Keys#Exporting_a_GPG_Key_Using_the_Command_Line
In case you need to restore from the backup later, you probably have to follow the import with gpg --edit-key <keyid> and trust it ultimately.

2) import into pacman
This is needed because pacman has its own keystore and different rules for trusting keys.
For this you need to have the public key exported in a file or uploaded to a keyserver. Then import and sign it with pacman-key: https://wiki.archlinux.org/index.php/pacman-key#Adding_unofficial_keys
If you're an official packager, then the new key will be distributed via a MSYS2 update: https://wiki.archlinux.org/index.php/pacman-key#Adding_developer_keys

3) actually sign stuff
Old packages: gpg --detach-sign --no-armor <pkg> for each package
New packages: just add --sign to makepkg command line, or use BUILDENV configuration array
Databases: repo-add -s -v <db> <pkg>
