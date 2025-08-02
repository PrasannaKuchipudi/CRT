#30-07-2025
try:
    x=int(input())
    result=x/0
    print(result)
except:
    print("Error")
try:
    age=int(input("Enter the age?"))
    if age<18:
        raise ValueError;
    else:
        print("the age is valid")
except ValueError:
    print("The age is not valid")
try:
    fileptr=open("file.txt","r")
    try:
        fileptr.write("Hi I am good")
    finally:
        fileptr.close() 
        print("file closed")
except:
    print("Error")
class ErrorInCode(Exception):
    def __init__(self,data):
        self.data=data 
    def __str__(self):
        return repr(self.data)
try:
    raise ErrorInCode(2000)
except ErrorInCode as ae:
    print("Received error:", ae.data)