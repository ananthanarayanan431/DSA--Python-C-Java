
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedinList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_end(self,data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_begininig(self):
        current = self.head
        self.head = self.head.next
        current.next = None

    def search(self,data):
        current = self.head
        while current is not None:
            if current.data==data:
                return True
            current=current.next
        return False

    def printf(self):
        current = self.head
        while current is not None:
            print(current.data," ")
            current=current.next

preparation = LinkedinList()
preparation.insert_end("Prepare")
preparation.printf()
preparation.insert_end("Roll")
preparation.insert_beginning("assemble")
preparation.printf()
print(preparation.search("Roll"))
print(preparation.search("Mixing"))