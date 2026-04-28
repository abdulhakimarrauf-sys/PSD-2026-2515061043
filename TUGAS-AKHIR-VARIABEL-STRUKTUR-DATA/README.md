Program ini berfungsi sebagai sistem manajemen parkir kendaraan mahasiswa yang mampu mencatat data NPM dan jenis kendaraan secara otomatis ke dalam slot yang tersedia, serta menampilkannya dalam format tabel dua kolom (Halaman A dan Halaman B). Struktur data yang diterapkan adalah Array 2 Dimensi (List of Lists) secara statis dengan ukuran tetap (6 slot), di mana algoritma yang digunakan mencakup Linear Search untuk menemukan slot kosong pertama ("Kosong") saat proses pengisian data, serta teknik Formatting String untuk memetakan indeks linier menjadi tampilan tabel dua kolom yang simetris di layar.


<img width="910" height="1300" alt="Tugas Akhir Judul 1" src="https://github.com/user-attachments/assets/8b1f723f-d2bd-498a-ab30-906418d5b457" />


1.	Mendefinisikan sebuah fungsi bernama menu agar bisa dipanggil berulang kali.
2.	Menampilkan judul program.
3.	Menampilkan teks opsi nomor 1.
4.	Menampilkan teks opsi nomor 2.
5.	Menampilkan teks opsi nomor 3.
6.	Menampilkan teks opsi nomor 4 untuk menghentikan program.
7.	
8.	Fungsi utama tempat seluruh logika program berjalan.
9.	
10.	Membuat List 2D berisi 6 elemen. Setiap elemen adalah list ["Kosong", "Kosong"] yang merepresentasikan NPM dan jenis kendaraan di tiap slot parkir.
11.	
12.	Perulangan tak terbatas agar program terus berjalan kembali ke menu setelah sebuah aksi selesai, kecuali jika dihentikan secara paksa atau melalui menu keluar.
13.	Memanggil fungsi menu yang telah didefinisikan sebelumnya.
14.	Mengambil input dari pengguna untuk menentukan aksi selanjutnya.
15.	
16.	Memeriksa apakah pengguna memilih menu nomor 1.
17.	Mencetak teks judul tabel.
18.	Mencetak header tabel. Kode :<25 berarti teks rata kiri dengan lebar kolom 25 karakter agar tampilan kolom A dan B sejajar.
19.	Sama seperti baris sebelumnya, ini mencetak sub-judul kolom tepat di bawah "HALAMAN A" dan "HALAMAN B" dengan jarak yang sama (25 karakter) agar tetap lurus.
20.	Melakukan perulangan sebanyak 3 kali (untuk baris 1, 2, dan 3).
21.	Mengambil data untuk Halaman A (indeks 0-2) dan memformatnya dengan nomor urut.
22.	Mengambil data untuk Halaman B (indeks 3-5) dan memformatnya dengan nomor urut 4-6.
23.	Mencetak data A dan B dalam satu baris yang sama secara berdampingan.
24.	
25.	Memeriksa apakah pengguna memilih menu nomor 2.
26.	Inisialisasi variabel penanda (flag) untuk mengecek apakah ada slot yang kosong.
27.	Memeriksa setiap slot dari urutan 1 sampai 6.
28.	Mengecek apakah slot tersebut masih kosong (ditandai dengan NPM "Kosong").
29.	Memberitahu pengguna slot mana yang sedang diisi.
30.	Menyimpan input NPM ke kolom pertama indeks tersebut.
31.	Menyimpan input jenis kendaraan ke kolom kedua.
32.	Hanya pesan konfirmasi bahwa proses berhasil.
33.	Mengubah penanda menjadi True karena pengisian berhasil.
34.	Keluar dari perulangan for agar hanya satu slot yang terisi dalam sekali aksi.
35.	Jika setelah dicek 6 kali tidak ada yang kosong!.
36.	Muncul pesan "semua slot parkir sudah penuh!".
37.	 
38.	Memeriksa apakah pengguna memilih menu nomor 3.
39.	Menangani error jika pengguna memasukkan karakter non-angka saat diminta nomor urut.
40.	Mengubah input angka menjadi indeks list (angka 1 menjadi indeks 0).
41.	Program memastikan bahwa nomor yang dimasukkan berada dalam jangkauan yang benar (tidak kurang dari 0 dan tidak lebih dari 5). Jika Anda memasukkan angka 10, program akan melompat ke bagian else.
42.	Menentukan nama halaman berdasarkan nomor slot (1-3 masuk A, 4-6 masuk B).
43.	Menampilkan judul yang memberitahu di halaman mana slot tersebut berada (A atau B).
44.	Ini adalah hasil akhirnya. {no+1}: Mengembalikan angka ke format manusia (0 jadi 1). {data[no][0]}: Mengambil isi NPM di slot tersebut. {data[no][1]}: Mengambil jenis kendaraan di slot tersebut.
45.	Jika pengguna
46.	Jika pengguna memasukkan angka di luar 1-6 (misalnya 99), pesan ini akan muncul.
47.	Ini adalah pasangan dari try di atas. 
48.	Jika saat diminta nomor urut Anda malah mengetik "Sepuluh" (huruf), maka bagian ini akan menangkap kesalahan tersebut dan memberikan peringatan yang sopan alih-alih program berhenti mendadak.
49.	 
50.	Memeriksa apakah pengguna memilih menu nomor 4.
51.	Memberikan umpan balik visual kepada pengguna bahwa permintaan untuk menutup program telah diterima dan diproses. Ini penting untuk pengalaman pengguna (user experience) agar mereka tahu program tidak berhenti karena error.
52.	Menghentikan perulangan while True untuk menutup program.
53.	
54.	Ini adalah baris pengaman standar di Python. Baris ini memastikan bahwa fungsi di dalamnya hanya akan berjalan jika file ini dijalankan secara langsung (misalnya dengan mengetik python nama_file.py). Jika file ini di-import sebagai modul oleh file lain, fungsi main() tidak akan berjalan secara otomatis.
55.	Baris ini adalah perintah untuk memanggil fungsi main() yang berisi seluruh logika program parkir. Tanpa pemanggilan ini, program hanya akan mendefinisikan fungsi-fungsi tanpa pernah benar-benar menjalankannya.

Output :
<img width="242" height="98" alt="Screenshot 2026-04-28 233901" src="https://github.com/user-attachments/assets/ac62f16b-8bcf-4630-b044-c757dddc752b" />

Menu 1 Sebelum di inputkan Nilai
<img width="265" height="187" alt="Screenshot 2026-04-28 233919" src="https://github.com/user-attachments/assets/23869b3c-ae9b-4b91-8737-9157566b5f02" />

Setelah di inputkan Nilai
<img width="302" height="191" alt="Screenshot 2026-04-28 234121" src="https://github.com/user-attachments/assets/be9204e4-ea69-4df0-a4a7-ed88bd6581f0" />

Menu 2
<img width="295" height="593" alt="Screenshot 2026-04-28 234313" src="https://github.com/user-attachments/assets/5dd4efdb-12ef-436c-a73b-9b6493cb8dad" />
<img width="281" height="322" alt="Screenshot 2026-04-28 234355" src="https://github.com/user-attachments/assets/a9ff685c-a3de-436d-b777-12b5d1d97b74" />

Menu 3
<img width="382" height="156" alt="Screenshot 2026-04-28 234446" src="https://github.com/user-attachments/assets/30ffe2c5-03fe-409f-8726-44944f1891a2" />

Link : https://youtu.be/asJau8u3QFE?si=h0sPt4cr18EYx4D_
