#!/usr/bin/python
#Author: Shawn Hoose
#Created: 10/12/2017
#Updated: 6/24/2019

## Libraries ##
import ctypes, sys
import psutil
import subprocess

def main():
    killName = "Spiricon.DataServer.exe" #Name of the process to kill
    if is_admin():
        killandStart(killName)
        sys.exit()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)

def is_admin(): #is_admin() from Martin De la Fuente / Eddie Parker on stackoverflow
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def killandStart(killName): #Kills process and starts BeamGage
    processes = {proc.name(): proc.pid for proc in psutil.process_iter()}
    if killName in processes:
        print('Found the process: ' + killName + " -- Killing it and starting BeamGage.")
        proc = psutil.Process(processes[killName])
        proc.kill()
        subprocess.call(['C:\Program Files\Spiricon\BeamGage Standard\Spiricon.Version5.exe'])
        sys.exit()
    else:
         print('Process: ' + killName + " was not found.")
         print("Starting BeamGage")
         subprocess.call(['C:\Program Files\Spiricon\BeamGage Standard\Spiricon.Version5.exe'])
         sys.exit()

if __name__ == "__main__":
    main()
