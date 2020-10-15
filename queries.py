import argparse
import psycopg2

#################################################################################################################################################
def readInputs():
    parser = argparse.ArgumentParser(description='run some SQL queries on the dataset')
    # options for selecting a Dog
    parser.add_argument('adopt', nargs='?')
    parser.add_argument('--breed' , '-b', help='which breed?')
    parser.add_argument('--temperament', '-t', help='temperament level? [low , medium, high]')
    parser.add_argument('--maintenance', '-m', help='maintenance level ? [assertive, neutral , passive]' )
    parser.add_argument('--age', '-a', help='age of the dog')
    parser.add_argument('--adopted-status', '-as', help='adopted status of the dog')
    parser.add_argument('--intake-type', '-i', help='intake type [stray, surrendered]')
    parser.add_argument('--gender', '-g', help='gender of the dog')

    args = parser.parse_args()
#################################################################################################################################################

def connectToDB():
    #Connect to an existing database
    conn = psycopg2.connect(dbname="project_412", user="postgres", password="1234")

# Open a cursor to perform database operations
    cur = conn.cursor()

# Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM dogs ;")
    try:
        occurrences = cur.fetchall()
        print(occurrences)
    except:
        print('Error occurred')

# Make the changes to the database persistent
    conn.commit()

# Close communication with the database
    cur.close()
#################################################################################################################################################

def main():
    readInputs()
    connectToDB()

#################################################################################################################################################
if __name__ == '__main__':
    main()