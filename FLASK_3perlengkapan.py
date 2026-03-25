13. CRUD FLASK LENGKAP

Di bawah ini saya buatkan versi lengkap dan basic, sesuai permintaan kamu, dan tanpa bind parameter pada query tambah dan ubah.

13.1 Struktur folder project
crud_flask/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── tambah.html
│   └── edit.html
│
├── static/
│   ├── css/
│   │   └── bootstrap.min.css
│   └── img/
13.2 Database MySQL
Buat database
CREATE DATABASE crud;
Gunakan database
USE crud;
Buat tabel produk
CREATE TABLE produk (
    id_produk INT AUTO_INCREMENT PRIMARY KEY,
    nama_produk VARCHAR(100),
    deskripsi_produk TEXT,
    jenis_produk VARCHAR(50),
    foto_produk VARCHAR(255)
);
