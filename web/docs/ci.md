---
summary: There are many ways to use MSYS2 in CI. The recommended way is Github Actions.
---
# Using MSYS2 in CI

## Github Actions (recommended)

Assuming you use GitHub this is the easiest way to get going. We provide a
GitHub Action which handles everything from installing the latest MSYS2,
updating it and installing all the packages you need. All you have to do is to
provide a BASH script that runs your code in the MSYS2 environment.

1) Create a workflow file, for example `.github/workflows/msys2.yml`, see [the GitHub docs for more details](https://docs.github.com/en/actions/writing-workflows/quickstart#creating-your-first-workflow)

2) Paste the following into your workflow file:

```yaml
name: MSYS2
on: [push, pull_request]

jobs:
  msys2-ucrt64:
    runs-on: windows-latest
    defaults:
      run:
        shell: msys2 {0}
    steps:
      - uses: actions/checkout@v3
      - uses: msys2/setup-msys2@v2
        with:
          msystem: UCRT64
          update: true
          install: git mingw-w64-ucrt-x86_64-gcc
      - name: CI-Build
        run: |
          echo 'Running in MSYS2!'
          ./ci-build.sh
```

For more details on the 'msys2/setup-msys2' action and all the available options
see https://github.com/marketplace/actions/setup-msys2

## GitLab

GitLab offers [shared Windows runners](https://docs.gitlab.com/ci/runners/hosted_runners/windows/)
with some [pre-installed software](https://gitlab.com/gitlab-org/ci-cd/shared-runners/images/gcp/windows-containers/-/blob/main/cookbooks/preinstalled-software/attributes/default.rb)
and you can build a project using the following `.gitlab-ci.yml`
snippet, which illustrates how to build a regular autotools-based
project.  See [GitLab's CI/CD documentation](https://docs.gitlab.com/topics/build_your_application/)
for general reference on CI/CD in GitLab.

```yaml
Windows-MSYS2-UCRT64:
  # https://docs.gitlab.com/ci/runners/hosted_runners/windows/
  tags: [ saas-windows-medium-amd64 ]
  script: # https://www.msys2.org/docs/ci/#gitlab
  - wget.exe -nv -O msys2.exe https://github.com/msys2/msys2-installer/releases/download/2025-02-21/msys2-base-x86_64-20250221.sfx.exe # https://github.com/msys2/msys2-installer/releases/download/nightly-x86_64/msys2-base-x86_64-latest.sfx.exe
  - Get-FileHash ./msys2.exe -Algorithm SHA256 | Format-List
  - ./msys2.exe -y -oC:\
  - Remove-Item msys2.exe
  - $env:CHERE_INVOKING = 'yes'
  - $env:MSYSTEM = 'UCRT64' # https://www.msys2.org/docs/environments/
  - C:\msys64\usr\bin\bash -lc ' '
  - C:\msys64\usr\bin\bash -lc 'pacman --noconfirm -Syuu'
  - C:\msys64\usr\bin\bash -lc 'pacman --noconfirm -Syuu'
  - |
    C:\msys64\usr\bin\bash -lcx '
    pacman --noconfirm -Syu git mingw-w64-ucrt-x86_64-autotools mingw-w64-ucrt-x86_64-gcc
    ./bootstrap
    ./configure
    make V=1 check VERBOSE=t'
  - C:\msys64\usr\bin\bash -lc 'grep ^PASS tests/basic.log'
```

## Appveyor

Appveyor provides a MSYS2 installation on all their images under `C:\msys64`,
see https://www.appveyor.com/docs/windows-images-software/

Make sure to use the `Visual Studio 2019` image or newer, as the MSYS2
installation on older images is outdated and updating there no longer works.

In case you want to update the MSYS2 installation and install packages you need
to update MSYS2 first. For this you need to run the following commands:

```powershell
# Update MSYS2
C:\msys64\usr\bin\bash -lc "pacman --noconfirm -Syuu"  # Core update (in case any core packages are outdated)
C:\msys64\usr\bin\bash -lc "pacman --noconfirm -Syuu"  # Normal update

# Then run your code
$env:CHERE_INVOKING = 'yes'  # Preserve the current working directory
$env:MSYSTEM = 'UCRT64'  # Start a 64 bit Mingw environment
C:\msys64\usr\bin\bash -lc "./ci-build.sh"
```

## Docker

Install MSYS2 under `C:\msys64` into a Windows based Docker image:

```docker
# select as base image matching your host to get process isolation
FROM mcr.microsoft.com/windows/servercore:2004

SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]

RUN [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \
  Invoke-WebRequest -UseBasicParsing -uri "https://github.com/msys2/msys2-installer/releases/download/nightly-x86_64/msys2-base-x86_64-latest.sfx.exe" -OutFile msys2.exe; \
  .\msys2.exe -y -oC:\; \
  Remove-Item msys2.exe ; \
  function msys() { C:\msys64\usr\bin\bash.exe @('-lc') + @Args; } \
  msys ' '; \
  msys 'pacman --noconfirm -Syuu'; \
  msys 'pacman --noconfirm -Syuu'; \
  msys 'pacman --noconfirm -Scc';
```

## Other Systems

On systems that don't provide MSYS2 integration you need to install and update
MSYS2 yourself.

1) Download and install MSYS2. For CI systems we provide a self extracting 
   archive, so you don't need any additional tools.

   ```powershell
   # Download the archive
   (New-Object System.Net.WebClient).DownloadFile('https://github.com/msys2/msys2-installer/releases/download/nightly-x86_64/msys2-base-x86_64-latest.sfx.exe', 'msys2.exe')
   .\msys2.exe -y -oC:\  # Extract to C:\msys64
   Remove-Item msys2.exe  # Delete the archive again
   ```

2) Run MSYS2 for the first time and update it

   ```powershell
   # Run for the first time
   C:\msys64\usr\bin\bash -lc ' '
   # Update MSYS2
   C:\msys64\usr\bin\bash -lc 'pacman --noconfirm -Syuu'  # Core update (in case any core packages are outdated)
   C:\msys64\usr\bin\bash -lc 'pacman --noconfirm -Syuu'  # Normal update
   ```

3) Run your code (`ci-build.sh` in this case)

   ```powershell
   $env:CHERE_INVOKING = 'yes'  # Preserve the current working directory
   $env:MSYSTEM = 'UCRT64'  # Start a 64 bit Mingw environment
   C:\msys64\usr\bin\bash -lc './ci-build.sh'
   ```

## FAQ

**My CI system doesn't exit at the end of the run and hangs. What's wrong?**

In some cases CI systems will wait until all processes you have started have
also ended, but the MSYS2 setup and update might spawn processes for gnupg etc.
that will stay around in the background forever. To end them all you can run:

```powershell
taskkill /F /FI "MODULES eq msys-2.0.dll"
```

**MSYS2 fails to update on Appveyor with some "key is unknown" error. What's wrong?**

The MSYS2 installation on older Appveyor images hasn't been updated in years and
is no longer supported. Either use the `Visual Studio 2019` image or newer, or
install MSYS2 manually as described above.
