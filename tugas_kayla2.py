# fungsi untuk menghitung total tagihan
def hitung_tagihan(harga, jumlah, status):
    total = harga * jumlah

    # cek diskon berdasarkan status member
    if status == "VIP":
        diskon = total * 0.15
    elif status == "REGULER" and total > 100000:
        diskon = total * 0.05
    else:
        diskon = 0

    # hitung total akhir setelah diskon
    total_akhir = total - diskon

    # ubah ke integer agar tidak tampil .0
    return int(total_akhir)


# perulangan utama program
while True:
    print("\n=== TOKO MAJU JAYA ===")
    print("1. Buat Pesanan Baru")
    print("2. Selesai & Tutup")

    pilih = input("Pilih menu: ")

    # jika user memilih menu 1
    if pilih == "1":
        # input nama pelanggan
        nama = input("Masukkan nama pelanggan: ").strip().upper()

        # input status member
        status = input("Masukkan status member (VIP/REGULER): ").strip().upper()

        # validasi status member
        if status != "VIP" and status != "REGULER":
            print("Status member harus VIP atau REGULER.")
            continue

        # input harga dan jumlah dengan try except
        try:
            harga = int(input("Masukkan harga barang: "))
            jumlah = int(input("Masukkan jumlah beli: "))
        except ValueError:
            print("Input tidak valid, harap masukkan angka.")
            continue

        # panggil fungsi hitung tagihan
        total_bayar = hitung_tagihan(harga, jumlah, status)

        # tampilkan struk ke layar
        print("\n--- STRUK PESANAN ---")
        print(f"Nama Pelanggan : {nama}")
        print(f"Status Member  : {status}")
        print(f"Total Bayar    : Rp {total_bayar}")

        # simpan data ke file
        file = open("data_pesanan.txt", "a")
        file.write(f"{nama},{total_bayar},{status}\n")
        file.close()

        print("Data pesanan berhasil disimpan.")

    # jika user memilih menu 2
    elif pilih == "2":
        print("Program selesai. Terima kasih.")
        break

    # jika input menu salah
    else:
        print("Pilihan tidak ada, silakan pilih 1 atau 2.")
