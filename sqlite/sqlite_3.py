'''
Created on Mar 5, 2017

@author: Hunter
'''
import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot (unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES (1451255552, '2016-01-02', 'Python', 8)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM stuffToPlot')
    #===========================================================================
    # data = c.fetchall() # fetchone for single row
    # print(data)
    #===========================================================================
    for row in c.fetchall():
        print(row)

#create_table()
#data_entry()

#===============================================================================
# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1) # Not used typically, but for sake of adding a second to the timestamp entry in the create_table
#===============================================================================
read_from_db()
c.close()
conn.close()