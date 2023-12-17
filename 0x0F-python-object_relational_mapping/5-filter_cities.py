#!/usr/bin/python3
""" script that takes in the name of a state as an argument and lists
 all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    curs = con.cursor()
    curs.execute("""Select c.name from states s, cities c where
                  c.state_id = s.id and s.name=%s""", (sys.argv[4],))
    rows = curs.fetchall()
    list = tuple(row[0] for row in rows)
    print(", ".join(list))
    curs.close()
    con.close()
