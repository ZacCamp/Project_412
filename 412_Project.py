from subprocess import call
import os
import shutil
import psycopg2
import sys

DB_NAME = 'project_412'

def getOpenConnection(user = 'postgres', password ='1234', dbname = 'Project_412'):
    
    return psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='localhost' password='" + password + "'")


def startUpDB (dbname):

    # Connect to defualt Postgres DB

    connection = getOpenConnection(dbname='postgres')
    connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connection.cursor()


    # Select from existing databases to see if database was created previously.

    cursor.execute('SELECT COUNT(*) FROM pg_catalog.pg_database WHERE datname = \'' + dbname + '\'')

    occurrences = cursor.fetchone()[0]

    if occurrences == 0:
        cursor.execute('CREATE DATABASE ' + dbname) 

        connection2 = getOpenConnection(dbname = DB_NAME)

        loadDogTable('dogs', 'dogs_data.txt', connection2) 
        loadShelterTable('shelters', 'shelter_data.txt', connection2)

        cursor2 = connection2.cursor()
        cursor2.execute("CREATE TABLE pet_adoption (adopterID int, employeeID int, date text, contractID int);")

    else:
        print('Database was created previously.')

    connection.commit()
    connection2.commit()
    cursor.close()
    cursor2.close()
    connection.close()

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

    


def main():

    startUpDB(DB_NAME)

    

if __name__ == '__main__':
    main()











































