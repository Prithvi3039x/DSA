class Node:
    def _init_(self,data):
        self.data = data
        self.next = Next

class Sll:
    def _init_(self):
        self.head = None

    def create(self,values):
        self.head = None
        tail = None
        for v in values:
            node = Node(v)
            if self.head is None:
                self.head = tail = node
            else:
                tail.next = node
                tail = node

    def traverse(self):
        values = []
        cur = self.head
        while cur:
            values.append(str(cur(data)))
            cur = cur.next
        print("=>".join(values) if values else "List is empty")

    def insert(self,pos,data):
        if pos < 0:
            node.next = self.head
            self.head = node
            return
        cur = self.head
        for _ in range(pos - 1):
            if cur is None:
                break
            cur = cur.next
        if cur is None:
            print("Invalid position")
            return
        node.next = cur.next
        cur.next = node


    def find_mid(self):
        if self.head is None:
            print("List is empty")
            return None
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Middle = ", slow.data)
        return slow.data


    def delete(self,key):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next and cur.next.data != key:
            cur = cur.next
        if cur.next is None:
            print(f"{key} not found")
        else:
            cur.next = cur.next.next


    def rev(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev


    def pair_sum(self):
        sums = []
        cur = self.head
        while cur:
            if cur.next:
                sums.append(cur.data + cur.next.data)
                cur = cur.next.next
            else:
                sums.append(cur.data)
                cur = None
        print("Pair sums: ", sums)
        return sums


def solution():

    Llist = sll()

    Llist.create([10,20,30,40,50])
    print("Created")

    Llist.traverse()
    Llist.find_mid()
    Llist.delete(40)
    print("after deleting 40:")
    Llist.traverse()
    Llist.rev()
    print("After reversing")
    Llist.traverse()
    Llist.pair_sum()

solution()