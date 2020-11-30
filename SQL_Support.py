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
connectionSupport = None
cursor3 = None

def initConnection():
    try:
        global connectionSupport 
        connectionSupport = getOpenConnection(dbname=DB_NAME)
        global cursor3 
        cursor3 = connectionSupport.cursor()
    except Exception:
        print("Error: Database not created yet.")
        # main()


#################################################################################################################################################

def insertPerson(name, ID):
    ID = int(ID)

    cursor3.execute("INSERT INTO person VALUES (%s, %s)", (name, ID))
    connectionSupport.commit()

#################################################################################################################################################


def insertAdopter(name, ID, zip, phone):
    ID = int(ID)
    zip = int(zip)

    cursor3.execute("INSERT INTO adopters VALUES (%s, %s, %s, %s)", (name, ID, zip, phone))
    connectionSupport.commit()
    
#################################################################################################################################################


def insertAdoption(adopterID, employeeID, dogID):
    time = datetime.now()
    contractID = getLargestContractID() + 1
    cursor3.execute('INSERT INTO pet_adoption VALUES (%s, %s, %s, %s , %s)', (adopterID, employeeID, dogID, time.strftime("%m-%d-%Y"), contractID)) #create new pet adoption
    cursor3.execute('UPDATE dogs SET adoptionStatus=true WHERE  dogID=' + str(dogID) + ' ;' ) #update dog adoption status for said dog in dogs table
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


    cursor3.execute("SELECT * FROM dogs WHERE breed "+breed+" AND intakeType "+intakeType+" AND sex "+sex+"AND maintenanceLevel "+maintenanceLevel+" AND temperament "+temperament+" AND age <= "+age+" AND adoptionStatus = 'false';")
    
    results = cursor3.fetchall()
    
    return results
    

#################################################################################################################################################

def getShelters(shelterID):
    cursor3.execute("SELECT * FROM shelters WHERE shelterid=" + str(shelterID) + ' ;')
    
    return cursor3.fetchall()

#################################################################################################################################################

def getShelterEmployee(shelterID):
    cursor3.execute("SELECT * FROM employees WHERE shelterid=" + str(shelterID) + ";")
    allResults = cursor3.fetchall()
    return allResults[random.randint(0,len(allResults) -1)] #return random person from results


#################################################################################################################################################

def getLargestPersonID():
    cursor3.execute("SELECT MAX(personID) FROM person ;") #get largest personID so we can add 1 and make new unique personID
    max = cursor3.fetchone()
    return int(max[0])

#################################################################################################################################################

def getLargestContractID():
    cursor3.execute('SELECT MAX(contractID) FROM pet_adoption ;')
    max = cursor3.fetchone() #get largest value for contractID currently set
    if max[0] is None:
        return 0
    else:
        return max[0]

#################################################################################################################################################

def getAdopterHistory(personID):
    cursor3.execute('SELECT * FROM pet_adoption WHERE adopterID=' + str(personID) + ' ;')
    return cursor3.fetchall()

#################################################################################################################################################

def getDogWithID(dogID):
    cursor3.execute('SELECT * FROM dogs WHERE dogID=' + str(dogID) + ' ;')
    return cursor3.fetchone()

#################################################################################################################################################

def deletePetAdoption(dogID, contractID):
    cursor3.execute('DELETE FROM pet_adoption WHERE contractID=' + str(contractID) + ' ;')
    cursor3.execute('UPDATE dogs SET adoptionStatus=false WHERE  dogID=' + str(dogID) + ' ;')
    connectionSupport.commit()
    print('Successfully deleted contract and updated dog adoption status')