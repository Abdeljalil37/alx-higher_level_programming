#!/usr/bin/python3
""" script that takes in arguments and displays all values in the states table
where name matches the argument. write that is safe from MySQL injections!"""

import sys
import MySQLdb

if __name__ == "__main__":

    con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.close()
