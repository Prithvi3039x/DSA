class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        p = 0
        while p != position - 1:
            if current is None:
                print("Invalid position")
                return
            current = current.next
            p += 1

        if current is None:
            print("Invalid position")
            return

        new_node.next = current.next
        new_node.prev = current
        current.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def delete(self, value):
        current = self.head

        if current.data == value:
            self.head = self.head.next
            self.head.prev = None

        else:
            while(current.data!=value and current):
                current = current.next
                if current == None:
                    print("Value is not present")
                    return
        current.prev.next = current.next
        current.next.prev = current.prev
        current = None

    def traverse(self):
        current = self.head

        while current is not None:
            print(current.data , end="->")
            current = current.next

        print("None")

        # while current is not None and current.data != value:
        #     current = current.next

        # if current is None:
        #     print("Value not found")
        #     return

        # if current.prev is None:
        #     self.head = current.next
        # else:
        #     current.prev.next = current.next

        # if current.next is not None:
        #     current.next.prev = current.prev

   
    def rev(self):
        current = self.head
        while current.next is not None:
            current = current.next

        while current:
            print(current.data, end="->")
            current = current.prev

        print("None")

dll = DoublyLinkedList()
dll.insert(1, 0)
dll.insert(2, 1)
dll.insert(3, 2)
dll.insert(4, 3)
dll.traverse()
dll.rev()
# dll.delete(20)
dll.traverse()


