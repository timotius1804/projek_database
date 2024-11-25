from tkinter import *
from tkinter import messagebox
from admin_page import admin_main
from manager_page import manager_main
from employee_page import employee_main
from PIL import Image, ImageTk

def button_konfirmasi(db, root, cursor, frame, name_entry, password_entry):
    user_name = name_entry.get().strip()
    user_password = password_entry.get().strip()

    if not user_name or not user_password:
        messagebox.showerror("Error", "Username and Password cannot be empty")
        return

    cursor.execute("SELECT * FROM user WHERE username = %s", (user_name,))
    data = cursor.fetchall()

    if data:
        data_password = data[0][2]
        data_type = data[0][3]
        user_id = data[0][0]

        if data_password == user_password:
            for widget in root.winfo_children():
                widget.destroy()
            if data_type == 'Admin':
                admin_main.admin(db, root, cursor, user_name, user_id)
            elif data_type == 'Manager':
                manager_main.manager(db, root, cursor, user_name, user_id)
            else:
                employee_main.employee(db, root, cursor, user_name, user_id)
        else:
            messagebox.showerror("Error", "Wrong Password")
    else:
        messagebox.showerror("Error", "Username not found")


def login(db, root: Tk, cursor):
    try:
        background_image = Image.open("background.jpg")
        background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
        background_photo = ImageTk.PhotoImage(background_image)
        root.background_photo = background_photo
    except FileNotFoundError:
        messagebox.showerror("Error", "Background image not found")
        root.destroy()
        return

    try:
        logo_image = Image.open("Logo_2.png")
        logo_width, logo_height = logo_image.size
        aspect_ratio = logo_width / logo_height
        new_width = 280
        new_height = int(new_width / aspect_ratio)
        logo_image = logo_image.resize((new_width, new_height), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_image)
        root.logo_photo = logo_photo
    except FileNotFoundError:
        messagebox.showerror("Error", "Logo image not found")
        root.destroy()
        return

    frame_background = Frame(root)
    frame_background.pack(fill="both", expand=True)

    canvas = Canvas(frame_background, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    login_frame = Frame(frame_background, bg="#f7e3c6", padx=20, pady=20)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")

    logo_label = Label(login_frame, image=logo_photo, bg="#f7e3c6")
    logo_label.grid(row=0, column=0, columnspan=2, pady=10)

    label_username = Label(login_frame, text="Username : ", font=("Arial", 14), bg="#f7e3c6")
    label_username.grid(row=1, column=0, pady=5)
    name_entry = Entry(login_frame, font=("Arial", 14))
    name_entry.grid(row=1, column=1, pady=5)

    label_password = Label(login_frame, text="Password : ", font=("Arial", 14), bg="#f7e3c6")
    label_password.grid(row=2, column=0, pady=5)
    password_entry = Entry(login_frame, font=("Arial", 14), show="*")
    password_entry.grid(row=2, column=1, pady=5)

    Login_button = Button(login_frame, text="Login", command=lambda: button_konfirmasi(db, root, cursor, login_frame, name_entry, password_entry))
    Login_button.grid(row=3, column=0, columnspan=2, pady=10)
