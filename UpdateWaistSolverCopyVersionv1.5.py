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
    AutoUpdate("*REMOVED*")
    path = "*REMOVED*"
    path2Old = "*REMOVED*"
    date = datetime.now()
    files = ListFolderDirectory(path)
    timeCheckFiles = []
    timeCheckFTime = []
    for i in range(0, len(files)):
        rfileTemp = re.findall("WaistSolver ", files[i])
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
        nFileName = "WaistSolverCopyVersion.xls"
        rPath = os.path.join(path2Old, nFileName) #CopyVersion Path - OLD
        oPath = os.path.join(path, rFileName) #UD Path
        if rPath:
            try:
                os.remove(rPath)
            except FileNotFoundError as e:
                print("\nDid not find " + rPath + ". Continuing without.\n")

        #Copies WaistSolver into Old folder and creates a copy
        x = 1
        while x == 1:
            try:
                copy(oPath, path2Old)
                copy(oPath, os.path.join(path, "WaistSolverCopyVersion.xls"))
                print("Run Successful!")
                print("press enter to exit...")
                input()
                exit()
            except PermissionError:
                print("The file " + nFileName + " could not be opened. It is currently open elsewhere. Please close the file. \nPress 'e' to exit this program, or press any other button to try again.\n")

                userInput = input()
                if userInput is 'e':
                    print("exiting program...")
                    x = 2
                    exit()
                else:
                    print("trying again...\n")


    else:
        rFileName = timeCheckFiles[timeCheckFTime.index(min(timeCheckFTime))]
        print("Found File: " + rFileName)
        nFileName = "WaistSolverCopyVersion.xls"
        rPath = os.path.join(path2Old, nFileName)
        oPath = os.path.join(path, rFileName)
        if rPath:
            try:
                os.remove(rPath)
            except FileNotFoundError as e:
                print("\nDid not find " + rPath + ". Continuing without.\n")

        #Copies WaistSolver into Old folder and creates a copy
        copy(oPath, path2Old)
        copy(oPath, os.path.join(path, "WaistSolverCopyVersion.xls"))

        print("Run Successful!")
        print("press enter to exit...")
        input()
        exit()

if __name__ == "__main__":
    main()
