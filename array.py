2. ARRAY DAN LIST

Di Python, yang paling sering dipakai adalah list.
Kalau di banyak bahasa lain sering disebut array, maka pada Python materi dasar biasanya memakai list.

2.1 List satu dimensi
buah = ["apel", "mangga", "jeruk", "pisang"]
print(buah)

2.2 Mengambil data list
Ambil data awal

buah = ["apel", "mangga", "jeruk", "pisang"]
print(buah[0])

Ambil data kedua
print(buah[1])

Ambil data terakhir
print(buah[-1])

Ambil data sebelum terakhir
print(buah[-2])

2.3 Mengambil beberapa data sekaligus
buah = ["apel", "mangga", "jeruk", "pisang", "melon"]

print(buah[0:3])   # dari index 0 sampai sebelum 3
print(buah[1:4])   # dari index 1 sampai sebelum 4
print(buah[:3])    # dari awal sampai sebelum 3
print(buah[2:])    # dari index 2 sampai akhir

2.4 Menambah data ke list

buah = ["apel", "mangga", "jeruk"]
buah.append("melon")
print(buah)

2.5 Mengubah data list

buah = ["apel", "mangga", "jeruk"]
buah[1] = "durian"
print(buah)

2.6 Menghapus data list

buah = ["apel", "mangga", "jeruk"]
buah.remove("mangga")
print(buah)

2.7 Perbedaan list dan tuple

List
Bisa diubah
Menggunakan []
data = ["Andi", "Budi", "Citra"]
data[0] = "Doni"
print(data)
Tuple
Tidak bisa diubah
Menggunakan ()
data = ("Andi", "Budi", "Citra")
print(data)

3. ARRAY MULTIDIMENSI

Array multidimensi adalah list yang berisi list lagi.

3.1 Contoh array 2 dimensi

nilai = [
    [80, 90, 85],
    [70, 75, 80],
    [88, 92, 95]
]

print(nilai)
3.2 Mengambil data array multidimensi
nilai = [
    [80, 90, 85],
    [70, 75, 80],
    [88, 92, 95]
]

print(nilai[0])      # baris pertama
print(nilai[1])      # baris kedua
print(nilai[2])      # baris ketiga
3.3 Mengambil data tertentu dari array multidimensi
nilai = [
    [80, 90, 85],
    [70, 75, 80],
    [88, 92, 95]
]

print(nilai[0][0])   # 80
print(nilai[0][1])   # 90
print(nilai[1][2])   # 80
print(nilai[2][1])   # 92

3.4 Studi kasus array multidimensi data mahasiswa
mahasiswa = [
    ["Andi", 80, 85],
    ["Budi", 75, 70],
    ["Citra", 90, 95]
]

print(mahasiswa[0])        # data mahasiswa pertama
print(mahasiswa[0][0])     # nama mahasiswa pertama
print(mahasiswa[0][1])     # nilai UTS mahasiswa pertama
print(mahasiswa[0][2])     # nilai UAS mahasiswa pertama

3.5 Perulangan array multidimensi
mahasiswa = [
    ["Andi", 80, 85],
    ["Budi", 75, 70],
    ["Citra", 90, 95]
]

for m in mahasiswa:
    print("Nama :", m[0])
    print("UTS  :", m[1])
    print("UAS  :", m[2])
    print("----------------")
4. HEAD DAN TAIL

head() dan tail() biasanya dipakai pada pandas DataFrame, terutama saat membaca file Excel atau CSV.

4.1 Import pandas
import pandas as pd
4.2 Contoh data sederhana
import pandas as pd

data = {
    "Nama": ["Andi", "Budi", "Citra", "Dina", "Eka"],
    "Nilai": [80, 75, 90, 85, 70]
}

df = pd.DataFrame(data)
print(df)

4.3 Head

Menampilkan data bagian atas.
print(df.head())

Menampilkan 3 data pertama:
print(df.head(3))
4.4 Tail

Menampilkan data bagian bawah.
print(df.tail())

Menampilkan 2 data terakhir:

print(df.tail(2))

4.5 Mengambil data tertentu dari DataFrame
print(df["Nama"])
print(df["Nilai"])

Ambil data baris pertama:
print(df.iloc[0])

Ambil data baris terakhir:
print(df.iloc[-1])

Ambil nilai kolom tertentu:

print(df.iloc[0]["Nama"])
print(df.iloc[2]["Nilai"])
