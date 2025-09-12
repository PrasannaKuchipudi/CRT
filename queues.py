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
