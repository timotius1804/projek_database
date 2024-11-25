from tkinter import *
from tkinter import ttk
from manager_page.manager_add_task import manager_add_task
from manager_page.manager_edit_task import manager_edit_task

# To-Do :
# 1. Turn logout button into back button
# 2. Display data based on project
# 3. Connect the buttons to their respective pages
# 4. Turn the file into a function to be called from the main file 
#    that accepts project identifier as an argument

def delete_task(db, cursor, tree,tree_main, project_id):
    selected = tree.selection()
    slected_value = tree.item(selected[0], "values")
    task_id = slected_value[0]
    cursor.execute(
        f"""
        DELETE FROM task WHERE taskid = '{task_id}'
        """
    )
    tree.delete(selected[0])

    # Update nilai pada Treeview utama
    selected_main = tree_main.selection()[0]
    current_values = tree_main.item(selected_main, "values")
    done_tasks, total_tasks = map(int, current_values[2].split("/"))
    if slected_value[3] == 'Done':
        done_tasks -= 1
        total_tasks -= 1
    else:
        total_tasks -=1

    status = current_values[3]
    if done_tasks == total_tasks:
        status = "Done"
        cursor.execute(
        f"""
        UPDATE project SET status = 'Done' WHERE projectid = {project_id}
        """
    )
    else:
        cursor.execute(
        f"""
        UPDATE project SET status = 'Not Done' WHERE projectid = {project_id}
        """
    )
    tree_main.item(selected_main, values=(current_values[0], current_values[1], f"{done_tasks}/{total_tasks}", status))
    db.commit()

# Membuat window utama
def taskProject(root, db, cursor, project_id, tree_main):
    task_window = Toplevel(root)
    task_window.attributes("-fullscreen", True)
    task_window.configure(bg="#faebd7")
    task_window.title("Employee Task Table")

    # Mendapatkan ukuran layar
    screen_width = task_window.winfo_screenwidth()

    # Label Selamat Datang
    project_name = "project_name"  # Ganti dengan nama project yang sesuai
    welcome_label = Label(task_window, text=f"Tasks for {project_name}",bg="#faebd7",font=("Arial", 16, "bold"))
    welcome_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    # Mengatur frame agar menempati sekitar 70% dari window
    frame = Frame(task_window, borderwidth=1, relief="solid", bg="white")  # Border untuk visualisasi
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
            background=[("selected", "#808080")],  # Warna latar belakang saat baris dipilih
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
    cursor.execute(
f"""
SELECT taskid, taskname, taskdue, status FROM task WHERE projectid = '{project_id}'
"""
    )
    data = cursor.fetchall()
    if data:
        for row in data:
            tree.insert("", "end", values=row)
    else:
        tree.insert("", "end", values=["", "No Task", "",])

    # Menambahkan frame dan tombol di sebelah kanan
    frame_two = Frame(task_window, borderwidth=0, relief="solid", bg="#faebd7")  # Border untuk visualisasi
    frame_two.grid(row=1, column=1, padx=0, pady=20, sticky="nsew")

    # Mengatur tombol "Add Task"
    View_details_button = Button(frame_two, bg= "white", text="Add Task", width=int(screen_width - screen_width * 0.96484375),  height=2, font=('Inter', 14), command=lambda: manager_add_task(task_window, db, cursor, tree, project_id, tree_main))
    View_details_button.grid(row=0, column=0, sticky="e", pady=10, padx=5)

    # Mengatur tombol "Edit Task"
    Mark_button = Button(frame_two, bg= "white", text="Edit Task", width=int(screen_width - screen_width * 0.96484375),  height=2, font=('Inter', 14), command=lambda: manager_edit_task(task_window, db, cursor, tree, tree_main))
    Mark_button.grid(row=1, column=0, sticky="e", pady=10, padx=5)

    # Mengatur tombol "Delete Task"
    Delete_button = Button(frame_two, bg= "white", text="Delete Task", width=int(screen_width - screen_width * 0.96484375),  height=2, font=('Inter', 14), command=lambda: delete_task(db, cursor, tree, tree_main, project_id))
    Delete_button.grid(row=2, column=0, sticky="e", pady=10, padx=5)

    # Menambahkan baris kosong sebelum tombol Logout
    frame_two.grid_rowconfigure(3, weight=1)  # Membiarkan baris 2 mengambil sisa ruang

    # Mengatur tombol "Logout" di pojok kanan bawah
    Logout_button = Button(frame_two, bg= "white", text="Back", width=int(screen_width - screen_width * 0.99453125), height=1, font=('Inter'), command=lambda: task_window.destroy())
    Logout_button.grid(row=4, column=0, sticky="se", pady=10, padx=5)  # Pindahkan ke baris 3

    # Mengatur agar frame dua dan treeview bisa menyesuaikan ukuran
    frame.grid_rowconfigure(0, weight=1)  # Membuat Treeview untuk mengambil sisa ruang
    frame.grid_columnconfigure(0, weight=1)  # Membuat kolom treeview untuk mengambil sisa ruang

    # Mengatur agar baris di task_window dapat menyesuaikan ukuran
    task_window.grid_rowconfigure(1, weight=1)  # Memberikan bobot pada baris 1 agar frame bisa mengambil ruang

