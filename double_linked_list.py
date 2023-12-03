class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(Self):
        current = Self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
    
    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev

                return
            current = current.next
dllist = DoubleLinkedList()

dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

print("Linked List Forward:")
dllist.display_forward()

print("\nLinked List Backward:")
dllist.display_backward()

dllist.delete(2)

print("\nLinked List After Deleting 2:")
dllist.display_forward()
        

