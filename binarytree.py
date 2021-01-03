global ans

arr = [0,1,2,3,4,5,6]

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:

    def __init__(self, arr):
        self.arr = arr
        self.head = self.createtree(arr)
    
    def createtree(self,arr):
        if arr == []:
            return 
        node = Node(arr[len(arr)//2])
        node.left = self.createtree(arr[:len(arr)//2])
        node.right = self.createtree(arr[(len(arr)//2)+1:len(arr)])
        return node

        


tree = Tree(arr)

ans = []
def preorder(node):
    global ans
    ans.append(node.val)
    if node.left != None:
        preorder(node.left)
    if node.right != None:
        preorder(node.right)

def inorder(node):
    global ans
    if node.left != None:
        inorder(node.left)
    ans.append(node.val)
    if node.right != None:
        inorder(node.right)

def postorder(node):
    global ans
    if node.left != None:
        postorder(node.left)
    if node.right != None:
        postorder(node.right)
    ans.append(node.val)


postorder(tree.head)
print(ans)