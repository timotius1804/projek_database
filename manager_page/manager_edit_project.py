from tkinter import *
from tkcalendar import Calendar
from datetime import date

# Membuat jendela utama
root = Tk()
root.title("Task Display Form")

# Mengatur jendela menjadi fullscreen
root.attributes("-fullscreen", True)
root.configure(bg="white")

# informasi lebar layar
screen_width = root.winfo_screenwidth()

# Label untuk Task Name (hanya teks)
label_task_name = Label(root, text="Task Name:", font=("Arial", 14), bg="white")
label_task_name_value = Entry(root, text="Example Task Name", font=("Arial", 14), bg="#ECECEC")
label_task_name.grid(row=0, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
label_task_name_value.grid(row=0, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

# Label untuk Task Description
label_task_description = Label(root, text="Task Description:", font=("Arial", 14), bg="white")
label_task_description.grid(row=1, column=0, sticky="ne", padx=(20, 10), pady=(20, 10))

# Frame untuk Task Description dan Scrollbar
frame_description = Frame(root, bg="#ECECEC")
frame_description.grid(row=1, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

# Text widget untuk Task Description dengan Scrollbar
text_task_description = Text(frame_description, width=int(screen_width*0.0859375), height=18, font=("Arial", 12), bg="#ECECEC")
text_task_description.pack(side="left", fill="both", expand=True)

# Label untuk Due Date (hanya teks)
label_due_date = Label(root, text="Due Date:", font=("Arial", 14), bg="white")
today = date.today()
label_due_date_value = Entry(root, font=("Arial", 14), bg="#ECECEC")
label_due_date.grid(row=2, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
label_due_date_value.grid(row=2, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

# Frame untuk kalender dan exit button
frame = Frame(root, bg="white")
frame.grid(row=3, column=1, pady=5)

# Kalender menggunakan tkcalendar
calendar = Calendar(frame, selectmode="day", date_pattern="dd/mm/yyyy")
calendar.grid(row=0, column=0, padx=(10, 20), pady=(20, 20), sticky="w")  # Gunakan sticky="w" untuk rata kiri

# Tombol Add Task
Back_button = Button(frame, text="Edit Project", height=2, width=10, font=('Inter', 14), command=root.destroy)
Back_button.grid(row=0, column=1, padx=(int(screen_width*0.46875), 20), pady=(20, 20), sticky="se")

root.mainloop()
