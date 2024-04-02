
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = new_node

    def pop(self):
        if self.top is None:
            return False
        popped = self.top
        self.top = self.top.next
        popped.next = None
        return popped.data

    def peek(self):
        if self.top:
            return self.top.data
        return False
    def printf(self):
        current = self.top
        while current is not None:
            print(current.data)
            current=current.next

stack1 = stack()
stack1.push('Anantha')
stack1.push('Narayanan')
stack1.printf()
if stack1.pop():
    print(stack1.pop())
else:
    print("No element to POP")



