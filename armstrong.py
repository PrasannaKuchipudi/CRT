n=int(input("Enter a number:"))
temp=n
b=len(str(n))
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**b
    temp=temp//10
if sum==n:
    print(f"{n} is a Armstrong Number")
else:
    print(f"{n} is not a Armstrong Number")


