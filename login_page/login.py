from tkinter import *

def login(root: Tk, cursor):
    root.title("")
    # Ukuran jendela
    window_width = 250
    window_height = 150

    # Mendapatkan ukuran layar
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Menghitung posisi x dan y untuk pusat layar
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Mengatur ukuran dan posisi jendela
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Label Welcome
    w = Label(root, text='Welcome')
    w.grid(row=0, column=0, columnspan=2, pady=10)

    # Frame untuk menampung input Name dan Password
    frame = Frame(root)
    frame.grid(row=1, column=0, padx=10, pady=5)

    # Label dan Entry untuk Name
    name_label = Label(frame, text=f"Name {'':<10}:")
    name_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    name_entry = Entry(frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    # Label dan Entry untuk Password
    password_label = Label(frame, text=f"Password  {'':<3}:")
    password_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    password_entry = Entry(frame, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    # Tombol Login
    Login_button = Button(frame, text="Login")
    Login_button.grid(row=2, column=1, sticky="e", pady=10, padx=5)


