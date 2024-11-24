from tkinter import *
from tkinter import ttk
from employee_page.employee_task import task_display

def task(root, cursor, tree, name, user_id):
    selected = tree.selection()
    selected_item = tree.item(selected[0], "values")
    cursor.execute(
f"""
SELECT taskname, deskripsi, taskdue, status FROM task WHERE taskid = '{selected_item[0]}'
"""
    )
    data = cursor.fetchall()
    task_display(root, cursor, data, name, user_id)


def mark_done_button(db, tree, cursor):
    selected = tree.selection()
    selected_item = tree.item(selected[0], "values")

    new_values = (*selected_item[:-1] , "Done" if selected_item[-1] == "Not Done" else "Not Done")
    tree.item(selected[0], values=new_values)
    cursor.execute(
f"""
UPDATE task SET status = '{new_values[-1]}' WHERE taskid = '{selected_item[0]}'
"""
    )
    db.commit()

def close_window(root):
    root.destroy()

# Membuat window utama
def employee(db, root, cursor, name, user_id):
    root.configure(bg="#faebd7")
    root.attributes("-fullscreen", True)
    root.title("Employee Task Table")

    # Mendapatkan ukuran layar
    screen_width = root.winfo_screenwidth()

    # Label Selamat Datang
    status = "Employee"
    global welcome_label
    welcome_label = Label(root,bg="#faebd7", text=f"Welcome, {name} ({status})")
    welcome_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    # Mengatur frame agar menempati sekitar 70% dari window
    global frame
    frame = Frame(root, borderwidth=1, relief="solid", bg="#faebd7")  # Border untuk visualisasi
    frame.grid(row=1, column=0, padx=30, pady=20, sticky="nsew")  # Mengatur padding

    # Membuat style khusus untuk Treeview
    style = ttk.Style()
    style.configure("Custom.Treeview", 
                    background="#ECECEC",         # Warna background sel data
                    fieldbackground="#ECECEC",    # Warna background kolom data
                    foreground="black",           # Warna teks
                    rowheight=25)                 # Tinggi setiap baris

    # Mengatur warna baris yang dipilih
    style.map("Custom.Treeview", 
            background=[("selected", "#4CAF50")],  # Warna latar belakang saat baris dipilih
            foreground=[("selected", "white")])    # Warna teks saat baris dipilih

    # Membuat Treeview dengan style yang baru
    columns = ("ID", "Task Name", "Due Date", "Status")
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=22, selectmode='browse', style="Custom.Treeview")
    tree.grid(row=0, column=0, sticky="nsew", padx=(0, 10))  # Menggunakan grid untuk menempatkan tree

    # Menetapkan nama kolom dan mengatur lebar kolom
    tree.heading("ID", text="ID")
    tree.heading("Task Name", text="Task Name")
    tree.heading("Due Date", text="Due Date")
    tree.heading("Status", text="Status")

    tree.column("ID", anchor="center", width=int(screen_width - screen_width * 0.9609375))
    tree.column("Task Name", anchor="w", width=int(screen_width - screen_width * 0.6875))
    tree.column("Due Date", anchor="w", width=int(screen_width - screen_width * 0.921875))
    tree.column("Status", anchor="center", width=int(screen_width - screen_width * 0.921875))


    # Menambahkan scrollbar vertikal dengan warna khusus
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")  # Menggunakan grid untuk scrollbar
    scrollbar_style = ttk.Style()
    scrollbar_style.configure("Vertical.TScrollbar", background="#ECECEC", troughcolor="#ECECEC")  # Warna scrollbar
    tree.configure(yscrollcommand=scrollbar.set)

    # Menambahkan beberapa data contoh ke dalam tabel
    cursor.execute(f"""
SELECT employeeid from employee where userid = {user_id}
""")
    employee_id = cursor.fetchall()[0][0]
    cursor.execute(
f"""
SELECT taskid, taskname, taskdue, status FROM task WHERE employeeid = {employee_id}
"""
    )
    data = cursor.fetchall()
    if data:
        for row in data:
            tree.insert("", "end", values=row)
            if row[3] == "Done": 
                tree.tag_configure("done", background="lightgreen") 
                tree.item(tree.get_children()[-1], tags="done") 
            elif row[3] == "Not Done": 
                tree.tag_configure("not_done", background="lightcoral") 
                tree.item(tree.get_children()[-1], tags="not_done")
    else:
        tree.insert("", "end", values=["", "No Task", "",])

    # Menambahkan frame dan tombol di sebelah kanan
    global frame_two
    frame_two = Frame(root, borderwidth=0, relief="solid", bg="#faebd7")  # Border untuk visualisasi
    frame_two.grid(row=1, column=1, padx=0, pady=20, sticky="nsew")

    # Mengatur tombol "View details"
    View_details_button = Button(frame_two,bg="white", text="View details", width=int(screen_width - screen_width * 0.96484375),  height=2, font=('Inter', 14), command=lambda: task(root, cursor, tree, name, user_id))
    View_details_button.grid(row=0, column=0, sticky="e", pady=10, padx=5)

    # Mengatur tombol "Mark as Done / Not Done"
    Mark_button = Button(frame_two,bg="white", text="Mark as Done /\nNot Done", width=int(screen_width - screen_width * 0.96484375),  height=2, font=('Inter', 14), command=lambda: mark_done_button(db, tree, cursor))
    Mark_button.grid(row=1, column=0, sticky="e", pady=10, padx=5)

    # Menambahkan baris kosong sebelum tombol Logout
    frame_two.grid_rowconfigure(2, weight=1)  # Membiarkan baris 2 mengambil sisa ruang

    # Mengatur tombol "Logout" di pojok kanan bawah
    Logout_button = Button(frame_two,bg="white", text="Logout", width=int(screen_width - screen_width * 0.99453125), height=1, font=('Inter'), command=lambda: close_window(root)) 
    Logout_button.grid(row=3, column=0, sticky="se", pady=10, padx=5)  # Pindahkan ke baris 3

    # Mengatur agar frame dua dan treeview bisa menyesuaikan ukuran
    frame.grid_rowconfigure(0, weight=1)  # Membuat Treeview untuk mengambil sisa ruang
    frame.grid_columnconfigure(0, weight=1)  # Membuat kolom treeview untuk mengambil sisa ruang

    # Mengatur agar baris di root dapat menyesuaikan ukuran
    root.grid_rowconfigure(1, weight=1)  # Memberikan bobot pada baris 1 agar frame bisa mengambil ruang


