Sistem Data Parkiran Motor Kampus

Program Sistem Data Parkiran Motor Kampus ini berfungsi sebagai sistem manajemen digital untuk mendata, menyimpan, mencari, dan menghapus informasi pelat nomor kendaraan berdasarkan jenis atau merek motor (key) yang parkir di area kampus secara instan dan efisien. Di dalam program ini, struktur data yang diterapkan adalah Hash Map Open Addressing dengan menggunakan metode Linear Probing sebagai algoritma penanganan benturan (collision handling). Melalui metode ini, ketika fungsi hash menghasilkan indeks memori yang sudah terisi oleh kendaraan lain, sistem secara otomatis akan melakukan penelusuran sekuensial maju satu demi satu slot ke depan untuk menemukan slot kosong terdekat berikutnya guna menempatkan data motor baru tersebut.

Source Code :
<img width="1648" height="4474" alt="tugas akhir" src="https://github.com/user-attachments/assets/0b1afcb7-d77c-42a3-bef3-4bdf205734df" />

Penjelasan Source Code :
1.	Rancangan atau blueprint kondisi pada slot.
2.	Slot kosong murni, belum pernah ditempati kendaraan sejak program berjalan.
3.	Slot sedang terisi aktif oleh data motor merek dan pelat nomor.
4.	Slot bernilai bekas hapus motor sudah keluar/pulang. Status ini menjaga agar rantai pencarian Linear Probing tidak terputus.
5.	 
6.	 
7.	Blueprint dalam menentukan pasangan.
8.	Konstruktor dalam pemanggilan objek.
9.	Menampung merek/jenis motor.
10.	Menampung nomor polisi / pelat kendaraan.
11.	Saat lahan parkir pertama dibuat, statusnya diatur sebagai EMPTY.
12.	 
13.	 
14.	Blueprint metode penanganan collision pada elemen yang disimpan di array.
15.	Inisialisasi ukuran awal pada array.
16.	Menentukan jumlah total slot parkir yang tersedia.
17.	Membuat list bernama 'table' berisi 10 objek lahan parkir kosong.
18.	 
19.	Definisi fungsi hash pada Hash Map.
20.	Mengonversi string merek motor menjadi angka integer unik acak bawaan Python.
21.	Angka integer tersebut dimodulus dengan ukuran tabel untuk mendapatkan indeks valid antara posisi 0 sampai 9.
22.	 
23.	Fungsi ini berjalan saat ada motor baru yang masuk ke area parkir.
24.	Hitung indeks parkir ideal untuk motor berdasarkan mereknya
25.	Wadah sementara untuk mencatat jika ada slot bekas motor keluar (DELETED).
26.	Perulangan Linear Probing jika tempat parkir ideal sudah ditempati motor lain.
27.	Jika tabrakan, geser maju 1 slot ke depan secara sirkular berputar ke 0 jika mentok di 9.
28.	Jika status slot ke-i adalah OCCUPIED.
29.	Merek motor yang ada di slot tersebut sama persis dengan key yang ingin dimasukkan.
30.	Maka sistem melakukan overwrite memperbarui nomor pelat/value motor tersebut.
31.	Langsung keluar dari fungsi dengan mengembalikan nilai True.
32.	Jika sistem menemukan slot yang statusnya DELETED bekas motor yang sudah keluar.
33.	Sistem akan memeriksa apakah variabel first_deleted masih bernilai -1.
34.	Jika iya, simpan indeks slot i tersebut ke dalam first_deleted.
35.	Bagian else ini berjalan jika slot ke-i berstatus EMPTY.
36.	Sebelum menempati slot kosong tersebut, sistem mengecek: jika selama perjalanan tadi kita sempat melewati slot berstatus DELETED.
37.	Maka alihkan target indeks i ke lokasi first_deleted agar slot bekas pakai tersebut terisi kembali terlebih dahulu.
38.	Simpan merek motor ke key.
39.	Simpan nomor pelat ke value.
40.	Ubah status slot menjadi OCCUPIED.
41.	Kembalikan True.
42.	Baris ini berada di luar perulangan for.
43.	Jika perulangan selesai artinya seluruh tabel sudah diperiksa maju satu per satu dan tidak menemukan slot EMPTY.
44.	Sistem melakukan pengecekan terakhir.
45.	Jika ada slot DELETED yang sempat disimpan.
46.	Data motor diparkir di slot tersebut dan mengembalikan True.
47.	Jika tidak ada juga tabel benar-benar penuh total, fungsi mengembalikan nilai False.
48.	 
49.	Fungsi ini digunakan untuk mencari informasi kendaraan di parkiran berdasarkan merek motornya.
50.	Mengubah teks merek motor yang dicari menjadi indeks angka awal menggunakan fungsi hash untuk mempercepat pencarian lokasi.
51.	Melakukan penelusuran maju satu demi satu slot (Linear Probing) secara sirkular berputar kembali ke indeks 0 jika sudah mencapai batas maksimal ukuran tabel.
52.	Mengantisipasi jika motor tersebut bergeser posisinya saat dimasukkan akibat fenomena tabrakan data (collision).
53.	Jika di tengah penelusuran sistem menemukan slot yang berstatus EMPTY.
54.	Pencarian langsung dihentikan dan mengembalikan None.
55.	Jika slot ke-i berstatus OCCUPIED dan merek motor di slot tersebut cocok dengan key yang dicari, fungsi sukses menemukan target.
56.	Mengembalikan seluruh objek data lahan parkir (self.table[i]).
57.	Jika perulangan selesai tanpa kecocokan, fungsi mengembalikan None.
58.	 
59.	Fungsi ini mensimulasikan proses ketika ada motor yang keluar dari area parkir kampus.
60.	Memanggil fungsi search untuk menemukan posisi motor terlebih dahulu.
61.	Jika hasil pencarian bernilai None motor tidak terdaftar di parkiran.
62.	Fungsi langsung mengembalikan nilai False.
63.	Jika motor ditemukan, ubah status slot tempat motor tersebut berada menjadi DELETED. Status ini menandakan slot sekarang kosong, tetapi pernah diisi, sehingga rantai pencarian Linear Probing motor lain di depannya tidak akan terputus.
64.	Fungsi berakhir dengan mengembalikan True.
65.	 
66.	Fungsi menampilkan deenah parkir.
67.	Mencetak judul menu ke terminal.
68.	Lalu melakukan perulangan indeks dari 0 sampai batas kapasitas tabel.
69.	Mencetak nomor urut slot parkir secara horizontal.
70.	Melakukan seleksi kondisi kondisi slot.
71.	Jika kosong murni cetak "EMPTY".
72.	Jika bekas pakai.
73.	Cetak "DELETED".
74.	Jika terisi aktif.
75.	Cetak data kendaraan dalam format (Merek, Nomor Pelat).
76.	 
77.	 
78.	Bagian ini mensimulasikan skenario nyata operasional lahan parkir kampus.
79.	Membuat satu objek instansiasi baru bernama motor yang mewakili area parkiran kampus berkapasitas 10 slot.
80.	Memasukkan data motor.
81.	Memasukkan data motor.
82.	Memasukkan data motor.
83.	Memasukkan data motor.
84.	Memasukkan data motor.
85.	Memasukkan data motor.
86.	Memvisualisasikan posisi slot parkir dari keenam motor tersebut ke layar terminal.
87.	 
88.	Menguji fungsi pencarian untuk mencari keberadaan motor "Mio".
89.	Karena motor "Mio" sudah dimasukkan sebelumnya, kondisi if hasil is not None akan terpenuhi.
90.	Program akan mencetak teks bahwa motor ditemukan beserta nomor pelatnya (BE 1234 AB).
91.	Kondisi lain.
92.	Motor "Mio" belum dimasukkan sebelumnya, kondisi if hasil is not None tidak terpenuhi.
93.	 
94.	Mensimulasikan motor "Mio" keluar dari parkiran dengan memanggil remove_key("Mio").
95.	Slot parkir yang tadinya ditempati oleh Mio kini berubah status menjadi DELETED.
96.	Denah parkiran dicetak ulang menggunakan display().
97.	 
98.	Program memanggil metode .search() pada objek motor dengan mengirimkan kata kunci pencarian "Ninja". Hasil pengembalian dari metode ini bisa berupa objek node/entry data atau None jika tidak ditemukan disimpan ke dalam variabel hasil.
99.	Melakukan pengecekan kondisi. Jika variabel hasil tidak kosong, artinya data motor dengan nama "Ninja" berhasil ditemukan di dalam struktur data.
100.	Baris ini hanya dieksekusi jika kondisi if bernilai True. Program akan mencetak pesan konfirmasi bahwa motor "Ninja" ditemukan, sekaligus menampilkan nilai propertinya seperti plat nomor atau data terkait lainnya melalui atribut hasil.value.
101.	Blok alternatif yang akan dieksekusi apabila kondisi pada if bernilai False artinya variabel hasil bernilai None.
102.	Program mencetak pesan informasi ke layar terminal bahwa motor dengan nama "Ninja" tidak ada di dalam sistem.
103.	 
104.	Program memanggil metode .insert() pada objek motor untuk menambahkan data kendaraan baru ke dalam struktur data, dengan nama kunci "Mio" dan nilai berupa plat nomor "BE 4321 AB".
105.	Mencetak teks judul/keterangan sementara ke layar untuk memberikan informasi visual sebelum menampilkan pembaruan isi data.
106.	Program memanggil metode .display() untuk mencetak dan menampilkan seluruh isi struktur data kendaraan terupdate ke layar terminal agar pengguna dapat melihat posisi motor "Mio" yang baru saja dimasukkan.
107.	 
108.	 
109.	Kondisi khusus untuk memeriksa lingkungan eksekusi Python. 
110.	Jika file skrip ini dijalankan secara langsung bukan diimpor oleh skrip lain, maka sistem diperintahkan untuk otomatis memicu dan menjalankan fungsi utama bernama main().

