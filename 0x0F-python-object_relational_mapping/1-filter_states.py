#!/usr/bin/python3
"""lists states with a name starting with N from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])
    cursor = con.cursor()
    cursor.execute("""Select * from states where name Like
                Binary 'N%' order by states.id""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    con.close()
