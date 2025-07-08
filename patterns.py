# Left-angled triangle
for i in range(1,6):
     print("*"*i)
#Inverted Left-angled triangle
for i in range(5,0,-1):
     print("*"*i)
#Right aligned triangle
for i in range(1,6):
    print(" "*(5-i)+"*"*i)
#Inverted right aligned triangle
for i in range(5,0,-1):
     print(" "*(5-i)+"*"*i)
 #Pyramid
for i in range(1,6):
   print(" "*(5-i)+"* "*i)
#Inverted pyramid
for i in range(5,0,-1):
     print(" "*(5-i)+"* "*i)
#Full Square
for i in range(5):
    print("*"*5)
#Hollow Square
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
           print(" ",end=" ")
    print()
#Cross Pattern
n=int(input("Enter n value:"))
for i in range(n):
    for j in range(n):
        if i==j or j==n-1-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#Number Triangle
n=int(input("Enter n value:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#Alphabet triangle
n=int(input("Enter n value:"))
for i in range(1,n+1):
    for j in range(i):
        print(chr(ord('A')+j),end=" ")
    print()










