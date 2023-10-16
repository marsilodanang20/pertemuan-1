# Menghitung Keliling dan Luas Layang-layang

import tkinter as tk
import math

def hitung_luas_dan_keliling():
    try:
        diagonal1 = float(entry_diagonal1.get())
        diagonal2 = float(entry_diagonal2.get())
        
        if diagonal1 > 0 and diagonal2 > 0:
            luas = 0.5 * diagonal1 * diagonal2
            keliling = 2 * math.sqrt(diagonal1**2 + diagonal2**2)
            hasil_text = f"Luas layang-layang: {luas:.2f} satuan persegi\nKeliling layang-layang: {keliling:.2f} satuan"
            label_hasil.config(text=hasil_text)
        else:
            label_hasil.config(text="Panjang diagonal harus positif.")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid.")

# Buat jendela utama
root = tk.Tk()
root.title("Hitung Keliling dan Luas Layang-Layang")

# Buat frame untuk mengelompokkan elemen
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Buat label untuk judul
label_judul = tk.Label(frame, text="Hitung Keliling dan Luas Layang-Layang", font=("Arial", 16))
label_judul.grid(row=0, column=0, columnspan=2, pady=10)

# Buat label dan entry untuk diagonal pertama
label_diagonal1 = tk.Label(frame, text="Diagonal Pertama:")
label_diagonal1.grid(row=1, column=0, sticky="w")
entry_diagonal1 = tk.Entry(frame)
entry_diagonal1.grid(row=1, column=1)

# Tambahkan label satuan (opsional)
label_satuan1 = tk.Label(frame, text="satuan")
label_satuan1.grid(row=1, column=2, sticky="w")

# Buat label dan entry untuk diagonal kedua
label_diagonal2 = tk.Label(frame, text="Diagonal Kedua:")
label_diagonal2.grid(row=2, column=0, sticky="w")
entry_diagonal2 = tk.Entry(frame)
entry_diagonal2.grid(row=2, column=1)

# Tambahkan label satuan (opsional)
label_satuan2 = tk.Label(frame, text="satuan")
label_satuan2.grid(row=2, column=2, sticky="w")

# Tombol hitung
button_hitung = tk.Button(frame, text="Hitung", command=hitung_luas_dan_keliling)
button_hitung.grid(row=3, column=0, columnspan=3, pady=10)

# Label untuk hasil
label_hasil = tk.Label(frame, text="", justify="left")
label_hasil.grid(row=4, column=0, columnspan=3)

# Jalankan aplikasi
root.mainloop()
