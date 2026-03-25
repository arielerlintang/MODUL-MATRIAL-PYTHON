10. STUDI KASUS XLSX
10.1 Membaca file xlsx
import pandas as pd

data = pd.read_excel("data.xlsx")
print(data)
10.2 Menampilkan head dan tail
import pandas as pd

data = pd.read_excel("data.xlsx")

print("Data awal")
print(data.head())

print("Data akhir")
print(data.tail())
10.3 Menampilkan data menjadi array
import pandas as pd

data = pd.read_excel("data.xlsx")
array_data = data.values

print(array_data)
