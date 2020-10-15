#################################################################################################################################################


def loadPersonTable(tableName, filePath, openConnection):

    cursor = openConnection.cursor()
    
    # Be sure to add primary and foreign keys later!!!!!!!!!!!!!
    cursor.execute("CREATE TABLE " + tableName + " (name text, personID int);")

    fp = open(filePath, "r")

    dataList = fp.readlines()
    
    for i in dataList:
        splitList = i.split('::')

        name = splitList[0]
        personID = int(splitList[1])

        cursor.execute("INSERT INTO " + tableName + " VALUES (%s, %s)", (name, personID))

    fp.close()

    cursor.close()
    openConnection.commit()


#################################################################################################################################################


def loadEmployeeTable(tableName, filePath, openConnection):

    cursor = openConnection.cursor()
    
    # Be sure to add primary and foreign keys later!!!!!!!!!!!!!
    cursor.execute("CREATE TABLE " + tableName + " (name text, personID int ,shelterID int);") 

    fp = open(filePath, "r")

    dataList = fp.readlines()
    
    for i in dataList:
        splitList = i.split('::')

        name = splitList[0]
        personID = int(splitList[1])
        shelterID = int(splitList[2])

        cursor.execute("INSERT INTO " + tableName + " VALUES (%s, %s, %s )", (name, personID, shelterID))

    fp.close()

    cursor.close()
    openConnection.commit()

#################################################################################################################################################


def loadAdopterTable(tableName, filePath, openConnection):

    cursor = openConnection.cursor()
    
    # Be sure to add primary and foreign keys later!!!!!!!!!!!!!
    cursor.execute("CREATE TABLE " + tableName + " (name text, personID int, zipCode int, phoneNumber text);") 

    fp = open(filePath, "r")

    dataList = fp.readlines()
    
    for i in dataList:
        splitList = i.split('::')

        name = splitList[0]
        personID = int(splitList[1])
        zipCode = int(splitList[2])
        phoneNumber = splitList[3]

        cursor.execute("INSERT INTO " + tableName + " VALUES (%s, %s, %s , %s)", (name, number, address, shelterID))

    fp.close()

    cursor.close()
    openConnection.commit()

#################################################################################################################################################

def loadDogTable(tableName, filePath, openConnection):

    cursor = openConnection.cursor()
    
    # Be sure to add primary and foreign keys later!!!!!!!!!!!!!
    cursor.execute("CREATE TABLE " + tableName + " (breed text, intakeType text, sex text, maintenanceLevel text, temperament text, age int, adoptionStatus text, shelterID int, dogID int);") 

    dogFile = open(filePath, "r")

    dataList = dogFile.readlines()
    
    for i in dataList:
        splitList = i.split('::')

        breed = splitList[0]
        intakeType = splitList[1]
        sex = splitList[2]
        maintenanceLevel = splitList[3]
        temperament = splitList[4]
        age = int(splitList[5])
        adoptionStatus = splitList[6]
        shelterID = int(splitList[7])
        dogID = int(splitList[8])

        cursor.execute("INSERT INTO " + tableName + " VALUES (%s, %s, %s , %s , %s , %s, %s, %s, %s)", (breed, intakeType, sex, maintenanceLevel, temperament, age, adoptionStatus, shelterID, dogID))

    dogFile.close()

    cursor.close()
    openConnection.commit()

#################################################################################################################################################


def loadShelterTable(tableName, filePath, openConnection):

    cursor = openConnection.cursor()
    
    # Be sure to add primary and foreign keys later!!!!!!!!!!!!!
    cursor.execute("CREATE TABLE " + tableName + " (name text, phoneNumber text, address text, shelterID int);") 

    fp = open(filePath, "r")

    dataList = fp.readlines()
    
    for i in dataList:
        splitList = i.split('::')

        name = splitList[0]
        number = splitList[1]
        address = splitList[2]
        shelterID = int(splitList[3])

        cursor.execute("INSERT INTO " + tableName + " VALUES (%s, %s, %s , %s)", (name, number, address, shelterID))

    fp.close()

    cursor.close()
    openConnection.commit()

#################################################################################################################################################