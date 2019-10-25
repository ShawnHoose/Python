#!usr/bin/python
#Author: Shawn Hoose
#Created: 1/4/19
#Updated: 8/28/19

### Imports ###
from photonicsfolders2 import FindLaserDataFolder
from photonicsfolders2 import AutoUpdate
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

class TimeError(Error):
    pass

def main():
    AutoUpdate("*REMOVED*", os.path.basename(__file__))
    savePath = "*REMOVED*"
    dt = datetime.now().date()
    todayDate = '{0}-{1}-{2:02}'.format(dt.month, dt.day, dt.year % 100)

    #multiple date loop
    multipleDate = True
    while multipleDate:
        #Gather date for data entry
        dateLoop = True
        while dateLoop:
            try:
                date = input("\nWhat date would you like to enter data for? (MM-DD-YY) ")
                #Ensure date formatting is correct and only contains ints
                if (len(date) is not 8) or (date[2] is not "-") or (date[5] is not "-"):
                    raise DateError

                #Check if date is within 30 days, raise error if not
                if (abs(datetime.strptime(date, "%m-%d-%y")-datetime.strptime(todayDate, "%m-%d-%y")).days) > 30:
                    raise LengthError

                #Checks to make sure date isn't in the future
                if (datetime.strptime(todayDate, "%m-%d-%y") - datetime.strptime(date, "%m-%d-%y")).days < 0:
                    raise TimeError

                dateLoop = False

            except TimeError as e:
                print("You cannot enter data for a date which has not yet happened, Marty. \n")

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
        modelPath = "*REMOVED*"
        modelFile = open(modelPath,"r")
        #Creates Set of model names
        modelList = set(line[:-1] for line in modelFile)

        serialN = {}

        loop = True
        while loop:
            try:
                laserNum = int(input("\nHow many lasers would you like to give data for? "))
                if laserNum < 1:
                    raise NumberError
                loop = False

            except ValueError as e:
                print("\nPlease input an integer value")

            except NumberError as e:
                print("Enter a value greater than 0")

        #Get all serial numbers of the systems
        for x in range(laserNum):
            loop2 = True
            while loop2:
                try:
                    if x == 0:
                        SN = str(input("\n1st Serial Number: "))
                        serialN[SN] = None
                    elif x == 1:
                        SN = str(input("\n2nd Serial Number: "))
                        if SN in serialN:
                            raise NumberError
                        serialN[SN] = None
                    elif x == 2:
                        SN = str(input("\n3rd Serial Number: "))
                        if SN in serialN:
                            raise NumberError
                        serialN[SN] = None
                    else:
                        SN = str(input("\n" + str(x+1) +"th Serial Number: "))
                        if SN in serialN:
                            raise NumberError
                        serialN[SN] = None


                    checkSplit = SN.split("-")
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
                    if SN in serialN:
                        serialN.pop(SN, None)

                except IndexError as e:
                    print("\nPlease enter the Serial Number in the proper YY-XXX format\n")
                    if SN in serialN:
                        serialN.pop(SN, None)

                except NumberError as e:
                    print("\nThat serial number was already entered. Please enter the correct serial number.")

        #Figure out which tests the system passed and failed
        print("*REMOVED*")

        keys = list(key for key in serialN.keys())

        for x in range(len(serialN)):
            loop3 = True
            while loop3:
                try:
                    passedTests = str(input("\nWhich tests did "+ keys[x] + " Pass? If updating failure, input 0\n"))

                    if passedTests == "0":
                        loop4 = True
                        while loop4:
                            try:
                                failedTest = str(input("Which test(s) did "+ keys[x] + " fail?\n"))
                                splitFail = failedTest.split(",")

                                if len(splitFail) > 4:
                                    raise LengthError
                                #Append the list to account for test results
                                failedList = set(splitFail)
                                for i in failedList:
                                    check6 = type(int(i)) is int

                                    if int(i) > 4:
                                        raise NumberError

                                    if not check6:
                                        raise ValueError

                                data = []
                                for k in range(1,5):
                                    if str(k) in failedList:
                                        data.append(0)
                                    else:
                                        data.append("")
                                serialN[keys[x]] = data
                                loop4 = False

                            except ValueError as e:
                                print("\nPlease input an integer")
                            except NumberError as e:
                                print("\nPlease input a number corresponding to the tests according to the list above")
                            except LengthError as e:
                                print("\nToo many tests have been indicated, please correct")
                    else:
                        splitPass = passedTests.split(",")

                        if len(splitPass) > 4:
                            raise LengthError

                        passedTestList = set(splitPass)

                        for i in passedTestList:
                            check5 = type(int(i)) is int

                            if int(i) > 4:
                                raise NumberError

                            if not check5:
                                raise ValueError

                        #Denote that the specific tests passed or haven't been tested
                        data = []
                        for j in range(1,5):
                            if str(j) in passedTestList:
                                data.append(1)
                            else:
                                data.append("")
                        serialN[keys[x]] = data

                    #Checks if model is in list, obtains if it isn't
                    checkSplit = keys[x].split("-")
                    folderPath = FindLaserDataFolder(checkSplit[0],keys[x])
                    serialized = folderPath.split("\\")[-1]

                    splitSerial = serialized.split(" ")

                    #Corrects model name if space between name and 'SP'
                    if len(splitSerial) > 2:
                        if splitSerial[2] == "SP":
                            splitSerial[1] = ''.join(splitSerial[1:3])

                    if len(splitSerial) is 1:
                        model = input("The model name detected does not match our list...Please input the correct model name. ")
                    else:
                        model = splitSerial[1]

                    #appends model and date to end of appropriate list
                    if model in modelList:
                        data.append(model)
                    elif len(splitSerial) is 1:
                        data.append(model)
                    else:
                        newModel = input("The model name detected does not match our list...Please input the correct model name. ")
                        data.append(newModel)

                    modelFile.close() #Close the modelList file
                    data.append(date)
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
                for x in range(len(serialN)):
                    output = [keys[x]]
                    output += serialN[keys[x]]
                    wr.writerow(output)

                print("\nSuccess! The CSV file " + fileName + " has been appended\n")

        else:
            with open(filePath,'w', newline='') as file:
                wr = csv.writer(file, quoting=csv.QUOTE_ALL)
                for x in range(len(serialN)):
                    output = [keys[x]]
                    output += serialN[keys[x]]
                    wr.writerow(output)

                print("\nSuccess! The file has been saved to the CSV folder as " + fileName + "\n")

        try:
            cont = input("Would you like to enter data for another date? ")
            if ((cont.lower() != "yes") and (cont.lower() != "no")):
                raise ValueError

            #exits loop if user only wants to enter one date
            if cont.lower() == "no":
                multipleDate = False

        except ValueError as e:
            print("\nError: You may only enter 'yes' or 'no'\n")

    print("\nPress Enter to exit this program...")
    input()
    sys.exit()

if __name__ == "__main__":
    main()
