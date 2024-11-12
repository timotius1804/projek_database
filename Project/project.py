import mysql.connector

# Koneksi ke MySQL
connection = mysql.connector.connect(
    host='localhost',        # Sesuaikan dengan host MySQL kamu
    user='root',    # Sesuaikan dengan user MySQL kamu
    password='inipassword' # Sesuaikan dengan password MySQL kamu
)

cursor = connection.cursor()

cursor.execute("USE companyDB")
cursor.execute(
    """
INSERT INTO employee (userid) VALUES
(7)
"""
)
cursor.execute("""
    INSERT INTO task (taskname, deskripsi, employeeid, projectid, taskdue, status) VALUES 
    ('Task 1', 'Description for Task 1', 2, 1, '2023-10-01', 'Not Done'),
    ('Task 2', 'Description for Task 2', 2, 1, '2023-10-02', 'Done'),
    ('Task 3', 'Description for Task 3', 2, 1, '2023-10-03', 'Not Done'),
    ('Task 4', 'Description for Task 4', 2, 1, '2023-10-04', 'Done'),
    ('Task 5', 'Description for Task 5', 2, 1, '2023-10-05', 'Not Done')
    """)


connection.commit()