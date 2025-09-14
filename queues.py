#12-09-2025
#Implementation using List
class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
    def isEmpty(self):
        return len(self.queue)==0
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return 
        return self.queue.pop(0) 
    def peek(self):
        if self.isEmpty():
            print("No elements in queue")
            return
        return self.queue[0]
a=Queue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.dequeue()
print(a.peek())   
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
#Priority Queue 
# Each element is associated with a priority.
# Element with higher priority is dequeued first.
# If priorities are equal, then FIFO is followed.
import heapq 
class PriorityQueue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item,priority):
        heapq.heappush(self.queue,(priority,item))
    def dequeue(self):
        if self.queue:
            return heapq.heappop(self.queue)[1]
        return "Queue is Empty"
    def display(self):
        print("Queue:",self.queue) 
pq=PriorityQueue()
pq.enqueue("task2",1)
pq.enqueue("task1",2)
pq.enqueue("task3",3)
pq.dequeue()
pq.display()  
# Double-Ended Queue (Deque)
#Insertions and deletions can be done from both ends.
from collections import deque 
dq=deque()
dq.append(10)
dq.appendleft(20)
dq.append(30)
print("Queue:",dq)
dq.pop()
dq.popleft()
print("After Deletion:",dq)
