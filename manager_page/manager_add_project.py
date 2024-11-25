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
    label_task_name = Label(window, text="Task Name :", font=("Arial", 14), bg="#faebd7")
    label_task_name_value = Entry(window, text="Example Task Name", font=("Arial", 14), bg="white")
    label_task_name.grid(row=0, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
    label_task_name_value.grid(row=0, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Label untuk Task Description
    label_task_description = Label(window, text="Task Description :", font=("Arial", 14), bg="#faebd7")
    label_task_description.grid(row=1, column=0, sticky="ne", padx=(20, 10), pady=(20, 10))

    # Frame untuk Task Description dan Scrollbar
    frame_description = Frame(window, bg="white")
    frame_description.grid(row=1, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Text widget untuk Task Description dengan Scrollbar
    text_task_description = Text(frame_description, width=int(screen_width*0.0859375), height=18, font=("Arial", 12), bg="white")
    text_task_description.pack(side="left", fill="both", expand=True)

    # Label untuk Due Date (hanya teks)
    label_due_date = Label(window, text="Due Date :", font=("Arial", 14), bg="#faebd7")
    today = date.today()
    label_due_date_value = Entry(window, font=("Arial", 14), bg="white")
    label_due_date.grid(row=2, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
    label_due_date_value.grid(row=2, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    frame = Frame(window, bg="#faebd7")
    frame.grid(row=3, column=1, pady=5)

    # Kalender menggunakan tkcalendar
    calendar = Calendar(frame, selectmode="day", date_pattern="dd/mm/yyyy")
    calendar.grid(row=0, column=0, padx=(10, 20), pady=(20, 20), sticky="w")  # Gunakan sticky="w" untuk rata kiri

    # Tombol Add Task
    Back_button = Button(frame,bg='white', text="Edit Project", height=2, width=10, font=('Inter', 14), command=lambda: add_project(window, db, cursor, label_task_name_value, manager_id, tree))
    Back_button.grid(row=0, column=1, padx=(int(screen_width*0.46875), 20), pady=(20, 20), sticky="se")