Output Source Code :
<img width="658" height="806" alt="Screenshot 2026-06-09 234443" src="https://github.com/user-attachments/assets/be4b5b76-e396-431c-be11-46fa3843d78b" />
Penjelasan Output Source Code : 
Output program menampilkan visualisasi alur kerja Sistem Data Parkiran Motor Kampus berbasis Hash Map Open Addressing yang berhasil mengelola penempatan slot parkir, pencarian data, serta penghapusan data kendaraan secara dinamis. Pada awalnya, denah menampilkan kondisi terisi aktif (OCCUPIED) oleh 6 unit motor pada slot tertentu serta menyisakan slot kosong (EMPTY). Saat motor "Mio" dipanggil keluar dari parkiran melalui fungsi remove_key, slot nomor 4 yang sebelumnya ditempati oleh motor tersebut secara cerdas diubah statusnya menjadi DELETED, sehingga rantai pelacakan posisi Linear Probing motor lain di sekitarnya (seperti motor "Ninja") tidak terputus dan tetap dapat ditemukan dengan sukses. Terakhir, ketika motor "Mio" masuk kembali ke parkiran kampus dengan nomor pelat baru (BE 4321 AB), algoritma program langsung mengoptimalkan ruang memori dengan menempati kembali slot berstatus DELETED tersebut menjadi terisi aktif kembali.

LInk YouTube : https://youtu.be/bbKRGU9GIW0
