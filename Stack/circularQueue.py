class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.rear.next = self.front

    def print(self):
        if self.front is None:
            print("Queue is empty")
            return
        current = self.front
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.front:
                break
        print(f"(back to front: {self.front.data})")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty..!")
            return None
        if self.front == self.rear: # last node
            data = self.front.data
            self.front = self.rear = None
            return data
        else:
            data = self.front.data
            self.front = self.front.next
            self.rear.next = self.front
            return data

cq = CQueue()

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)

cq.dequeue()
cq.print()
cq.dequeue()
cq.print()
cq.dequeue()
cq.print()
cq.dequeue()
cq.print()