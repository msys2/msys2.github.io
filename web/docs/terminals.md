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
* In the tab dropdown menu select "Settings" which opens a code editor showing
  a JSON configuration file.
* Insert the example profiles shown below under the `profiles` key. Note that
  the examples assume that you have MSYS2 installed under `C:\msys64`.
* You can make one of the MSYS2 profiles the default by setting the `defaultProfile`
  key to the `guid` value of one of the profile entries.

For more info on the different profile settings see
https://docs.microsoft.com/en-us/windows/terminal/customize-settings/profile-settings <br style="clear:both"/>

```json
// This makes UCRT64 the default shell
"defaultProfile": "{17da3cac-b318-431e-8a3e-7fcdefe6d114}",
"profiles": {
  "list":
  [
    // ...
    {
      "guid": "{17da3cac-b318-431e-8a3e-7fcdefe6d114}",
      "name": "UCRT64 / MSYS2",
      "commandline": "C:/msys64/msys2_shell.cmd -defterm -here -no-start -ucrt64",
      "startingDirectory": "C:/msys64/home/%USERNAME%",
      "icon": "C:/msys64/ucrt64.ico",
      "font": 
      {
        "face": "Lucida Console",
        "size": 9
      }
    },
    {
      "guid": "{71160544-14d8-4194-af25-d05feeac7233}",
      "name": "MSYS / MSYS2",
      "commandline": "C:/msys64/msys2_shell.cmd -defterm -here -no-start -msys",
      "startingDirectory": "C:/msys64/home/%USERNAME%",
      "icon": "C:/msys64/msys2.ico",
      "font": 
      {
        "face": "Lucida Console",
        "size": 9
      }
    },
    // ...
  ]
}
```

* The `commandline` in that profile will launch bash shell by default. To change
  default login shell, install the corresponding package for that shell and append
  `-shell` option with the command line. For example,
  - To set `fish` shell as default:
    ```
    "commandline": "C:/msys64/msys2_shell.cmd -defterm -here -no-start -ucrt64 -shell fish"
    ```
  - To set `zsh` shell as default:
    ```
    "commandline": "C:/msys64/msys2_shell.cmd -defterm -here -no-start -ucrt64 -shell zsh"
    ```

## Sublime Text

![image](sublime.png){: align=right width=45% }

[Sublime Text](https://www.sublimetext.com/) is a text and source code editor.
It features syntax highlighting, code folding, terminal output window, and more.
To add the MSYS2 terminal profile in Sublime Text, please follow these steps:

* Install [Terminus package](https://packagecontrol.io/packages/Terminus) using
  Package Control.

* In the menu bar, select Preferences > Package Settings > Terminus > Settings
  option. This will open Terminus.sublime-settings file in separate Sublime Text
  window with two panes.

* In the right pane, add the following configuration for UCRT64.

* Change the command options as usual to use other terminal environments. If the
  Terminus.sublime-settings is not empty append the above section after others.

```json
{
  "shell_configs": [
    {
      "name": "UCRT64",
      "cmd": [
        "cmd.exe",
        "/c",
        "C:/msys64/msys2_shell.cmd -defterm -here -no-start -ucrt64"
      ],
      "env": {},
      "enable": true,
      "platforms": ["windows"]
    }
  ]
}
```

* Now the UCRT64 environment can be opened like any other shell in Sublime Text.
  Press Ctrl + Shift + P > Terminus: List shells > UCRT64 > Open in tab or pane.
