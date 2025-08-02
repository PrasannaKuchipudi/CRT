#Squares(Basic structure)
square=[x*x for x in range(5)]
print(square)
#User input
n=list(map(int,input().split()))
square=[x**2 for x in n]
print(square)
#Even numbers only(If condition)
n=list(map(int,input().split()))
even=[x for x in n if x%2==0]
print(even)
#Even or odd (if-else condition)
n=list(map(int,input().split()))
even=['even' if x%2==0 else 'odd' for x in n]
print(even)
#Create a list of cubes from 1 to 5
n=[x**3 for x in range(1,6)]
print(n)
#Filter all numbers divisible by 3 from 0 to 20
n=[x for x in range(0,21) if x%3==0]
print(n)
#Replace numbers with “high” if >50 else “low” from [10, 60, 45, 80]
n=[10,60,45,80]
b=["high" if x>50 else "low" for x in n]
print(b)
#Squaring odd numbers only
n=list(map(int,input().split()))
b=[x*x for x in n if x%2==1]
print(b)
