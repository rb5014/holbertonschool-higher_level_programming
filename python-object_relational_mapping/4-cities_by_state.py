#!/usr/bin/python3
"""
4-cities_by_state -  lists all cities from the database hbtn_0e_4_usa

    Your script should take 3 arguments: mysql username, mysql password and
    database name
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at
    port 3306
    Results must be sorted in ascending order by cities.id
    You can use only execute() once
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
"""
import MySQLdb
from sys import argv as a


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=a[1],
                         password=a[2], db=a[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states""")

    for row in c.fetchall():
        print(row) if row[1] == a[4] else None
    c.close()
