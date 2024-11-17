from tkinter import *
from tkcalendar import Calendar
from datetime import date

def back():
    task_window.destroy()

# Membuat jendela utama
def task_display(root: Tk, cursor, data, name, user_id):
    global task_window
    task_window = Toplevel(root)
    task_window.attributes("-fullscreen", True)
    task_window.title("Task Display Form")
    task_window.configure(bg="white")

    # informasi lebar layar
    screen_width = task_window.winfo_screenwidth()

    # Label untuk Task Name (hanya teks)
    label_task_name = Label(task_window, text="Task Name:", font=("Arial", 14), bg="white")
    label_task_name_value = Label(task_window, text=f"{data}", font=("Arial", 14), bg="#ECECEC")
    label_task_name.grid(row=0, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
    label_task_name_value.grid(row=0, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Label untuk Task Description
    label_task_description = Label(task_window, text="Task Description:", font=("Arial", 14), bg="white")
    label_task_description.grid(row=1, column=0, sticky="ne", padx=(20, 10), pady=(20, 10))

    # Frame untuk Task Description dan Scrollbar
    frame_description = Frame(task_window, bg="#ECECEC")
    frame_description.grid(row=1, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # Text widget untuk Task Description dengan Scrollbar
    text_task_description = Text(frame_description, width=int(screen_width*0.0859375), height=18, wrap="word", font=("Arial", 12), state="normal", bg="#ECECEC")
    scrollbar = Scrollbar(frame_description, orient="vertical", command=text_task_description.yview)
    text_task_description.configure(yscrollcommand=scrollbar.set)

    # Masukkan teks deskripsi ke dalam Text widget
    task_description_text = data  # Ambil deskripsi dari data
    text_task_description.insert("1.0", task_description_text)

    # Atur agar teks tidak bisa diedit oleh pengguna
    text_task_description.config(state="disabled")

    # Menempatkan Text widget dan Scrollbar
    text_task_description.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Label untuk Due Date (hanya teks)
    label_due_date = Label(task_window, text="Due Date:", font=("Arial", 14), bg="white")
    today = date.today()
    due_date_text = today.strftime("%d/%m/%Y") + " (5 days)"  # Contoh tanggal dan sisa hari
    label_due_date_value = Label(task_window, text=due_date_text, font=("Arial", 14), bg="#ECECEC")
    label_due_date.grid(row=2, column=0, sticky="e", padx=(20, 10), pady=(20, 10))
    label_due_date_value.grid(row=2, column=1, sticky="w", padx=(10, 20), pady=(20, 10))

    # frame untuk calender dan exit button
    frame = Frame(task_window,bg="white")
    frame.grid(row=3, column=1, pady=5)

    # Kalender menggunakan tkcalendar
    calendar = Calendar(frame, selectmode="day", date_pattern="dd/mm/yyyy")
    calendar.grid(row=0, column=0, padx=(10, 0), pady=(20, 20), sticky="w")

    # Tombol Back
    Back_button = Button(frame, text="Back",  height=2,width=10, font=('Inter', 14),command=back)
    Back_button.grid(row=0, column=1, padx=int(screen_width*0.49), pady=(20, 20), sticky="se")


