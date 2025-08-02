#31-07-2025
# class car:
#     color="Black" #class variable
#     model="Thar"
# car1=car()
# b=car()
# print(car1.color)
# print(b.model) 
# class movie:
#     def __init__(self,movie_name,release_year):
#          self.movie_name=movie_name
#          self.release_year=release_year
# a=movie("HI NANNA",2023)
# b=movie("Shyam Singha Roy",2021)
# print(a.movie_name)
# print(b.release_year) 
#Instance method
# class Student:
#     def __init__(self,name,course): #method
#         self.name=name
#         self.course=course
#     def student_details(self,city,course_year):
#         self.city=city
#         self.course_year=course_year
# c=Student("Prasanna","B.Tech") #instance variable
# d=Student("Bhaskar","M.B.B.S")
# c.student_details("Hyderabad",2022)
# d.student_details("Banglore",2021)
# print(c.name)
# print(d.course_year)
# #Class method
# class Person:
#     age=16
#     @classmethod
#     def update_age(cls,count):
#         cls.age=count 
# Person.update_age(18)
# print(Person.age)
# #Static method  
# class Person:
#     @staticmethod 
#     def hello():
#         print("Hello All")
# Person.hello()
# #Removing spaces and special characters in a string
# n=input()
# str=""
# for i in n:
#     if i.isalnum() or i.isspace():
#         str+=i
# print(str) 
#Write a python program to print second largest number in list (without using max(),sort())
