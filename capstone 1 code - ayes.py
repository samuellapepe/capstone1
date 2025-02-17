import datetime
from tabulate import tabulate

# Data koleksi buku (ID, title, author, genre, horror)
koleksiBuku = {
    "HOR001": {"title": "Cintaku Bersemi di Purwadhika", "author": "Samuella Pepe", "genre": "Horror", "year": 2022},
    "HOR002": {"title": "Bisikan Hutan Larangan", "author": "Fahmi Alamsyah", "genre": "Horror", "year": 2014},
    "HOR003": {"title": "Misteri Rumah Kosong", "author": "Joko Setiawan", "genre": "Horror", "year": 2020},
    "HOR004": {"title": "Hantu Kosan 13", "author": "Tono Wibowo", "genre": "Horror", "year": 2018},
    "HOR005": {"title": "Ketukan Tengah Malam", "author": "Eka Purnama", "genre": "Horror", "year": 2014},
    "COM001": {"title": "Bangku Kosong", "author": "Ayes Pepe", "genre": "Comedy", "year": 2023},
    "COM002": {"title": "Ketawa Sampai Mewek", "author": "Budi Santoso", "genre": "Comedy", "year": 2010},
    "COM003": {"title": "Ngopi Sambil Guling-Guling", "author": "Rizky Hidayat", "genre": "Comedy", "year": 2015},
    "COM004": {"title": "Juragan Angkringan", "author": "Dian Permana", "genre": "Comedy", "year": 2017},
    "COM005": {"title": "Cinta Ditolak, Nasi Bungkus Bertindak", "author": "Tono Wibowo", "genre": "Comedy", "year": 2012},
    "ROM001": {"title": "Senja di Kota Tua", "author": "Rizky Anwar", "genre": "Romance", "year": 2015},
    "ROM002": {"title": "Harmoni Musim Semi", "author": "Larasati Putri", "genre": "Romance", "year": 2020},
    "ROM003": {"title": "Sepasang Hati di Musim Hujan", "author": "Rizky Aditya", "genre": "Romance", "year": 2018},
    "ROM004": {"title": "Bunga di Taman Kenangan", "author": "Siti Maharani", "genre": "Romance", "year": 2015},
    "ROM005": {"title": "Janji di Bawah Pohon Sakura", "author": "Fajar Setiawan", "genre": "Romance", "year": 2020},
    "KUL001": {"title": "Rahasia Dapur Nusantara", "author": "Chef Budi Santoso", "genre": "Kuliner", "year": 2015},
    "KUL002": {"title": "Menyajikan Hidangan Lezat", "author": "Sari Wulandari", "genre": "Kuliner", "year": 2018},
    "KUL003": {"title": "Resep Tradisional Khas Indonesia", "author": "Dewi Kartika", "genre": "Kuliner", "year": 2017},
    "KUL004": {"title": "Seribu Rasa Masakan Asia", "author": "Riko Wijaya", "genre": "Kuliner", "year": 2020},
    "KUL005": {"title": "Panduan Memasak untuk Pemula", "author": "Lina Prasetyo", "genre": "Kuliner", "year": 2019},
    "MIT001": {"title": "Mitos dan Legenda Nusantara", "author": "Eko Prasetyo", "genre": "Mitos", "year": 2013},
    "MIT002": {"title": "Kutukan Seribu Tahun", "author": "Dian Prasetyo", "genre": "Mitos", "year": 2018},
    "MIT003": {"title": "Rahasia Makhluk Tak Kasat Mata", "author": "Rizky Anwar", "genre": "Mitos", "year": 2016},
    "MIT004": {"title": "Asal Usul Gunung Berapi", "author": "Siti Wulandari", "genre": "Mitos", "year": 2020},
    "MIT005": {"title": "Jejak Siluman di Nusantara", "author": "Arman Wijaya", "genre": "Mitos", "year": 2014},
    "MYS001": {"title": "Di Balik Kabut Pegunungan", "author": "Budi Santoso", "genre": "Misteri", "year": 2017},
    "MYS002": {"title": "Kasus Hilangnya Bayangan", "author": "Rizky Anwar", "genre": "Misteri", "year": 2019},
    "MYS003": {"title": "Misteri Kota yang Menghilang", "author": "Arman Wijaya", "genre": "Misteri", "year": 2015},
    "MYS004": {"title": "Jejak Tak Terlihat", "author": "Siti Wulandari", "genre": "Misteri", "year": 2021},
    "MYS005": {"title": "Rahasia Pintu Terkunci", "author": "Budi Santoso", "genre": "Misteri", "year": 2018},
}

