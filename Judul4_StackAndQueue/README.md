Sistem Parkiran Kendaraan pada Kapal Feri


Program Sistem Parkiran Kendaraan pada Kapal Feri ini berfungsi untuk mengelola simulasi penataan dan keluar masuknya kendaraan di dalam dek kapal feri secara digital, di mana setiap kendaraan yang masuk akan dialokasikan ruangnya berdasarkan ukuran slot yang dibutuhkan serta divalidasi agar tidak memiliki nama ganda demi memastikan keunikan data. Algoritma struktur data yang diterapkan pada program ini adalah Stack atau tumpukan berbasis media penyimpanan Array list statis, yang mengimplementasikan prinsip LIFO (Last In First Out) di mana kendaraan yang terakhir kali masuk diposisi paling atas diposisikan sebagai kendaraan yang wajib dikeluarkan pertama kali saat kapal bersandar demi menghindari hambatan fisik di dalam dek kapal.


Source Code:
<img width="1664" height="3752" alt="ta judul 4" src="https://github.com/user-attachments/assets/99f209e7-de97-478e-8db7-94a0b0cd8142" />


Penjelasan Source Code:
1.	Mendeklarasikan sebuah kelas bernama StackArray.
2.	Konstruktor objek yang otomatis berjalan saat objek stack dibuat. Nilai default kapasitas maksimal dek kapal diatur sebanyak 50 slot jika tidak ditentukan lain.
3.	Menyimpan batas maksimal kapasitas slot ke dalam variabel objek self.MAX.
4.	Membuat sebuah list python berukuran sesuai self.MAX yang diisi dengan nilai kosong (None) sebagai representasi fisik dari slot-slot parkiran di dalam kapal.
5.	Mengatur variabel penunjuk posisi teratas tumpukan (top_idx) bernilai -1. Angka -1 menandakan bahwa saat ini belum ada satu pun kendaraan yang parkir stack dalam kondisi kosong.
6.	 
7.	Pengecekan kondisi kosong (is_empty)
8.	Melakukan evaluasi logika. Jika top_idx bernilai -1, fungsi akan mengembalikan nilai True artinya parkiran kosong. Jika tidak, akan mengembalikan nilai False.
9.	 
10.	Fungsi untuk mengecek apakah ruang dek masih muat untuk menampung kendaraan baru dengan ukuran tertentu (size).
11.	Menghitung secara matematis: jika posisi top_idx saat ini ditambah dengan ukuran kendaraan baru ternyata nilainya sama dengan atau melebihi batas indeks maksimum (self.MAX), fungsi akan mengembalikan nilai True artinya ruang tidak cukup/penuh.
12.	 
13.	Fungsi untuk memasukkan kendaraan bernama x yang membutuhkan slot sebanyak size.
14.	Melakukan perulangan looping dari indeks 0 hingga posisi kendaraan teratas (top_idx) untuk memeriksa kendaraan yang sudah terparkir.
15.	Memeriksa apakah nama kendaraan yang ingin masuk (x) ternyata sama dengan nama kendaraan yang sudah ada di indeks ke-i.
16.	Jika nama kendaraan duplikat ditemukan, cetak pesan peringatan.
17.	Untuk menghentikan paksa fungsi push agar data duplikat tidak masuk.
18.	Memanggil fungsi is_full untuk memeriksa sisa ruang dek kapal.
19.	Jika ruang tidak cukup, program mencetak pesan "Stack penuh".
20.	Cetak informasi sisa slot yang tersedia.
21.	Membatalkan proses.
22.	Jika semua validasi lolos, lakukan perulangan sebanyak nilai size ukuran kendaraan.
23.	Menaikkan pointer indeks teratas sebanyak 1 posisi ke atas.
24.	Mengisi slot pada indeks top_idx yang baru tersebut dengan nama kendaraan x.
25.	Mencetak konfirmasi di layar bahwa kendaraan berhasil masuk ke parkiran sesuai alokasi slotnya.
26.	 
27.	Fungsi mengeluarkan kendaraan (pop).
28.	Memeriksa apakah kapal dalam kondisi kosong tanpa kendaraan. 
29.	Cetak "Stack kosong".
30.	Hentikan fungsi.
31.	Jika ada kendaraan, program akan mengambil nama kendaraan yang berada di posisi paling atas (self.st[self.top_idx]) dan mencetak pesan keberhasilan keluar.
32.	Menurunkan indeks penunjuk top_idx sebanyak 1 angka ke bawah. Secara tidak langsung, elemen teratas tersebut dianggap terhapus dari sistem karena penunjuk tumpukan telah bergeser ke elemen di bawahnya.
33.	 
34.	Fungsi mengintip kendaraan teratas (peek).
35.	Melakukan validasi kondisi kosong.
36.	Cetak Kosong.
37.	Proses dihentikan.
38.	Menampilkan nama kendaraan yang berada di posisi paling atas dek kapal saat ini posisi yang paling dekat dengan pintu keluar tanpa menghapus atau mengubah data tersebut.
39.	 
40.	Fungsi menampilkan isi parkiran (display).
41.	Untuk mengecek status keterisian dek kapal.
42.	Mencetak teks "Stack kosong".
43.	Menghentikan fungsi.
44.	Jika parkiran tidak kosong, program membuat variabel indeks pembantu bernama i dan mengisinya dengan posisi indeks teratas (self.top_idx). Hal ini dilakukan agar kita bisa menelusuri isi parkiran mundur ke bawah dari kendaraan yang paling dekat dengan pintu keluar.
45.	Memulai perulangan utama looping yang akan terus berjalan selama nilai indeks i masih valid atau belum melewati batas dasar stack yaitu indeks 0.
46.	Di setiap awal perulangan, program mengambil nama kendaraan yang berada di indeks i saat itu untuk disimpan ke variabel nama_kendaraan.
47.	Variabel ukuran diatur ulang menjadi 0 untuk mulai menghitung jumlah slot kendaraan tersebut.
48.	Memulai perulangan bersandar nested loop untuk menghitung panjang blok kendaraan yang sama. 
49.	Selama indeks i belum habis (>= 0) dan isi array pada self.st[i] masih sama dengan nama kendaraan yang sedang diperiksa, maka nilai ukuran akan ditambah 1.
50.	Indeks i dikurangi 1 melangkah mundur ke slot di bawahnya.
51.	Setelah keluar dari perulangan bersarang (artinya program sudah menemukan batas akhir dari kendaraan tersebut), program mencetak ringkasan datanya ke layar komputer contoh output: Truk ukuran: 5 slot. 
52.	 
53.	 
54.	Fungsi ini mengatur alur jalannya menu program interaktif berbasis teks CLI yang menjembatani komunikasi antara sistem dengan pengguna.
55.	Sebuah objek stack baru bernama stack dari kelas StackArray().
56.	Untuk menampung angka menu.
57.	Memulai perulangan menu interaktif. Program akan terus menampilkan pilihan menu dan meminta input selama pengguna tidak memilih menu nomor 5 Hitung Total Kendaraan/Keluar.
58.	Serangkaian perintah untuk mencetak teks visual menu ke layar terminal pengguna di setiap awal siklus perulangan.
59.	Serangkaian perintah untuk mencetak teks visual menu ke layar terminal pengguna di setiap awal siklus perulangan.
60.	Serangkaian perintah untuk mencetak teks visual menu ke layar terminal pengguna di setiap awal siklus perulangan.
61.	Serangkaian perintah untuk mencetak teks visual menu ke layar terminal pengguna di setiap awal siklus perulangan.
62.	Serangkaian perintah untuk mencetak teks visual menu ke layar terminal pengguna di setiap awal siklus perulangan.
63.	Serangkaian perintah untuk mencetak teks visual menu ke layar terminal pengguna di setiap awal siklus perulangan.
64.	Serangkaian perintah untuk mencetak teks visual menu ke layar terminal pengguna di setiap awal siklus perulangan.
65.	Mencoba
66.	Mengambil input ketikan dari pengguna dan langsung mengubahnya menjadi tipe data bilangan bulat (int).
67.	Jika pengguna salah mengetikkan input berupa huruf atau simbol, blok except ValueError akan menangkap error tersebut agar program tidak mendadak mati crash.
68.	Memunculkan pesan "Input tidak valid!".
69.	Melompati sisa kode ke bawah untuk mengulang menu dari atas menggunakan continue.
70.	Jika pengguna memilih menu 1, program masuk ke logika penambahan kendaraan Push.
71.	Percobaan
72.	Sistem meminta input nama kendaraan (val).
73.	Sistem meminta input jumlah kapasitas slot yang dibutuhkan (size).
74.	Jika input ukuran yang dimasukkan berupa angka valid, sistem memanggil fungsi stack.push(val, size).
75.	Jika salah memasukkan format data.
76.	Mencetak "Input tidak valid!".
77.	Jika pengguna memilih menu 2.
78.	Memanggil metode stack.pop() untuk mengeluarkan satu kendaraan teratas yang posisinya paling dekat dengan pintu keluar kapal feri.
79.	Jika pengguna memilih menu 3.
80.	Memanggil fungsi stack.peek() untuk mengintip kendaraan apa yang sedang berada di posisi paling atas tumpukan tanpa mengeluarkannya dari parkiran.
81.	Jika pengguna memilih menu 4.
82.	Memanggil fungsi stack.display() yang alur per barisnya telah dijelaskan pada bagian I di atas untuk menampilkan seluruh isi kendaraan di dalam dek kapal.
83.	Jika pengguna memilih menu 5.
84.	Program menghitung jumlah total slot memori yang terisi dengan cara menambahkan nilai 1 pada variabel penunjuk posisi teratas (stack.top_idx + 1).
85.	Nilai ini disimpan ke variabel count lalu dicetak ke layar. Setelah baris ini selesai dieksekusi, kondisi while pilih != 5 di atas akan bernilai False, sehingga perulangan menu otomatis berhenti.
86.	Jika pengguna memasukkan angka menu di luar rentang yang tersedia (misalnya angka 7 atau 9), program akan langsung masuk ke blok else.
87.	Menampilkan pesan "Pilihan tidak valid!".
88.	 
89.	 
90.	Baris ini melakukan pengecekan kondisi lingkungan environment.
91.	Jika file skrip Python ini dijalankan secara langsung oleh pengguna bukan dipanggil/import oleh file lain, maka Python diperintahkan untuk langsung memicu dan menjalankan fungsi main().


