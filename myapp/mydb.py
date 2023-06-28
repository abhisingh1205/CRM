import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root'
)

curserObject = dataBase.cursor()

curserObject.execute("CREATE DATABASE mydb")

print("All done")