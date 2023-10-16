# Menghitung Keliling dan Luas Persegi panjang

import tkinter as tk

def hitung_luas_dan_keliling():
    try:
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        
        if panjang > 0 and lebar > 0:
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            hasil_text = f"Luas persegi panjang: {luas:.2f} satuan persegi\nKeliling persegi panjang: {keliling:.2f} satuan"
            label_hasil.config(text=hasil_text)
        else:
            label_hasil.config(text="Panjang dan lebar harus positif.")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid.")

# Buat jendela utama
root = tk.Tk()
root.title("Hitung Keliling dan Luas Persegi Panjang")

# Buat label dan entry untuk panjang
label_panjang = tk.Label(root, text="Panjang:")
label_panjang.grid(row=0, column=0)
entry_panjang = tk.Entry(root)
entry_panjang.grid(row=0, column=1)

# Buat label dan entry untuk lebar
label_lebar = tk.Label(root, text="Lebar:")
label_lebar.grid(row=1, column=0)
entry_lebar = tk.Entry(root)
entry_lebar.grid(row=1, column=1)

# Tombol hitung
button_hitung = tk.Button(root, text="Hitung", command=hitung_luas_dan_keliling)
button_hitung.grid(row=2, column=0, columnspan=2)

# Label untuk hasil
label_hasil = tk.Label(root, text="", justify="left")
label_hasil.grid(row=3, column=0, columnspan=2)

# Jalankan aplikasi
root.mainloop()
