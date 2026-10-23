class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:  # or if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def print(self):
        current = self.front
        if self.rear == None:
            print("Queue is empty")
            return
        while current:
            print(current.data , end = "<-")
            current = current.next
        print(None)

    def dequeue(self):
        if self.front is None:
            print("Queue is empty..!")
            return None
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
                print("Now queue is empty..!")
            return data



q = LQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()


q.print()



    