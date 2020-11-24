import random
import sys
import time 
import os
from datetime import datetime, timedelta

NUMBER_OF_PEOPLE = 50
NUMBER_OF_PET_ADOPTIONS = 100
NUMBER_OF_DOGS = 1000
NUMBER_OF_PET_APPLICATIONS = 100
intakeType = ['surrendered', 'stray']
sex = ['male', 'female']
maintenanceLevel = ['low', 'medium', 'high']
temperament = ['assertive', 'neutral', 'passive']
breed = ['affenpinscher','Afghan hound','Airedale terrier','Akita','Alaskan Malamute','American Staffordshire terrier','American water spaniel','Australian cattle dog','Australian shepherd','Australian terrier','basenji','basset hound','beagle','bearded collie','Bedlington terrier','Bernese mountain dog','bichon frise','black and tan coonhound','bloodhound','border collie','border terrier','borzoi','Boston terrier','bouvier des Flandres','boxer','briard','Brittany','Brussels griffon','bull terrier','bulldog','bullmastiff','cairn terrier','Canaan dog','Chesapeake Bay retriever','Chihuahua','Chinese crested','Chinese shar-pei','chow chow','Clumber spaniel','cocker spaniel','collie','curly-coated retriever','dachshund','Dalmatian','Doberman pinscher','English cocker spaniel','English setter','English springer spaniel','English toy spaniel','Eskimo dog','Finnish spitz','flat-coated retriever','fox terrier','foxhound','French bulldog','German shepherd','German shorthaired pointer','German wirehaired pointer','golden retriever','Gordon setter','Great Dane','greyhound','Irish setter','Irish water spaniel','Irish wolfhound','Jack Russell terrier','Japanese spaniel','keeshond','Kerry blue terrier','komondor','kuvasz','Labrador retriever','Lakeland terrier','Lhasa apso','Maltese','Manchester terrier','mastiff','Mexican hairless','Newfoundland','Norwegian elkhound','Norwich terrier','otterhound','papillon','Pekingese','pointer','Pomeranian','poodle','pug','puli','Rhodesian ridgeback','Rottweiler','Saint Bernard','saluki','Samoyed','schipperke','schnauzer','Scottish deerhound','Scottish terrier','Sealyham terrier','Shetland sheepdog','shih tzu','Siberian husky','silky terrier','Skye terrier','Staffordshire bull terrier','soft-coated wheaten terrier','Sussex spaniel','spitz','Tibetan terrier','vizsla','Weimaraner','Welsh terrier','West Highland white terrier','whippet','Yorkshire terrier']
#==================================================================================================================

def createDogFile():
    dataAsList = []

    for ID in range(NUMBER_OF_DOGS):

        dataAsList.append(breed[random.randint(0, 114)] + "::") #breed
        dataAsList.append(intakeType[random.randint(0, 1)] + "::") #intake type
        dataAsList.append(sex[random.randint(0, 1)] + "::") #gender

        dataAsList.append(maintenanceLevel[random.randint(0, 2)] + "::") #maintenanceLevel
        dataAsList.append(temperament[random.randint(0, 2)] + "::") #temperament

        dataAsList.append(str(random.randint(1, 13)) + "::") # age

        dataAsList.append('false' + "::") # adopted status
        dataAsList.append(str(random.randint(0,4)) + "::") #shelterID
        dataAsList.append(str(ID) + "::\n") # sequential id

    File = open("dogs_data.txt", "w")

    for line in dataAsList:
        File.write(line)
#==================================================================================================================

def createShelterFile():   
    shelterAndNumber = [('Friends For Life Animal Rescue', '(480) 497-8296', '952 W Melody Ave, Gilbert, AZ 85233'), ('Foothills Animal Rescue', '(480) 488-9890', '10197 E Bell Rd, Scottsdale, AZ 85260'), ('Maricopa County Animal Care and Control', '(602) 506-7387', '2500 S 27th Ave, Phoenix, AZ 85009'), ('AAWL Adoption Center', '(602) 781-3906', '3111 W Chandler Blvd, Chandler, AZ 85226'), ('Arizona Animal Welfare League & SPCA', '(602) 273-6852', '25 N 40th St, Phoenix, AZ 85034')]

    dataAsList = []

    for ID in range(5):

        for item in shelterAndNumber[ID]:
             dataAsList.append(item + "::")

        dataAsList.append(str(ID) + "::\n") # sequential id

    File = open("shelter_data.txt", "w")

    for line in dataAsList:
        File.write(line)

#==================================================================================================================

