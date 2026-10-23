# Stack using linked list
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            current = self.top
            print("Popped element: ",current.data)
            self.top = self.top.next
            current = None
        
    def print(self):
        current = self.top
        print ("Stack Elements")
        while current is not None:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.top
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.top = prev
        print("Stack reversed")
        
st = Stack()
st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(78))

st.print()
st.pop()
st.print()
print("After reverse:")
st.reverse()
st.print()