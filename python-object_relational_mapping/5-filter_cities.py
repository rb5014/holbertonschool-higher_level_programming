#!/usr/bin/python3
"""
5-filter_cities -  takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa

    Your script should take 4 arguments: mysql username, mysql password,
    database name and state name (SQL injection free!)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at
    port 3306
    Results must be sorted in ascending order by cities.id
    You can use only execute() once
    The results must be displayed as they are in the example below
    Your code should not be executed when imported
"""
import MySQLdb
from sys import argv as a


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=a[1],
                         password=a[2], db=a[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT cities.name FROM cities
              LEFT JOIN states ON cities.state_id = states.id
              WHERE states.name = '{}'""".format(a[4]))
    flag = True
    for row in c.fetchall():
        if flag is False:
            print(", ", end="")
        else:
            flag = False
        print(row[0], end="")
    print()
    c.close()
