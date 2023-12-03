class DataQueue:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        self.data.append(item)
        print(f"Data '{item}' berhasil ditambahkan.")

    def remove_data(self):
        if not self.is_empty():
            removed_item = self.data.pop(0)
            print(f"Data '{removed_item}' berhasil dihapus.")
        else:
            print("Queue kosong. Tidak dapat menghapus data.")

    def display_data(self):
        if not self.is_empty():
            print("Data saat ini dalam queue:")
            for item in self.data:
                print(item)
        else:
            print("Queue kosong. Tidak ada data ditampilkan.")

    def is_empty(self):
        return len(self.data) == 0

def main():
    queue = DataQueue()

    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Tampilkan Data")
        print("4. Keluar")

        choice = input("Pilih menu (1-4): ")

        if choice == '1':
            data_input = input("Masukkan data: ")
            queue.add_data(data_input)
        elif choice == '2':
            queue.remove_data()
        elif choice == '3':
            queue.display_data()
        elif choice == '4':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan 1-4.")

if __name__ == "__main__":
    main()
