from tkinter import *
from tkcalendar import Calendar
from datetime import date
import os as window

# To-Do :
# 1. Fix the Edit Task button to edit the task to the database
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
    return hasil[0][0]



def edit_task(root, db, cursor, task_id, name_label, description_label, employee_id_label, due_date_label, status, tree,tree_main):#tree main juga di add disini :
    name = name_label.get()
    description = description_label.get("1.0", END)
    due_date = due_date_label.get()
    employee_id = ambil_employee_id(cursor,employee_id_label)
    name_label.delete(0, END)
    description_label.delete("1.0", END)
    due_date_label.delete(0, END)
    employee_id_label.delete(0, END)
    cursor.execute(
        f"""
        UPDATE task
        SET taskname = '{name}', deskripsi = '{description}', taskdue = '{due_date}', employeeid = {employee_id}
        WHERE taskid = {task_id}
        """
    )
    tree.item(tree.selection()[0], values=(task_id, name, due_date, status))
    tree_main.item(tree_main.selection()[0], values=(task_id,name,due_date,status))
    db.commit()
    root.destroy()


# Membuat jendela utama
def manager_edit_task(root, db, cursor, tree, tree_main):
    selected = tree.selection()
    items = tree.item(selected[0], "values")
    task_id = items[0]
    cursor.execute(
        f"""
        SELECT * from task where taskid = {task_id}
        """
    )
    values = cursor.fetchall()[0]
    window = Toplevel(root)
    window.title("Task Display Form")

    # Mengatur jendela menjadi fullscreen
    window.attributes("-fullscreen", True)
    window.configure(bg="#faebd7")

    # informasi lebar layar
    screen_width = window.winfo_screenwidth()

    # Label untuk Task Name (hanya teks)
    label_task_name = Label(window, text="Task Name:", font=("Arial", 14), bg="white")
    label_task_name_value = Entry(window, text="Example Task Name", font=("Arial", 14), bg="#ECECEC")
    label_task_name_value.insert(0, values[1])
    label_task_name.grid(row=0, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
    label_task_name_value.grid(row=0, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    label_task_employee = Label(window, text="Employee Name:", font=("Arial", 14), bg="white")
    label_task_employee_value = Entry(window, text="employee", font=("Arial", 14), bg="#ECECEC")
    
    label_task_employee.grid(row=1, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
    label_task_employee_value.grid(row=1, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Label untuk Task Description
    label_task_description = Label(window, text="Task Description:", font=("Arial", 14), bg="white")
    label_task_description.grid(row=2, column=0, sticky="ne", padx=(20, 10), pady=(20, 10))

    # Frame untuk Task Description dan Scrollbar
    frame_description = Frame(window, bg="#ECECEC")
    frame_description.grid(row=2, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Text widget untuk Task Description dengan Scrollbar
    text_task_description = Text(frame_description, width=int(screen_width*0.0859375), height=18, font=("Arial", 12), bg="#ECECEC")
    text_task_description.insert(1.0, values[2])
    text_task_description.pack(side="left", fill="both", expand=True)

    # Label untuk Due Date (hanya teks)
    label_due_date = Label(window, text="Due Date:", font=("Arial", 14), bg="white")
    today = date.today()
    label_due_date_value = Entry(window, font=("Arial", 14), bg="#ECECEC")
    label_due_date_value.insert(0, values[5])
    label_due_date.grid(row=3, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
    label_due_date_value.grid(row=3, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Frame untuk kalender dan exit button
    frame = Frame(window, bg="white")
    frame.grid(row=3, column=1, pady=5)

    # Kalender menggunakan tkcalendar
    calendar = Calendar(frame, selectmode="day", date_pattern="yyyy-mm-dd")
    calendar.selection_set(values[5])  # Set the calendar to the initial value from the selected item
    calendar.grid(row=0, column=5, padx=(10, 20), pady=(20, 20), sticky="w")  # Gunakan sticky="w" untuk rata kiri

    def update_due_date_value(event):
        label_due_date_value.delete(0, END)
        label_due_date_value.insert(0, calendar.get_date())
    calendar.bind("<<CalendarSelected>>", update_due_date_value)
    # Tombol Add Task
    Back_button = Button(frame,bg="white", text="Edit Task", height=2, width=10, font=('Inter', 14), command=lambda: edit_task(window, db, cursor, task_id, label_task_name_value, text_task_description, label_task_employee_value, label_due_date_value, values[6], tree,tree_main))
    Back_button.grid(row=0, column=1, padx=(int(screen_width*0.46875), 20), pady=(20, 20), sticky="se")


