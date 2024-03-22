#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """

import sys
import MySQLdb


if __name__ == '__main__':
     """Function that connects to MySQL server on localhost at port 3306"""

    if len(sys.argv) == 5:
        mydb = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        )
        mycursor = mydb.cursor()
        state_name = sys.argv[4]
        query = 'SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC;'
        mycursor.execute(query, (state_name,))
        rows = mycursor.fetchall()
        for row in rows:
            print(row)
        mydb.close()
