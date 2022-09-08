'''
The Script creates a database table having three fields,
and populates the table
'''
import sqlite3

# Here we try to execute the SQL commands
try:
    # connect to database
    db = sqlite3.connect('mydb.db')
    # delete table if it exists
    db.execute('Drop table if exists computers')
    # create table
    db.execute('Insert into computers (Brand, Disk, Screen) values\
               ("Beta",1204,18)')
    db.execute('Insert into computers (Brand, Disk, Screen) values\
               ("Cosmos",512,22)')
    db.execute('Insert into computers (Brand, Disk, Screen) values\
               ("Europa",512,19)')

    # save changes
    db.commit()
except sqlite3.OperationalError:
    # print the message if an SQL error occurs
    print('You\'ve something wrong in the SQL declaration')
