#!/usr/bin/python

######## Relevant Libraries ##############
import sys                               #
import os                                #
import subprocess                        #
import shutil                            #
from shutil import copy                  #
from datetime import datetime, timedelta #
*REMOVED*         #
##########################################


def main():
    *REMOVED*
    *REMOVED*
    *REMOVED*
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
        mPath = os.path.join(path2Old, rFileName) #UD Path - OLD
        rPath = os.path.join(path2Old, nFileName) #CopyVersion Path - OLD
        oPath = os.path.join(path, rFileName) #UD Path
        oNPath = os.path.join(path,nFileName) #CopyVersion Path
        if rPath:
            try:
                os.remove(rPath)
            except FileNotFoundError as e:
                pass
        copy(oPath, path2Old) #Places copy of UD into Old Folder
        os.rename(mPath, rPath) #Renames UD in old folder to "WaistSolverCopyVersion"
        os.remove(oNPath) #Removes CopyVersion from parent folder
        copy(rPath, path) #copies CopyVersion from Old into parent folder
        os.rename(rPath, mPath) #renames CopyVersion in old folder to original name
        print("Run Successful!")
        print("press enter to exit...")
        input()
        exit()

    else:
        rFileName = timeCheckFiles[timeCheckFTime.index(min(timeCheckFTime))]
        print("Found File: " + rFileName)
        nFileName = "WaistSolverCopyVersion.xls"
        mPath = os.path.join(path2Old, rFileName)
        rPath = os.path.join(path2Old, nFileName)
        oPath = os.path.join(path, rFileName)
        oNPath = os.path.join(path,nFileName)
        if rPath:
            try:
                os.remove(rPath)
            except FileNotFoundError as e:
                pass
        copy(oPath, path2Old)
        os.rename(mPath, rPath)
        os.remove(oNPath)
        copy(rPath, path)
        os.rename(rPath, mPath)
        print("Run Successful!")
        print("press enter to exit...")
        input()
        exit()

if __name__ == "__main__": main()
