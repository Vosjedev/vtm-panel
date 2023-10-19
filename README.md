# vtm-panel
A panel for [vtm](https://github.com/netxs-group/vtm).  
A new update is here! VTM now has integration for panels, and the code is updated to use that!

The panel currently shows:
- user@hostname
- (seperator)
- RAM usage (% and MB)
- CPU usage (%)
- battery (charging, %)
- date
- time
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

see [this issue](https://github.com/netxs-group/vtm/issues/397) on the vtm repo for updates. (This does not mean file updates).
