from tkinter import *
from tkcalendar import Calendar
from datetime import date

# To-Do :
# 1. Fix the Add Project button to add the project to the database
# 2. Fix the calendar to display the currene and allow the user to select a date
# 3. Turn the file into a function to be called from the main file
def add_project(root, db, cursor, name_label, manager_id, tree):
    name = name_label.get()
    name_label.delete(0, END)
    cursor.execute(
        f"""
        INSERT INTO project (projectname, managerid)
        VALUES ('{name}', '{manager_id}')
        """
    )
    cursor.execute(
        """
        SELECT LAST_INSERT_ID()
        """
    )
    last_id = cursor.fetchall()[0][0]
    tree.insert("", "end", values=(last_id, name, "0/0", 'Not Done'))
    db.commit()
    root.destroy()
    
def manager_add_project(root, db, cursor, tree, manager_id):
    window = Toplevel(root)
    # Mengatur jendela menjadi fullscreen
    window.attributes("-fullscreen", True)
    window.configure(bg="#faebd7")

    # informasi lebar layar
    screen_width = window.winfo_screenwidth()

        # Label untuk Task Name (hanya teks)
    label_task_name = Label(window, text="Project Name :", font=("Arial", 14), bg="#faebd7")
    label_task_name_value = Entry(window, text="Example Project Name", font=("Arial", 14), bg="white")
    label_task_name.grid(row=0, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
    label_task_name_value.grid(row=0, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    frame = Frame(window, bg="#faebd7")
    frame.grid(row=3, column=1, pady=5)

    # Tombol Add Task
    Back_button = Button(frame,bg='white', text="Add Project", height=2, width=10, font=('Inter', 14), command=lambda: add_project(window, db, cursor, label_task_name_value, manager_id, tree))
    Back_button.grid(row=0, column=1, padx=(int(screen_width*0.46875), 20), pady=(20, 20), sticky="se")

