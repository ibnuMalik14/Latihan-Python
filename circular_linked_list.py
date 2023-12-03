class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if self.is_empty():
            print("Circular Linked List is empty.")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

    def delete(self, data):
        if self.is_empty():
            print("Cannot delete from an empty list.")
            return

        current = self.head
        prev = None

        # Traverse the list to find the node to be deleted
        while current.data != data:
            if current.next == self.head:
                print(f"{data} not found in the list.")
                return
            prev = current
            current = current.next

        # If the node to be deleted is the only node in the list
        if current == self.head and current.next == self.head:
            self.head = None
        elif current == self.head:  # If the node to be deleted is the head
            prev = self.head
            while prev.next != self.head:
                prev = prev.next
            prev.next = current.next
            self.head = current.next
        else:
            prev.next = current.next

# Contoh penggunaan circular linked list
clist = CircularLinkedList()

clist.append(1)
clist.append(2)
clist.append(3)
clist.append(4)

print("Circular Linked List:")
clist.display()

clist.delete(2)

print("\nCircular Linked List After Deleting 2:")
clist.display()
