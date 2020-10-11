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

        connection.commit()

        connection2 = getOpenConnection(dbname = DB_NAME)

        loadDogTable('dogs', 'dogs_data.txt', connection2) 

    else:
        print('Database was created previously.')

    connection.commit()
    cursor.close()
    connection.close()

def loadDogTable(tableName, filePath, openConnection):

    cursor = openConnection.cursor()
    
    # Be sure to add primary and foreign keys later!!!!!!!!!!!!!
    cursor.execute("CREATE TABLE " + tableName + " (intakeType text, sex text, maintenanceLevel text, temperament text, age int, dogID int);") 

    dogFile = open(filePath, "r")

    dataList = dogFile.readlines()
    
    for i in dataList:
        splitList = i.split('::')

        intakeType = splitList[0]
        sex = splitList[1]
        maintenanceLevel = splitList[2]
        temperament = splitList[3]
        age = int(splitList[4])
        dogID = int(splitList[5])

        cursor.execute("INSERT INTO " + tableName + " VALUES (%s, %s, %s , %s , %s , %s)", (intakeType, sex, maintenanceLevel, temperament, age, dogID))

    dogFile.close()

    cursor.close()
    openConnection.commit()


def main():

    startUpDB(DB_NAME)

    

if __name__ == '__main__':
    main()











































