import random
import sys
import time 
import os

def main():

    temp = []
    dataList = [] 
    contractIDList = random.sample(range(100), 100)  # generate 100 random numbers list 0-99 no repeats
    dogRandomList = random.sample(range(1000), 100)  # generate 100 random numbers list 0-999 no repeats

    with open("dogs_data.txt", "r") as fp:  # first 100 dogs in file will be used
        for line in fp: 
            splitList = line.split('::')
            dogID = splitList[7] 
            temp.append(dogID)
            
    for i in range(100):
        #chooses 1 of dog from 1000 as as 1 contractId from 100
        dataList.append(temp[dogRandomList[i]] + "::" + str(contractIDList[i]) + "::\n" )
        
    with open("is_adopted.txt", 'w') as fp:
        for line in dataList:
            fp.write(line)

    
if __name__ == '__main__':
    main()

