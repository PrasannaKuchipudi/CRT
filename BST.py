#19-09-2035
#BST Tree
class Node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 
def searchBST(root,target):
    while root:
        if target==root.data:
            return root 
        elif target<root.data:
            root=root.left
        else:
            root=root.right 
    return None 
root=Node(9)
root.left=Node(2)
root.right=Node(11)
root.left.left=Node(1)
root.left.right=Node(5)
root.right.left=Node(10)
root.right.right=Node(14)
root.left.right.left=Node(4)
root.left.right.right=Node(7)
ans=searchBST(root,7)
if ans is not None:
    print(ans.data)
else:
    print("Null")
#INSERTION 
class Node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None  
def insertBST(root,key):
    new_node=Node(key)
    if root is None:
        return new_node 
    current=root 
    parent=None 
    while current:
        parent=current 
        if key< current.data:
            current=current.left
        elif key>current.data:
            current=current.right 
        else:
            return root
    
    if key < parent.data:
        parent.left = new_node
    else:
        parent.right = new_node
    
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

root = Node(9)
root.left = Node(2)
root.right = Node(11)
root.left.left = Node(1)
root.left.right = Node(5)
root.right.left = Node(10)
root.right.right = Node(14)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root = insertBST(root, 6)
inorder(root)
#DELETION
#LEAF NODE 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 
def insertBST(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insertBST(root.left, key)
    elif key > root.data:
        root.right = insertBST(root.right, key)
    return root
def deleteNode(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None and root.right is None:
            return None
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
root = Node(9)
root.left = Node(2)
root.right = Node(11)
root.left.left = Node(1)
root.left.right = Node(5)
root.right.left = Node(10)
root.right.right = Node(14)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
print("Before Deletion:")
inorder(root)
print()
root = deleteNode(root, 7)
print("After Deletion:")
inorder(root)
#DELETION
class Node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 
def insertBST(root,key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left=insertBST(root.left,key)
    elif key > root.data:
        root.right=insertBST(root.right,key)
    return root 
def minValueNode(node):
    current=node 
    while current.left:
        current=current.left 
    return current    
def deleteNode(root,key):
    if root is None:
        return root 
    if key < root.data:
        root.left=deleteNode(root.left,key)
    elif key>root.data:
        root.right=deleteNode(root.right,key)
    else:
        if root.left is None:
            return root.right 
        elif root.right is None:
            return root.left 
        temp=minValueNode(root.right)
        root.data=temp.data 
        root.right=deleteNode(root.right,temp.data)
    return root    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
root=Node(9)
root.left=Node(2)
root.right=Node(11)
root.left.left=Node(1)
root.left.right=Node(5)
root.right.left=Node(10)
root.right.right=Node(14)
root.left.right.left=Node(4)
root.left.right.right=Node(7)
print("Before Deletion:")
inorder(root)
print()
root=deleteNode(root,11)
print("After Deletion:")
inorder(root)