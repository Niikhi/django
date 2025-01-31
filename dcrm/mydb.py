import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Innovitcrota.12",
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS newcommer")

print("Success")