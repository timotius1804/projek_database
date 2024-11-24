import tkinter as tk
from tkinter import ttk



# Membuat jendela utama
root = tk.Tk()
root.title("Pilihan atau Ketik Input")

# Variabel untuk menyimpan pilihan
choice_var = tk.StringVar()

# Daftar pilihan
options = []

# Dropdown (Combobox) dengan fitur pencarian
dropdown = ttk.Combobox(root, textvariable=choice_var, values=options)
dropdown.set("Pilih atau ketik opsi")  # Placeholder
dropdown.pack(pady=10)

# Tombol Submit
submit_button = ttk.Button(root, text="Submit")
submit_button.pack(pady=10)

# Label hasil
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()
