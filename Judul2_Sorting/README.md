Daftar Peminjaman Barang

Deskripsi
Program daftar peminjaman barang ini berfungsi untuk mendata dan mengorganisir nama-nama barang yang dipinjam oleh pengguna agar tersusun secara rapi berdasarkan urutan alfabet (A-Z). Dengan adanya program ini, pengguna dapat memasukkan jumlah serta identitas barang yang dipinjam, kemudian sistem akan secara otomatis memproses daftar tersebut sehingga lebih mudah untuk dibaca dan dicari kembali dalam daftar yang terstruktur. Algoritma struktur data yang diterapkan dalam program ini adalah Insertion Sort. Algoritma ini bekerja dengan cara membagi daftar menjadi bagian yang sudah terurut dan bagian yang belum terurut, kemudian mengambil satu per satu elemen (nama barang) dari bagian yang belum terurut untuk disisipkan ke posisi yang tepat pada bagian yang sudah terurut. Proses ini dilakukan dengan membandingkan nilai string (mengabaikan perbedaan huruf besar/kecil) dan menggeser posisi elemen lainnya hingga seluruh daftar peminjaman tersusun secara kronologis berdasarkan abjad. 


Source Code 
<img width="1434" height="1660" alt="Tugas Akhir Judul 2" src="https://github.com/user-attachments/assets/624ae0a2-1d2a-47d8-9dfd-9b9389886a43" />


Penjelasannya
1.	Sebagai fungsi dari algoritma pengurutan dengan (arr) sebagai daftar nama barang dan  (n) jumlah total barang.
2.	Melakukan perulangan mulai dari indeks ke-1 hingga elemen terakhir (n-1). Elemen pertama (indeks 0) dianggap sebagai bagian yang sudah terurut di awal. 
3.	Menyimpan nama barang pada indeks saat ini ke dalam variabel sementara (temp) untuk dibandingkan.
4.	Menentukan indeks j tepat di sebelah kiri i sebagai titik awal perbandingan ke belakang.
5.	Melakukan perulangan selama belum mencapai awal daftar (j >= 0) dan nama barang di posisi j secara alfabetis lebih besar daripada nama barang di temp. Penggunaan .lower() memastikan perbandingan tidak sensitif terhadap huruf besar atau kecil.
6.	Menggeser nama barang yang lebih besar satu posisi ke kanan untuk memberi ruang bagi elemen yang lebih kecil.
7.	Mengurangi nilai j agar perbandingan berlanjut ke elemen berikutnya di sebelah kiri.
8.	Setelah menemukan posisi yang tepat, nama barang di variabel temp dimasukkan ke dalam posisi tersebut.
9.	 
10.	 
11.	Fungsi ini mengatur alur interaksi dengan pengguna (input/output).
12.	Memulai blok penanganan kesalahan untuk mengantisipasi input yang tidak sesuai tipe data yang diminta.
13.	Meminta pengguna memasukkan jumlah barang dalam bentuk angka bulat (integer).
14.	Menangkap kesalahan jika pengguna memasukkan data selain angka (misalnya teks) pada input jumlah barang.
15.	Menampilkan pesan peringatan jika terjadi kesalahan input jumlah barang.
16.	Menghentikan eksekusi fungsi main() secara paksa agar program tidak berlanjut dengan data yang salah.
17.	Mendeklarasikan list (array) kosong bernama arr yang akan digunakan untuk menyimpan daftar nama barang.
18.	Memberikan instruksi kepada pengguna untuk mulai memasukkan nama-nama barang.
19.	Melakukan perulangan sebanyak n kali untuk mengambil input nama barang sesuai jumlah yang ditentukan di awal.
20.	Memulai perulangan tak terbatas untuk memastikan setiap input nama barang berhasil masuk tanpa error sebelum lanjut ke barang berikutnya.
21.	Membuka blok pengecekan kesalahan di dalam perulangan input barang.
22.	Mengambil input dari pengguna dan memastikan datanya dibaca sebagai teks (string).
23.	Menambahkan nama barang yang baru saja diinputkan ke dalam list arr.
24.	Keluar dari perulangan while True untuk melanjutkan ke iterasi for berikutnya (menginput barang selanjutnya)
25.	Menangkap kesalahan tipe data jika input nama barang tidak sesuai.
26.	Memberikan peringatan agar pengguna mengulangi input nama barang jika terjadi kesalahan.
27.	Menampilkan daftar nama barang dalam urutan asli (sesuai urutan input) menggunakan format f-string.
28.	Memanggil fungsi insertion_sort untuk mengurutkan daftar barang di dalam variabel arr.
29.	Mencetak teks keterangan hasil pengurutan tanpa berpindah ke baris baru (end=" ").
30.	Melakukan perulangan untuk mengakses setiap elemen di dalam list arr yang sudah terurut.
31.	Mencetak masing-masing nama barang satu per satu secara horizontal dengan spasi sebagai pemisah.
32.	Mencetak karakter baris baru untuk merapikan tampilan akhir pada terminal.
33.	 
34.	 
35.	Sebuah pengecekan standar Python untuk memastikan bahwa fungsi di bawahnya hanya dijalankan jika file ini dieksekusi secara langsung sebagai program utama, bukan saat diimpor oleh file lain.
36.	Memanggil fungsi main() untuk memulai seluruh proses program.


Output Program
<img width="506" height="42" alt="Screenshot 2026-05-05 204436" src="https://github.com/user-attachments/assets/5648cc0a-ab94-4c8c-8833-77a9a4fbddf4" />

Output Setelah Diinputkan Jumlah Barang dan Sebelum Diinputkan Daftar Barang
<img width="506" height="102" alt="Screenshot 2026-05-05 204534" src="https://github.com/user-attachments/assets/bf180773-67a0-4695-8748-631aa81d9f05" />

Output Setelah Diinputkan Daftar Barang
<img width="1659" height="435" alt="Screenshot 2026-05-05 204402" src="https://github.com/user-attachments/assets/1e598e62-7353-4c80-843f-600b994ea1dc" />

Penjelasan Keseluruhan Output
Program akan meminta user memasukkan jumlah barang peminjaman terlebih dahulu. Setelah itu, user diminta memasukkan nama barang yang dipinjam sesuai dengan jumlah data tersebut. Program akan menampilkan array sebelum diurutkan, lalu mengurutkannya menggunakan Insertion Sort secara ascending dengan membandingkan karakter huruf (mengabaikan huruf kapital) sehingga data ditampilkan secara rapi berdasarkan urutan alfabet dari A ke Z.

LInk YouTube : https://youtu.be/58Xshm3gSWo
