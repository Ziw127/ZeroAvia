import psycopg2
from psycopg2 import Error


try:
    # This API opens a connection to the PostgreSQLdb, if db is opened successfully,
    # it returns a connection object.
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "ZeroAvia",
        user = "postgres",
        password = "postgre123",
        port = "5432")

    print("Connected database successfully!")
    # This routine creates a cursor which will be used throughout of your db programming with Python
    cur = conn.cursor()

    # execute an SQL statement
    # fetch data from table fuelcell
    cur.execute("SELECT id, powerrating, weight, volume, ratedvoltage, heatleakage, consumption,efficiency FROM fuelcell")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    print("Select from fuelcell Successfully!")

    # fetch data from table fuelcell
    # cur.execute("SELECT * FROM fueltank")
    # rows = cur.fetchall()
    # for row in rows:
    #     print(row)
    # print("Select from fueltank Successfully!")

    # commit the current transaction if you do not call this,
    # anything you did since the last call to commit() is not visible from 
    # other db connection
    conn.commit()
    conn.close() # close the database connection
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if conn:
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")

