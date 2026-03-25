# ==============================
# GOOGLE COLAB - DATA MINING XLSX ROBLOX
# Upload file Excel, baca data, ubah ke array,
# kluster berdasarkan Rating, lalu visualisasi
# ==============================

# 1. Import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# 2. Upload file Excel
uploaded = files.upload()

# Ambil nama file yang diupload
file_name = list(uploaded.keys())[0]

# 3. Baca file Excel
df = pd.read_excel(file_name)

# 4. Tampilkan 5 data awal
print("=== 5 DATA AWAL ===")
print(df.head())

# 5. Tampilkan data dalam bentuk array
data_array = df.values
print("\n=== DATA DALAM BENTUK ARRAY ===")
print(data_array)

# 6. Pastikan kolom Rating bertipe numerik
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# Hapus data yang Rating-nya kosong / error
df = df.dropna(subset=['Rating']).copy()

# 7. Pengelompokan 3 kluster berdasarkan Rating
# Batas kluster buatan sendiri:
# Rating < 70      = Cluster 1 (Rendah)
# Rating 70 - 84   = Cluster 2 (Sedang)
# Rating >= 85     = Cluster 3 (Tinggi)

def tentukan_cluster(rating):
    if rating < 70:
        return "Cluster 1 - Rendah"
    elif rating < 85:
        return "Cluster 2 - Sedang"
    else:
        return "Cluster 3 - Tinggi"

df['Cluster'] = df['Rating'].apply(tentukan_cluster)

# 8. Tampilkan hasil klustering
print("\n=== HASIL KLUSTERING ===")
print(df[['Name', 'Rating', 'Cluster']].head(20))

# 9. Jumlah data per kluster
jumlah_cluster = df['Cluster'].value_counts()
print("\n=== JUMLAH DATA PER KLUSTER ===")
print(jumlah_cluster)

# 10. Visualisasi 1: Bar chart jumlah data per cluster
plt.figure(figsize=(8,5))
jumlah_cluster.plot(kind='bar')
plt.title('Jumlah Data per Cluster Berdasarkan Rating')
plt.xlabel('Cluster')
plt.ylabel('Jumlah Game')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# 11. Visualisasi 2: Scatter plot Rating per game
# Agar warna berbeda per cluster
warna_cluster = {
    "Cluster 1 - Rendah": "red",
    "Cluster 2 - Sedang": "orange",
    "Cluster 3 - Tinggi": "green"
}

plt.figure(figsize=(12,6))
for cluster in df['Cluster'].unique():
    data_cluster = df[df['Cluster'] == cluster]
    plt.scatter(data_cluster.index, data_cluster['Rating'], label=cluster)

plt.title('Visualisasi Cluster Berdasarkan Rating')
plt.xlabel('Index Data')
plt.ylabel('Rating')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 12. Simpan hasil klustering ke file Excel baru
output_file = "hasil_klustering_roblox.xlsx"
df.to_excel(output_file, index=False)

print(f"\nFile hasil berhasil dibuat: {output_file}")
files.download(output_file)
