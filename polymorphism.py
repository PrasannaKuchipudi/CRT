# 06-08-2025
# Polymorphism - Many ways
# 1.Compile Time Polymorphism  - Method overloading (arguments,passing parameters) It executes in the time of compilation 
# 2.Run-Time Polymorphism - Method Overriding - It executes in the time of Run-Time
# 3.Operator Overloading - 
# 4.Duck Typing - 
class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog:
    def sound(self):
        print("Bow")
class Cat:
    def sound(self):
        print("Meow")
def get_sound(a):
    a.sound()
get_sound(Animal())
get_sound(Dog())
get_sound(Cat())
# Checking type
class Dog:
    def sound(self):
        print("Bow")
class Cat:
    def sound(self):
        print("Meow")
def get_sound(a):
    if isinstance(a,Dog) or isinstance(a,Cat):
        a.sound()
get_sound(Dog())
get_sound(Cat())
#Method Overloading - Compile Time Polymorphism
class hello:
    def add(self,a,b=0,c=0):
        return a+b+c
obj=hello()
print(obj.add(1,2))
print(obj.add(3))
print(obj.add(1,2,3)) 
#Method Overriding- Run Time Polymorphism
class Chocolates:
    def sweet(a):
        print("Diary Milk")
class Biscuits(Chocolates):
    def sweet(a):
        print("Hide and Seek")
obj=Biscuits()
obj.sweet()       
#Operator Overloading 
# This special method overrides the behavior of the + operator.
# Instead of adding two objects directly (which normally raises an error), it adds their marks attributes.
# Internally calls: s1.__add__(s2)
class Student:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,other):
        return self.marks + other.marks 
s1=Student(20)
s2=Student(25)
sum=s1+s2
print(sum)
