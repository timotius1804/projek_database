from login_page import login
import db_init
from tkinter import *
import mysql.connector 

if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "boimau17"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'companyDB'")
    result = mycursor.fetchone()
    if result:
        db_exists = True
    else:
        db_exists = False

    if not db_exists:
        print("Database not found, creating new database")
        db_init.db_init(mycursor, mydb)
    else:
        print("Database already exists")
        mycursor.execute("USE companyDB")

    root = Tk()
    login.login(mydb, root, mycursor)

    root.attributes("-fullscreen", True)
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))


    root.mainloop()