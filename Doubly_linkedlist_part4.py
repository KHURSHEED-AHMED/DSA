class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
        new_node.prev = last_node

    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None

    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        itr = self.head
        while itr.next.next:
            itr = itr.next

        itr.next = None

    def func_print(self):
        if self.head is None:
            print("List is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begin(9)
    ll.insert_at_begin(4)
    ll.insert_at_begin(5)
    ll.func_print()  # Prints: 5-->4-->9-->

    ll.delete_first()
    ll.func_print()  # Prints: 4-->9-->

    ll.delete_last()
    ll.func_print()  # Prints: 4-->
