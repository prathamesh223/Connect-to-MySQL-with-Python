import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Shiv",
    database = "database_name"
)

print(db)