import random
import sys
import time 
import os

shelterAndNumber = [('Friends For Life Animal Rescue', '(480) 497-8296', '952 W Melody Ave, Gilbert, AZ 85233'), ('Foothills Animal Rescue', '(480) 488-9890', '10197 E Bell Rd, Scottsdale, AZ 85260'), ('Maricopa County Animal Care and Control', '(602) 506-7387', '2500 S 27th Ave, Phoenix, AZ 85009'), ('AAWL Adoption Center', '(602) 781-3906', '3111 W Chandler Blvd, Chandler, AZ 85226'), ('Arizona Animal Welfare League & SPCA', '(602) 273-6852', '25 N 40th St, Phoenix, AZ 85034')]

def main():

    dataAsList = []

    for ID in range(5):

        for item in shelterAndNumber[ID]:
             dataAsList.append(item + "::")

        dataAsList.append(str(ID) + "::\n") # sequential id

    File = open("shelter_data.txt", "w")

    for line in dataAsList:
        File.write(line)

if __name__ == '__main__':
    main()

