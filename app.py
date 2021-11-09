from flask import Flask, render_template, request
import sqlite3

# This line creates the flask app
app = Flask(__name__)

# This line opens a connection to the database
conn = sqlite3.connect("Coordinate.db")

#This is the homepage which is also the map page
#Here I access the database and create lists of latitudes and longitudes
#I then send the lists to the html file to be added to the map
#The map and markers are created using javascript and google maps API
@app.route('/')
def Map():
    with sqlite3.connect("Coordinate.db") as conn:
            cursor = conn.execute("SELECT * from COORDINATES")
            lat= []
            long = []
            for row in cursor:
                lat.append(row[0])
                long.append(row[1])
    return render_template('index.html', lat=lat, long=long, flen = len(lat))

#This function adds new coordinates to the coordinates table
#These coordinates are used to create markers on the map
@app.route('/addCoordinates', methods = ['POST'])
def changeCoordinates():
    lat = request.form['lat']
    long = request.form['long']
    with sqlite3.connect("Coordinate.db") as conn:
        conn.execute("INSERT INTO COORDINATES (LAT, LONG) VALUES (" + "'" + lat + "', '"+long+"')")
    return Map()

#This function opens the coordinates html file
#This file is used to display all the coordinates within the SQL database
@app.route('/Coordinates')
def Coordinates():
    with sqlite3.connect("Coordinate.db") as conn:
            cursor = conn.execute("SELECT * from COORDINATES")
            lat= []
            long = []
            for row in cursor:
                lat.append(row[0])
                long.append(row[1])
    return render_template('coordinates.html', lat=lat, long=long, flen = len(lat))

#This specifies a certain port I would like the app to run on
if __name__ == '__main__':
     app.run(host='0.0.0.0', port ='5150')