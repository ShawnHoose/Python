#!usr/bin/python


### Imports ###
from *REMOVED*
import shutil
import csv
import sys
import os
from datetime import datetime

class Error(Exception):
    pass

class LengthError(Error):
    pass

class NumberError(Error):
    pass

class DateError(Error):
    pass

def main():
    savePath = *REMOVED*
    dt = datetime.now().date()
    todayDate = '{0}-{1}-{2:02}'.format(dt.month, dt.day, dt.year % 100)

    #Gather date for data entry
    dateLoop = True
    while dateLoop:
        try:
            date = input("What date would you like to enter data for? (MM-DD-YY) ")
            #Ensure date formatting is correct and only contains ints
            if (len(date) is not 8):
                raise DateError
            if ((date[2] is not "-") or (date[5] is not "-")):
                raise DateError

            #Check to see if date only contains integers between the hyphens
            index = 0
            while index < 7:
                intCheck = type(int(date[index:index + 2])) is int
                index += 3

            #Check if date is within 30 days, raise error if not
            if (abs(datetime.strptime(date, "%m-%d-%y")-datetime.strptime(todayDate, "%m-%d-%y")).days) > 30:
                raise LengthError

            dateLoop = False

        except DateError as e:
            print("Incorrect date format. Please use the provided format.\n")

        except ValueError as e:
            print("Your date can only contain integer values or it must be a real date. Please correct. \n")

        except LengthError as e:
            print("Please enter a date within 30 days of today's date\n")

    fileList = [f for f in os.listdir(savePath) if os.path.isfile(os.path.join(savePath, f))]

    fileName = str(date) + ".csv"
    filePath = os.path.join(savePath, fileName)

    #Get model names from file to compare to
    serverPath = *REMOVED*
    modelPath = os.path.join(serverPath, "modelList.txt")
    modelFile = open(modelPath,"r")
    modelList = modelFile.read().splitlines()

    loop = True
    while loop:
        try:
            laserNum = int(input("\nHow many lasers would you like to give data for? "))
            if laserNum is 0:
                raise NumberError
            serialN = [[] for x in range(0,laserNum)]
            loop = False

        except ValueError as e:
            print("\nPlease input an integer value")

        except NumberError as e:
            print("Enter a value greater than 0")

    #Get all serial numbers of the systems
    for x in range(0,laserNum):
        loop2 = True
        while loop2:
            try:
                if x == 0:
                    SN = str(input("\n1st Serial Number: "))
                    serialN[x].append(SN)
                elif x == 1:
                    SN = str(input("\n2nd Serial Number: "))
                    for j in range(0,len(serialN)):
                        if str(SN) in serialN[j]:
                            raise NumberError
                    serialN[x].append(SN)
                elif x == 2:
                    SN = str(input("\n3rd Serial Number: "))
                    for j in range(0,len(serialN)):
                        if str(SN) in serialN[j]:
                            raise NumberError
                    serialN[x].append(SN)
                else:
                    SN = str(input("\n" + str(x+1) +"th Serial Number: "))
                    for j in range(0,len(serialN)):
                        if str(SN) in serialN[j]:
                            raise NumberError
                    serialN[x].append(SN)


                checkSplit = serialN[x][0].split("-")
                #check to ensure Serial Number is in correct format
                check = type(int(checkSplit[0])) is int
                check2 = type(int(checkSplit[1])) is int
                check3 = True
                check4 = True

                if len(checkSplit) is not 2:
                    check4 = False
                if len(checkSplit[0]) is not 2:
                    check3 = False
                if len(checkSplit[1]) is not 3:
                    check4 = False

                if (check is False) or (check2 is False):
                    raise ValueError
                if (check3 is False) or (check4 is False):
                    raise IndexError

                loop2 = False

            except ValueError as e:
                print("\nPlease input an integer value\n")
                del serialN[x][0]

            except IndexError as e:
                print("\nPlease enter the Serial Number in the proper YY-XXX format\n")
                del serialN[x][0]

            except NumberError as e:
                print("That serial number was already entered. Please enter the correct serial number.")

    #Figure out which tests the system passed and failed
    print("*REMOVED*")

    for x in range(0,len(serialN)):
        loop3 = True
        while loop3:
            try:
                passedTests = str(input("\nWhich tests did "+ serialN[x][0] + " Pass? If updating failure, input 0\n"))

                if passedTests == "0":
                    loop4 = True
                    while loop4:
                        try:
                            failedTest = int(input("Which test did "+ serialN[x][0] + " fail?\n"))

                            #ensure no number greater than the largest corresponding test was entered
                            if failedTest > 4:
                                raise NumberError

                            loop4 = False

                        except ValueError as e:
                            print("\nPlease input an integer")
                        except NumberError as e:
                            print("\nPlease input a correct integer corresponding to a test")
                    #Append the list to account for test results
                    for k in range(1,5):
                        if k is failedTest:
                            serialN[x].append(0)
                        else:
                            serialN[x].append("")

                else:
                    passedTestList = passedTests.split(",")

                    for i in passedTestList:
                        check5 = type(int(i)) is int

                        if int(i) > 4:
                            raise NumberError

                    if not check5:
                        raise ValueError

                    #Denote that the specific tests passed or haven't been tested
                    for j in range(1,5):
                        if str(j) in passedTestList:
                            serialN[x].append(1)
                        else:
                            serialN[x].append("")

                #Checks if model is in list, obtains if it isn't
                checkSplit = serialN[x][0].split("-")
                folderPath = FindLaserDataFolder(checkSplit[0],serialN[x][0])
                serialized = folderPath.split("\\")[-1]

                splitSerial = serialized.split(" ")

                #Corrects model name if space between name and 'SP'
                if len(splitSerial) > 2:
                    if splitSerial[2] == "SP":
                        splitSerial[1] = ''.join(splitSerial[1:3])

                model = splitSerial[1]
                #appends model and date to end of appropriate list
                if model in modelList:
                    serialN[x].append(model)
                else:
                    newModel = input("The model name detected does not match our list...Please input the correct model name. ")
                    serialN[x].append(newModel)
                modelFile.close() #Close the modelList file
                serialN[x].append(date)
                loop3 = False

            except NumberError as e:
                print("\nPlease input a number corresponding to the tests according to the list above")

            except ValueError as e:
                print("\nPlease input integers only")

            except LengthError as e:
                print("\nToo many tests have been indicated, please correct")

    #If file already exists, append data to end, otherwise create file
    if fileName in fileList:
        with open(filePath,'a', newline='') as file:
            wr = csv.writer(file, quoting=csv.QUOTE_ALL)
            for x in range(0,len(serialN)):
                wr.writerow(serialN[x])

            print("\nSuccess! The CSV file " + fileName + " has been appended\n")

    else:
        with open(filePath,'w', newline='') as file:
            wr = csv.writer(file, quoting=csv.QUOTE_ALL)
            for x in range(0,len(serialN)):
                wr.writerow(serialN[x])

            print("\nSuccess! The file has been saved to the CSV folder as " + fileName + "\n")

    print("Press Enter to exit this program...")
    input()
    sys.exit()

if __name__ == "__main__":
    main()
