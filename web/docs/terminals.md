---
summary: Terminals with which MSYS2 can be used.
---
# Terminals

## Mintty

![image](mintty.png){: align=right width=45% }

![image](launchers.png){: align=right style="clear:both" width=45% }

[Mintty](https://mintty.github.io) is the default terminal application in MSYS2
and is included in the installer. We also include some custom Mintty integration
by providing separate launchers with corresponding .ini configuration files
(msys2{.exe,.ini}/ucrt64{.exe,.ini}/...) for all the MSYS2
environments, so you can easily configure your environments and pin the
launchers to your Windows taskbar.



See https://github.com/msys2/msys2-launcher and https://mintty.github.io for
more details.<br style="clear:both"/>



## Windows Terminal

![image](winterm.png){: align=right width=45% }

The new Windows Terminal application, which by default supports cmd, powershell
and WSL can also be extended to support a MSYS2 shell.

* Get it via the [Windows app store](https://aka.ms/terminal) if you don't have
  it installed already.
* In the tab dropdown menu select "Settings" which opens a settings page
* In the left sidebar, click on "+ Add a new profile" under "Profiles". Note that
  the examples assume that you have MSYS2 installed under `C:\msys64`.
* In the opened page, click on "+ New empty profile".
* Under Name, enter "MSYS" (or the name you want)
* Under Command line, enter `C:/msys64/msys2_shell.cmd -defterm -no-start -[term]`. Replace `[term]` by the terminal you want you use, such as `msys`, `ucrt64`, etc.
* Click on "Save changes".

For more info on the different profile settings see
https://docs.microsoft.com/en-us/windows/terminal/customize-settings/profile-settings <br style="clear:both"/>

## Konsole

![image](konsole.png){: align=right width=45% }

[Konsole](https://konsole.kde.org/) is a powerful and customizable terminal
emulator made by KDE. MSYS2 provides it as a [mingw package](https://packages.msys2.org/base/mingw-w64-konsole).
To use it with MSYS2, first install the appropriate package and create a new
profile with the following steps.

* In the Konsole window menu bar, select "Settings" > "Create New Profile...".
* Select it as a default profile to always open msys2 environment at start.
* Add profile name and following command.

```
C:\\msys64\\msys2_shell.cmd -defterm -here -no-start -ucrt64
```

* Now close and restart Konsole.

## Cmder

![image](cmder.png){: align=right width=45% }

[Cmder](https://cmder.app/) is a portable console emulator for Windows based on [ConEmu](https://conemu.github.io/) that aims to provide a portable and convenient terminal for Windows. It comes bundled with most of the popular UNIX commands and supports a quake-style slide drop down that allows immediate access to the terminal via a global keyboard shortcut.

To use it with MSYS2, click the hamburger menu on the right lower bar and click `settings` to open the settings window. 

1. Navigate to `Startup` > `Tasks` and then click the `+` symbol to create a new task. You can set any name you like, for example `bash::msys2 ucrt64`.

2.  In the command section, copy the following script:

  ```cmd
  set MSYSTEM=UCRT64 & set "CHERE_INVOKING=1" & "C:\msys64\usr\bin\bash.exe" --login -i
  ```

3. Click `Save Settings` button.

4. Open a new tab with the shortcut `Ctrl + T`. On the new console dialog, select the `task` you just created and then click the `Start` button. 

To customize further, you can press `Ctrl + Alt + P` to open the settings window and set the task you created as the default one.  You can also click the `Startup dir` button to change the default startup directory.
