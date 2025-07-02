A=int(input("Enter amount:"))
denominations=[2000,500,200,50,20,5,2,1]
notes=[]
for i in denominations:
    count=A//i
    A%=i
    notes.append(count)
print(f"2000:{notes[0]}")
print(f"500:{notes[1]}")
print(f"200:{notes[2]}")
print(f"50:{notes[3]}")
print(f"20:{notes[4]}")
print(f"5:{notes[5]}")
print(f"2:{notes[6]}")
print(f"1:{notes[7]}")