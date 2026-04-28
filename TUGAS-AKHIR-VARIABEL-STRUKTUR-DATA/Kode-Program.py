def menu():
    print("SISTEM PARKIR MAHASISWA (HALAMAN A & B)")
    print("1. Tampilkan Tabel Parkir")
    print("2. Input Data (NPM & Kendaraan)")
    print("3. Cari Detail Urutan")
    print("4. Keluar")

def main():

    data = [["Kosong", "Kosong"] for _ in range(6)]
    
    while True:
        menu()
        pilih = input("Pilih menu: ")

        if pilih == '1':
            print("\nDATA PARKIRAN")
            print(f"{'HALAMAN A':<25}  {'HALAMAN B':<20}")
            print(f"{'Data (NPM-Motor)':<25}  {'Data (NPM-Motor)':<20}")
            for i in range(3):
                A = f"{i+1}. {data[i][0]}-{data[i][1]}"
                B = f"{i+4}. {data[i+3][0]}-{data[i+3][1]}"
                print(f"{A:<25}  {B:<20}")

        elif pilih == '2':
            slot_ditemukan = False
            for i in range(6):
                if data[i][0] == "Kosong":
                    print(f"\nMengisi otomatis untuk Slot Nomor {i+1}")
                    data[i][0] = input("NPM       : ")
                    data[i][1] = input("Kendaraan : ")
                    print("Data tersimpan!")
                    slot_ditemukan = True
                    break
            if not slot_ditemukan:
                print("\nMaaf, semua slot parkir sudah penuh!")

        elif pilih == '3':
            try:
                no = int(input("Cek nomor tempat (1-6): ")) - 1
                if 0 <= no < 6:
                    lokasi = "Halaman A" if no < 3 else "Halaman B"
                    print(f"\nDETAIL DATA [{lokasi}]")
                    print(f"Hasil: Slot {no+1} diisi oleh {data[no][0]} dengan kendaraan {data[no][1]}")
                else:
                    print("Nomor tempat tidak valid!")
            except ValueError:
                print("Masukkan angka yang valid!")

        elif pilih == '4':
            print("Selesai. Terima kasih!")
            break

if __name__ == "__main__":
    main()