# data peminjaman buku
peminjamanBuku = {} #dictionary buku yang dipinjam

# data akun pengguna
akunAdmin = {"admin": "admin123"} #username dan password admin
akunPeminjam = {"user": "user123"} #username dan password peminjam

#login pengguna
def login(): #mendefinisikan fungsi login
    while True: #melakukan proses login sampai login berhasil
        print("\n=== SELAMAT DATANG DI PERPUSTAKAAN AYES ===")
        print("Silahkan melakukan login terlebih dahulu. Siapakah anda?")
        print("1. Admin")
        print("2. Peminjam")
        print("3. Keluar")
        pilihan = input("Pilih jenis pengguna: ") #pilih input untuk login
        
        if pilihan == "1": #login sebagai admin
            username = input("Masukkan username admin: ") #masukkan username
            password = input("Masukkan password: ") #masukkan password
            if akunAdmin.get(username) == password: #jika benar, maka login berhasil
                print("\nLogin sebagai Admin berhasil!")
                return "admin"
            else: #jika salah, ulang proses login
                print("\nUsername atau password salah!")
        elif pilihan == "2": #login sebagai peminjam
            username = input("Masukkan username peminjam: ")
            password = input("Masukkan password: ")
            if akunPeminjam.get(username) == password:
                print("\nLogin sebagai Peminjam berhasil!")
                return "peminjam"
            else:
                print("\nUsername atau password salah!")
        elif pilihan == "3": #keluar dari seluruh sistem
            print("Terima kasih, sampai jumpa!")
            exit() #menghentikan eksekusi program, keluar dari program
        else:
            print("Pilihan tidak valid, coba lagi.")

#menampilkan daftar buku
def tampilkanBuku(): #mendefinisikan fungsi tampilkan buku
    daftarBuku = [[key, value["title"], value["author"], value["genre"], value["year"], 
        "Sedang Dipinjam" if key in peminjamanBuku else "Tersedia"] #jika buku ada dalam peminjamanBuku, maka status sedang dipinjam, dan sebaliknya
        for key, value in koleksiBuku.items()] #.items() mengembalikan fungsi key dan value (key : ID, value : title, author, genre, year)
    
    print(tabulate(daftarBuku, headers=["ID", "Judul", "Penulis", "Genre", "Tahun", "Ketersediaan"], tablefmt="grid")) #nampilin tabelnya

# mencari buku berdasarkan kategori tertentu
def cariBuuku(kategori, kataKunci): #mendefinisikan fungsi cari buku, kategori berisi mau cari buku berdasarkan apa, kata kunci untuk mempermudah pencarian buku
    hasilPencarian = [] #list kosong untuk menampung hasil pencarian
    for key, value in koleksiBuku.items(): #cek apakah setiap buku dalam koleksiBuku untuk menentukan apakah sesuai kriteria pencarian atau tidak
        ketersediaan = "Tersedia" if key in koleksiBuku else "Tidak Tersedia"
        #cek kecocokan berdasarkan katgori
        if (kategori == "judul" and kataKunci.lower() in value["title"].lower()) or \
           (kategori == "penulis" and kataKunci.lower() in value["author"].lower()) or \
           (kategori == "genre" and kataKunci.lower() in value["genre"].lower()) or \
           (kategori == "tahun" and str(value["year"]) == str(kataKunci)):
            hasilPencarian.append([key, value["title"], value["author"], value["genre"], value["year"], ketersediaan]) #menambahkan buku yang sesuai dengan pencarian ke list
    #menampilkan hasil pencarian
    if hasilPencarian: #kalau ada buku yang cocok, akan langsung ditampilkan
        print("\nHasil Pencarian:")
        headers = ["ID", "Judul", "Penulis", "Genre", "Tahun", "Status"]
        print(tabulate(hasilPencarian, headers=headers, tablefmt="grid"))
    else: #kalau hasil tidak cocok
        print("\nBuku tidak ditemukan berdasarkan kategori tersebut.")

