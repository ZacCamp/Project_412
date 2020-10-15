import random
import sys
import time 
import os

Names = ["Beitris Pereira",
"Hillary Davidi",
"Reinald O'Luney",
"Dacia Billanie",
"Benson Moatt",
"Samantha Briton",
"Waldon Klemencic",
"Reinhold Rabjohns",
"Chantalle Stickel",
"Darcy Tredger",
"Joel Lowbridge",
"Alyssa Barkus",
"Tommie Shiel",
"Ellen Baglan",
"Benedict Gounot",
"Hana Schechter",
"Venita Kwietek",
"Ikey Simkovich",
"Margit Abbett",
"Berny Cullerne",
"Feodora Kee",
"Symon Le Pine",
"Clayborn Ternault",
"Giraud Tweddell",
"Pooh Tooke",
"Regen Acton",
"Milly Miko",
"Lennie Klimaszewski",
"Pete Finlater",
"Kamilah Lingwood",
"Raddie Stokey",
"Regine Arrowsmith",
"Leonora Proudley",
"Nollie Lembke",
"Lay Kierans",
"Linette Waylen",
"Stella Chrstine",
"Alexander Finicj",
"Katrina Blindermann",
"Ax Andrysek",
"Hill Simyson",
"Kimberlyn Pods",
"Ivy Pattullo",
"Warde Storch",
"Julissa Martyns",
"Falito O'Scully",
"Galven Watkin",
"Cordie Huson",
"Onofredo Guittet",
"Barbee Brunger"]

def main():

    dataAsList = []
    namesList =[]
    for ID in range(50):
        dataAsList.append(Names[ID]+"::")
        dataAsList.append(str(ID) + "::\n") # sequential id

    File = open("person.txt", "w")

    for line in dataAsList:
        File.write(line)

if __name__ == '__main__':
    main()

