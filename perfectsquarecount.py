A=int(input("Enter start number:"))
B=int(input("Enter end number:"))
count=0
for i in range(A,B+1):
    if int(i**0.5)**2==i:
        count+=1
print(count)