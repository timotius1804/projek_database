from tkinter import *
from tkcalendar import Calendar
from datetime import date

# To-Do :
# 1. Fix the Edit Project button to edit the project to the database
# 2. Fix the calendar to display the current date and allow the user to select a date
# 3. Turn the file into a function to be called from the main file
def edit_project(root, db, cursor, project_id, name_label, tree):
    name = name_label.get()
    name_label.delete(0, END)
    cursor.execute(
        f"""
        UPDATE project
        SET projectname = '{name}'
        WHERE projectid = {project_id}
        """
    )
    tree.item(tree.selection()[0], values=(project_id, name))
    db.commit()
    root.destroy()


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

    # Frame untuk kalender dan exit button
    frame = Frame(popup, bg="white")
    frame.grid(row=3, column=1, pady=5)

    # Tombol Add Task
    Back_button = Button(frame, text="Edit Project", height=2, width=10, font=('Inter', 14), command=lambda: edit_project(popup, db, cursor, items[0], label_task_name_value, tree))
    Back_button.grid(row=0, column=1, padx=(int(screen_width*0.46875), 20), pady=(20, 20), sticky="se")

