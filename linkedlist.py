#03-09-2025
#Linked List 
class Node:
    def __init__(self,value=0,next_Node=None):
        self.data=value 
        self.next=next_Node 
p1=Node(10,None)
p2=Node(20)
p3=Node()
print(p1.data)
print(p2.data)
print(p3.data)
print(p1.next,p2.next,p3.next)                                                                             
#Insertion at Begining
class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
class LinkedList:
    def __init__(self):
        self.head=None 
    def insert_begin(self,data):
        new=Node(data)
        new.next=self.head 
        self.head=new 
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return
        self.head=self.head.next   
    def update_begin(self,new_data):
        if not self.head:
            print("List is empty")
            return 
        self.head.data=new_data
    def display(self):
        temp=self.head 
        while temp:
            print(temp.data,end="->")
            temp=temp.next 
        print("None")
l1=LinkedList()
l1.insert_begin(100)
l1.insert_begin(200)
l1.display()  
l1.delete_begin()
l1.display()
l1.update_begin(200)
l1.display()
#Insertion at the end
class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
class LinkedList:
    def __init__(self):
        self.head=None 
    def insert_end(self,data):
        new=Node(data)
        if not self.head:
            self.head=new 
            return 
        temp=self.head 
        while temp.next:
            temp=temp.next 
        temp.next=new 
    def deletion_end(self):
        if not self.head: 
            print("List is empty")
            return 
        if not self.head.next: #only one node 
            self.head=None 
            return 
        temp=self.head 
        while temp.next.next:
            temp=temp.next 
        temp.next=None   
    def display(self):
            temp=self.head 
            while temp:
                print(temp.data,end="->")
                temp=temp.next 
            print("None") 
l2=LinkedList()
l2.insert_end(100)
l2.insert_end(200)
l2.display()
l2.deletion_end()
l2.display()
#Insertion at Particular Position 
class Node:
        def __init__(self,data):
            self.data=data 
            self.next=None 
class LinkedList:
        def __init__(self):
           self.head=None 
        def insert_pos(self,pos,data):
            new=Node(data)
            if pos==0:
                    new.next=self.head 
                    self.head=new 
                    return
            temp=self.head 
            for i in range(pos-1):
                temp=temp.next
            new.next=temp.next 
            temp.next=new 
        def delete_pos(self,pos):
            if not self.head:
                print("List is empty")
                return 
            if pos==0:
                self.head=self.head.next 
                return 
            temp=self.head 
            for i in range(pos-1):
                if not temp.next:
                    print("Position out of range")
                    return 
                temp=temp.next 
            if not temp.next:
                print("Position out of range")
                return 
            temp.next=temp.next.next     
        def update_pos(self,pos,new_data):
            if not self.head:
                print("List is empty")
                return 
            temp=self.head 
            for i in range(pos):
                if not temp:
                  print("Position out of bound")
                  return 
                temp=temp.next 
            if temp:
                temp.data=new_data 
                return 
            else:
                print("Position out of range")   
        def traverse(self):
            if not self.head:
                print("List is empty")
                return 
            temp=self.head 
            while temp:
                print(temp.data,end=" -> ")
                temp=temp.next  
            print("None") 
        def display(self):
            temp=self.head 
            while temp:
                print(temp.data,end="->")
                temp=temp.next 
            print("None")
l3=LinkedList()
l3.insert_pos(0,10)
l3.insert_pos(1,20)
l3.display()
l3.update_pos(0,30)
l3.display()
l3.traverse()
l3.delete_pos(0)
l3.display()





