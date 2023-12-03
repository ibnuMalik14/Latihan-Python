class Stack:
    def __init__(self) :
        self.items = []

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("percobaan pop pada stack kosong")
        topIdx = len(self.items)-1
        item = self.items[topIdx]
        del self.items[topIdx]
        return item
    def push(self, item):
        self.items.append(item)
    
    def top(self):
        if self.isEmpty():
            raise RuntimeError("Percobaan akses top pada stack kosong")
        topIdx = len(self.items)-1
        return self.items[topIdx]
    
    def isEmpty(self):
        return len(self.items) == 0

def main():
    s = Stack()
    lst = list(range(10))
    lst2 = []
    for k in lst:
        s.push(k)

    if s.top() == 9:
        print("Tes 1 berhasil")
    else:
        print("Tes 1 gagal")

    while not s.isEmpty():
        lst2.append(s.pop())

    lst2.reverse()
    if lst2 != lst:
        print("Tes 2 gagal")
    else:
        print("Tes 2 berhasil")

    try:
        s.pop()
        print("Tes 3 gagal")
    except RuntimeError:
        print("Tes 3 berhasil")
    except:
        print("Tes 3 gagal")

    try:
        s.top()
        print("Tes 4 gagal")
    
    except RuntimeError:
        print("Tes 4 berhasil")
    except:
        print(" Tes 4 gagal")

if __name__ == "__main__":
    main()
