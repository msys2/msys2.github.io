# Using MSYS2 in CI

## Github Actions (recommended)

Assuming you use GitHub this is the easiest way to get going. We provide a
GitHub Action which handles everything from installing the latest MSYS2,
updating it and installing all the packages you need. All you have to do is to
provide a BASH script that runs your code in the MSYS2 environment.

1) Create a workflow file, see [the GitHub docs forr details](https://docs.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow#creating-a-workflow-file)

2) Paste the following into your workflow file:

```yaml
name: Hello World
on: [push, pull_request]

jobs:
  build:
    runs-on: windows-latest
    defaults:
      run:
        shell: msys2 {0}
    steps:
      - uses: actions/checkout@v2
      - uses: msys2/setup-msys2@v1
        with:
          msystem: MINGW64
          update: true
          install: git mingw-w64-x86_64-toolchain
      - name: CI-Build
        run: |
          echo 'Running in MSYS2!'
          ./ci-build.sh
```

For more details on the 'msys2/setup-msys2' action and all the available options
see https://github.com/msys2/setup-msys2

## Appveyor

Appveyor provides a MSYS2 installation on all their images under `C:\msys64`,
see https://www.appveyor.com/docs/windows-images-software/

In case you want to update the MSYS2 installation and install packages you need
to update MSYS2 first. For this you need to run the following commands:

```powershell
# Update MSYS2
C:\msys64\user\bin\bash -lc "pacman -Syuu"  # Core update (in case any core packages are outdated)
C:\msys64\user\bin\bash -lc "pacman -Syuu"  # Normal update

# Then run your code
$env:CHERE_INVOKING = 'yes'  # Preserve the current working directory
$env:MSYSTEM = 'MINGW64'  # Start a 64 bit Mingw environment
C:\msys64\user\bin\bash -lc "./ci-build.sh"
```

## Other Systems

On systems that don't provide MSYS2 integration you need to install and update
MSYS2 yourself.

1) Download and install MSYS2. For CI systems we provide a self extracting 
   archive, so you don't need any additional tools.

   ```powershell
   # Download the archive
   (New-Object System.Net.WebClient).DownloadFile('https://github.com/msys2/msys2-installer/releases/download/2020-06-29/msys2-base-x86_64-20200629.sfx.exe', 'msys2.exe')
   .\msys2.exe -y -oC:\  # Extract to C:\msys64
   Remove-Item msys2.exe  # Delete the archive again
   ```

2) Run MSYS2 for the first time and update it

   ```powershell
   # Run for the first time
   C:\msys64\usr\bin\bash -lc ' '
   # Update MSYS2
   C:\msys64\usr\bin\bash -lc 'pacman -Syuu'  # Core update (in case any core packages are outdated)
   C:\msys64\usr\bin\bash -lc 'pacman -Syuu'  # Normal update
   ```

3) Run your code (`ci-build.sh` in this case)

   ```powershell
   $env:CHERE_INVOKING = 'yes'  # Preserve the current working directory
   $env:MSYSTEM = 'MINGW64'  # Start a 64 bit Mingw environment
   C:\msys64\usr\bin\bash -lc './ci-build.sh'
   ```
