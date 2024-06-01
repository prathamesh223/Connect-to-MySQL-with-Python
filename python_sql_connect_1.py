import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Shiv"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE database_name")