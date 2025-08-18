#18-08-2025
#BUILT-IN FUNCTIONS  
#1.MATH FUNCTION
import math 
#sqrt - Square root of a number
print("Square root value:",math.sqrt(25))
#factorial - Factorial of a number
print("Factorial value:",math.factorial(5))
#ceil - Greatest value after given number if after point is in betwwen 1 to 9 or 01 to 99
print("Poitive ceil value:",math.ceil(8.99)),print("Negative ceil value:",math.floor(-4.01))
#floor - Same value  if after point is in betwwen 0 to 9 
print("Positive floor value:",math.floor(8.99)), print("Negative floor value:",math.floor(-3.1))
#gcd - Greatest Common Divisor 
print("GCD of two numbers:",math.gcd(10,20))
#Pi Value Constant
print("Pi value:",math.pi)
#e Value Constant
print("e value:",math.e)
#power value - (Base value,power value)
print("Power value:",math.pow(2,4))
#log value - Log value using base and power 
print("Log value:",math.log(10)),print("Log value:",math.log(10,2))
#lcm - Least Common MUltiple 
print("LCM Of two numbers:",math.lcm(2,4,6,18,9))  
#2.RANDOM FUNCTION 
import random
#random() - Random float between 0.0 to 1.0 
print(random.random())
#randint() - Random number in between range
print(random.randint(1,10))
#randrange() - Random number in between range
print(random.randrange(1,100))
#choice() - It prints random value in given tuple or list
a=["Prasanna","Hardik","Nani","Bhaskar","Ammu","Kumari"]
print(random.choice(a))
#shuffle() - It shuffle the items in the given list 
b=["rose","lilly","jasmine","mari-gold"]
random.shuffle(b)
print(b) 
#Using both math and random functions
import math,random 
print(math.pi,random.random())
