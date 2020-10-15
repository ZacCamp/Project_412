#################################################################################################################################################


def loadPersonTable(tableName, filePath, openConnection):

    cursor = openConnection.cursor()
    
    # Be sure to add primary and foreign keys later!!!!!!!!!!!!!
    cursor.execute("CREATE TABLE " + tableName + " (name text, phoneNumber text, address text, shelterID int);") 

    shleterFile = open(filePath, "r")

    dataList = shleterFile.readlines()
    
    for i in dataList:
        splitList = i.split('::')

        name = splitList[0]
        number = splitList[1]
        address = splitList[2]
        shelterID = int(splitList[3])

        cursor.execute("INSERT INTO " + tableName + " VALUES (%s, %s, %s , %s)", (name, number, address, shelterID))

    shleterFile.close()

    cursor.close()
    openConnection.commit()


#################################################################################################################################################


def loadEmployeeTable(tableName, filePath, openConnection):

    cursor = openConnection.cursor()
    
    # Be sure to add primary and foreign keys later!!!!!!!!!!!!!
    cursor.execute("CREATE TABLE " + tableName + " (name text, phoneNumber text, address text, shelterID int);") 

    shleterFile = open(filePath, "r")

    dataList = shleterFile.readlines()
    
    for i in dataList:
        splitList = i.split('::')

        name = splitList[0]
        number = splitList[1]
        address = splitList[2]
        shelterID = int(splitList[3])

        cursor.execute("INSERT INTO " + tableName + " VALUES (%s, %s, %s , %s)", (name, number, address, shelterID))

    shleterFile.close()

    cursor.close()
    openConnection.commit()

#################################################################################################################################################


def loadAdopterTable(tableName, filePath, openConnection):

    cursor = openConnection.cursor()
    
    # Be sure to add primary and foreign keys later!!!!!!!!!!!!!
    cursor.execute("CREATE TABLE " + tableName + " (name text, phoneNumber text, address text, shelterID int);") 

    shleterFile = open(filePath, "r")

    dataList = shleterFile.readlines()
    
    for i in dataList:
        splitList = i.split('::')

        name = splitList[0]
        number = splitList[1]
        address = splitList[2]
        shelterID = int(splitList[3])

        cursor.execute("INSERT INTO " + tableName + " VALUES (%s, %s, %s , %s)", (name, number, address, shelterID))

    shleterFile.close()

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

    shleterFile = open(filePath, "r")

    dataList = shleterFile.readlines()
    
    for i in dataList:
        splitList = i.split('::')

        name = splitList[0]
        number = splitList[1]
        address = splitList[2]
        shelterID = int(splitList[3])

        cursor.execute("INSERT INTO " + tableName + " VALUES (%s, %s, %s , %s)", (name, number, address, shelterID))

    shleterFile.close()

    cursor.close()
    openConnection.commit()

#################################################################################################################################################