#meminjam buku
def pinjamBuku(judulBuku, tanggalPinjam, namaPeminjam, sudahMelihatDaftar): #mendefinisikan fungsi pinjam buku
    #mencari buku dalam koleksi
    idBuku = None #menyimpan id buku yang cocok dengan judul buku
    for key, value in koleksiBuku.items(): 
        if value["title"].lower() == judulBuku.lower(): #membandingkan judul buku yang ingin dipinjam dengan judul buku dalam koleksi
            idBuku = key 
            break
    #jika buku tidak ditemukan, program akan mencetak error dan proses peminjaman berhenti
    if idBuku is None:
        print("\nJudul buku tidak ditemukan.")
        return
    #jika buku ada dalam daftar pinjam, buku tersebut sedang dipinjam
    if idBuku in peminjamanBuku:
        print(f"\nBuku '{judulBuku}' sedang dipinjam. Silahkan pinjam buku lain.")
        return
    #menampilkan status ketersediaan buku, dan meminta konfirmasi peminjaman buku
    print(f"\nBuku {judulBuku} {'sedang dipinjam' if idBuku in peminjamanBuku else 'tersedia'}")
    pilihan = input("Apakah Anda ingin melanjutkan meminjam buku ini? (ya/tidak): ").strip().lower() #strip() digunakan untuk menghapus spasi kosong di awal dan akhir string
    if pilihan != "ya": #jika tidak, peminjaman dibatalkan 
        print("\nPeminjaman dibatalkan.")
        return
    #menentukan batas pengembalian
    batasPengembalian = datetime.datetime.strptime(tanggalPinjam, "%Y-%m-%d") + datetime.timedelta(days=7) #mengubah string menjadi datetime, batas pengembalian 7 hari
    #data peminjam
    peminjamanBuku[idBuku] = {
        "title": koleksiBuku[idBuku]["title"], #judul buku yang dipinjam
        "author": koleksiBuku[idBuku]["author"], #penulis buku
        "genre": koleksiBuku[idBuku]["genre"], #genre buku
        "year": koleksiBuku[idBuku]["year"], #tahun terbit buku
        "tanggalPinjam": tanggalPinjam, #tanggal pinjam
        "batasPengembalian": batasPengembalian.strftime("%Y-%m-%d"), #batas pengembalian
        "peminjam": namaPeminjam
    }
    #menampilkan hasil peminjaman
    print(f"\nBuku '{judulBuku}' berhasil dipinjam. Harap dikembalikan sebelum {batasPengembalian.strftime('%Y-%m-%d')}.")

