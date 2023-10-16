# Menghitung Keliling dan Luas Segitiga

import tkinter as tk

def hitung_luas_dan_keliling():
    try:
        alas = float(entry_alas.get())
        tinggi = float(entry_tinggi.get())
        sisi1 = float(entry_sisi1.get())
        sisi2 = float(entry_sisi2.get())
        sisi3 = float(entry_sisi3.get())
        
        if alas > 0 and tinggi > 0 and sisi1 > 0 and sisi2 > 0 and sisi3 > 0:
            luas = 0.5 * alas * tinggi
            keliling = sisi1 + sisi2 + sisi3
            hasil_text = f"Luas segitiga: {luas:.2f} satuan persegi\nKeliling segitiga: {keliling:.2f} satuan"
            label_hasil.config(text=hasil_text)
        else:
            label_hasil.config(text="Panjang alas, tinggi, dan sisi-sisi harus positif.")
    except ValueError:
        label_hasil.config(text="Masukkan angka yang valid.")

# Buat jendela utama
root = tk.Tk()
root.title("Hitung Keliling dan Luas Segitiga")

# Buat label dan entry untuk alas
label_alas = tk.Label(root, text="Alas:")
label_alas.grid(row=0, column=0)
entry_alas = tk.Entry(root)
entry_alas.grid(row=0, column=1)

# Buat label dan entry untuk tinggi
label_tinggi = tk.Label(root, text="Tinggi:")
label_tinggi.grid(row=1, column=0)
entry_tinggi = tk.Entry(root)
entry_tinggi.grid(row=1, column=1)

# Buat label dan entry untuk sisi 1
label_sisi1 = tk.Label(root, text="Sisi 1:")
label_sisi1.grid(row=2, column=0)
entry_sisi1 = tk.Entry(root)
entry_sisi1.grid(row=2, column=1)

# Buat label dan entry untuk sisi 2
label_sisi2 = tk.Label(root, text="Sisi 2:")
label_sisi2.grid(row=3, column=0)
entry_sisi2 = tk.Entry(root)
entry_sisi2.grid(row=3, column=1)

# Buat label dan entry untuk sisi 3
label_sisi3 = tk.Label(root, text="Sisi 3:")
label_sisi3.grid(row=4, column=0)
entry_sisi3 = tk.Entry(root)
entry_sisi3.grid(row=4, column=1)

# Tombol hitung
button_hitung = tk.Button(root, text="Hitung", command=hitung_luas_dan_keliling)
button_hitung.grid(row=5, column=0, columnspan=2)

# Label untuk hasil
label_hasil = tk.Label(root, text="", justify="left")
label_hasil.grid(row=6, column=0, columnspan=2)

# Jalankan aplikasi
root.mainloop()
