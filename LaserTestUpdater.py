#!usr/bin/python


### Imports ###
from photonicsfolders2 import AutoUpdate
import shutil
import csv
import os
from datetime import datetime

class Error(Exception):
    pass

class LengthError(Error):
    pass

class NumberError(Error):
    pass

def main():
    desktopPath = os.path.join(os.environ["HOMEPATH"],'Desktop')
    loop = True
    while loop:
        try:
            laserNum = int(input("\nHow many lasers would you like to give data for? "))
            serialN = [[] for x in range(0,laserNum)]
            loop = False
        except ValueError as e:
            print("\nPlease input an integer value")


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
    print("\nUse the below numbers to indicate the tests that you want to enter information for:\n1 - Chamber\n2 - Vibration\n3 - LTT\n4 - Shock\n\nYou may enter multiple tests separated by a comma.")

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

                loop3 = False

            except NumberError as e:
                print("\nPlease input a number corresponding to the tests according to the list above")

            except ValueError as e:
                print("\nPlease input integers only")

            except LengthError as e:
                print("\nToo many tests have been indicated, please correct")

    dt = datetime.now().date()
    date = '{0}-{1}-{2:02}'.format(dt.month, dt.day, dt.year % 100)
    fileName = str(date) + ".csv"
    filePath = os.path.join(desktopPath, fileName)

    with open(filePath,'w', newline='') as file:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        for x in range(0,len(serialN)):
            wr.writerow(serialN[x])

        print("\nSuccess! The file has been saved to your desktop as " + fileName + "\n")
    print("Press Enter to exit this program...")
    input()
    exit()

if __name__ == "__main__":
    main()
