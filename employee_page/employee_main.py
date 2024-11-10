from tkinter import *
from tkinter import ttk

# Membuat window utama
def employee(root, cursor, name):
    root.configure(bg="white")
    root.attributes("-fullscreen", True)
    root.title("Employee Task Table")

    # Mendapatkan ukuran layar
    screen_width = root.winfo_screenwidth()

    # Label Selamat Datang
    status = "Employee"
    welcome_label = Label(root, text=f"Welcome, {name} ({status})")
    welcome_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    # Mengatur frame agar menempati sekitar 70% dari window
    frame = Frame(root, borderwidth=1, relief="solid", bg="white")  # Border untuk visualisasi
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
    data = [
        (1, "Complete project documentation", "In Progress"),
        (2, "Develop login module", "Completed"),
        (3, "Test user registration", "Pending"),
        (4, "Design database schema", "In Progress"),
        (5, "Review pull requests", "Completed"),
    ] * 10  # Duplikasi data untuk mengisi lebih banyak baris

    for row in data:
        tree.insert("", "end", values=row)

    # Menambahkan frame dan tombol di sebelah kanan
    frame_two = Frame(root, borderwidth=0, relief="solid", bg="white")  # Border untuk visualisasi
    frame_two.grid(row=1, column=1, padx=0, pady=20, sticky="nsew")

    # Mengatur tombol "View details"
    View_details_button = Button(frame_two, text="View details", width=int(screen_width - screen_width * 0.96484375),  height=2, font=('Inter', 14))
    View_details_button.grid(row=0, column=0, sticky="e", pady=10, padx=5)

    # Mengatur tombol "Mark as Done / Not Done"
    Mark_button = Button(frame_two, text="Mark as Done /\nNot Done", width=int(screen_width - screen_width * 0.96484375),  height=2, font=('Inter', 14))
    Mark_button.grid(row=1, column=0, sticky="e", pady=10, padx=5)

    # Menambahkan baris kosong sebelum tombol Logout
    frame_two.grid_rowconfigure(2, weight=1)  # Membiarkan baris 2 mengambil sisa ruang

    # Mengatur tombol "Logout" di pojok kanan bawah
    Logout_button = Button(frame_two, text="Logout", width=int(screen_width - screen_width * 0.99453125), height=1, font=('Inter'))
    Logout_button.grid(row=3, column=0, sticky="se", pady=10, padx=5)  # Pindahkan ke baris 3

    # Mengatur agar frame dua dan treeview bisa menyesuaikan ukuran
    frame.grid_rowconfigure(0, weight=1)  # Membuat Treeview untuk mengambil sisa ruang
    frame.grid_columnconfigure(0, weight=1)  # Membuat kolom treeview untuk mengambil sisa ruang

    # Mengatur agar baris di root dapat menyesuaikan ukuran
    root.grid_rowconfigure(1, weight=1)  # Memberikan bobot pada baris 1 agar frame bisa mengambil ruang


