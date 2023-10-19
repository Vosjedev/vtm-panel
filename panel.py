#!/usr/bin/env python3
import datetime,os,socket,psutil,pwd
from time import sleep

leftModules=['userhostname']
rightModules=['ram','cpu','bat','date','time']

print('\033[?1049h')
whatToRemoveWhenFull=['date','userhostname','bat','cpu','ram']

def compile(usedLeftModules,usedRightModules):
    def compileSide(mods):
        res=""
        for mod in mods:
            if mod=='userhostname':
                res=f"{res} | {userhost}"
            elif mod=='ram':
                res=f"{res} | {raminfo}"
            elif mod=='cpu':
                res=f"{res} | {cpuinfo}"
            elif mod=='bat':
                res=f"{res} | {batinfo}"
            elif mod=='date':
                res=f"{res} | {date}"
            elif mod=='time':
                res=f"{res} | {time}"
        return res[3:]
    
    left=compileSide(usedLeftModules)
    right=compileSide(usedRightModules)
        
    return (left,right)

def getWidthOfSep(left,right):
    return int(cols-len(left)-len(right)-2)

while True:
    cols,lines=os.get_terminal_size()
    
    bat=psutil.sensors_battery()
    batinfo=f"{str(bat.percent).split('.')[0]}%"
    if bat.power_plugged:
        batinfo=f"Charging, {batinfo}"
    else:
        batinfo=f"Battery:  {batinfo}"
        
    now=datetime.datetime.now()
    date=f"{now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second}"
    date=str(now).split('.')[0].split(' ')[0]
    time=str(now).split('.')[0].split(' ')[1]
    userhost=f"{pwd.getpwuid(os.getuid()).pw_name}@{socket.gethostname()}"
    
    raminfo=f"RAM: {psutil.virtual_memory()[2]}% ({int(psutil.virtual_memory()[3]/1000000)}MB)"
    cpuinfo=f"CPU: {psutil.cpu_percent()}"
    
    
    usedLeftModules=leftModules.copy()
    usedRightModules=rightModules.copy()
    removedModules=[]
    while True:
        left,right=compile(usedLeftModules,usedRightModules)
        if getWidthOfSep(left,right)>0:
            break
        for mod in whatToRemoveWhenFull:
            if mod in removedModules:
                continue
            else:
                try: usedLeftModules.remove(mod)
                except ValueError: pass
                try: usedRightModules.remove(mod)
                except ValueError: pass
                removedModules.append(mod)
        
    
    seperator=' '*int(cols-len(left)-len(right)-2)
    print(f"\n{left}{seperator}{right}",end='',flush=True)
    # break
    sleep(.5)
