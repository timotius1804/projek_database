from login_page import login
import db_init
from tkinter import *
import mysql.connector 

if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "inipassword"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'companyDB'")
    result = mycursor.fetchall()
    if result:
        db_exists = True
    else:
        db_exists = False

    if not db_exists:
        db_init.db_init(mycursor)
    else:
        mycursor.execute("USE companyDB")

    root = Tk()
    login.login(root, mycursor)

    root.mainloop()