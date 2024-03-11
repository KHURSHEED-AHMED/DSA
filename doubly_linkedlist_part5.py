class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def delete_at_index(self, index):
        current = self.head
        if index == 0:
            if current is not None:
                self.head = current.next
                if self.head:
                    self.head.prev = None
                del current
                return
        count = 0
        while current is not None:
            if count == index:
                break
            current = current.next
            count += 1
        if current is None:
            return
        if current.next is not None:
            current.next.prev = current.prev
        if current.prev is not None:
            current.prev.next = current.next
        del current

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage:
dll = DoublyLinkedList()
dll.head = Node(1)
second = Node(2)
third = Node(3)
dll.head.next = second
second.prev = dll.head
second.next = third
third.prev = second

print("Original list:")
dll.print_list()

index_to_delete = 1
dll.delete_at_index(index_to_delete)
print(f"Doubly linked list after deleting node at index {index_to_delete}:")
dll.print_list()
