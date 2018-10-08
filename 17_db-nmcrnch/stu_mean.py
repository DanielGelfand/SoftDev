#Scriptors -- Daniel Gelfand && Bo Lu
#SoftDev1 pd6
#K17 -- AVERAGE
#2018-10-09

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

#CREATING THE TABLE
command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)"
c.execute(command)

#Gives us max id -> for looping
numRows = 0;

#Opening peeps.csv and reading
with open("peeps.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        numRows +=1;
        #print(row['name'], row['age'], row['id'])
        #Adding onto the command to incorporate names, ages, and ids in CSV file using .format()

        command = "INSERT INTO peeps VALUES ( '{}', '{}', '{}')".format(row['name'], row['age'], row['id'])

        c.execute(command)


#CREATING COURSES TABLE
command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)"
c.execute(command)

with open("courses.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row['code'], row['mark'], row['id'])
        #Adding onto the command to incorporate codes, marks, and ids in CSV file
        command = "INSERT INTO courses VALUES ( '{}', '{}', '{}')".format(row['code'], row['mark'], row['id'])
        c.execute(command)

# command = "INSERT INTO peeps VALUES (\' " + alison + "',"+ 16 +","+ 5 +")"
#==========================================================

#comamnd = "CREATE TABLE peeps_avg(id INTEGER, avg INTEGER)"
#c.execute(command)


#Finds average of given id
def getAvg(tempid):
   command = "SELECT mark FROM COURSES WHERE (id = {} )".format(tempid)
   c.execute(command)

   #latest query placed into marks
   marks = c.fetchall()
   counter = 0;
   sum = 0;

   #Loops through marks in database
   for grade in marks:
       #print(grade)
       sum += grade[0]
       counter +=1;
   return (sum/counter)


#print(getAvg(1))
command = "CREATE TABLE peeps_avg(id INTEGER, avg INTEGER)"
c.execute(command)

#Fills table of student averages
def fillTable():

    #[1,maxId]
    for i in range(1,numRows+1):
        '''**************PRINTING INFO***************'''
        print("ID:",i)
        command = "SELECT name FROM peeps WHERE (id = {} )".format(i)
        c.execute(command)
        #Fetch the name
        name = c.fetchone()
        print("Name:",name[0])
        print("AVG:",getAvg(i))
        '''******************************************'''
        command = "INSERT INTO peeps_avg VALUES({},{})".format(i,getAvg(i))
        c.execute(command)


fillTable()
   #command = "INSERT INTRO peeps_avg VALUES(id, avg)"
   #print(numRows)


db.commit() #save changes
db.close()  #close database
