arr = [0,1,2,3,4,5,6]

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:

    def __init__(self, arr):
        self.arr = arr
        self.head = Node(arr[len(arr)//2])

tree = Tree(arr)
print(tree.head.val)