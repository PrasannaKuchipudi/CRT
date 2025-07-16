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
#Call by value
def modify(x):
    x=x+5
    print("Inside function:",x)
a=10
modify(a)
print("Outside function:",a)
#Call by reference
def add_item(my_list):
    my_list.append(99)
    print("Inside function:",my_list)
numbers=[1,2,3]
add_item(numbers)
print("Outside function:",numbers)
#lambda function
add=lambda a,b:a+b
print(add(9,3))
#Example-2: No Arguments
greet=lambda:"Hello!"
print(greet())
#Example-3: Lambda with one argument
square=lambda x:x*x
print(square(6))
#Example-4: Lambda in a map() function
n=[1,2,3,4]
squares=list(map(lambda x:x**2,n))
print(squares)
#Example-5: Convert to uppercase
names=['anu','gowtham','naani']
upper_names=list(map(str.upper,names))
print(upper_names)
#Scope
#Local scope
def Hi():
    name="why"
    print("Hello",name)
Hi()
#Global scope
x=10 
def show(x):
    print(x)
show()
print(x)
#Enclosed Function
def outer():
    x=10
    def inner():
        nonlocal x
        x+=5
        print("Inner:",x)
    inner()
    print("Outer:",x)
outer()
#Built-in Scope
x=[1,2,3,4,5]
print(len(x))
print(max(x))
print(sum(x))
#Args
def greet(*args):
    for name in args:
        print("Hello",name)
greet("Prasanna","Kavya")
#Example-2
def show(*args):
    for item in args:
        print(item)
data=[1,2,3,4]
show(*data)
#kwargs
def func(**kwargs):
      print(kwargs)
func(name="Anu",age=22)
#Recursion
def x(n):
    if n==0:
        print("Hello")
        return
    print(n)
    x(n-1)
x(5)
#Example-2
def factorial(n):
    if n==0 or n==1:
        return 1

    return n*factorial(n-1)
print(factorial(6))



