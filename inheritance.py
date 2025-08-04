#04-08-2025
#Inheritance 
#Single Inheritance - One parent class and one chid class
class Parent:
    def greet(self):
        print("Hello")
class child(Parent):
    def greeks(self):
        print("Hi")
b=child()
b.greeks()
b.greet()
#Multi-Level Inheritance (diferent function names)
class Nani:
    def Eega(self):
        print("Samantha")
class Ntr(Nani):
    def Temper(self):
        print("Kajal")
class Arjun(Ntr):
    def Pushpa(self):
        print("Rashmika")
M=Arjun()
M.Pushpa()
M.Temper()
M.Eega()
#Multilevel Inheritance (same function names)(downward) (Overrides parent method)
class GrandParent:
    def greet(self):
        print("Hi from GrandParent")
class Parent(GrandParent):
    def greet(self):
        print("Hi from Parent")
class Child(Parent):
    def greet(self):
        print("Hi from Child")
obj=Child()
obj.greet()
#Multiple Inheritance (Inherits from multiple parents)(Different Function Name)
class Nani:
    def ShyamSinghaRoy(self):
        print("Sai Pallavi")
class Dulquer:
    def SitaRamam(self):
        print("Mrunal Thakur")
class AlluArjun(Nani,Dulquer):
    def DJ(self):
        print("Pooja Hegde")
obj=AlluArjun()
obj.DJ()
obj.SitaRamam()
obj.ShyamSinghaRoy()
#Multiple Inheritance (Same Function Name)
class Grandparent:
    def hi(self):
        print("Hello from GrandParent")
class Parent:
    def hi(self):
        print("Hello from Parent")
class Child(Grandparent,Parent):#First inherited class function output printed
      pass 
obj=Child()
obj.hi()
#Multiple Inheritance (Same Function Name)(Override grandparent and parent method)
class Grandparent:
    def hi(self):
        print("Hello from GrandParent")
class Parent:
    def hi(self):
        print("Hello from Parent")
class Child(Grandparent,Parent):
    def hi(self):
        print("Hello from Child")
obj=Child()
obj.hi()
#Hierarchical Inheritance(Overides Previous methods)(same function names)
class Parent:
   def hi(self):
        print("Parent")
class Child1(Parent):
    def hi(self):
        print("Child1")
class Child2(Parent):
    def hi(self):
        print("Child2")
c=Child1()
B=Child2()
c.hi()
B.hi()
#Hierarchical Inheritance(Overides Previous methods)(different function names)
class Parent:
   def hi(self):
        print("Parent")
class Child1(Parent):
    def hello(self):
        print("Child1")
class Child2(Parent):
    def hee(self):
        print("Child2")
c=Child1()
B=Child2()
c.hi()
c.hello()
B.hi()
B.hee()
#Hybrid Inheritance - Combination of different types of Inheritances 
class fruits:
    def yellow(self):
        print("Mango")
class flowers:
    def red(self):
        print("Rose")
class vegetables(fruits, flowers):  # Multiple Inheritance
    def green(self):
        print("Mirchi")
class leaf(vegetables):  # Multilevel Inheritance
    def brown(self):
        print("Dry Leaf")
obj = leaf()
obj.brown()
obj.green()
obj.yellow()
obj.red()
#Super Keyword
class Cricket:
    def Hardik(self):
        print(" Right‑hand batter")
class Cricket2(Cricket):
    def Hardik(self):
        print("Right‑arm medium fast bowler")
        super().Hardik()
h=Cricket2()
h.Hardik()