# 11-08-2025
# Encapsulation 
# Hides implementation of code
# Abstraction divides into abstract class and abstract methods 
# abc - Abstract base class -> Module 
# Syntax 
# from abc import ABC,abstract method 
#    class classname(abc):
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod 
    def stop(self):
        pass 
class Car(Vehicle):
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")
c=Car()
c.start()
c.stop()

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod 
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")
class Bike(Vehicle):
    def start(self):
        print("Bike started")
    def stop(self):
        print("Bike stopped")
c=Car()
c.start()
c.stop()
d=Bike()
d.start()
d.stop()

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod 
    def stop(self):
        pass 
    @abstractmethod 
    def speed(self):
        pass
    @abstractmethod 
    def cost(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")
    def speed(self):
        print("Car speed")
    def cost(self):
        print("Car cost")
class Bike(Vehicle):
    def start(self):
        print("Bike started")
    def stop(self):
        print("Bike stopped")
    def speed(self):
        print("Bike speed")
    def cost(self):
        print("Bike cost")
c=Car()
c.start()
c.cost()
d=Bike()
d.speed()
d.stop()
#ABSTRACT METHOD 
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
#Subclass-1
class Dog(Animal):
    def sound(self):
        return "Dog Bow Bow..."
#Subclass-2
class Cat(Animal):
    def sound(self):
        return "Cat Meow Meow..." 
k=[Dog(),Cat()] 
for a in k:
    print(a.sound())
#Example-2 
from abc import ABC, abstractmethod 
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass
    @abstractmethod
    def refund(self):
        pass 
class CreditCardPayment(PaymentGateway):
    def pay(self):
        return "Paid amount via Credit Card"
    def refund(self):
        return "Refunded amount to Credit Card"
class UPIPayment(PaymentGateway):
    def pay(self):
        return "Paid amount via UPI"
    def refund(self):
        return "Refunded amount to UPI"
j=[CreditCardPayment(),UPIPayment()]
for k in j:
    print(k.pay())
    print(k.refund())
#Online Shopping Discount System
from abc import ABC, abstractmethod
class Product(ABC):
    def __init__(self,name,price):
        self.name=name 
        self.price=price 
    @abstractmethod
    def calculate_discounted_price(self):
        pass 
class Electronics(Product):
     def calculate_discounted_price(self):
         return self.price - (self.price*0.10)
class Clothing(Product):
     def calculate_discounted_price(self):
         return self.price - (self.price*0.20)
class Groceries(Product):
     def calculate_discounted_price(self):
         return self.price - (self.price*0.05)
name1=input("Enter the name for Electonics:")
price1=float(input("Enter the price for Electronics:"))
name2=input("Enter the name for Clothing:")
price2=float(input("Enter the price for Clothing:"))
name3=input("Enter the name for Groceries:")
price3=float(input("Enter the price for Groceries:"))
k=[Electronics(name1,price1),Clothing(name2,price2),Groceries(name3,price3)]
for d in k:
    print(f"{d.name} - Original Price {d.price} - Discounted Price {d.calculate_discounted_price()}")
