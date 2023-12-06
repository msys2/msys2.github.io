# MSYS2 Keyring

* Repository: <https://github.com/msys2/MSYS2-keyring>
* Also see <https://wiki.archlinux.org/index.php/Pacman/Package_signing>

### Master Keys

| Master Key                                                                                                         | Full Fingerprint                                    | Owner                                           |
|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|-------------------------------------------------|
| [0xF40D263ECA25678A](https://keyserver.ubuntu.com/pks/lookup?op=vindex&fingerprint=on&search=0xF40D263ECA25678A) | `D55E7A6D7CE9BA1587C0ACACF40D263ECA25678A` | [alexpux](https://github.com/Alexpux)           |
| [0x9F418C233E652008](https://keyserver.ubuntu.com/pks/lookup?op=vindex&fingerprint=on&search=0x9F418C233E652008) | `B91BCF3303284BF90CC043CA9F418C233E652008` | [nacho](https://github.com/nacho)               |
| [0xDA7EF2ABAEEA755C](https://keyserver.ubuntu.com/pks/lookup?op=vindex&fingerprint=on&search=0xDA7EF2ABAEEA755C) | `9DD0D4217D75A33B896159E6DA7EF2ABAEEA755C` | [martell](https://github.com/martell)           |
| [0x790AE56A1D3CFDDC](https://keyserver.ubuntu.com/pks/lookup?op=vindex&fingerprint=on&search=0x790AE56A1D3CFDDC) | `6E8FEAFF9644F54EED90EEA0790AE56A1D3CFDDC` | [elieux](https://github.com/elieux)             |
| [0x755B8182ACD22879](https://keyserver.ubuntu.com/pks/lookup?op=vindex&fingerprint=on&search=0x755B8182ACD22879) | `69985C5EB351011C78DF7F6D755B8182ACD22879` | [lazka](https://github.com/lazka)               |

### Developer Keys

Each of these keys is signed by at least three master keys.

| Developer Key                                                                                                      | Full Fingerprint                         | Owner                                           |
|--------------------------------------------------------------------------------------------------------------------|------------------------------------------|-------------------------------------------------|
| [0x5F92EFC1A47D45A1](https://keyserver.ubuntu.com/pks/lookup?op=vindex&fingerprint=on&search=0x5F92EFC1A47D45A1) | `AD351C50AE085775EB59333B5F92EFC1A47D45A1` | [alexpux](https://github.com/Alexpux)           |
| [0x974C8BE49078F532](https://keyserver.ubuntu.com/pks/lookup?op=vindex&fingerprint=on&search=0x974C8BE49078F532) | `87771331B3F1FF5263856A6D974C8BE49078F532` | [elieux](https://github.com/elieux)             |
| [0xFA11531AA0AA7F57](https://keyserver.ubuntu.com/pks/lookup?op=vindex&fingerprint=on&search=0xFA11531AA0AA7F57) | `5F944B027F7FE2091985AA2EFA11531AA0AA7F57` | [lazka](https://github.com/lazka)               |

### Master Key Signatures

| Developer Key | Signed by                                    |
|---------------|----------------------------------------------|
| alexpux       | alexpux, nacho, martell, lazka               |
| elieux        | elieux, alexpux, lazka                       |
| lazka         | alexpux, lazka, elieux                       |
