#EXample-1: Grading system
marks=int(input("Enter your marks:"))
if marks>=90:
    print("Grade:A")
elif marks>=70:
    print("Grade:B")
elif marks>=60:
    print("Grade:C")
elif marks>=40:
    print("Grade:D")
else:
    print("Fail")
#EXAMPLE-2: GREATEST AMONG THREE NUMBERS
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
if a>b and a>c:
    print("a is greatest value.")
elif b>a and b>c:
    print("b is greatest value.")
else:
    print("c is greatest value.")
#EXAMPLE-3 : AGING SYSYTEM
age=int(input("Enter age:"))
if age<15:
    print("Children")
elif age>=15 and age<=19:
    print("Teenage")
else:
    print("Citizen")
#Example-4 : Simple Calculator92 numbers,1 operator)
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
op=input("Enter operator(+,-,*,/):")
if op=="+":
    print("Result:",num1+num2)
elif op=="-":
    print("Result:",num1-num2)
elif op=="*":
    print("Result:",num1*num2)
elif op=="/":
    print("Result:",num1/num2)
else:
    print("Invalid Operator")
#Example-5: Traffic Signals
color=input("Enter color:").upper()
if color=="RED":
    print("Stop")
elif color=="GREEN":
    print("Go")
elif color=="YELLOW":
    print("Wait")
else:
    print("No signal")
