from tkinter import *

# To-Do :
# 1. Add functionality to the Edit User button and connect it to the database
def edit_user(db, cursor, name, password, user_type, tree):
    cursor.execute(
        f"""
        UPDATE user
        SET user_password = '{password}', user_type = '{user_type}'
        WHERE user_name = '{name}'
        """
    )
    selected = tree.selection()
    items = tree.item(selected[0], "values")
    tree.item(selected[0], values=(items[0], name, password, user_type))
    db.commit()

def open_popup(root, db, cursor, tree):
    selected = tree.selection()
    items = tree.item(selected[0], "values")

    popup = Toplevel(root)
    popup.title("")
    # Ukuran jendela
    window_width = 250
    window_height = 150

    # Mendapatkan ukuran layar
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()

    # Menghitung posisi x dan y untuk pusat layar
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Mengatur ukuran dan posisi jendela
    popup.geometry(f"{window_width}x{window_height}+{x}+{y}")


    # Frame untuk menampung input Name dan Password
    frame = Frame(popup)
    frame.grid(row=0, column=0, padx=10, pady=5)

    # Label dan Entry untuk Name
    name_label = Label(frame, text=f"Name {'':<10}:")
    name_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    name_entry = Entry(frame)
    name_entry.insert(0, items[1])
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    # Label dan Entry untuk Password
    password_label = Label(frame, text=f"Password  {'':<3}:")
    password_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    password_entry = Entry(frame, show="*")
    password_entry.insert(0, items[2])
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    # Label dan Entry untuk user_type
    user_type_label = Label(frame, text=f"User Type  {'':<3}:")
    user_type_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    user_type_entry = Entry(frame, show="*")
    user_type_entry.insert(0, items[3])
    user_type_entry.grid(row=2, column=1, padx=5, pady=5)

    # Tombol Edit_user
    Edit_user_button = Button(frame, text="Edit User", command=lambda: edit_user(db, cursor, name_entry.get(), password_entry.get(), user_type_entry.get(), tree))
    Edit_user_button.grid(row=3, column=1, sticky="e", pady=10, padx=5)

