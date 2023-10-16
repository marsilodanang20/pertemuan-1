# Menghitung Keliling dan Luas lingkaran

import tkinter as tk
import math

def hitung_luas_dan_keliling():
    try:
        jari_jari = float(entry_jari_jari.get())
        
        if jari_jari > 0:
            luas = math.pi * jari_jari**2
            keliling = 2 * math.pi * jari_jari
            hasil_text = f"Luas lingkaran: {luas:.2f} satuan persegi\nKeliling lingkaran: {keliling:.2f} satuan"
            label_hasil.config(text=hasil_text)
        else:
            label_hasil.config(text="Jari-jari harus positif.")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid.")

# Buat jendela utama
root = tk.Tk()
root.title("Hitung Keliling dan Luas Lingkaran")

# Buat frame untuk mengelompokkan elemen
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Buat label untuk judul
label_judul = tk.Label(frame, text="Hitung Keliling dan Luas Lingkaran", font=("Arial", 16))
label_judul.grid(row=0, column=0, columnspan=2, pady=10)

# Buat label dan entry untuk jari-jari
label_jari_jari = tk.Label(frame, text="Jari-jari Lingkaran:")
label_jari_jari.grid(row=1, column=0, sticky="w")
entry_jari_jari = tk.Entry(frame)
entry_jari_jari.grid(row=1, column=1)

# Tambahkan label satuan (opsional)
label_satuan = tk.Label(frame, text="satuan")
label_satuan.grid(row=1, column=2, sticky="w")

# Tombol hitung
button_hitung = tk.Button(frame, text="Hitung", command=hitung_luas_dan_keliling)
button_hitung.grid(row=2, column=0, columnspan=3, pady=10)

# Label untuk hasil
label_hasil = tk.Label(frame, text="", justify="left")
label_hasil.grid(row=3, column=0, columnspan=3)

# Jalankan aplikasi
root.mainloop()
