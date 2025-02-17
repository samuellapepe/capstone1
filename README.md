# Sistem Perpustakaan AYES 

## Deskripsi Program

Sistem Perpustakaan AYES adalah program berbasis Python untuk mengelola koleksi buku di perpustakaan. Program ini memungkinkan pengguna untuk login sebagai admin atau peminjam, mencari buku, meminjam buku, mengembalikan buku, serta menambah atau menghapus buku dari koleksi.

## Fitur Utama

1. Login Pengguna

    * Admin melakukan management perpustakaan dan dapat mengakses semua menu.

    * *Peminjam hanya dapat melihat buku dan peminjaman dilkaukan pada Admin.

2. Menampilkan Daftar Buku

    * Opsi untuk menampilkan semua buku atau mencari berdasarkan kategori tertentu (judul, penulis, genre, tahun).

3. Peminjaman Buku

    * Pengguna dapat meminjam buku dan Admin akan mencatatnya dengan memasukkan judul dan informasi peminjaman.

    * Sistem akan mencatat batas waktu pengembalian (7 hari).

4. Pengembalian Buku

    * Peminjam dapat mengembalikan buku kepada Admin.

    * Sistem menghitung denda keterlambatan jika melebihi batas waktu pengembalian dan peminjam akan dikenai denda sesuai dengan peraturan.

5. Manajemen Buku

    * Admin dapat menambah dan menghapus buku dari koleksi.

## Instalasi dan Penggunaan

1. Persyaratan

    * Menggunakan bahasa pemrograman Python

    * Modul tabulate (jika belum terinstal, gunakan perintah pip install tabulate) 

    * Modul datetime (jika belum terinstall, gunakan perintah pip install tabulate)

2. Cara Menjalankan Program

    * Jalankan script Python yang terlampir

    * Pilih opsi login sebagai Admin atau Peminjam dengan memasukkan username dan password.

    * Ikuti instruksi dalam menu pada program untuk menggunakan fitur yang tersedia.

## Struktur Data

    
* koleksiBuku: Dictionary yang menyimpan data buku dengan format {ID: {title, author, genre, year}}

* peminjamanBuku: Dictionary yang mencatat buku yang sedang dipinjam.

* akun_admin & akun_peminjam: Dictionary untuk autentikasi pengguna.

## Catatan Tambahan

* Admin dapat menghapus buku hanya jika buku tersebut tidak sedang dipinjam.

* Peminjam harus memasukkan tanggal dalam format YYYY-MM-DD saat meminjam atau mengembalikan buku.

* Denda keterlambatan dihitung sebesar Rp10.000 per hari keterlambatan.

## Kontributor

Dikembangkan oleh Tim AYES Library Management.


## Lisensi

Program ini merupakan projek Bootcamp JCDS 2804 Purwadhika.

![flowchart capstone-Main Menu drawio](https://github.com/user-attachments/assets/5fec7c54-be79-407c-9807-480f11c386ba)
![flowchart capstone-Read Menu drawio](https://github.com/user-attachments/assets/88f1737d-405d-497d-90c1-2d9388b4a37c)
![flowchart capstone-update menu drawio](https://github.com/user-attachments/assets/a3e7166f-ada0-4511-bc10-ead04351ca81)
![flowchart capstone-create menu drawio](https://github.com/user-attachments/assets/2adf19e5-cf15-405e-9d95-0c9f285387df)
![flowchart capstone-delete menu drawio](https://github.com/user-attachments/assets/80bb0bdb-5f57-471a-b5b4-36e2137415e7)
