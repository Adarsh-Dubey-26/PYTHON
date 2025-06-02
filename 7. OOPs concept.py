# OOPs: to  map real world scenarios, we use objects in code.
# This is called Object Oriented Programming (OOPs).
# We use concept of OOPs to reduce code redundancy and to make code reusable.
# Objects are instances of classes.
# Class is a blueprint for creating objects.
#NOTE Class vo blueprint h, jisme ham batate h ki Object m kya kya features hone chahiye.
# Class is a collection of attributes and methods. 
# Attributes are variables that belong to the class.
# Methods are functions that belong to the class. 

# class students:       # Basic syntax to create a class
#     name = "Adarsh"
# s1 = students()       # Basic syntax to create an object of a class
# print(s1.name)  

# CONSTRUCTOR: A constructor is a special method that is called when an object is created.
# It is used to initialize the attributes of the class. 
# __init__() is the constructor method in Python, all classes have this function, which is always executed when the object is initiated.

# class student:

#     #Default constructor
#     def __init__(self):
#         pass      # this is default constructor, agar ham nhi banayenge toh automatically ban jayega.

#     #Parameterized constructor
#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks

# s1 = student("Adarsh Dubey", 90) 
# print(s1.name, s1.marks) 
# s2 = student("Yugant Dubey", 89)
# print(s2.name, s2.marks)  

# ATTRIBUTES: Attributes are variables that belong to the class.
#   Class attributes which are common to all objects of the class
#   Instance(Object) attributes are specific to each instance of the class.

# class student:
#     # Class attribute
#     school = "ABC High School"

#     def __init__(self, fullname, marks):
#         # Instance attributes
#         self.name = fullname
#         self.marks = marks 

# print(student.school)   # Accessing class attribute using class name
# s1 = student("Adarsh Dubey", 90)    # Accessing instance attributes using object
# print(s1.name, s1.marks) 
# s2 = student("Yugant Dubey", 89)    # Accessing instance attributes using object
# print(s2.name, s2.marks)  



# Del Keyword: It is used to delete an object or an attribute of an object.
# eg: del s1 or del s1.name

# Private Attributes and Methods:
# In Python, we can make attributes and methods private by prefixing them with double underscores (__).



# METHODS: Methods are functions that belong to the class. 
# class student:
#     college_name = "XYZ College"
#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks

#     def welcome(self):
#         print("Welcome student", self.name, "to", self.college_name) 

#     def marks_info(self):
#         print("Marks of", self.name, "are", self.marks)
# s1 = student("Adarsh Dubey", 90)
# s1.welcome() 
# s1.marks_info() 



# TYPES OF METHODS: (Decorators are used to define the type of method)
    # 1. Instance Method: These are the most common type of methods. They take self as the first parameter and can access instance attributes and methods.
        # (self)
    # 2. Static Method: These are methods that don't use the self parameter and can be called on the class itself, rather than on an instance of the class.
        # @staticmethod

        # class student:
        #     @staticmethod           #Decorator
        #     def college():
        #         print("Welcome to ABC College")
        # s1 = student()
        # s1.college() 

    # 3. Class Method : Class methods are methods that are bound to the class and receive the class as the first argument, rather than an instance of the class.
        # @classmethod (__class__)

    # 4. Proerty Method: Property methods are used to define getters and setters for class attributes. They allow you to define methods that can be accessed like attributes.
        # @property

    # 5. Super Method: Used to access the parent class methods and attributes.
        # class car:
        #     def __init__(self, type):
        #       self.type = type
        #     @staticmethod
        #     def start():
        #         print("Car Started..")
        #     @staticmethod
        #     def stop():
        #         print("Car Stopped..")

        # class electric_car(car):
        #     def __init__(self, name, type):
        #         self.name = name
        #         super().__init__(type)  # Calling the type attribute of the parent class
        #         super().start()         # Calling the start method of the parent class

        # car1 = electric_car("Tesla", "Electric")
        # print(car1.name, car1.type) 

        
#  FUNDAMENTAL PRINCIPLES OF OOPs:

# -> Abstraction: Hiding the implementation details of class and only showing the essential features to the user.
# class car:
#     def __init__(self):
#         self.accelerator = False
#         self.brk = False
#         self.clutch = False
    
#     def start(self):
#         self.accelerator = True
#         self.clutch = True
#         print("Car Started..") 

# car1 = car()
# car1.start()       
        # Here we hide the implementation details of how the car starts, we just show the essential feature of starting the car.