#mengembalikan buku
def kembalikanBuku(judulBuku, tanggalKembali, namaPengembali):
    #mencari buku dalam daftar pinjam
    idBuku = next((key for key, value in peminjamanBuku.items() if value["title"].lower() == judulBuku.lower()), None) #next() digunakan untu mencari ID berdasarkan judul
    #jika buku tidak ditemukan dalam peminjaman
    if idBuku is None:
        print("\nJudul buku tidak ditemukan dalam daftar peminjaman.")
        return
    #mencocokan nama peminjam dan nama pengembali
    dataPeminjaman = peminjamanBuku[idBuku]
    if dataPeminjaman["peminjam"].strip().lower() == namaPengembali.strip().lower(): #jika cocok
        print("Data ditemukan.")
    else: #jika tidak cocok
        print("Data tidak ditemukan.")
        return
    #menghapus buku dari daftar pinjam, buku sudah dikembalikan
    dataPeminjaman = peminjamanBuku.pop(idBuku)
    #mengembalikan buku ke dalam koleksi buku
    koleksiBuku[idBuku] = {
        "title": dataPeminjaman["title"],
        "author": dataPeminjaman["author"],
        "genre": dataPeminjaman["genre"],
        "year": dataPeminjaman["year"]
    }
    #menampilkan status pengembalian buku
    print(f"\nBuku telah dikembalikan oleh {namaPengembali}.")
    #menghitung denda keterlambatan
    tanggalPinjam = datetime.datetime.strptime(dataPeminjaman['tanggalPinjam'], "%Y-%m-%d")
    tanggalKembali = datetime.datetime.strptime(tanggalKembali, "%Y-%m-%d")
    terlambat = (tanggalKembali - tanggalPinjam).days - 7
    denda = max(0, terlambat * 10000) #denda keterlambatan 10.000 per hari
    #proses membayar denda
    if denda > 0: #kalo ada denda, bayar
        while True: #supaya proses pas uangnya kurang bisa keulang terus sampe uangnya pas
            print(f"Denda keterlambatan: Rp{denda}") #kasih tau dendanya berapa
            jumlahUang = int(input("Masukkan jumlah uang: ")) #masukin jumlah uangnya
            if jumlahUang == denda: #kalo jumlah uang pas sama dendanya
                print("Terima kasih telah membayar denda dan mengembalikan buku!")
                break
            elif jumlahUang < denda: #uang bayarnya kurang
                print("Uang yang Anda masukkan kurang. Silakan masukkan jumlah yang cukup.")
            else:
                kembalian = jumlahUang - denda #kalo uang bayarnya kelebihan, jadi dapet kembalian
                print(f"Terima kasih. Kembalian Anda: Rp{kembalian}.")
                break
    else: #kalo ngembaliin bukunya tepat waktu
        print("Tidak ada denda keterlambatan. Terima kasih telah mengembalikan buku tepat waktu")

#menambahkan buku ke daftar buku
def tambahBuku():
    #input data buku
    judul = input("Masukkan judul buku: ").title()
    penulis = input("Masukkan nama penulis: ").title()
    genre = input("Masukkan genre buku: ").capitalize()
    tahun = int(input("Masukkan tahun terbit: "))
    
    #cek buku sudah ada dalam koleksi
    for buku in koleksiBuku.values(): 
        if buku["title"].lower() == judul.lower(): #bandingin buku yang baru dimasukin sama yang udah ada
            print("\nBuku sudah ada dalam koleksi. Tidak dapat menambahkan duplikasi.") #kalau ada, proses berhenti, untuk menghindari duplikasi buku
            return
    #membuat ID unik untuk setiap buku yang baru dimasukkan
    kodeGenre = genre[:3].upper() #mengambil 3 huruf pertama dalam genre dan diubah menjadi huruf besar semua
    existingIDs = [int(str(idBuku)[3:]) for idBuku in koleksiBuku.keys() if str(idBuku).startswith(kodeGenre)] #buat menentukan id buku yang baru ditambahkan dari koleksi buku
    #menentukan nomor buku untuk id buku yang baru
    newNumber = max(existingIDs, default=0) + 1 #ngambil angka yang terbesar di existingID terus ditambah 1, kalo genrenya baru berarti dimulai dari 1
    newID = f"{kodeGenre}{newNumber:03d}" #bikin ID baru, 3 huruf awal genre, nomor buku 3 digit
    #masukkin ke daftar buku
    koleksiBuku[newID] = {"title": judul, "author": penulis, "genre": genre, "year": tahun}
    print(f"\nBuku '{judul}' berhasil ditambahkan dengan ID {newID}.")
    tampilkanBuku()

