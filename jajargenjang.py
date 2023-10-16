# Menghitung keliling dan luas jajar genjang

import tkinter as tk

def hitung_luas_dan_keliling():
    try:
        alas = float(entry_alas.get())
        tinggi = float(entry_tinggi.get())
        sisi1 = float(entry_sisi1.get())
        sisi2 = float(entry_sisi2.get())
        
        if alas > 0 and tinggi > 0 and sisi1 > 0 and sisi2 > 0:
            luas = alas * tinggi
            keliling = 2 * (sisi1 + sisi2)
            hasil_text = f"Luas jajar genjang: {luas:.2f} satuan persegi\nKeliling jajar genjang: {keliling:.2f} satuan"
            label_hasil.config(text=hasil_text)
        else:
            label_hasil.config(text="Panjang alas, tinggi, dan sisi-sisi harus positif.")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid.")

# Buat jendela utama
root = tk.Tk()
root.title("Hitung Keliling dan Luas Jajar Genjang")

# Buat frame untuk mengelompokkan elemen
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Buat label untuk judul
label_judul = tk.Label(frame, text="Hitung Keliling dan Luas Jajar Genjang", font=("Arial", 16))
label_judul.grid(row=0, column=0, columnspan=2, pady=10)

# Buat dictionary untuk satuan
satuan_options = ["meter", "sentimeter", "milimeter"]
satuan_var = tk.StringVar()
satuan_var.set(satuan_options[0])  # Set satuan default

# Buat label dan entry untuk alas
label_alas = tk.Label(frame, text="Alas:")
label_alas.grid(row=1, column=0, sticky="w")
entry_alas = tk.Entry(frame)
entry_alas.grid(row=1, column=1)

# Buat opsi menu untuk satuan
satuan_menu = tk.OptionMenu(frame, satuan_var, *satuan_options)
satuan_menu.grid(row=1, column=2, sticky="w")

# Buat label dan entry untuk tinggi
label_tinggi = tk.Label(frame, text="Tinggi:")
label_tinggi.grid(row=2, column=0, sticky="w")
entry_tinggi = tk.Entry(frame)
entry_tinggi.grid(row=2, column=1)

# Buat opsi menu untuk satuan
satuan_menu = tk.OptionMenu(frame, satuan_var, *satuan_options)
satuan_menu.grid(row=2, column=2, sticky="w")

# Buat label dan entry untuk sisi 1
label_sisi1 = tk.Label(frame, text="Sisi 1:")
label_sisi1.grid(row=3, column=0, sticky="w")
entry_sisi1 = tk.Entry(frame)
entry_sisi1.grid(row=3, column=1)

# Buat opsi menu untuk satuan
satuan_menu = tk.OptionMenu(frame, satuan_var, *satuan_options)
satuan_menu.grid(row=3, column=2, sticky="w")

# Buat label dan entry untuk sisi 2
label_sisi2 = tk.Label(frame, text="Sisi 2:")
label_sisi2.grid(row=4, column=0, sticky="w")
entry_sisi2 = tk.Entry(frame)
entry_sisi2.grid(row=4, column=1)

# Buat opsi menu untuk satuan
satuan_menu = tk.OptionMenu(frame, satuan_var, *satuan_options)
satuan_menu.grid(row=4, column=2, sticky="w")

# Tombol hitung
button_hitung = tk.Button(frame, text="Hitung", command=hitung_luas_dan_keliling)
button_hitung.grid(row=5, column=0, columnspan=3, pady=10)

# Label untuk hasil
label_hasil = tk.Label(frame, text="", justify="left")
label_hasil.grid(row=6, column=0, columnspan=3)

# Jalankan aplikasi
root.mainloop()
