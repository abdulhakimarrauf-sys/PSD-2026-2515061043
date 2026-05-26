Sistem Data Berat Sapi Kurban

Program Sistem Data Berat Sapi Kurban ini berfungsi sebagai aplikasi manajemen data interaktif untuk mencatat, menyimpan, dan menganalisis berat hewan ternak (sapi) kurban secara digital menggunakan struktur data non-linear Binary Search Tree (BST). Algoritma struktur data yang diterapkan di dalam program ini meliputi penataan data terurut otomatis melalui fungsi rekursif insertion (di mana berat sapi yang lebih ringan dari simpul acuan diletakkan di subpohon kiri, dan yang lebih berat di subpohon kanan), algoritma pencarian biner (binary search) untuk mendeteksi keberadaan berat sapi tertentu, metode penelusuran pohon (tree traversal) berupa Inorder, Preorder, dan Postorder untuk menyajikan variasi laporan data, serta algoritma penelusuran ekstrem linear (while-loop) guna mendeteksi bobot sapi paling ringan (minimum) maupun paling berbobot (maximum).

Spource Code
<img width="1554" height="5994" alt="TA BST Dasar" src="https://github.com/user-attachments/assets/c6d0ea47-045e-4e46-bf6c-7bac058c48bd" />

Penjelasan Source Code
1.	Mengimpor fungsi bawaan input dan print secara eksplisit dari modul builtins guna memastikan fungsi standar masukan dan keluaran dapat berjalan dengan normal.
2.	 
3.	
4.	Mendeklarasikan kelas bernama Node. Kelas ini bertindak sebagai cetakan (blueprint) untuk membuat setiap simpul atau elemen di dalam struktur pohon.
5.	Metode konstruktor (__init__) yang otomatis dijalankan saat sebuah simpul baru dibuat, dengan menerima parameter key (nilai data).
6.	Menyimpan nilai data yang dikirim melalui parameter key ke dalam atribut objek self.key. Pada program ini, variabel tersebut akan menyimpan angka bobot berat sapi.
7.	Menginisialisasi penunjuk (pointer) sebelah kiri dengan nilai awal None. Bagian ini berfungsi untuk menyimpan referensi ke simpul anak kiri (left child).
8.	Menginisialisasi penunjuk (pointer) sebelah kanan dengan nilai awal None. Bagian ini berfungsi untuk menyimpan referensi ke simpul anak kanan (right child).
9.	 
10.	 
11.	Mendeklarasikan kelas utama bernama BSTDasar yang membungkus seluruh fungsi operasi manipulasi, perhitungan, dan penelusuran pohon.
12.	Metode konstruktor kelas BSTDasar.
13.	Baris ini menetapkan atribut self.root dengan nilai awal None, yang menandakan bahwa saat objek pohon pertama kali dibuat di memori, pohon dalam keadaan kosong (belum memiliki akar).
14.	 
15.	Fungsi penolong internal (helper) yang berjalan secara rekursif untuk mencari posisi koordinat penempatan simpul baru secara tepat. Menerima parameter simpul yang sedang diperiksa (root) dan nilai yang ingin dimasukkan (key).
16.	Kondisi pembatas rekursi (base case). Jika penelusuran sampai pada posisi kosong (None).
17.	Program akan membuat objek simpul baru lewat perintah Node(key) dan mengembalikannya ke atas untuk disambungkan pada simpul induknya.
18.	Berdasarkan aturan utama BST, jika nilai data baru (key) lebih kecil daripada nilai simpul saat ini (root.key).
19.	Program melakukan pemanggilan fungsi dirinya sendiri secara rekursif menuju ke arah anak kiri (root.left). Hasil pembuatan simpul di bawahnya nanti akan ditautkan kembali pada properti root.left.
20.	Jika nilai data baru (key) lebih besar daripada nilai simpul saat ini (root.key).
21.	Program melakukan pemanggilan rekursif masuk ke arah cabang anak kanan (root.right).
22.	Mengembalikan objek simpul saat ini kembali ke tumpukan rekursif di atasnya guna menjaga keutuhan struktur pohon yang telah dilewati agar tidak terputus.
23.	 
24.	Fungsi publik yang dipanggil oleh antarmuka menu pengguna.
25.	Fungsi ini memicu metode rekursif insert_node dengan selalu memulai langkah penelusuran pertama kali dari akar utama pohon (self.root).
26.	 
27.	Fungsi helper rekursif untuk mencari keberadaan nilai data tertentu di dalam pohon.
28.	Jika langkah penelusuran melacak hingga ke ujung cabang bawah yang bernilai kosong (None), artinya data tidak ditemukan di dalam pohon.
29.	Fungsi mengembalikan nilai logika False.
30.	Jika nilai data pada simpul yang sedang diperiksa (root.key) sama persis dengan kunci target yang dicari (key), pencarian sukses.
31.	Fungsi mengembalikan nilai logika True.
32.	Jika kunci yang dicari lebih kecil dari nilai simpul saat ini.
33.	Fungsi melakukan pemanggilan rekursif untuk mencari ke arah subpohon cabang kiri (root.left).
34.	Jika kunci yang dicari lebih besar dari nilai simpul saat ini, otomatis fungsi melakukan pemanggilan rekursif untuk mencari ke arah subpohon cabang kanan (root.right).
35.	 
36.	Fungsi publik untuk memicu metode search_node.
37.	Mengoper alamat akar utama (self.root) sebagai titik awal pencarian.
38.	 
39.	Fungsi Melakukan penelusuran pohon dengan urutan aturan Kiri ke Root ke Kanan.
40.	Jika langkah penelusuran melacak hingga ke ujung cabang bawah yang bernilai kosong (None), artinya data tidak ditemukan di dalam pohon.
41.	Fungsi berhenti.
42.	Program akan bergerak ke anak kiri terdalam terlebih dahulu.
43.	Mencetak nilainya.
44.	Memproses simpul induk dan anak kanan. Pada struktur BST, hasil cetakan urutan ini dipastikan menampilkan data berat sapi yang terurut rapi dari bobot terkecil hingga terbesar (ascending).
45.	 
46.	Melakukan penelusuran pohon dengan urutan aturan Root ke Kiri ke Kanan.
47.	Jika langkah penelusuran melacak hingga ke ujung cabang bawah yang bernilai kosong (None), artinya data tidak ditemukan di dalam pohon.
48.	Fungsi berhenti.
49.	Program mencetak nilai simpul induknya terlebih dahulu.
50.	Menelusuri cabang anak kiri.
51.	Menelusuri cabang anak kanan.
52.	 
53.	Melakukan penelusuran pohon dengan urutan aturan Kiri ke Kanan ke Root.
54.	Jika langkah penelusuran melacak hingga ke ujung cabang bawah yang bernilai kosong (None), artinya data tidak ditemukan di dalam pohon.
55.	Fungsi berhenti.
56.	Program menyelesaikan semua kunjungan ke simpul-simpul anak di lapisan bawah kiri terlebih dahulu.
57.	Program menyelesaikan semua kunjungan ke simpul-simpul anak di lapisan bawah kanan juga.
58.	Mencetak nilai simpul induknya di akhir.
59.	 
60.	Mencari nilai terkecil di dalam pohon. 
61.	Jika pohon kosong.
62.	Mengembalikan nilai -1.
63.	Jika terisi, variabel pelacak current diletakkan di akar.
64.	Program melakukan perulangan while.
65.	Untuk terus bergeser menuruni cabang kiri (current.left) hingga mentok.
66.	Nilai di ujung kiri bawah tersebut dikembalikan sebagai nilai berat sapi terkecil.
67.	 
68.	Mencari nilai terbesar di dalam pohon.
69.	Jika pohon kosong.
70.	Mengembalikan nilai -1.
71.	Jika terisi, variabel pelacak current diletakkan di akar.
72.	Fungsi ini melakukan perulangan while.
73.	Untuk terus bergerak menuruni cabang sebelah kanan (current.right) hingga mentok.
74.	Nilai di ujung kanan bawah tersebut dikembalikan sebagai nilai berat sapi terbesar.
75.	 
76.	Menghitung total seluruh jumlah simpul (node) yang aktif di dalam pohon.
77.	Jika bertemu simpul kosong (None).
78.	Mengembalikan nilai 0.
79.	Jika berisi, rumusnya menghitung nilai 1 (mewakili simpul saat ini) ditambah total simpul hasil rekursi dari cabang anak kiri dan cabang anak kanan.Pada aplikasi, ini digunakan untuk menghitung total jumlah sapi.
80.	 
81.	Menghitung jumlah total akumulasi (penjumlahan matematis) dari seluruh nilai data yang tersimpan di dalam pohon.
82.	Jika bertemu simpul kosong (None).
83.	Mengembalikan nilai 0.
84.	Logika rekursinya mirip dengan count_nodes, namun angka pembilangnya diganti dengan nilai data dari simpul itu sendiri (root.key). Pada aplikasi, ini digunakan untuk menghitung total berat keseluruhan sapi kurban.
85.	 
86.	 
87.	Fungsi anatrmuka utama.
88.	Membuat instansi/objek baru dari kelas pohon (bst = BSTDasar())
89.	Menginisialisasi variabel pengontrol pilihan menu pilih dengan nilai awal 0.
90.	Memulai perulangan menu utama program CLI (Command Line Interface) yang akan terus berputar selama pengguna tidak memilih menu nomor 10 (Keluar).
91.	Mencetak teks judul aplikasi dan daftar pilihan menu operasi dari nomor 1 sampai 10 ke layar terminal pengguna.
92.	Cetak opsi menu.
93.	Cetak opsi menu.
94.	Cetak opsi menu.
95.	Cetak opsi menu.
96.	Cetak opsi menu.
97.	Cetak opsi menu.
98.	Cetak opsi menu.
99.	Cetak opsi menu.
100.	Cetak opsi menu.
101.	Cetak opsi menu.
102.	Kondisi awal.
103.	Program meminta input dari pengguna melalui fungsi input(). Teks yang dimasukkan kemudian dipaksa diubah menjadi tipe data bilangan bulat (integer) menggunakan fungsi int(), lalu hasilnya disimpan ke dalam variabel pilih.
104.	Jika pengguna memasukkan karakter non-angka (seperti huruf atau simbol), konversi ke int() akan gagal dan memicu eror ValueError.
105.	Eror tersebut langsung ditangkap oleh blok except, mencetak pesan peringatan.
106.	Perintah continue akan memaksa program melompati sisa kode di bawahnya untuk langsung mengulang perulangan menu dari awal.
107.	Jika nilai pilih adalah 1.
108.	Kondisi awal.
109.	Program meminta input berat sapi (x).
110.	Jika input berupa angka valid, program memanggil fungsi bst.insert(x).
111.	Untuk menyisipkan angka berat sapi tersebut ke dalam arsitektur pohon biner.
112.	Jika input tidak valid (bukan angka), program menangkap eror.
113.	Menampilkan pesan "Input tidak valid!".
114.	Jika nilai pilih adalah 2.
115.	Kondisi awal.
116.	Program mengambil input angka berat yang dicari (x). 
117.	Fungsi pencarian bst.search(x) dipanggil, jika metode tersebut mengembalikan nilai logika True.
118.	Teks "Ditemukan" akan dicetak.
119.	Jika menghasilkan False. 
120.	Teks "Tidak ditemukan" yang akan dicetak.
121.	Jika input tidak valid (bukan angka), program menangkap eror.
122.	Menampilkan pesan "Input tidak valid!".
123.	Jika nilai pilih adalah 3.
124.	Fungsi ini akan mencetak seluruh data berat sapi secara horizontal ke samping dengan urutan dari bobot terkecil hingga terbesar (ascending).
125.	Program memanggil fungsi penelusuran bst.inorder dengan mengirimkan titik awal dari akar pohon (bst.root).
126.	Perintah print() kosong di akhir digunakan untuk membuat baris baru.
127.	Jika nilai pilih adalah 4.
128.	Fungsi ini menelusuri struktur data pohon biner dengan urutan mencetak simpul induk terlebih dahulu sebelum turun mendalam ke cabang anak kiri dan anak kanannya.
129.	Program memanggil fungsi penelusuran bst.preorder mulai dari bst.root.
130.	Perintah print() kosong di akhir digunakan untuk membuat baris baru.
131.	Jika nilai pilih adalah 5.
132.	Fungsi ini menelusuri struktur data dengan aturan menyelesaikan pencetakan seluruh simpul anak di lapisan terbawah terlebih dahulu sebelum mencetak nilai simpul induknya.
133.	Program memanggil fungsi penelusuran bst.postorder mulai dari bst.root.
134.	Perintah print() kosong di akhir digunakan untuk membuat baris baru.
135.	Jika nilai pilih adalah 6.
136.	Program memanggil fungsi bst.find_min(bst.root) yang menelusuri cabang sebelah kiri pohon hingga mentok, lalu mencetak nilai berat sapi paling ringan yang ditemukan di ujung pohon tersebut.
137.	Jika nilai pilih adalah 7.
138.	Program memanggil fungsi bst.find_max(bst.root) yang menelusuri cabang sebelah kanan pohon hingga mentok, lalu mencetak nilai berat sapi paling besar/berat di dalam sistem.
139.	Jika nilai pilih adalah 8.
140.	Program mengeksekusi metode rekursif bst.count_nodes(bst.root) untuk menghitung seberapa banyak total simpul (node) aktif yang ada di dalam pohon, yang merepresentasikan total ekor sapi yang sudah diinput.
141.	Jika nilai pilih adalah 9.
142.	Program mengeksekusi metode rekursif bst.sum_nodes(bst.root) untuk menjumlahkan secara akumulatif setiap nilai numerik berat sapi yang tersimpan di semua simpul pohon biner.
143.	Jika nilai pilih adalah 10.
144.	program mencetak kalimat "Program selesai.". Karena nilai variabel pilih sudah berubah menjadi 10, kondisi pada perulangan luar (while pilih != 10) akan bernilai salah (False), sehingga perulangan otomatis berhenti dan aplikasi ditutup.
145.	Jika pengguna memasukkan data berupa angka bulat namun di luar jangkauan pilihan menu yang tersedia (misalnya angka 0, 11, atau 99).
146.	Program masuk ke blok else ini untuk menampilkan pesan peringatan "Pilihan tidak valid!" sebelum mengulang menu kembali.
147.	 
148.	 
149.	Merupakan sintaks kondisional bawaan Python untuk mendeteksi lingkungan eksekusi berkas file.
150.	Baris ini memastikan fungsi antarmuka utama main() hanya akan dipicu dan dijalankan secara otomatis jika file script ini dieksekusi secara langsung oleh pengguna melalui terminal, bukan karena diimpor oleh file script lain.

