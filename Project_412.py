from subprocess import call
import os
import shutil
import psycopg2
import sys
import loadData as loadHelper #import all load statements

DB_NAME = 'project_412'


def getOpenConnection(user='postgres', password='1234', dbname='Project_412'):

    return psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='localhost' password='" + password + "'")

#################################################################################################################################################


def startUpDB(dbname):

    # Connect to defualt Postgres DB

    connection = getOpenConnection(dbname='postgres')
    connection.set_isolation_level(
        psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connection.cursor()

    # Select from existing databases to see if database was created previously.

    cursor.execute(
        'SELECT COUNT(*) FROM pg_catalog.pg_database WHERE datname = \'' + dbname + '\'')

    occurrences = cursor.fetchone()[0]

    if occurrences == 0:
        cursor.execute('CREATE DATABASE ' + dbname)

        connection2 = getOpenConnection(dbname=DB_NAME)
        ##################################   Load Tables   ##################################
        loadHelper.loadDogTable('dogs', 'dogs_data.txt', connection2)
        loadHelper.loadShelterTable('shelters', 'shelter_data.txt', connection2)
        loadHelper.loadPersonTable('person','person.txt', connection2)
        loadHelper.loadEmployeeTable('employees', 'employee.txt', connection2)
        loadHelper.loadAdopterTable('adopters', 'adopter.txt', connection2) # Needs additional columns, simply create empty table and populate during runtime
        loadHelper.loadPetAdoptionTable('pet_adoption', 'pet_adoptions.txt', connection2)
        loadHelper.loadAppliesForTable('applies_for' , 'applies_for.txt' , connection2)
        #cursor2 = connection2.cursor()
        #cursor2.execute(
        #    "CREATE TABLE pet_adoption (adopterID int, employeeID int, dogID text, date text, contractID int);")

    else:
        print('Database was created previously.')

    connection.commit()
    connection2.commit()
    cursor.close()
    #cursor2.close()
    connection.close()
    connection2.close()

#################################################################################################################################################


def main():

    startUpDB(DB_NAME)

#################################################################################################################################################

connectionSupport = getOpenConnection(dbname=DB_NAME)
cursor = connectionSupport.cursor()

#################################################################################################################################################

def insertPerson(name, ID):
    ID = int(ID)

    cursor.execute("INSERT INTO person VALUES (%s, %s)", (name, ID))

def insertAdopter(name, ID, zip, phone):
    ID = int(ID)
    zip = int(zip)

    cursor.execute("INSERT INTO adopters VALUES (%s, %s, %s, %s)", (name, ID, zip, phone))
    
#################################################################################################################################################

def getDogs(breed, intakeType, sex, maintenanceLevel, temperment, age):
    
    any = '[any]'

    if any == age:
        age = '100'

    if any == breed:
        breed = "LIKE '%'"
    else:
        breed = "= " + "'" + breed + "'"

    if any == intakeType:
        intakeType = "LIKE '%'"
    else:
        intakeType = "= " + "'" + intakeType + "'"

    if any == sex:
        sex = "LIKE '%'"
    else:
        sex = "= " + "'" + sex + "'"

    if any == maintenanceLevel:
        maintenanceLevel = "LIKE '%'"
    else:
        maintenanceLevel = "= " + "'" + maintenanceLevel + "'"

    if any == temperment:
        temperment = "LIKE '%'"
    else:
        temperment = "= " + "'" + temperment + "'"


    cursor.execute("SELECT * FROM dogs WHERE breed "+breed+" AND intakeType "+intakeType+" AND sex "+sex+"AND maintenanceLevel "+maintenanceLevel+" AND temperament "+temperment+" AND age <= "+age+" AND adoptionStatus = 'false';")
    
    results = cursor.fetchall()
    
    return results
    

#################################################################################################################################################


#################################################################################################################################################


#################################################################################################################################################


#################################################################################################################################################

# if __name__ == '__main__':
#     main()
