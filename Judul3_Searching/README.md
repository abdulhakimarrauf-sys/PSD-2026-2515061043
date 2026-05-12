Pencari Huruf Pada Kumpulan Data Dengan Sequential Searching


Program ini berfungsi untuk memproses pencarian karakter spesifik di dalam sebuah larik data huruf secara sistematis, di mana sistem akan memvalidasi input pengguna dan mengembalikan seluruh posisi indeks serta jumlah total kemunculan huruf tersebut. Algoritma struktur data yang diterapkan adalah Sequential Searching (atau Linear Search), yang bekerja dengan prinsip menelusuri setiap elemen di dalam struktur data array satu per satu dari awal hingga akhir tanpa mensyaratkan data dalam kondisi terurut.


Source Code:
<img width="1648" height="1356" alt="Tugas Akhir Judul 3" src="https://github.com/user-attachments/assets/b6262c28-7844-4428-9b77-207f955fefd6" />


Penjelasan Source Code:
1.	Fungsi melakukan pencarian seluruh posisi huruf yang cocok di dalam array.
2.	Membuat list kosong untuk menyimpan posisi (indeks) di mana huruf ditemukan. Jika ada lebih dari satu, semua posisi akan tersimpan di sini.
3.	Inisialisasi variabel penghitung (iterator) mulai dari nol sebagai indeks awal array.
4.	Mengubah input pencarian menjadi huruf kapital. Hal ini memastikan jika pengguna memasukkan 'a', program tetap bisa mencocokkannya dengan 'A' di dalam data.
5.	Melakukan perulangan selama nilai i masih lebih kecil dari jumlah total elemen dalam data. Ini memastikan setiap elemen diperiksa satu per satu.
6.	Memeriksa apakah elemen pada indeks saat ini sama dengan huruf yang dicari.
7.	Jika cocok, simpan nomor indeks tersebut ke dalam list indices.
8.	Menaikkan nilai i agar perulangan berlanjut ke elemen berikutnya.
9.	Mengirimkan daftar indeks yang ditemukan kembali ke bagian pemanggil fungsi.
10.	
11.	Fungsi mengatur alur interaksi dengan pengguna dan eksekusi program.
12.	Mendefinisikan kumpulan data huruf yang akan menjadi objek pencarian.
13.	Hasil keluaran kumpulan data huruf yang akan menjadi objek pencarian.
14.	Membuat perulangan tanpa henti untuk memastikan pengguna memberikan input yang benar sebelum lanjut ke proses pencarian.
15.	Mengambil input dari pengguna dan menghapus spasi di awal atau akhir yang tidak sengaja terketik.
16.	Validasi keamanan. Program hanya akan lanjut (break) jika input tepat satu karakter dan merupakan alfabet. Jika tidak, akan muncul pesan kesalahan.
17.	Program hanya akan lanjut (break).
18.	Sebagai umpan balik kepada pengguna ketika data yang mereka masukkan tidak memenuhi kriteria yang ditetapkan pada kondisi if sebelumnya.
19.	Bahwa data yang mereka masukkan tidak sesuai dengan kriteria yang diminta oleh sistem dan meminta mereka untuk mencoba lagi dengan input yang benar satu huruf alfabet.
20.	Memanggil fungsi pencarian dengan mengirimkan data dan huruf target, lalu menyimpan hasilnya ke variabel found_indices.
21.	Program memeriksa apakah panjang (length) dari list found_indices lebih besar dari nol. Jika lebih besar dari 0, berarti ada minimal satu kecocokan data yang ditemukan. Jika 0, berarti daftar tersebut kosong dan tidak ada data yang cocok.
22.	Jika data ditemukan, baris ini mencetak pesan ke layar. Penggunaan .upper() memastikan huruf ditampilkan sebagai kapital, dan len(found_indices) menunjukkan jumlah total kemunculan huruf tersebut.
23.	Baris ini memberikan informasi lokasi spesifik di mana saja huruf tersebut berada dengan mencetak seluruh isi list indeks.
24.	Bagian ini adalah alternatif jika kondisi pada blok if tidak terpenuhi artinya len(found_indices) adalah 0.
25.	Program memberikan umpan balik kepada pengguna bahwa proses pencarian telah selesai dilakukan di seluruh elemen array, namun tidak ada karakter yang sesuai dengan input pengguna.
26.	
27.	Memastikan fungsi main() hanya dijalankan jika file ini dieksekusi secara langsung, bukan saat diimpor sebagai modul oleh file lain.
28.	Fungsi main.


Output Program Sebelum Diinputkan Huruf yang Dicari:
<img width="891" height="70" alt="Screenshot 2026-05-12 221122" src="https://github.com/user-attachments/assets/23ecdf74-812b-48d8-8548-612ccd44f966" />

Output Program Setelah Diinputkan Huruf yang Dicari:
<img width="891" height="124" alt="Screenshot 2026-05-12 221152" src="https://github.com/user-attachments/assets/91443f80-9b98-408f-967e-447be273d618" />

Penjelasan Output:
Program akan menampilkan seluruh isi kumpulan data huruf dalam bentuk array kepada user di awal eksekusi. Setelah itu, program meminta user memasukkan satu karakter huruf yang ingin dicari, dengan sistem validasi yang memastikan input hanya berupa satu karakter alfabet. Program kemudian menjalankan algoritma Sequential Searching untuk memindai setiap elemen array secara berurutan guna menemukan kecocokan tanpa memedulikan perbedaan huruf besar atau kecil (case-insensitive). Hasil akhirnya, program akan menampilkan jumlah total kemunculan huruf tersebut beserta daftar posisi indeksnya secara spesifik jika data ditemukan, atau memberikan pesan bahwa data tidak ditemukan jika seluruh elemen telah diperiksa.


LInk YouTube : https://youtu.be/Z3pnTyGS3Y0?feature=shared


<img width="3152" height="4512" alt="IMG_20260512_224811_535@1616007011" src="https://github.com/user-attachments/assets/ca5301f8-03a1-4e87-b53a-15f514fba6a4" />
