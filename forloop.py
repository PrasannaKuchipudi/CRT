# for i in range(5):
#     print(i)
#BREAK CONDITION
# for j in range(10):
#     if j==4:
#         break
#     print(j)
#CONTINUE CONDITION
# for k in range(5):
#     if k==3:
#        continue
#     print(k)
#LIST ITERATION
# list=[1,2,3,"prasanna",8.9,True]
# for j in list:
#     print(j)
#EVEN NUMBERS
# for i in range(20):
#     if i%2==0:
#        print(i)
#ODD NUMBERS
# for i in range(10):
#     if i%2!=0:
#        print(i)
#
#POSITIVE
# list=[1,2,-1,-2]
# for i in list:
#     if i>0:
#         print(i)
#NEGATIVE
# list=[1,2,-1,-2]
# for i in list:
#     if i<0:
#         print(i)
#TABLE
# n=int(input("Enter a number:"))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print()
