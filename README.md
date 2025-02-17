## Sistem Perpustakaan AYES 

# Deskripsi

Sistem Perpustakaan AYES adalah program berbasis Python untuk mengelola koleksi buku di perpustakaan. Program ini memungkinkan pengguna untuk login sebagai admin atau peminjam, mencari buku, meminjam buku, mengembalikan buku, serta menambah atau menghapus buku dari koleksi.

# Fitur Utama

Login Pengguna

Admin dapat mengelola koleksi buku dan peminjaman.

Peminjam dapat mencari dan meminjam buku.

Menampilkan Daftar Buku

Opsi untuk menampilkan semua buku atau mencari berdasarkan kategori tertentu (judul, penulis, genre, tahun).

Peminjaman Buku

Pengguna dapat meminjam buku dengan memasukkan judul dan informasi peminjaman.

Sistem mencatat batas waktu pengembalian (7 hari).

Pengembalian Buku

Pengguna dapat mengembalikan buku.

Sistem menghitung denda keterlambatan jika melebihi batas waktu pengembalian.

Manajemen Buku (Admin)

Admin dapat menambah dan menghapus buku dari koleksi.

Instalasi dan Penggunaan

Persyaratan

Python 3.x

Modul tabulate (jika belum terinstal, gunakan perintah pip install tabulate)

Cara Menjalankan Program

Jalankan script Python:

python cobacoba6.py

Pilih opsi login sebagai Admin atau Peminjam.

Ikuti instruksi dalam menu untuk menggunakan fitur yang tersedia.

Struktur Data

koleksiBuku: Dictionary yang menyimpan data buku dengan format {ID: {title, author, genre, year}}

peminjamanBuku: Dictionary yang mencatat buku yang sedang dipinjam.

akun_admin & akun_peminjam: Dictionary untuk autentikasi pengguna.

Catatan Tambahan

Admin dapat menghapus buku hanya jika buku tersebut tidak sedang dipinjam.

Peminjam harus memasukkan tanggal dalam format YYYY-MM-DD saat meminjam atau mengembalikan buku.

Denda keterlambatan dihitung sebesar Rp10.000 per hari keterlambatan.

Kontributor

Dikembangkan oleh Tim AYES Library Management.

Lisensi

Program ini bersifat open-source dan dapat dimodifikasi sesuai kebutuhan.

