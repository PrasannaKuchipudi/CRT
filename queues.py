# #12-09-2025
# #Implementation using List
# class Queue:
#     def __init__(self):
#         self.queue=[]
#     def enqueue(self,data):
#         self.queue.append(data)
#     def isEmpty(self):
#         return len(self.queue)==0
#     def dequeue(self):
#         if self.isEmpty():
#             print("Queue is empty")
#             return 
#         return self.queue.pop(0) 
#     def peek(self):
#         if self.isEmpty():
#             print("No elements in queue")
#             return
#         return self.queue[0]
# a=Queue()
# a.enqueue(1)
# a.enqueue(2)
# a.enqueue(3)
# a.dequeue()
# print(a.peek())   
#Implementation using Linked List 
class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
class Queue:
    def __init__(self):
        self.head=None 
        self.tail=None 
    def enqueue(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode 
            self.tail=newNode
        else:
            self.tail.next=newNode 
            self.tail=newNode 
    def isEmpty(self):
        return self.head==None 
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.head=self.head.next 
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.head.data 
b=Queue()
b.enqueue(100)
b.enqueue(200)
b.enqueue(300)
b.dequeue()
print(b.peek())

