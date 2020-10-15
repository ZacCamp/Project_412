import random
import sys
import time 
import os
from datetime import datetime, timedelta


def getRandomTime():#generate random dates 
    start = datetime.now()
    end = start + timedelta(days=random.randint(-100 ,-50))
    random_date = start + (end - start) * random.random()
    return random_date

def main():
    with open('pet_adoptions.txt', 'w') as fp:
        for i in range(100):
            contractID = str(i)  #sequential ID for contract ID
            contactDate = str(getRandomTime().date()) #random date
            fp.write( contactDate + "::" + contractID + "::\n")
    
  


    
if __name__ == '__main__':
    main()

