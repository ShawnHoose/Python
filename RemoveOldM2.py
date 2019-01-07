#!/usr/bin/python
#Author: Shawn Hoose
#Created: 2/12/18

#### Libraries ####
import sys, os
from os import listdir
from os.path import isfile, join
*REMOVED*
####################

#This program will scan through the entire year folder and remove all the old M2 data files
def main():
    #AutoUpdate("\\\PHOTONIX04\Quality Control\QC\\Updated Python Executables", os.path.basename(__file__)) #Ensures latest version
    fileTypes = ['m2-scor-data','bsqData'] #file extension types to delete
    safety = True #Check variable for safety loop
    #filePath = "\\PHOTONIX04\Laser Data and Test Reports\Test Reports (by Year)\\"
    filePath = "\\Users\shoose\Desktop\Python Projects\DeleteTestFolder"
    while safety == True: #Safety loop to make sure you delete the right year
        year = askYear() #Get the year
        safety = safetyCheck(year, filePath, fileTypes) #Make sure the user wants to delete that years data

def askYear():
    return int(input("What year would you like to delete the M2 data files for? "))

def safetyCheck(year, path, types):
    yesNo = input("This will permanently remove all the M2 data files for all of " + str(year) + ". Are you sure you want to do this? " ).lower()
    if yesNo == "yes":
        safety = False
        print("\nAlright, here we go!\n")
        removeFiles(path, year, types)
        return safety #ensures that the loop exits
        print("Press Enter to exit...")
        input()
        exit()
    else:
        print("Process aborted...\nPress enter to exit...")
        input()
        exit()

def removeFiles(path, year, types):
    counter = 0
    dataFiles = ['RLG', 'CSV', 'csv', 'rlg']
    exclude = set([])
    folder = str(year) + " Laser Data"
    path = os.path.join(path, folder)

    for dirs, subdir, _ in os.walk(path): #Walks through the directory and each subdirectory and finds all files
        dirPath = os.path.join(path, dirs)
        for child in subdir: #Finds directories with "Final Test" and excludes them from the search and delete process
            if ("Final" in child) or ("final" in child):
                exclude.add(child)
        subdir[:] = [sd for sd in subdir if sd not in exclude]

        for elem in subdir: #Searches through and gets all files for current directory
            elemPath = os.path.join(dirPath, elem)
            files = [f for f in listdir(elemPath) if isfile(join(elemPath, f))] #Gets all files in current directory
            compare = []
            for file in files: #Creates a list of all csv,rlg files to compare the names to
                fileName = file.split('.')
                if (fileName[0].lower() not in compare) and (fileName[-1] in dataFiles):
                    newNameList = fileName[0].split()
                    if (len(newNameList) > 3) and (newNameList[-2].lower() == 'log'):
                        del(newNameList[-2:])
                        newName = ' '.join(newNameList)
                        compare.append((newName).lower())
                    else:
                        compare.append(fileName[0].lower())
                else:
                    continue

            for file in files: #Action on each file that the walk finds (this will be every file in the directory)
                finalFiles = file.split('.')
                fileLoc = os.path.join(elemPath, file)
                if (finalFiles[-1] in types) and (str(finalFiles[0].lower()) in compare): #Looks for only files that end in the proper extension and have an associated CSV or RLG file
                    counter += 1
                    fileLocList = fileLoc.split('\\')
                    fileLocList[-1] = ("REMOVE" + str(counter))
                    removeName = '\\'.join(fileLocList)
                    os.rename(fileLoc,removeName)

                    print("Removing file: " + str(fileLoc))
                else:
                    continue

    if counter > 0:
        print("\nSuccess!\nRemoved " + str(counter) + " files from the " + str(year) + " Laser Data folder.")
    else:
        print("There were no files found that are safe to delete")
if __name__ == "__main__": main()