def createPersonFile():
    Names = ["Beitris Pereira", "Hillary Davidi", "Reinald O'Luney", "Dacia Billanie", "Benson Moatt", "Samantha Briton", "Waldon Klemencic", "Reinhold Rabjohns", "Chantalle Stickel", "Darcy Tredger", "Joel Lowbridge", "Alyssa Barkus", "Tommie Shiel", "Ellen Baglan", "Benedict Gounot", "Hana Schechter", "Venita Kwietek", "Ikey Simkovich", "Margit Abbett", "Berny Cullerne", "Feodora Kee", "Symon Le Pine", "Clayborn Ternault", "Giraud Tweddell", "Pooh Tooke", "Regen Acton", "Milly Miko", "Lennie Klimaszewski", "Pete Finlater", "Kamilah Lingwood", "Raddie Stokey", "Regine Arrowsmith", "Leonora Proudley", "Nollie Lembke", "Lay Kierans", "Linette Waylen", "Stella Chrstine", "Alexander Finicj", "Katrina Blindermann", "Ax Andrysek", "Hill Simyson", "Kimberlyn Pods", "Ivy Pattullo", "Warde Storch", "Julissa Martyns", "Falito O'Scully", "Galven Watkin", "Cordie Huson", "Onofredo Guittet", "Barbee Brunger"]
    dataAsList = []
    namesList =[]
    for ID in range(NUMBER_OF_PEOPLE):
        dataAsList.append(Names[ID]+"::")
        dataAsList.append(str(ID) + "::\n") # sequential id

    File = open("person.txt", "w")

    for line in dataAsList:
        File.write(line)

#==================================================================================================================

def createEmployeeAndAdopterFile(): 
    zipCode = ["85023", "85032", "85002", "85003", "85048", "85064", "85055", "85067", "85026"]
    phones = ["303-561-1772","127-155-3630","530-686-3980", "491-266-9936", "968-389-8023", "928-854-3130", "242-811-0549", "403-501-3816", "893-238-0755", "567-566-1601", "923-119-4415", "671-789-2165", "242-250-0794", "167-656-2415", "828-934-5952", "982-198-5617", "559-588-4022", "902-560-1980", "734-666-0238", "994-942-8710", "153-500-7399", "952-789-6137", "566-907-9841", "996-278-0828", "828-891-0950", "936-799-5177", "198-283-0427", "653-931-4874", "308-992-9310", "355-291-9016", "304-632-3567", "881-225-8008", "562-434-1038", "357-141-2445", "842-815-9410", "998-886-9578", "442-790-8299", "974-494-7705", "574-687-7054", "771-191-2001", "730-883-6735", "527-435-2408", "373-994-2819", "166-269-0705", "543-140-4294", "669-756-4029", "963-996-1315", "704-193-8471", "178-829-9221", "842-108-8903"]

    employeeList = []
    adopterList = []
    with open("person.txt", "r") as fp:
        counter = 0
        for line in fp:
            randomNum = random.randint(0, 1)# random number to see if person is employee or adopter
            if(randomNum == 0) : #if adopter
                adopterList.append(line[: len(line) - 1] + zipCode[random.randint(0, len(zipCode) - 1)] + "::" + phones[counter] + "::\n")  #zip code and phone
                counter+= 1
            elif (randomNum == 1):  #if employee
                shelterID = str(random.randint(0,4))
                employeeList.append(line[: len(line) - 1] + shelterID + "::\n" ) # add employee to list

    
    with open("adopter.txt", "w") as adopterFile:
        for line in adopterList:
          adopterFile.write(line)

    with open("employee.txt", "w") as employeeFile:
        for line in employeeList:
            employeeFile.write(line)

#==================================================================================================================

def getRandomTime():#generate random dates 
    start = datetime.now()
    end = start + timedelta(days=random.randint(-100 ,-50))
    random_date = start + (end - start) * random.random()
    return random_date

#==================================================================================================================
#
#def createPetAdoptionFile():
#    with open('pet_adoptions.txt', 'w') as fp:
#        for i in range(NUMBER_OF_PET_ADOPTIONS):
#            contractID = str(i)  #sequential ID for contract ID
#            contactDate = str(getRandomTime().date()) #random date
#            fp.write(contactDate + "::" + contractID + "::\n")

#==================================================================================================================

def createAppliesForFile():
    dataList = []
    with open("adopter.txt", "r") as fp:
        for line in fp:
            splitList = line.split('::')
            dataList.append(splitList[1])#personID
            
    with open("applies_for.txt", 'w') as fp:
        for i in range(NUMBER_OF_PET_APPLICATIONS):
            desiredSex = sex[random.randint(0, 1)]  #male or female
            desiredBreed = breed[random.randint(0, len(breed) - 1)]  #
            desiredTemperament = temperament[random.randint(0,len(temperament)-1)]
            maxMaintenanceLevel = maintenanceLevel[random.randint(0, len(maintenanceLevel) - 1)]
            desiredIntakeType = intakeType[random.randint(0, len(intakeType) - 1)]
            maxAge = str(random.randint(0, 14))
            personID = str(dataList[random.randint(0,len(dataList)-1)]) #pick one of adopters randomly
            fp.write( desiredBreed + "::" + desiredSex  + "::"  + desiredTemperament + "::" + maxMaintenanceLevel + "::" + desiredIntakeType + "::" + maxAge + "::" +personID +  "::\n" )
#==================================================================================================================

def main():
    createDogFile()
    createShelterFile()
    createPersonFile()
    createEmployeeAndAdopterFile()
    createPetAdoptionFile()
    createAppliesForFile()
    
#==================================================================================================================

if __name__ == '__main__':
    main()

