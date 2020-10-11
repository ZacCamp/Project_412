import random
import sys
import time 
import os

intakeType = ['surrendered', 'stray']
sex = ['male', 'female']
maintenanceLevel = ['low', 'medium', 'high']
temperment = ['assertive', 'neutral', 'passive']

def main():

    dataAsList = []

    for ID in range(1000):

        dataAsList.append(intakeType[random.randint(0, 1)] + "::")
        dataAsList.append(sex[random.randint(0, 1)] + "::")

        dataAsList.append(maintenanceLevel[random.randint(0, 2)] + "::")
        dataAsList.append(temperment[random.randint(0, 2)] + "::")

        dataAsList.append(str(random.randint(1, 13)) + "::") # age
        dataAsList.append(str(ID) + "::\n") # sequential id

    File = open("dogs_data.txt", "w")

    for line in dataAsList:
        File.write(line)

if __name__ == '__main__':
    main()

