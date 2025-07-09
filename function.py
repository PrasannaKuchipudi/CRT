#Defining a Function example
def Hi():
    print("Hello! Students")
Hi()
#Using function
def students():
    return 80
Tot_students=students()
print("Total students",Tot_students)
#Without func
def students():
    return 80
Tot_students=students()
print("Total students",80)
#Positional Arguments
def Hi(name):
    print("Hello",name)
Hi("Prasanna")
#Default Arguments
def Hi(name="Friends"):
    print("Hello",name)
Hi()
#Keyword Arguments
def student(name,age):
    print("Name:",name)
    print("Age:",age)
student(age=19,name="Prasanna")
#No Arguments,No return value
def func():
    print("keep smiling")
func()
#With Arguments,No return value
def greet(name):
    print("Hello",name)
greet("students")
#No Arguments,With Return value
def Hi():
    return "friends"
value=Hi()
print("Wishes:",value)
#With Arguments and Return Value
def add(a,b):
    return a+b
result=add(2,5)
print("Sum:",result)