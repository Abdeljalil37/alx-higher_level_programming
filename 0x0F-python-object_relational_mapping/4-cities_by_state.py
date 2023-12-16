#!/usr/bin/python3
""" Script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    curs = con.cursor()
    curs.execute("""select cities.id, cities.name, s.name from states s, cities
                  where cities.state_id = s.id order by cities.id;""")
    for row in curs.fetchall():
        print(row)
    curs.close()
    con.close()
