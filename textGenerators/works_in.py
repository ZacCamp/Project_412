import random
import sys
import time 
import os

def main():

    dataList = []
    with open("employee.txt", "r") as fp:
        for line in fp:
            splitList = line.split('::')
            shelterID = random.randint(0,4)
            personID = splitList[1]
            dataList.append(personID + "::" + str(shelterID) + "::\n")

    with open("works_in.txt", 'w') as fp:
        for line in dataList:
            fp.write(line)

    
if __name__ == '__main__':
    main()

