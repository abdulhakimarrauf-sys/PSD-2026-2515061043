class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        int_key = hash(key) 
        return (int_key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]
        return None

    def remove_key(self, key):
        entry = self.search(key)
        if entry is None:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\nData Parkiran Motor Kampus (Open Addressing, Linear Probing):")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")
            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")
            else:
                print(f"({self.table[i].key},{self.table[i].value})")


def main():
    motor = HashMapOpenAddressing()
    motor.insert("Beat", "BE 1840 ZX")
    motor.insert("Mio", "BE 1234 AB")
    motor.insert("Vario", "BE 5678 CD")
    motor.insert("Ninja", "BE 9012 EF")
    motor.insert("Supra", "BE 3456 GH")
    motor.insert("Scoopy", "BE 7890 IJ")
    motor.display()

    hasil = motor.search("Mio")
    if hasil is not None:
        print(f"\nMotor 'Mio' ditemukan, value = {hasil.value}")
    else:
        print("\nMotor 'Mio' tidak ditemukan")

    motor.remove_key("Mio")
    print("\nSetelah menghapus motor 'Mio':")
    motor.display()

    hasil = motor.search("Ninja")
    if hasil is not None:
        print(f"\nMotor 'Ninja' ditemukan, value = {hasil.value}")
    else:
        print("\nMotor 'Ninja' tidak ditemukan")

    motor.insert("Mio", "BE 4321 AB")
    print("\nSetelah memasukkan motor 'Mio':")
    motor.display()


if __name__ == "__main__":
    main()
