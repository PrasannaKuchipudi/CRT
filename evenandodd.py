n=int(input("Enter a number:"))
for i in range(n+1):
    if i%2==0:
        print(f"{i} EVEN")
    else:
        print(f"{i} ODD")