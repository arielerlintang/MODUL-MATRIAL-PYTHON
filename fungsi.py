8. FUNGSI
8.1 Fungsi biasa
def salam():
    print("Selamat belajar Python")

salam()
8.2 Fungsi dengan parameter
def salam(nama):
    print("Halo", nama)

salam("Eluvia")
8.3 Fungsi dengan return
def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
print(hasil)
8.4 Fungsi untuk menghitung nilai
def hitung_nilai(uts, uas):
    nilai_akhir = (uts + uas) / 2
    return nilai_akhir

hasil = hitung_nilai(80, 90)
print("Nilai akhir =", hasil)
8.5 Fungsi yang cocok untuk Flask

Dalam Flask, fungsi dipakai untuk memproses data.

def hitung_total(harga, jumlah):
    return harga * jumlah

total = hitung_total(5000, 3)
print(total)
