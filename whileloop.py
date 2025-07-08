count=0
while count<5:
    print(count)
    count+=1
#BREAK
count=0
while count<10:
    if count==5:
        break
    print(count)
    count+=1

#CONTINUE
count=6
while count<10:
    if count==5:
        continue
    print(count)
    count+=1
#Break on user input 'exit'
while True:
    a=input("Type Something:")
    if a=="exit":
        break
    print("You typed:",a)
#Break in while loop
i=1
while True:
    if i==8:
        break
    print(i)
    i+=1
#Continue in while loop
i=0
while i<10:
    i+=1
    if i==3 or i==6:
        continue
    print(i)

