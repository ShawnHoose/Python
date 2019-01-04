#!/usr/bin/python
#Author: Shawn Hoose
#Created: 10/12/2017
#Updated: 10/12/2017

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
    i = 0 #counter to see if we don't find the proper process
    processes = list(psutil.process_iter()) #Creates list of running processes
    for i in range(0, len(processes)):
        for proc in processes:  #Loops through each looking for the right one, then kills it when it matches the name
            if proc.name() == killName:
                print('Found the process: ' + killName + " -- Killing it and starting BeamGage.")
                proc.kill()
                subprocess.call(['C:\Program Files\Spiricon\BeamGage Standard\Spiricon.Version5.exe']) #Opens BeamGage
                sys.exit()
                break

        if (i == len(processes) - 1): # If it has gone through all the processes and did not find the right one, open BeamGage.
            print('Process: ' + killName + " was not found.")
            print("Starting BeamGage")
            subprocess.call(['C:\Program Files\Spiricon\BeamGage Standard\Spiricon.Version5.exe']) #Opens BeamGage
            sys.exit()



if __name__ == "__main__": main()
