#15-09-2025
#Linear Data Structure - Stacks,Queues,LinkedList,List 
#Non-Linear Data Structure - Trees,Graphs      
#A binary tree which follows tree constraints and it must have two nodes and maximum nodes of binary tree is two nodes  
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.right=Node(3)
root.right.right=Node(6)
#InORDER TRAVERSAL 
def IOT(root):
    if root==None:
        return
    IOT(root.left)
    print(root.data,end=" ")
    IOT(root.right) 
IOT(root)
#PreOrder Traversal 
def IOT(root):
    if root==None:
        return
    print(root.data,end=" ")
    IOT(root.left)
    IOT(root.right) 
IOT(root)
#PostOrder Traversal 
def IOT(root):
    if root==None:
        return
    IOT(root.left)
    IOT(root.right) 
    print(root.data,end=" ")
IOT(root)


