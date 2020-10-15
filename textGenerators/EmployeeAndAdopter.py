import random
import sys
import time 
import os

zipCode = ["85023", "85032", "85002", "85003", "85048", "85064", "85055", "85067", "85026"]
phones = ["303-561-1772",
"127-155-3630",
"530-686-3980",
"491-266-9936",
"968-389-8023",
"928-854-3130",
"242-811-0549",
"403-501-3816",
"893-238-0755",
"567-566-1601",
"923-119-4415",
"671-789-2165",
"242-250-0794",
"167-656-2415",
"828-934-5952",
"982-198-5617",
"559-588-4022",
"902-560-1980",
"734-666-0238",
"994-942-8710",
"153-500-7399",
"952-789-6137",
"566-907-9841",
"996-278-0828",
"828-891-0950",
"936-799-5177",
"198-283-0427",
"653-931-4874",
"308-992-9310",
"355-291-9016",
"304-632-3567",
"881-225-8008",
"562-434-1038",
"357-141-2445",
"842-815-9410",
"998-886-9578",
"442-790-8299",
"974-494-7705",
"574-687-7054",
"771-191-2001",
"730-883-6735",
"527-435-2408",
"373-994-2819",
"166-269-0705",
"543-140-4294",
"669-756-4029",
"963-996-1315",
"704-193-8471",
"178-829-9221",
"842-108-8903"]



def main():

    employeeList = []
    adopterList = []
    fp = open("person.txt", "r")
    counter = 0
    for line in fp:
        randomNum = random.randint(0, 1)
        if(randomNum == 0) : #if adopter
            adopterList.append(line[: len(line) - 1] + zipCode[random.randint(0, len(zipCode) - 1)] + "::" + phones[counter] + "::\n")  #zip code and ID
            counter+= 1
        elif (randomNum == 1):#if employee
            employeeList.append(line)
    fp.close()

    adopterFile = open("adopter.txt", "w")

    for line in adopterList:
        adopterFile.write(line)
    adopterFile.close()

    employeeFile = open("employee.txt", 'w')

    for line in employeeList:
        employeeFile.write(line)
    adopterFile.close()


if __name__ == '__main__':
    main()