# -> Encapsulation: Wrapping data and functions into a single unit(object). 
    # Class in which has attributes and methods is an example of encapsulation.
    # Code we wrote till now is examples of encapsulation.




# -> Inheritance: When one class derives the property and method of another class.
# class car:
#     @staticmethod
#     def start():
#         print("Car Started..")
#     @staticmethod
#     def stop():
#         print("Car Stopped..")

# class electric_car(car):
#     def __init__(self, name, mileage):
#         self.name = name
#         self.mileage = mileage

# car1 = electric_car("Tesla", 300)
# car2 = electric_car("Nissan", 350) 

# print(car1.name, car1.mileage, car1.start())
# print(car2.name, car2.mileage, car2.start())

    # Types of Inheritance:
        # 1. Single Inheritance: One class inherits from another class.
        # 2. Multiple Inheritance: One class inherits from multiple classes.
        # 3. Multilevel Inheritance: One class inherits from another class, which in turn inherits from another class.
        # 4. Hierarchical Inheritance: Multiple classes inherit from a single class.
        # 5. Hybrid Inheritance: A combination of multiple inheritance and multilevel inheritance.


# -> Polymorphism: The ability of different classes to be treated as instances of the same class through a common interface.
# Best examples of polymorphism are operator overloading and method overriding.
# operator overloading:  When the same operator is allowed to have different meaning according to the context.
    # EX: simplest example of operator overloading,
# print(5 + 10)               # Addition of two integers
# print("Hello " + "World")   # Concatenation of two strings
# print([1, 2] + [3, 4])      # Concatenation of two lists






# PRACTISE QUESTION:
# Q.1: Create astudent class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average.
# class student:
#     def __init__(self, name, marks1, marks2, marks3):
#         self.name =  name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3

#     def average(self):
#         avg = (self.marks1 + self.marks2 + self.marks3) / 3
#         print("Average of marks are: ", avg)

# name = input("Enter your name: ")
# marks1 = int(input("Enter marks of subject 1: "))
# marks2 = int(input("Enter marks of subject 2: "))
# marks3 = int(input("Enter marks of subject 3: "))
# s1 = student(name, marks1, marks2, marks3) 
# s1.average() 


# Q.2: Create account class with 2 attributes, balance and account number. Create methods for debit, credit and printing the balance. 
# class account:
#     def __init__(self, acc_num, balance):
#         self.acc_num = acc_num
#         self.balance = balance
    
#     def debit(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount      # balance = balance - amount
#             print("Debited amount: ", amount)
#         else:
#             print("insufficient balance")
    
#     def credit(self, amount):
#         self.balance += amount          # balance = balance + amount
#         print("Amount Credited: ", amount)

#     def print_balance(self):
#         print("Current balance: ", self.balance)

# acc_num = input("Enter account number: ")
# balance = float(input("Enter initial balance: "))

# acc1 = account(acc_num, balance)
# acc1.print_balance()

# acc1.debit(float(input("Enter amount to debit: ")))
# acc1.print_balance()

# acc1.credit(float(input("Enter amount to credit: ")))
# acc1.print_balance() 


# Q.3: Create a circle class to create a circle with radius r suing the constructor. Define an area() method of the class which calculates the area of the circle.
    # define perimeter() method of the class which allows you to calculate the perimeter of the circle.
# class circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         area = 3.14 * self.radius ** 2
#         print("Area of the circle of radius", self.radius, "is: ", area)
#     def perimeter(self):
#         perimeter = 2 * 3.14 * self.radius
#         print("Perimeter of the circle with radius", self.radius, "is: ", perimeter)

# radius = float(input("Enter the radius of the circle: "))
# c1 = circle(radius)
# c1.area()
# c1.perimeter()


# Q.4: Define a Employee class eith attributes role, department and salary. This also has a showdetails() method.
    # Create an engineer class that inherits properties from employee and has additional attributes : name and age.
# class employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
#     def showdetails(self):
#         print("Role: ", self.role)
#         print("Department: ", self.department)
#         print("Salary: ", self.salary)

# class engineer(employee):
#     def __init__(self, name, age, role, department, salary):
#         super().__init__(role, department, salary)
#         self.name = name
#         self.age = age
#     def showdetails(self):
#         super().showdetails()
#         print("Name: ", self.name)
#         print("Age: ", self.age) 

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# role = input("Enter your role: ")
# department = input("Enter your department: ")
# salary = float(input("Enter your salary: "))
# e1 = engineer(name, age, role, department, salary)
# e1.showdetails()  