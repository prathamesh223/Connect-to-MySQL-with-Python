import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="Shiv",
    database="database_name"
)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE office_staff (
    id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    person_name VARCHAR(255),
    phone_number VARCHAR(255)
)
""")
