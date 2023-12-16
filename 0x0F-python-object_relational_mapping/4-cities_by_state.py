#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    curs = con.cursor()
    curs.execute("""select c.id, c.name, s.name from states s, cities c where
                 c.state_id = s.id order by c.id;""")
    for row in curs.fetchall():
        print(row)
    curs.close()
    con.close()
