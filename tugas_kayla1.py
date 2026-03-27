def hitung_tagihan(harga, jumlah, status):
    total = harga * jumlah

    if status == "VIP":
        diskon = total * 0.15
    elif status == "REGULER" and total > 100000:
        diskon = total * 0.05
    else:
        diskon = 0

    total_akhir = total - diskon
    return total_akhir


while True:
    print("\n=== TOKO MAJU JAYA ===")
    print("1. Buat Pesanan Baru")
    print("2. Selesai & Tutup")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Masukkan nama pelanggan: ").strip().upper()
        status = input("Masukkan status member (VIP/REGULER): ").strip().upper()

        try:
            harga = int(input("Masukkan harga barang: "))
            jumlah = int(input("Masukkan jumlah beli: "))
        except ValueError:
            print("Input tidak valid, harap masukkan angka.")
            continue

        total_bayar = hitung_tagihan(harga, jumlah, status)

        print("\n--- STRUK PESANAN ---")
        print(f"Nama Pelanggan : {nama}")
        print(f"Status Member  : {status}")
        print(f"Total Bayar    : Rp {total_bayar}")

        file = open("data_pesanan.txt", "a")
        file.write(f"{nama},{total_bayar},{status}\n")
        file.close()

        print("Data pesanan berhasil disimpan.")

    elif pilih == "2":
        print("Program selesai. Terima kasih.")
        break

    else:
        print("Pilihan tidak ada, silakan pilih 1 atau 2.")
