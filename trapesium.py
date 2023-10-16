# Menghitung Keliling dan Luas Trapesium

import tkinter as tk

def hitung_luas_dan_keliling():
    try:
        sisi_atas = float(entry_sisi_atas.get())
        sisi_bawah = float(entry_sisi_bawah.get())
        tinggi = float(entry_tinggi.get())
        
        luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
        keliling = sisi_atas + sisi_bawah + 2 * sisi_kiri.get()
        
        label_hasil.config(text=f"Luas trapesium: {luas:.2f} satuan persegi\nKeliling trapesium: {keliling:.2f} satuan")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid.")

# Buat jendela utama
root = tk.Tk()
root.title("Hitung Keliling dan Luas Trapesium")

# Buat label dan entry untuk sisi atas
label_sisi_atas = tk.Label(root, text="Sisi Atas:")
label_sisi_atas.grid(row=0, column=0)
entry_sisi_atas = tk.Entry(root)
entry_sisi_atas.grid(row=0, column=1)

# Buat label dan entry untuk sisi bawah
label_sisi_bawah = tk.Label(root, text="Sisi Bawah:")
label_sisi_bawah.grid(row=1, column=0)
entry_sisi_bawah = tk.Entry(root)
entry_sisi_bawah.grid(row=1, column=1)

# Buat label dan entry untuk tinggi
label_tinggi = tk.Label(root, text="Tinggi:")
label_tinggi.grid(row=2, column=0)
entry_tinggi = tk.Entry(root)
entry_tinggi.grid(row=2, column=1)

# Buat label dan entry untuk sisi kiri (opsional)
label_sisi_kiri = tk.Label(root, text="Sisi Kiri (opsional):")
label_sisi_kiri.grid(row=3, column=0)
sisi_kiri = tk.DoubleVar()
entry_sisi_kiri = tk.Entry(root, textvariable=sisi_kiri)
entry_sisi_kiri.grid(row=3, column=1)

# Tombol hitung
button_hitung = tk.Button(root, text="Hitung", command=hitung_luas_dan_keliling)
button_hitung.grid(row=4, column=0, columnspan=2)

# Label untuk hasil
label_hasil = tk.Label(root, text="", justify="left")
label_hasil.grid(row=5, column=0, columnspan=2)

# Jalankan aplikasi
root.mainloop()
