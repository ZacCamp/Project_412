from subprocess import call
import os
import shutil
import psycopg2
import sys
import random
import loadData as loadHelper  #import all load statements
from datetime import datetime

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

if __name__ == '__main__':
    main()

#################################################################################################################################################

connectionSupport = getOpenConnection(dbname=DB_NAME)
cursor = connectionSupport.cursor()

#################################################################################################################################################

def insertPerson(name, ID):
    ID = int(ID)

    cursor.execute("INSERT INTO person VALUES (%s, %s)", (name, ID))
    connectionSupport.commit()

#################################################################################################################################################


def insertAdopter(name, ID, zip, phone):
    ID = int(ID)
    zip = int(zip)

    cursor.execute("INSERT INTO adopters VALUES (%s, %s, %s, %s)", (name, ID, zip, phone))
    connectionSupport.commit()
    
#################################################################################################################################################


def insertAdoption(adopterID, employeeID, dogID):
    time = datetime.now()
    contractID = getLargestContractID() + 1
    cursor.execute('INSERT INTO pet_adoption VALUES (%s, %s, %s, %s , %s)', (adopterID, employeeID, dogID, time.strftime("%m-%d-%Y"), contractID)) #create new pet adoption
    cursor.execute('UPDATE dogs SET adoptionStatus=true WHERE  dogID=' + str(dogID) + ' ;' ) #update dog adoption status for said dog in dogs table
    connectionSupport.commit()
    print("REGISTERED ADOPTION AND UPDATED DOG ADOPTION STATUS")
    
#################################################################################################################################################

def getDogs(breed, intakeType, sex, maintenanceLevel, temperament, age):
    
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

    if any == temperament:
        temperament = "LIKE '%'"
    else:
        temperament = "= " + "'" + temperament + "'"


    cursor.execute("SELECT * FROM dogs WHERE breed "+breed+" AND intakeType "+intakeType+" AND sex "+sex+"AND maintenanceLevel "+maintenanceLevel+" AND temperament "+temperament+" AND age <= "+age+" AND adoptionStatus = 'false';")
    
    results = cursor.fetchall()
    
    return results
    

#################################################################################################################################################

def getShelters(shelterID):
    cursor.execute("SELECT * FROM shelters WHERE shelterid=" + str(shelterID) + ' ;')
    
    return cursor.fetchall()

#################################################################################################################################################

def getShelterEmployee(shelterID):
    cursor.execute("SELECT * FROM employees WHERE shelterid=" + str(shelterID) + ";")
    allResults = cursor.fetchall()
    return allResults[random.randint(0,len(allResults) -1)] #return random person from results


#################################################################################################################################################

def getLargestPersonID():
    cursor.execute("SELECT MAX(personID) FROM person ;") #get largest personID so we can add 1 and make new unique personID
    max = cursor.fetchone()
    return int(max[0])

#################################################################################################################################################

def getLargestContractID():
    cursor.execute('SELECT MAX(contractID) FROM pet_adoption ;')
    max = cursor.fetchone() #get largest value for contractID currently set
    if max[0] is None:
        return 0
    else:
        return max[0]

#################################################################################################################################################

def getAdopterHistory(personID):
    cursor.execute('SELECT * FROM pet_adoption WHERE adopterID=' + str(personID) + ' ;')
    return cursor.fetchall()

#################################################################################################################################################

def getDogWithID(dogID):
    cursor.execute('SELECT * FROM dogs WHERE dogID=' + str(dogID) + ' ;')
    return cursor.fetchone()

#################################################################################################################################################

def deletePetAdoption(dogID, contractID):
    cursor.execute('DELETE FROM pet_adoption WHERE contractID=' + str(contractID) + ' ;')
    cursor.execute('UPDATE dogs SET adoptionStatus=false WHERE  dogID=' + str(dogID) + ' ;')
    connectionSupport.commit()
    print('Successfully deleted contract and updated dog adoption status')

    

# if __name__ == '__main__':
#     main()
