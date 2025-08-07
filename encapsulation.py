#07-08-2025
#Encapsulation
#Get - To retrieve the data
#Set - To update or insert the data
#Access Modifiers - Public,Protect,Private  
#Public - self.variablename
#Protect - self._variablename
#Private - self.__variablename
#Public
class Student:
    def __init__(self):
        self.name="Prasanna"
obj=Student()
print(obj.name)
#Protect
class Student:
    def __init__(self):
        self._a="Bhaskar"
obj=Student()
print(obj._a)
#Private
class Student:
    def __init__(self):
        self.__b="Hanuman"
obj=Student()
print(obj._Student__b)
#get and set
class Student:
    def __init__(self):
        self.__c=""
    def set_name(self,n):
        self.__c=n 
    def get_name(self):
        return self.__c 
obj=Student()
obj.set_name("Prasanna")
print(obj.get_name())
#Combination of all 
class Employee:
    def __init__(self,emp_id,name,salary,department):
        self.emp_id=emp_id
        self.__name=name
        self.__salary=salary
        self._department=department 
    def set_salary(self,new_salary):
        if new_salary>0:
           self.__salary=new_salary 
        else:
            print("Invalid salary. Must be positive.")
    def get_salary(self):
        return self.__salary  
    def set_name(self,new_name):
        if new_name.strip()!="":
            self.__name=new_name 
        else:
            print("Name cannot be empty.")
    def get_name(self):
        return self.__name 
    def display_employee(self):
        print("\nEmployee Details")
        print("---------------------")
        print(f"Employee ID    :  {self.emp_id}")
        print(f"Employee Name  :  {self.__name}")
        print(f"Department     :  {self._department}")
        print(F"Employee Salary :  {self.__salary}")
s=Employee(100,"Prasanna",80000,"Software Developer")
print("Public ID:", s.emp_id)
print("Protected Department:", s._department)
print("Private Name:", s.get_name())
print("Private Salary:", s.get_salary())
s.set_name("Prasanna Kuchipudi")
s.set_salary(90000)
s.set_name("")
s.display_employee()