#menghapus buku dari daftar buku
def hapusBuku():
    #masukkan ID buku yang ingin dihapus
    idBuku = input("Masukkan ID buku yang ingin dihapus: ")
    #cek buku ada dalam daftar koleksi
    if idBuku in koleksiBuku:
        buku = koleksiBuku[idBuku]
        #menampilin detail buku sebelum dihapus
        print("\nDetail Buku:")
        print(f"Judul: {buku['title']}")
        print(f"Penulis: {buku['author']}")
        print(f"Tahun Terbit: {buku['year']}")
        #konfirmasi penghapusan
        konfirmasi = input("\nApakah Anda yakin ingin menghapus buku ini? (ya/tidak): ").lower() #beneran mau dihapus ga?
        if konfirmasi == "ya": #kalo ya, buku dihapus
            koleksiBuku.pop(idBuku)
            print(f"\nBuku '{buku['title']}' berhasil dihapus dari perpustakaan.")  
        else: #kalo enggak, buku ga jadi dihapus
            print("\nPenghapusan dibatalkan.")
    else: #kalo buku gaada di daftar koleksi, balik ke menu awal
        print("\nID buku tidak ditemukan. Kembali ke menu awal.")

#menampilkan menu untuk admin
def menuAdmin():
    sudahMelihatDaftar = False
    while True:
        print("\nApa yang ingin anda lakukan?")
        print("1. Lihat daftar buku")
        print("2. Peminjaman buku")
        print("3. Pengembalian buku")
        print("4. Menambahkan buku")
        print("5. Menghapus buku")
        print("6. Kembali ke menu login")
        print("7. Logout")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            konfirmasi = konfirmasi = input("Apakah Anda ingin menampilkan semua buku? (ya/tidak): ").strip().lower()
            if konfirmasi == "ya":
                tampilkanBuku
            else:
                kategori = input("Cari berdasarkan (judul/penulis/genre/tahun): ")
                nilai = input("Masukkan kata kunci pencarian: ")
                cariBuuku(kategori, nilai)
        elif pilihan == "2":
            tampilkanBuku()
            judulBuku = input("Masukkan judul buku: ").title()
            namaPeminjam = input("Masukkan nama peminjam: ").title()
            tanggalPinjam = input("Masukkan tanggal peminjaman (YYYY-MM-DD): ")
            pinjamBuku(judulBuku, tanggalPinjam, namaPeminjam, sudahMelihatDaftar)
            sudahMelihatDaftar = False
        elif pilihan == "3":
            judulBuku = input("Masukkan judul buku: ").title()
            namaPengembali = input("Masukkan nama pengembali: ").title()
            tanggalPinjam = input("Masukkan tanggal peminjaman (YYYY-MM-DD): ")
            tanggalKembali = input("Masukkan tanggal pengembalian (YYYY-MM-DD): ")
            kembalikanBuku(judulBuku, tanggalKembali, namaPengembali)
        elif pilihan == "4":
            tambahBuku()
        elif pilihan == "5":
            hapusBuku()
        elif pilihan == "6":
            login()
        elif pilihan == "7":
            logout()
            exit()
        else:
            print("Pilihan tidak valid, coba lagi.")

#menampilkan menu peminjam
def menuPeminjam():
    while True:
        print("\nApa yang ingin anda lakukan?")
        print("1. Lihat daftar buku")
        print("2. Cari buku yang diinginkan")
        print("3. Kembali ke menu login")
        print("4. Logout")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            tampilkanBuku()
        elif pilihan == "2":
            kategori = input("Cari berdasarkan (judul/penulis/genre/tahun): ")
            nilai = input("Masukkan kata kunci pencarian: ")
            cariBuuku(kategori, nilai)
        elif pilihan == "3":
            login()
        elif pilihan == "4":
            logout()
            exit()
            
        else:
            print("Pilihan tidak valid, coba lagi.")

#fungsi logout
def logout():
    while True:
        print("\nApakah anda benar ingin keluar?") #konfirmasi keluar
        pilihan = input("ya atau tidak: ").strip().lower()
        if pilihan == "ya":
            print("Terima kasih, sampai jumpa!")
            exit()  #keluar dari program
        elif pilihan == "tidak":
            return  #kembali ke menu sebelumnya
        else:
            print("Pilihan tidak valid, coba lagi.")

#definisiin fungsi user role
def userRole():
    while True:
        userRole = login()
        if userRole == "admin":
            menuAdmin()
        elif userRole == "peminjam":
            menuPeminjam()

#panggil user role supaya keseluruhan kode jalan
userRole()