Output Source Code Sebelum Diinput:
<img width="278" height="197" alt="image" src="https://github.com/user-attachments/assets/b26c6c40-15c6-4b86-8c1f-e0976a94cf60" />

Output Source Code Setelah Diinput:
<img width="307" height="782" alt="Screenshot 2026-05-26 233457" src="https://github.com/user-attachments/assets/5edf7b3e-d2cc-4b9d-a4f1-ca8beb88c34a" />

<img width="316" height="771" alt="Screenshot 2026-05-26 233514" src="https://github.com/user-attachments/assets/93f8f30b-cad5-4879-b7a3-b2bef4130308" />

<img width="323" height="915" alt="Screenshot 2026-05-26 233531" src="https://github.com/user-attachments/assets/dd5eef99-7824-4e6c-9be0-62aab115d54d" />

<img width="275" height="361" alt="Screenshot 2026-05-26 233549" src="https://github.com/user-attachments/assets/d8a81380-9dfd-491b-ae4b-46ff933d34b5" />

Penjelasan Output Source Code:
Berdasarkan hasil eksekusi program pada gambar tangkapan layar, sistem berhasil mengelola data berat sapi kurban dengan struktur Binary Search Tree (BST) melalui serangkaian input data bobot secara bertahap, dimulai dari nilai 500, 300, 190, 999, 777, hingga 101. Melalui penelusuran struktur pohon tersebut, program dapat menampilkan data berat sapi yang terurut dari yang teringan hingga terberat secara Inorder (101 190 300 500 777 999), variasi urutan Preorder (500 300 190 101 999 777), dan urutan Postorder (101 190 300 777 999 500). Selain itu, fitur analisis data bekerja secara akurat dengan mendeteksi bobot sapi kurban terkecil pada angka 101 kg, bobot terbesar mencapai 999 kg, total hewan ternak yang terdaftar sebanyak 6 ekor sapi, serta akumulasi total berat keseluruhan sapi kurban di dalam sistem yang mencapai 2867 kg.

LInk YouTube : https://youtu.be/7UOj5Mr5ta8
