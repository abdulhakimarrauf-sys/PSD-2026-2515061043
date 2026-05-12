def sequential_search(data, target):
    indeks = []
    i = 0
    target = target.upper() 
    while i < len(data):
        if data[i] == target:
            indeks.append(i)
        i += 1
    return indeks

def main():
    data = ['H', 'A', 'K', 'I', 'M', 'A', 'R', 'R', 'A', 'U', 'F']
    print(f"Data array: {data}")
    while True:
        target = input("Masukkan huruf yang ingin dicari: ").strip()
        if len(target) == 1 and target.isalpha():
            break
        else:
            print("Input tidak valid, masukkan satu huruf saja (A-Z).")
    found_indeks = sequential_search(data, target)
    if len(found_indeks) > 0:
        print(f"Huruf '{target.upper()}' ditemukan sebanyak {len(found_indeks)} kali.")
        print(f"Ditemukan pada indeks ke: {found_indeks}")
    else:
        print(f"Huruf '{target.upper()}' tidak ditemukan dalam array.")

if __name__ == "__main__":
    main()
