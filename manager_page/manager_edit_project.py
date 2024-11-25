from tkinter import *
from tkcalendar import Calendar
from datetime import date

# To-Do :
# 1. Fix the Edit Project button to edit the project to the database
# 2. Fix the calendar to display the current date and allow the user to select a date
# 3. Turn the file into a function to be called from the main file
def edit_project(root, db, cursor, project_id, name_label, progress_label, status_label, tree):
    name = name_label.get()
    name_label.delete(0, END)
    cursor.execute(
        f"""
        UPDATE project
        SET projectname = '{name}'
        WHERE projectid = {project_id}
        """
    )
    tree.item(tree.selection()[0], values=(project_id, name, progress_label, status_label))
    db.commit()
    root.destroy()


def manager_edit_project(root, db, cursor, tree):  
    selected = tree.selection()
    items = tree.item(selected[0], "values")
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
    label_task_name_value.insert(0, items[1])
    label_task_name_value.grid(row=0, column=1, sticky="w", padx=(10, 20), pady=(20, 10))



    # Frame untuk kalender dan exit button
    frame = Frame(window, bg="#faebd7")
    frame.grid(row=3, column=1, pady=5)

    # Tombol Add Task
    Back_button = Button(frame,bg='white', text="Edit Project", height=2, width=10, font=('Inter', 14), command=lambda: edit_project(window, db, cursor, items[0], label_task_name_value, items[2], items[3], tree))
    Back_button.grid(row=0, column=1, padx=(int(screen_width*0.46875), 20), pady=(20, 20), sticky="se")


