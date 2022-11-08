#!/usr/bin/python3
"""
2-my_filter_states - takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.

    Your script should take 4 arguments: mysql username, mysql password,
    database name and state name searched (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at
    port 3306
    You must use format to create the SQL query with the user input
    Results must be sorted in ascending order by states.id
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
