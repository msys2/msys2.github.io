1. Why is `update-core` not found after an `update-core`?

    The function of `update-core` is transferred to `pacman -Syuu`.

2. Windows: After `pacman -Syu` a command window lingers after startup.

    Change the argument `/K` to `/C` in all three start menu shortcuts.

3. What to do when Pacman is telling me there are conflicts in the file system?

    This indicates that Pacman isn't sure it is safe to overwrite some files.  This sometimes happens during regular package updates, but could also happen if you installed some software manually (`make install`, `npm install npm -g` etc.).  To continue with the operation, pass `--overwrite <conflicting_file_path>` to the Pacman command line.  For other options, see the [Arch Linux FAQ entry about Pacman file conflicts](https://wiki.archlinux.org/index.php/Pacman#.22Failed_to_commit_transaction_.28conflicting_files.29.22_error).

4. Pacman says:
```
looking for conflicting packages...
error: failed to prepare transaction (could not satisfy dependencies)
:: installing mingw-w64-x86_64-gcc (9.1.0-1) breaks dependency 'mingw-w64-x86_64-gcc=8.3.0-2' required by mingw-w64-x86_64-gcc-ada
:: installing mingw-w64-x86_64-gcc (9.1.0-1) breaks dependency 'mingw-w64-x86_64-gcc=8.3.0-2' required by mingw-w64-x86_64-gcc-objc
:: installing mingw-w64-x86_64-gcc (9.1.0-1) breaks dependency 'mingw-w64-i686-gcc=8.3.0-2' required by mingw-w64-i686-gcc-ada
:: installing mingw-w64-x86_64-gcc (9.1.0-1) breaks dependency 'mingw-w64-i686-gcc=8.3.0-2' required by mingw-w64-i686-gcc-objc
```

Ada and ObjC were unsupported for a while in MSYS2 builds due to long-standing issues with the i686 variant.  One had to run `pacman -R mingw-w64-x86_64-gcc-ada mingw-w64-x86_64-gcc-objc` and/or `pacman -R mingw-w64-i686-gcc-ada mingw-w64-i686-gcc-objc`, then update.
