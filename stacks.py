#Implementation using list 
stack=[]
stack.append(10)
stack.append(20)
stack.append(30) 
print(stack)
print(stack.pop()) 
print(stack)
#Implementation using deque
from collections import deque  
stack=deque()
stack.append(100)
stack.append(200)
stack.append(300) 
print(stack)
print(stack.pop()) 
print(stack)
#Implementation using lifoqueue 
from queue import LifoQueue 
max_size=3
stack=LifoQueue(max_size)
stack.put(40)
stack.put(50)
stack.put(60)
print(stack.qsize())
print(list(stack.queue))
print(stack.empty())
print(stack.full())
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def isEmpty(self):
        return len(self.stack)==0
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return 
        return self.stack[-1]   
d=Stack()
d.push(100)
d.push(200)
d.push(300)
d.pop()
print(d.peek())
print(d.isEmpty())
#Implementation using Linked List  
class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None
class Stack:
    def __init__(self):
        self.head=None 
    def push(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode 
        else:
            newNode.next=self.head 
            self.head=newNode 
    def isEmpty(self):
        return self.head==None 
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.head=self.head.next 
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.head.data 
l=Stack()
l.push(1)
l.push(2)
l.push(3)
l.pop()
print(l.peek())

