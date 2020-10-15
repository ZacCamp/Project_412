import random
import sys
import time 
import os

def main():

    dataList = []
    with open("dogs_data.txt", "r") as fp:
        for line in fp:
            splitList = line.split('::')
            shelterID = random.randint(0,4) #generate random shelter to assign to ID
            dogID = splitList[7]
            dataList.append(dogID + "::" + str(shelterID) + "::\n")

    with open("lives_in.txt", 'w') as fp:
        for line in dataList:
            fp.write(line)

    
if __name__ == '__main__':
    main()

