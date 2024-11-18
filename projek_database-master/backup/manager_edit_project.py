from tkinter import *
from tkcalendar import Calendar
from datetime import date

# To-Do :
# 1. Fix the Edit Project button to edit the project to the database
# 2. Fix the calendar to display the current date and allow the user to select a date
# 3. Turn the file into a function to be called from the main file

def manager_edit_project(root, db, cursor, tree):  
    selected = tree.selection()
    items = tree.item(selected[0], "values")
    popup = Toplevel(root)
    popup.title("Task Display Form")

    # Mengatur jendela menjadi fullscreen
    popup.attributes("-fullscreen", True)
    popup.configure(bg="white")

    # informasi lebar layar
    screen_width = popup.winfo_screenwidth()

    # Label untuk Task Name (hanya teks)
    label_task_name = Label(popup, text="Task Name:", font=("Arial", 14), bg="white")
    label_task_name_value = Entry(popup, text="Example Task Name", font=("Arial", 14), bg="#ECECEC")
    label_task_name.grid(row=0, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
    label_task_name_value.insert(0, items[1])
    label_task_name_value.grid(row=0, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Label untuk Task Description
    label_task_description = Label(popup, text="Task Description:", font=("Arial", 14), bg="white")
    label_task_description.grid(row=1, column=0, sticky="ne", padx=(20, 10), pady=(20, 10))

    # Frame untuk Task Description dan Scrollbar
    frame_description = Frame(popup, bg="#ECECEC")
    frame_description.grid(row=1, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Text widget untuk Task Description dengan Scrollbar
    text_task_description = Text(frame_description, width=int(screen_width*0.0859375), height=18, font=("Arial", 12), bg="#ECECEC")
    text_task_description.insert(1.0, items[2])
    text_task_description.pack(side="left", fill="both", expand=True)

    # Label untuk Due Date (hanya teks)
    label_due_date = Label(popup, text="Due Date:", font=("Arial", 14), bg="white")
    today = date.today()
    label_due_date_value = Entry(popup, font=("Arial", 14), bg="#ECECEC")
    label_due_date_value.insert(0, items[3])
    label_due_date.grid(row=2, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
    label_due_date_value.grid(row=2, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Frame untuk kalender dan exit button
    frame = Frame(popup, bg="white")
    frame.grid(row=3, column=1, pady=5)

    # Kalender menggunakan tkcalendar
    calendar = Calendar(frame, selectmode="day", date_pattern="yyyy-mm-dd")
    calendar.set_date(items[3])  # Set the calendar to the initial value from the selected item
    calendar.grid(row=0, column=0, padx=(10, 20), pady=(20, 20), sticky="w")  # Gunakan sticky="w" untuk rata kiri

    def update_due_date_value(event):
        label_due_date_value.delete(0, END)
        label_due_date_value.insert(0, calendar.get_date())

    calendar.bind("<<CalendarSelected>>", update_due_date_value)

    # Tombol Add Task
    Back_button = Button(frame, text="Edit Project", height=2, width=10, font=('Inter', 14), command=root.destroy)
    Back_button.grid(row=0, column=1, padx=(int(screen_width*0.46875), 20), pady=(20, 20), sticky="se")

