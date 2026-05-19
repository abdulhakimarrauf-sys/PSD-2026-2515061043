class StackArray:
    def __init__(self, max_size=50):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self, size=1):
        return self.top_idx + size >= self.MAX

    def push(self, x, size=1):
        for i in range(self.top_idx + 1):
            if self.st[i] == x:
                print(f"Kendaraan dengan nama '{x}' sudah ada di dalam parkiran kapal.")
                return
        if self.is_full(size):
            print("Stack penuh")
            print(f"size tersisa: {self.MAX - self.top_idx - 1}")
            return
        for _ in range(size):
            self.top_idx += 1
            self.st[self.top_idx] = x
        print(f"Push {x} berhasil dengan ukuran {size}")

    def pop(self):
        if self.is_empty():
            print("Stack kosong")
            return
        print(f"Pop {self.st[self.top_idx]} berhasil")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Stack kosong")
            return
        print(f"Elemen teratas: {self.st[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("Stack kosong")
            return
        i = self.top_idx
        while i >= 0:
            nama_kendaraan = self.st[i]
            ukuran = 0
            while i >= 0 and self.st[i] == nama_kendaraan:
                ukuran += 1
                i -= 1
            print(f"{nama_kendaraan} ukuran: {ukuran} slot")


def main():
    stack = StackArray()
    pilih = 0
    while pilih != 5:
        print("\nSISTEM PARKIRAN KENDARAAN PADA KAPAL FERI")
        print("\n=== STACK (Array) ===")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Tampilkan")
        print("5. Hitung Total Kendaraan")
        try:
            pilih = int(input("Pilih opsi: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            try:
                val = str(input("Kendaraan: "))
                size = int(input("Ukuran: "))
                stack.push(val, size)
            except ValueError:
                print("Input tidak valid!")
        elif pilih == 2:
            stack.pop()
        elif pilih == 3:
            stack.peek()
        elif pilih == 4:
            stack.display()
        elif pilih == 5:
            count = stack.top_idx + 1
            print(f"Total kendaraan di dalam kapal: {count}")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
