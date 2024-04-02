
import queue
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head:
            current = self.head
            self.head = self.head.next
            current.next = None

            if self.head is None:
                self.tail = None

    def printf(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

# queue1 = Queue()
# queue1.enqueue("Anantha")
# queue1.enqueue("Narayanan")
# queue1.printf()

# queue1.dequeue()
# queue1.printf()

order = queue.SimpleQueue()
order.put("Anantha")
order.put("Narayanan")
order.put("R")

print("The size of: ",order.qsize())
print(order.get())
print(order.get())
print(order.get())