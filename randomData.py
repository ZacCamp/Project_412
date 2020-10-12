import random
import sys
import time 
import os

intakeType = ['surrendered', 'stray']
sex = ['male', 'female']
maintenanceLevel = ['low', 'medium', 'high']
temperment = ['assertive', 'neutral', 'passive']
breed = ['affenpinscher','Afghan hound','Airedale terrier','Akita','Alaskan Malamute','American Staffordshire terrier','American water spaniel','Australian cattle dog','Australian shepherd','Australian terrier','basenji','basset hound','beagle','bearded collie','Bedlington terrier','Bernese mountain dog','bichon frise','black and tan coonhound','bloodhound','border collie','border terrier','borzoi','Boston terrier','bouvier des Flandres','boxer','briard','Brittany','Brussels griffon','bull terrier','bulldog','bullmastiff','cairn terrier','Canaan dog','Chesapeake Bay retriever','Chihuahua','Chinese crested','Chinese shar-pei','chow chow','Clumber spaniel','cocker spaniel','collie','curly-coated retriever','dachshund','Dalmatian','Doberman pinscher','English cocker spaniel','English setter','English springer spaniel','English toy spaniel','Eskimo dog','Finnish spitz','flat-coated retriever','fox terrier','foxhound','French bulldog','German shepherd','German shorthaired pointer','German wirehaired pointer','golden retriever','Gordon setter','Great Dane','greyhound','Irish setter','Irish water spaniel','Irish wolfhound','Jack Russell terrier','Japanese spaniel','keeshond','Kerry blue terrier','komondor','kuvasz','Labrador retriever','Lakeland terrier','Lhasa apso','Maltese','Manchester terrier','mastiff','Mexican hairless','Newfoundland','Norwegian elkhound','Norwich terrier','otterhound','papillon','Pekingese','pointer','Pomeranian','poodle','pug','puli','Rhodesian ridgeback','Rottweiler','Saint Bernard','saluki','Samoyed','schipperke','schnauzer','Scottish deerhound','Scottish terrier','Sealyham terrier','Shetland sheepdog','shih tzu','Siberian husky','silky terrier','Skye terrier','Staffordshire bull terrier','soft-coated wheaten terrier','Sussex spaniel','spitz','Tibetan terrier','vizsla','Weimaraner','Welsh terrier','West Highland white terrier','whippet','Yorkshire terrier']

def main():

    dataAsList = []

    for ID in range(1000):

        dataAsList.append(breed[random.randint(0, 114)] + "::")
        dataAsList.append(intakeType[random.randint(0, 1)] + "::")
        dataAsList.append(sex[random.randint(0, 1)] + "::")

        dataAsList.append(maintenanceLevel[random.randint(0, 2)] + "::")
        dataAsList.append(temperment[random.randint(0, 2)] + "::")

        dataAsList.append(str(random.randint(1, 13)) + "::") # age

        dataAsList.append('false' + "::") # adopted status

        dataAsList.append(str(ID) + "::\n") # sequential id

    File = open("dogs_data.txt", "w")

    for line in dataAsList:
        File.write(line)

if __name__ == '__main__':
    main()

