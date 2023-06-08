#!/bin/python3
from time import sleep
import datetime,os,pwd,socket,colorama,subprocess,psutil

colorama.init()

vtmversion=subprocess.check_output(['vtm', '--version']).decode()[0:-1]
while True:
    cols,lines=os.get_terminal_size()

    bat=psutil.sensors_battery()
    batinfo=f"{str(bat.percent).split('.')[0]}%"
    if bat.power_plugged:
        batinfo=f"Charging, {batinfo}"
    else:
        batinfo=f"battery:  {batinfo}"

    now=datetime.datetime.now()
    date=f"{now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second}"
    date=str(now).split('.')[0]

    left=f"{date} | {pwd.getpwuid(os.getuid()).pw_name}@{socket.gethostname()} | {lines}x{cols}"
    right=f"{batinfo} | {vtmversion}"
    seperator=" "*int(cols-len(left)-len(right))
    print(f"\033[0;37;40m\033[0;0H"+left+seperator+right,end='',flush=True)
    sleep(0.5)
