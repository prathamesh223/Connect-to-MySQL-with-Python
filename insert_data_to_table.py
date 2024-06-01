
import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Shiv",
    database = "database_name"
)

cursor = db.cursor()

query = "INSERT INTO office_staff (id, person_name, phone_number) VALUES (%s, %s, %s)"

values = (1 ,"ABC", 123)

cursor.execute(query, values)

db.commit()