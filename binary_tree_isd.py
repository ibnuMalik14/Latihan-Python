class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.value:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(val, node.left)
        elif val > node.value:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(val, node.right)

    def search(self, val):
        return self._search(val, self.root) if self.root else None

    def _search(self, val, node):
        if node is None or node.value == val:
            return node
        elif val < node.value:
            return self._search(val, node.left)
        else:
            return self._search(val, node.right)

    def delete(self, val):
        self.root = self._delete(val, self.root) if self.root else None

    def _delete(self, val, node):
        if node is None:
            return None

        if val < node.value:
            node.left = self._delete(val, node.left)
        elif val > node.value:
            node.right = self._delete(val, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.value = self._min_value(node.right)
            node.right = self._delete(node.value, node.right)
        return node

    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.value

    def display_tree(self):
        self._display_tree(self.root)

    def _display_tree(self, node):
        if node:
            self._display_tree(node.left)
            print(node.value, end=' ')
            self._display_tree(node.right)

# Contoh Penggunaan
tree = BinaryTree()

while True:
    print("\nMenu:")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display Tree")
    print("5. Exit")

    choice = int(input("Pilih menu (1-5): "))

    if choice == 1:
        val = int(input("Masukkan nilai yang akan diinsert: "))
        tree.insert(val)
    elif choice == 2:
        val = int(input("Masukkan nilai yang akan dicari: "))
        result = tree.search(val)
        if result:
            print(f"Nilai {val} ditemukan dalam pohon.")
        else:
            print(f"Nilai {val} tidak ditemukan dalam pohon.")
    elif choice == 3:
        val = int(input("Masukkan nilai yang akan dihapus: "))
        tree.delete(val)
        print(f"Nilai {val} telah dihapus dari pohon.")
    elif choice == 4:
        print("Pohon Biner Pencarian:")
        tree.display_tree()
    elif choice == 5:
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan 1-5.")
