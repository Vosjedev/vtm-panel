# vtm-panel
A panel for [vtm](https://github.com/netxs-group/vtm).  
A new update is here! VTM now has integration for panels, and the code is updated to use that!

The panel
currently shows:
- user@hostname
- (seperator)
- RAM usage (% and MB)
- CPU usage (%)
- battery (charging, %)
- date
- time

Example of the contents:
```
user@hostname                                                 RAM: 33.6% (4123MB) | CPU: 3.2% | Charging, 96% | 2023-01-02 | 11:22:33
```

when the screen is full data disapears in the following order:
- date
- user@hostname
- battery
- cpu
- ram
  (clock never disappears)

## how to install
0. Make sure python3 is installed and in the PATH.
1. Download `panel.py`.
2. Make sure psutil is installed: `pip install psutil`.
3. Place `panel.py` in a good location. I do not recommend your downloads folder, but rather something like a scripts folder in your home or user directory.
4. Configure vtm. Edit the following lines in your config to be like this (replace `/full/path/to/panel.py` with the actual path):
```xml
    <panel> <!-- Desktop info panel. -->
        <cmd = "python3 /full/path/to/panel.py"/> <!-- Command-line to activate. -->
        <cwd = "/"/> <!-- Working directory. -->
        <height = 1 /> <!-- Desktop space reserved on top. -->
    </panel>
```
If you do not have a config, see [this page](https://github.com/netxs-group/vtm/blob/master/doc/settings.md) for the default, and more info on editing the config.


see [this issue](https://github.com/netxs-group/vtm/issues/397) on the vtm repo for updates. (This does not mean file updates).
