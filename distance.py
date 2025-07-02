D=int(input("Enter distance:"))
score=0
if D<=50:
    score+=D*3
elif D<=100:
    score+=50*3+(D-50)*5
elif D<=200:
    score+=50*3+50*5+(D-100)*6
elif D<=250:
    score+=50*3+50*5+100*6+(D-200)*8
else:
    score+=50*3+50*5+100*6+200*8+(D-250)*10
score+=100
print(score) 
