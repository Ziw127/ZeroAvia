import psycopg2
from psycopg2 import Error


try:
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "ZeroAvia",
        user = "postgres",
        password = "postgre123",
        port = "5432")

    print("Connected database successfully!")
    cur = conn.cursor()

    # fetch data from table fuelcell
    cur.execute("SELECT id, powerrating, weight, volume, ratedvoltage, heatleakage, consumption,efficiency FROM fuelcell")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print("Select from fuelcell Successfully!")

    # fetch data from table fuelcell
    cur.execute("SELECT * FROM fueltank")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print("Select from fueltank Successfully!")

    conn.commit()
    conn.close()
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if conn:
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")

