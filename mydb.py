import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = 'Vk@84178',
)


#prepare a cursor object

curserObject = dataBase.cursor()

#create a database

curserObject.execute("CREATE DATABASE djangopro")
print("All done")