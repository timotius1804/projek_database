import mysql.connector

# Koneksi ke MySQL
connection = mysql.connector.connect(
    host='localhost',        # Sesuaikan dengan host MySQL kamu
    user='root',    # Sesuaikan dengan user MySQL kamu
    password='Yeet_mydatabase2' # Sesuaikan dengan password MySQL kamu
)

cursor = connection.cursor()


cursor.execute("USE companyDB;")

cursor.execute("desc Employees")
rows = cursor.fetchall()
for row in rows:
    print(row)