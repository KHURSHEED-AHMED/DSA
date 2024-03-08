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

    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index")
            return
        if index == 0:
            self.insert_at_begin(data)
            return

        new_node = Node(data)
        count = 0
        itr = self.head
        while itr:
            if count == index:
                new_node.prev = itr.prev
                new_node.next = itr
                itr.prev.next = new_node
                itr.prev = new_node
                return
            count += 1
            itr = itr.next

        print("Index out of range")

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
    ll.insert_at_begin(30)
    ll.insert_at_begin(20)
    ll.insert_at_begin(10)
    ll.func_print()  # Prints: 10-->20-->30-->

    ll.insert_at_index(2, 25)
    ll.func_print()  # Prints: 10-->20-->25-->30-->
