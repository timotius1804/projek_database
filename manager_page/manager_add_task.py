from tkinter import *
from tkcalendar import Calendar
from datetime import date

# To-Do :
# 1. Fix the Add Task button to add the task to the database
# 2. Fix the calendar to display the current date and allow the user to select a date
# 3. Turn the file into a function to be called from the main file

# Membuat jendela utama
def manager_add_task(root, db, cursor, tree):
    window = Toplevel(root)
    window.title("Task Display Form")

    # Mengatur jendela menjadi fullscreen
    window.attributes("-fullscreen", True)
    window.configure(bg="white")

    # informasi lebar layar
    screen_width = window.winfo_screenwidth()

    # Label untuk Task Name (hanya teks)
    label_task_name = Label(window, text="Task Name:", font=("Arial", 14), bg="white")
    label_task_name_value = Entry(window, text="Example Task Name", font=("Arial", 14), bg="#ECECEC")
    label_task_name.grid(row=0, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
    label_task_name_value.grid(row=0, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Label untuk Task Description
    label_task_description = Label(window, text="Task Description:", font=("Arial", 14), bg="white")
    label_task_description.grid(row=1, column=0, sticky="ne", padx=(20, 10), pady=(20, 10))

    # Frame untuk Task Description dan Scrollbar
    frame_description = Frame(window, bg="#ECECEC")
    frame_description.grid(row=1, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Text widget untuk Task Description dengan Scrollbar
    text_task_description = Text(frame_description, width=int(screen_width*0.0859375), height=18, font=("Arial", 12), bg="#ECECEC")
    text_task_description.pack(side="left", fill="both", expand=True)

    # Label untuk Due Date (hanya teks)
    label_due_date = Label(window, text="Due Date:", font=("Arial", 14), bg="white")
    today = date.today()
    label_due_date_value = Entry(window, font=("Arial", 14), bg="#ECECEC")
    label_due_date.grid(row=2, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
    label_due_date_value.grid(row=2, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Frame untuk kalender dan exit button
    frame = Frame(window, bg="white")
    frame.grid(row=3, column=1, pady=5)

    # Kalender menggunakan tkcalendar
    calendar = Calendar(frame, selectmode="day", date_pattern="dd/mm/yyyy")
    calendar.grid(row=0, column=0, padx=(10, 20), pady=(20, 20), sticky="w")  # Gunakan sticky="w" untuk rata kiri

    # Tombol Add Task
    Back_button = Button(frame, text="Add Task", height=2, width=10, font=('Inter', 14))
    Back_button.grid(row=0, column=1, padx=(int(screen_width*0.46875), 20), pady=(20, 20), sticky="se")
