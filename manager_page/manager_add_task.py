from tkinter import *
from tkcalendar import Calendar
from datetime import date
from tkinter import ttk

# To-Do :
# 1. Fix the Add Task button to add the task to the database
# 2. Fix the calendar to display the current date and allow the user to select a date
# 3. Turn the file into a function to be called from the main file


#Mengambil id employee berdasarkan usernamenya
def ambil_employee_id(cursor,employee_name):
    cursor.execute(
        f"""
        select userid from user
        where username = "{employee_name}";

        """
    )
    hasil = cursor.fetchall()

    cursor.execute(
        f"""
        select employeeid from employee
        where userid = "{hasil[0][0]}";
        """
    )

    hasil = cursor.fetchall()
    return hasil[0][0]


def add_task(root, db, cursor, name_label, description_label, employee_name_label, project_id, due_date_label, tree,tree_main):#tree main juga di add kesini:
    employee_name = employee_name_label.get()
    description = description_label.get("1.0", END)
    due_date = due_date_label.get()
    employee_id = ambil_employee_id(cursor,employee_name)
    name = name_label.get()
    name_label.delete(0, END)
    description_label.delete("1.0", END)
    due_date_label.delete(0, END)
    employee_name_label.delete(0, END)
    print(employee_id)
    cursor.execute(
        f"""
        INSERT INTO task (taskname, deskripsi, employeeid, projectid, taskdue)
        VALUES ('{name}', '{description}', {int(employee_id)}, {project_id}, '{due_date}')
        """
    )
    cursor.execute(
        """
        SELECT LAST_INSERT_ID()
        """
    )
    last_id = cursor.fetchall()[0][0]
   
    tree.insert("", "end", values=(last_id, name, due_date, 'Not Done'))    
    cursor.execute(
        f"""
        UPDATE project SET status = 'Not Done' WHERE projectid = {project_id}
        """
    )

    selected_main = tree_main.selection()
    current_values = tree_main.item(selected_main, "values")
    done_tasks, total_tasks = map(int, current_values[2].split("/"))
    tree_main.item(selected_main, values=(current_values[0], current_values[1], f"{done_tasks}/{total_tasks+1}", "Not Done"))
    db.commit()
    root.destroy()
# Membuat jendela utama
def manager_add_task(root, db, cursor, tree, project_id,tree_main):
    window = Toplevel(root)
    window.title("Task Display Form")

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

    # Label untuk Employee Name

    choice_var = StringVar() # Variabel untuk menyimpan pilihan
    cursor.execute(
        """
        SELECT username FROM user WHERE usertype = 'Employee'
        """
    )
    employees = cursor.fetchall()
    options = employees # Daftar pilihan

    label_task_employee = Label(window, text="Employee Name :", font=("Arial", 14), bg="#faebd7")
    label_task_employee_value = ttk.Combobox(window, textvariable=choice_var, values=options)
    label_task_employee.grid(row=1, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
    label_task_employee_value.grid(row=1, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Label untuk Task Description
    label_task_description = Label(window, text="Task Description :", font=("Arial", 14), bg="#faebd7")
    label_task_description.grid(row=2, column=0, sticky="ne", padx=(20, 10), pady=(20, 10))

    # Frame untuk Task Description dan Scrollbar
    frame_description = Frame(window, bg="white")
    frame_description.grid(row=2, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Text widget untuk Task Description dengan Scrollbar
    text_task_description = Text(frame_description, width=int(screen_width*0.0859375), height=15, font=("Arial", 12), bg="white")
    text_task_description.pack(side="left", fill="both", expand=True)

    # Label untuk Due Date (hanya teks)
    label_due_date = Label(window, text="Due Date :", font=("Arial", 14), bg="#faebd7")
    today = date.today()
    label_due_date_value = Entry(window, font=("Arial", 14), bg="white")
    label_due_date.grid(row=3, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
    label_due_date_value.grid(row=3, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Frame untuk kalender dan exit button
    frame = Frame(window, bg="#faebd7")
    frame.grid(row=4, column=1, pady=10)

    # Kalender menggunakan tkcalendar
    calendar = Calendar(frame, selectmode="day", date_pattern="yyyy-mm-dd")
    calendar.grid(row=0, column=0, padx=(10, 20), pady=(20, 20), sticky="w")  # Gunakan sticky="w" untuk rata kiri

    def update_due_date_value(event):
        label_due_date_value.delete(0, END)
        label_due_date_value.insert(0, calendar.get_date())

    calendar.bind("<<CalendarSelected>>", update_due_date_value)
    label_due_date_value.insert(0, calendar.get_date())

    # Tombol Add Task
    Back_button = Button(frame,bg="white", text="Add Task", height=2, width=10, font=('Inter', 14), command=lambda: add_task(window, db, cursor, label_task_name_value, text_task_description, label_task_employee_value, project_id, label_due_date_value, tree,tree_main))
    Back_button.grid(row=0, column=1, padx=(int(screen_width*0.46875), 20), pady=(20, 20), sticky="se")
