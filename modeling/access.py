############ NOTE: THIS CODE DOES NOT WORK RIGHT NOW BECAUSE WE CANNOT REMOTELY CONNECT TO THE DATABASE
############ this should be our 'data pipeline' script. 
from mission_profile_class.py import *
from model_classes.py import *
import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user='postgre',
                                  password='postgre123',
                                  host='localhost',
                                  port=5432,
                                  database=)

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


cursor = connection.cursor()

#fetching the rows of the postgre tables
cursor.execute('''SELECT * from FuelTank''')
ft_result = cursor.fetchone()

cursor.execute('''SELECT * from FuelCell''')
fc_result = cursor.fetchone()

cursor.execute('''SELECT * from PDU''')
pdu_result = cursor.fetchone()

cursor.execute('''SELECT * from Inverter''')
inverter_result = cursor.fetchone()

cursor.execute('''SELECT * from Motor''')
motor_result = cursor.fetchone()

cursor.execute('''SELECT * from MissionProfile''')
mp_result = cursor.fetchone() #possibly fetchall call, depending on datastruct

######################## assign values to objects

######################## do calculations/make graphs/etc

######################## send calculations to postgre tables
sql = """INSERT INTO outputs(output_name)
             VALUES(%f) RETURNING output_id;"""


# for example
sql = """INSERT INTO outputs(energy_required)
             VALUES(%f) RETURNING output_id;"""


######################## commit changes
connection.commit()
cursor.close()
connection.close()