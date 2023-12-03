class Queue:
    def __init__(self):
        self.items = []
        self.frontIdx = 0

    def __compress(self):
        newlst = []
        for i in range(self.frontIdx, len(self.items)):
            newlst.append(self.items[i])
        
        self.items = newlst
        self.frontIdx = 0
    
    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Percobaan dequeue pada queue kosong")
        
        # mengkompress queue saat keadaan setengah penuh
        if self.frontIdx*2 > len(self.items):
            self.__compress()

        item = self.items[self.frontIdx]
        self.frontIdx += 1
        return item
    
    def enqueue(self, item):
        self.items.append(item)
    
    def front(self):
        if self.isEmpty():
            raise RuntimeError("Percobaan akses front queue kosong")
        return self.items[self.frontIdx]
    
    def isEmpty(self):
        return self.frontIdx == len(self.items)

def main():
    q = Queue()
    lst = list(range(10))
    lst2 = []

    for k in lst:
        q.enqueue(k)

    if q.front() == 0:
        print("Tes 1 berhasil")
    else:
        print("Tes 1 gagal")
    
    while not q.isEmpty():
        lst2.append(q.dequeue())

    if lst2 == lst:
        print("Tes 2 berhasil")
    else:
        print("Tes 2 gagal")

    for k in lst:
        q.enqueue(k)
    
    lst2 = []

    while not q.isEmpty():
        lst2.append(q.dequeue())
    
    if lst2 == lst:
        print("Tes 3 berhasil")
    else:
        print("Tes 3 gagal")
    
    try:
        q.dequeue()
        print("Tes 4 gagal")
    except RuntimeError:
        print("Tes 4 berhasil")
    except:
        print("Tes 4 gagal")
    
    try:
        q.front()
        print("Tes 5 gagal")
    except RuntimeError:
        print("Tes 5 berhasil")
    except:
        print("Tes 5 gagal")

if __name__=="__main__":
    main()