Output Source Code:
<img width="261" height="733" alt="Screenshot 2026-05-19 232723" src="https://github.com/user-attachments/assets/6187c079-591a-44ab-95bb-53ebad958fe7" />

<img width="428" height="800" alt="Screenshot 2026-05-19 232750" src="https://github.com/user-attachments/assets/b2bbe41a-aacb-4584-9486-542bc689937e" />


Penjelasan Output Source Code:
Output dari program Sistem Parkiran Kendaraan pada Kapal Feri ini menampilkan menu interaktif berbasis teks Command Line Interface yang secara dinamis merepresentasikan kondisi penataan memori di dalam dek kapal feri. Ketika pengguna memilih opsi untuk menampilkan isi parkiran, sistem memanfaatkan algoritma looping mundur untuk membaca tumpukan dari posisi teratas (top_idx) hingga ke dasar array, lalu mengelompokkan elemen indeks yang berturut-turut memiliki nama data yang identik agar hanya tercetak satu kali baris ringkasan di layar beserta informasi total slot kapasitas yang dihabiskannya. Sementara itu, opsi penghitungan total kendaraan memberikan informasi langsung mengenai jumlah keseluruhan slot indeks memori yang saat ini sedang terpakai di dalam array secara akurat berdasarkan kalkulasi posisi penunjuk stack aktif (top_idx + 1).

LInk YouTube : https://youtu.be/fGvj37EeL20?si=EzOmZTD82VJyysoR
