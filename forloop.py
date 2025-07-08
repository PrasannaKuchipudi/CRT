for i in range(5):
    print(i)
#BREAK CONDITION
for j in range(10):
    if j==4:
        break
    print(j)
#CONTINUE CONDITION
for k in range(5):
    if k==3:
       continue
    print(k)
#LIST ITERATION
list=[1,2,3,"prasanna",8.9,True]
for j in list:
    print(j)
#EVEN NUMBERS
for i in range(20):
    if i%2==0:
       print(i)
#ODD NUMBERS
for i in range(10):
    if i%2!=0:
       print(i)
#POSITIVE
list=[1,2,-1,-2]
for i in list:
    if i>0:
        print(i)
#NEGATIVE
list=[1,2,-1,-2]
for i in list:
    if i<0:
        print(i)
#TABLE
n=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
#1 to 10 tables 
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print()
#Stop printing characters on space
text="Hello World!"
for char in text:
    if char==' ':
        break
    print(char)
#Skip vowels
text="education"
vowels="aeiou"
for char in text:
    if char in vowels:
        continue
    print(char)
#Break on first number>20
n=[5,10,20,25,30]
for num in n:
    if num>20:
        break
    print(num)
#Continue even numbers
for i in range(1,21):
    if i%2==0:
        continue
    print(i)
#Break if total sum>100
n=[10,20,30,40,15,5,7]
total=0
for num in n:
    total+=num
    if total>100:
        break
    print("Sum:",total)
#Skip words starting with 'b'
String=["bat","apple","banana","cat","dog"]
for word in String:
    if word.startswith('b'):
        continue
    print(word)
#Nested loop with break
for i in range(1,4):
    for j in range(1,10):
        if i*j>20:
            break
        print(f"{i}*{j}={i*j}")
#Find first even and break
nums=[1,3,5,8,9]
for num in nums:
    if num%2==0:
        print("First even:",num)
        break
#Continue on divisible by 4 or 6
for i in range(1,31):
    if i%4==0 or i%6==0:
        continue
    print(i)
#Skip every third character
text="abcdefghij"
for index,char in enumerate(text,1):
    if index%3==0:
        continue
    print(char)