#!usr/bin/python


### Imports ###
from photonicsfolders2 import AutoUpdate
import shutil
import csv
import os

class Error(Exception):
    pass

class LengthError(Error):
    pass

class NumberError(Error):
    pass

def main():
    desktopPath = os.path.join(os.environ["HOMEPATH"],'Desktop')

    try:
        laserNum = int(input("\nHow many lasers would you like to give data for? "))
        serialN = [[] for x in range(0,laserNum)]
    except ValueError as e:
        print("\nPlease input an integer value\n")

    #Get all serial numbers of the systems
    try:
        for x in range(0,laserNum):
            try:
                if x == 0:
                    SN = str(input("\n1st Serial Number: "))
                    serialN[x].append(SN)
                elif x == 1:
                    SN = str(input("\n2nd Serial Number: "))
                    serialN[x].append(SN)
                elif x == 2:
                    SN = str(input("\n3rd Serial Number: "))
                    serialN[x].append(SN)
                else:
                    SN = str(input("\n" + str(x) +"th Serial Number: "))
                    serialN[x].append(SN)

                checkSplit = serialN[x][0].split("-")

                #check to ensure Serial Number is in correct format
                check = type(int(checkSplit[0])) is int
                check2 = type(int(checkSplit[1])) is int
                check3 = True
                check4 = True

                if len(checkSplit[0])>2:
                    check3 = False
                if len(checkSplit[1])>3:
                    check4 = False

                if (check is False) or (check2 is False):
                    raise ValueError
                if (check3 is False) or (check4 is False):
                    raise LengthError

            except LengthError as e:
                print("\nIncorrect Serial Number format. Please correct.\n")

            except ValueError as e:
                print("\nPlease input an integer value\n")

    except IndexError as e:
        print("\nPlease enter the Serial Number in the proper YY-XXX format\n")

    except ValueError as e:
        print("\nPlease input an integer value\n")

    #Figure out which tests the system passed and failed
    print("\n1 - Chamber\n2 - Vibration\n3 - LTT\n4 - Shock\n\nYou may enter multiple tests separated by a comma.")

    for x in range(0,len(serialN)):
        try:
            passedTests = str(input("\nWhich tests did "+ serialN[x][0] + " Pass? If updating failure, input 0\n"))

            if passedTests == "0":
                try:
                    failedTest = int(input("Which test did "+ serialN[x][0] + " fail?\n"))

                    #ensure no number greater than the largest corresponding test was entered
                    if failedTest > 4:
                        raise NumberError

                except ValueError as e:
                    print("\nPlease input an integer\n")
                except NumberError as e:
                    print("\nPlease input a correct integer corresponding to a test\n")
                #Append the list to account for test results
                for k in range(1,5):
                    print(x,k)
                    if k is failedTest:
                        serialN[x].append(0)
                    else:
                        serialN[x].append("")
                    print(serialN[x])

            else:
                passedTestList = passedTests.split(",")

                if len(passedTestList) > 4:
                    raise LengthError

                #Denote that the specific tests passed or haven't been tested
                for j in range(1,5):
                    if str(j) in passedTestList:
                        serialN[x].append(1)
                    else:
                        serialN[x].append("")
            print(serialN)

        except ValueError as e:
            print("\nPlease input integers only\n")

        except LengthError as e:
            print("\nToo many tests have been indicated, please correct\n")

    firstFileName = input("What would you like to name the CSV?")
    fileName = firstFileName + ".csv"
    filePath = os.path.join(desktopPath, fileName)

    with open(filePath,'w', newline='') as file:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        for x in range(0,len(serialN)):
            wr.writerow(serialN[x])
            # for data in serialN[x]:
            #     wr.writerow([data])

        print("Success! The file has been saved to your desktop as " + fileName + "\n")
    print("Press Enter to exit this program...")
    input()
    exit()

if __name__ == "__main__":
    main()
