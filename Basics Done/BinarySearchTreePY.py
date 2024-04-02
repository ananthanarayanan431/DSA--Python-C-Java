
import queue
class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left_child = left
        self.right_child = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self,value):
        current = self.root
        while current:
            if value==current.data:
                return True
            elif value<current.data:
                current=current.left_child
            else:
                current=current.right_child
        return False

    def insert(self,data):
        new_node = TreeNode(data)
        if self.root is None:
            self.root=new_node
            return
        else:
            current = self.root
            while True:
                if data<current.data:
                    if current.left_child is None:
                        current.left_child = new_node
                        return
                    else:
                        current = current.left_child
                elif data>current.data:
                    if current.right_child is None:
                        current.right_child = new_node
                        return
                    else:
                        current = current.right_child

    def minBST(self):
        current = self.root
        while current.left_child:
            current=current.left_child
        return current.data
    def Inorder(self,current):
        if current:
            self.Inorder(current.left_child)
            print(current.data,end=" ")
            self.Inorder(current.right_child)

    def Preorder(self,current):
        if current:
            print(current.data,end=" ")
            self.Preorder(current.left_child)
            self.Preorder(current.right_child)

    def Postorder(self,current):
        if current:
            self.Preorder(current.left_child)
            self.Preorder(current.right_child)
            print(current.data,end=" ")

    def BFS(self):
        visited_nodes=list()
        if self.root:
            bfs_queue = queue.SimpleQueue()
            bfs_queue.put(self.root)
            while not bfs_queue.empty():
                current = bfs_queue.get()
                visited_nodes.append(current.data)
                if current.left_child:
                    bfs_queue.put(current.left_child)
                if current.right_child:
                    bfs_queue.put(current.right_child)
        return visited_nodes





BST=BinarySearchTree()
BST.insert(65)
BST.insert(20)
BST.insert(70)
BST.insert(10)
BST.insert(22)
BST.insert(68)
BST.insert(75)

print("Inorder Traversal")
BST.Inorder(BST.root)

print("\nPreorder Traversal")
BST.Preorder(BST.root)

print("\nPostorder Traversal")
BST.Postorder(BST.root)

print("\nBreadth First Search -Binary Tree")
print(BST.BFS())





