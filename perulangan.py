5. PERULANGAN
5.1 For

Digunakan jika jumlah perulangan sudah diketahui.

for i in range(1, 6):
    print("Perulangan ke-", i)
Contoh menampilkan isi list
buah = ["apel", "mangga", "jeruk"]

for item in buah:
    print(item)
5.2 While

Digunakan jika perulangan berdasarkan kondisi.

i = 1

while i <= 5:
    print("Perulangan ke-", i)
    i += 1
5.3 Do While

Python tidak memiliki do while secara langsung, tetapi bisa disimulasikan seperti ini:

while True:
    print("Ini dijalankan minimal sekali")
    jawab = input("Ulangi lagi? (y/t): ")
    if jawab == "t":
        break
