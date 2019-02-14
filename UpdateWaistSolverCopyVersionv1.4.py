#!/usr/bin/python
#Author: Ouutong Phooprasert
#Created: 6/8/2017
#Updated: 1/28/19 (Hoose)

######## Relevant Libraries ##############
import sys                               #
import os                                #
import subprocess                        #
import shutil                            #
from shutil import copy                  #
from datetime import datetime, timedelta #
from photonicsfolders2 import *          #
##########################################


def main():
    AutoUpdate("*REMOVED*", os.path.basename(__file__))
    path = "*REMOVED*"
    path2Old = "*REMOVED*"
    date = datetime.now()
    files = ListFolderDirectory(path)
    timeCheckFiles = []
    timeCheckFTime = []
    for i in range(0, len(files)):
        rfileTemp = re.findall("*REMOVED*", files[i])
        try:
            rFileName2 = rfileTemp[0].strip()
            rFileName = files[i]
            fdtTemp = os.path.getmtime(os.path.join(path, files[i]))
            fileDate = datetime.fromtimestamp(fdtTemp)
            timeCheckFTime.append(date - fileDate)
            timeCheckFiles.append(files[i])
        except IndexError as e:
            pass
    if len(timeCheckFiles) == 1:
        print("Found File: " + rFileName)
        nFileName = "*REMOVED*"
        rPath = os.path.join(path2Old, nFileName) #CopyVersion Path - OLD
        oPath = os.path.join(path, rFileName) #UD Path
        if rPath:
            try:
                os.remove(rPath)
            except FileNotFoundError as e:
                print("\nDid not find " + rPath + ". Continuing without.\n")

        #Copies WaistSolver into Old folder and creates a copy
        copy(oPath, path2Old)
        copy(oPath, os.path.join(path, "*REMOVED*"))
        print("Run Successful!")
        print("press enter to exit...")
        input()
        exit()

    else:
        rFileName = timeCheckFiles[timeCheckFTime.index(min(timeCheckFTime))]
        print("Found File: " + rFileName)
        nFileName = "*REMOVED*"
        rPath = os.path.join(path2Old, nFileName)
        oPath = os.path.join(path, rFileName)
        if rPath:
            try:
                os.remove(rPath)
            except FileNotFoundError as e:
                print("\nDid not find " + rPath + ". Continuing without.\n")

        #Copies WaistSolver into Old folder and creates a copy
        copy(oPath, path2Old)
        copy(oPath, os.path.join(path, "*REMOVED*"))

        print("Run Successful!")
        print("press enter to exit...")
        input()
        exit()

if __name__ == "__main__":
    main()
