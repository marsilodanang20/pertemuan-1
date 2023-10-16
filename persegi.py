# Menghitung Keliling dan Luas Persegi

import tkinter as tk

def hitung_luas_dan_keliling():
    try:
        sisi = float(entry_sisi.get())
        
        if sisi > 0:
            luas = sisi ** 2
            keliling = 4 * sisi
            hasil_text = f"Luas persegi: {luas:.2f} satuan persegi\nKeliling persegi: {keliling:.2f} satuan"
            label_hasil.config(text=hasil_text)
        else:
            label_hasil.config(text="Panjang sisi harus positif.")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid.")

# Buat jendela utama
root = tk.Tk()
root.title("Hitung Keliling dan Luas Persegi")

# Buat frame untuk mengelompokkan elemen
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Buat label untuk judul
label_judul = tk.Label(frame, text="Hitung Keliling dan Luas Persegi", font=("Arial", 16))
label_judul.grid(row=0, column=0, columnspan=2, pady=10)

# Buat label dan entry untuk sisi
label_sisi = tk.Label(frame, text="Panjang Sisi:")
label_sisi.grid(row=1, column=0, sticky="w")
entry_sisi = tk.Entry(frame)
entry_sisi.grid(row=1, column=1)

# Tombol hitung
button_hitung = tk.Button(frame, text="Hitung", command=hitung_luas_dan_keliling)
button_hitung.grid(row=2, column=0, columnspan=2, pady=10)

# Label untuk hasil
label_hasil = tk.Label(frame, text="", justify="left")
label_hasil.grid(row=3, column=0, columnspan=2)

# Jalankan aplikasi
root.mainloop()
