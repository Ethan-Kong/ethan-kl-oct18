# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:33:16 2018

@author: ethan.kong
"""

import sqlite3 as lite
import sys
con = None
try:
    con = lite.connect("data/testdb.db")
    cur = con.cursor()
    #cur.execute('SELECT SQLIE_VERSION()')
    cur.execute('SELECT * from stuff')
    #data = cur.fetchone()
    #print(f'SQLite version; {data}')
    
except lite.Error as e:
    print (f"Error {e.args[0]}")
finally:
    if con:
        con.close()        
    
