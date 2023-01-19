---
summary: Just-in-time debugging with MSYS2
---

# Just-in-time Debugging

## MSYS2 processes

To get just-in-time debugging of MSYS2 processes, use the `error_start` `MSYS` environment variable setting:
```bash
export MSYS="error_start:$(cygpath -w /usr/bin/gdb)"
./crashy.exe
```

## Native Windows processes

MINGW gdb can be used as a [Windows JIT debugger](https://docs.microsoft.com/en-us/windows/win32/debug/configuring-automatic-debugging#configuring-automatic-debugging-for-application-crashes).
This is documented [here](https://www.sourceware.org/gdb/current/onlinedocs/gdb/Cygwin-Native.html) under `signal-event`.

As Administrator:
```bash
regtool add -w '/HKLM/SOFTWARE/Microsoft/Windows NT/CurrentVersion/AeDebug'
regtool set -w '/HKLM/SOFTWARE/Microsoft/Windows NT/CurrentVersion/AeDebug/Debugger' \"$(cygpath -w /mingw64/bin/gdb.exe)'" -ex "attach %ld" -ex "signal-event %ld" -ex "continue"'
regtool set -w '/HKLM/SOFTWARE/Microsoft/Windows NT/CurrentVersion/AeDebug/Auto' 1

regtool add -W '/HKLM/SOFTWARE/Microsoft/Windows NT/CurrentVersion/AeDebug'
regtool set -W '/HKLM/SOFTWARE/Microsoft/Windows NT/CurrentVersion/AeDebug/Debugger' \"$(cygpath -w /mingw32/bin/gdb.exe)'" -ex "attach %ld" -ex "signal-event %ld" -ex "continue"'
regtool set -W '/HKLM/SOFTWARE/Microsoft/Windows NT/CurrentVersion/AeDebug/Auto' 1
```

### Native Windows processes started from MSYS2

When a native process which was started (possibly indirectly) from an MSYS2 process (such as `bash`) crashes, it does not invoke
the registered debugger (or Windows Error Reporting), unless the `SetErrorMode` `SEM_NOGPFAULTERRORBOX` flag was cleared in the meantime
(`SetErrorMode` flags are inherited from a parent process by default).  As of [msys2-runtime](https://packages.msys2.org/package/msys2-runtime?repo=msys) `3.2.0-2`, it is possible to tell MSYS2 to
create processes without inheriting its error mode flags by setting an `MSYS` environment variable setting:
```bash
export MSYS=winjitdebug
exec bash
./crashy.exe
```
(note that the option needs to be set in the parent process, so `bash` needs to be restarted, assuming you are starting processes from `bash`).
