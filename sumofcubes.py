M=int(input("Enter start number:"))
N=int(input("Enter end number:"))
sum=0
for i in range(M,N+1):
    sum+=i**3
print(f"Sum of cubes from {M} to {N} range is:{sum}")
