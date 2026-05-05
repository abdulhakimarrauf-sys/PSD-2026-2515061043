def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j].lower() > temp.lower():
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


def main():
    try:
        n = int(input("Masukkan jumlah barang peminjaman: "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    print("Masukkan nama barang yang dipinjam:")
    for i in range(n):
        while True:
            try:
                nama = str(input())
                arr.append(nama)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan nama barang!")
    print(f"Array sebelum diurutkan: {arr}")
    insertion_sort(arr, n)
    print("Array setelah diurutkan (Insertion Sort):", end=" ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


if __name__ == "__main__":
    main()
