x=3
if x>5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
#EXAMPLE-1 - EVEN&ODD
n=int(input("Enter a number:"))
if n%2==0:
    print("Even number")
else:
    print("Odd number")
#Example-2 - Positive & Negative
num=int(input("Enter num:"))
if num>0:
    print("Positive number")
else:
    print("Negative number")
#EXAMPLE-3 - Check if aperson is eligible to vote
age=int(input("Enter age:"))
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
#EXAMPLE-4 - Find the largest of two numbers
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
if a>b:
    print("a is greater")
else:
    print("b is greater")
#Example-5 - Check if a character is a vowel or consonant
character=input("Enter a character")
if character in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonant")
#EXAMPLE-6 PASSWORD VALID OR NOT
Password=input("Enter a password:")
a="prasanna"
if Password==a:
    print("VALID")
else:
    print("INVALID")
#Example-7 - LEAP YEAR OR NOT
year=int(input("Enter year:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")
#Example-8 - PASS OR FAIL
Marks=int(input("Enter marks:"))
if Marks>=40:
    print("PASS")
else:
    print("FAIL")
