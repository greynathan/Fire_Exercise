import sqlite3

#This file is to create a database to be connected with the rest of the 
# flask app

#this creates the database if there is none and connects to it if there is
conn = sqlite3.connect("Coordinate.db")

#this try will create the needed table if there is no table
try:
    conn.execute(
        '''CREATE TABLE COORDINATES
        (LAT TEXT NOT NULL, LONG TEXT NOT NULL);'''
    )

#If there is a table this will catch it and not make a new one  
except:
    print("You already have a db.")