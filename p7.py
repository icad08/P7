import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():

    try:
        for index, entry in enumerate(entries):
            nilai = entry.get()
            if not nilai.isdigit() or not (0 <= int(nilai) <= 100):
                raise ValueError(f"Nilai pada Mata Pelajaran {index + 1} harus antara 0 dan 100.")
        
        # Logika sederhana untuk menentukan prediksi prodi
        # (Anda bisa mengganti logika ini sesuai kebutuhan)
        total_nilai = sum(int(entry.get()) for entry in entries)
        if total_nilai >= 800:
            hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
        else:
            hasil_label.config(text="Prediksi Prodi: Prodi Lain")

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))


root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

# Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#f0f0f0")
judul_label.pack(pady=20)

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)

entries = []
for i in range(10):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12), bg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#4CAF50", fg="black")
prediksi_button.pack(pady=30)

hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="blue", bg="#f0f0f0")
hasil_label.pack(pady=20)

root.mainloop()