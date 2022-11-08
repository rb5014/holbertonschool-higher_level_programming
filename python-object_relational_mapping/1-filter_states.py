#!/usr/bin/python3
"""
1-filter_states - lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

    Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at port 3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
    import MySQLdb
    from sys import argv as a
"""
import MySQLdb
from sys import argv as a


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=a[1],
                         password=a[2], db=a[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states""")

    for row in c.fetchall():
        print(row) if row[1][0] == 'N' else None
