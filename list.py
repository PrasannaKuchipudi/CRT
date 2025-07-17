# List=[10,20,"kiet",50]
# List[1]=80
# print(List)
# print(type(List))
# print(List[0])
# #LIST SLICING
# list=[10,20,30,40,50,60]
# print(list[1:3:1])
# #LIST METHODS
# #1.append() - Add element to list
# a=[10,20,30,40,50,60]
# a.append(90)
# print(a)
# #2.extend() - Add elements to list 
# a=[10,20,30,40]
# a.extend([90,100])
# print(a)
# #3.insert() - Insert element at particular position
# a=[10,20,30,40,50]
# a.insert(1,90)
# print(a)
# #4.remove()- REmove an element from list using element
# a=[10,20,30,40]
# a.remove(10)
# print(a)
# #5.index() - To check index of element in list
# a=[10,20,30,40]
# b=a.index(10)
# print(b)
# #6.pop() - To remove an element from list using index
# a=[10,20,30]
# a.pop(1)
# print(a)
# #7.clear() - Clear the elements from the list
# a=[10,20]
# a.clear()
# print(a)
# #8.count() - Return the count of particular element
# a=[10,20,30,10,40,10,90,70]
# b=a.count(10)
# print(b)
# #9.sort() - Sort the list
# a=[90,10,40,29,56]
# a.sort()
# print(a)
# #10.reverse() - To reverse the list
# a=[90,60,40,30,10]
# a.reverse()
# print(a)
# #11.copy() - Copy the list
# a=[10,40,80,70]
# b=a.copy()
# print(b)
# #Task-2
# a=[0,1,2,3,4,5,6,7,8,9]
# print(a[-7:-2:2])
# a=[1,2,3,4,5,6,7]
# print(a[5:1:-1])
# a=['a','b','c','d','e','f']
# # print(a[::2][1:])
# a=[1,2,3,4,5]
# print(a[-100:3]) #Highest negative number default as 0
# a=[1,2,3,4,5]
# print(a[::-2])
#Task-2
# #1.Add elements to a list
# a=[10,20,30]
# a.append(40)
# print(a)
# #2.Add element at a specific position
# a=[10,20,30,40]
# a.insert(1,80)
# print(a)
# #3.Delete a specific element
# a=[10,20,30]
# a.remove(10)
# print(a)
# #4.Remove and reverse an elment
# a=[1,2,3,4,5]
# a.remove(4)
# print(a)
# b=a.reverse()
# print(a)
# #5.Sort elements in ascending order
# a=[9,4,6,1,2,8]
# a.sort()
# print(a)
# #6.Seperate Even and Odd Numbers
# a=[1,2,3,4,5,6,7]
# even=[]
# odd=[]
# for i in a:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even numbers:",even)
# print("Odd Numbers:",odd)
#7.Password check
a=["prasanna","ammu","bhaskar"]
password=input("Enter a password:")
for i in a:
    if i==password:
        print("True")
        break
    else:
        print("False")
        break