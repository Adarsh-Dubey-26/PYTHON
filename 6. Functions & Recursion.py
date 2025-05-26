# FUNCTIONS: Block of statements that perform a specific task.

# def sum(a, b):        #Function definition; # a & b are parameters.
#     sum = a+b
#     print(sum)
#     return sum
# sum(5, 6)             #Function call "sum"; # 5 & 6 are arguments.

# We use functions to reduce redundancy in code, to make it reusable, and to improve readability.

# def avg(a, b, c):
#     avg =  (a + b + c)/ 3
#     return avg
# Average = avg(7, 8, 9)
# print(Average) 


# TYPES OF FUNCTIONS:
# 1. Built-in Functions: Functions that are already defined in Python.
    #    Example: print(), len(), type(), range(), etc. 
# 2. User-defined Functions: Functions that are defined by the user.
# 3. Lambda Functions: Anonymous functions defined using the lambda keyword.
# 4. Recursive Functions: Functions that call themselves to solve a problem.

# DEFAULT PARAMETERS:
# def prod(a = 1, b = 2):
#     print(a*b)
#     return a*b
# # prod() 
# # prod(5) 
# # prod(a = 1, b = 6)  
# prod(5, 7)


# PRACTICE QUESTIONS: 
# Q.1: WAP to print the length of a list. 
# list_1 = ["apple", "banana", "cherry", "watermelon", "kiwi", "orange"]
# list_2 = ["Ironman", "captain america", "thor", "loki", "hulk"]

# def list_len(list):
#     print(len(list))
#     return len(list)

# list_len(list_1)
# list_len(list_2) 


# Q.2: WAP to print the element of a list in a single list.
# fruits = ["apple", "banana", "cherry", "watermelon", "kiwi", "orange"] 
# def element(list):
#     for item in list:
#         print(item, end = " ") 
#     return item
# element(fruits) 


# Q.3: WAP to find the factorial of n.
# def factorial(n):
#     fact = 1
#     for i in range (1, n+1):
#         fact *= i
#     print(fact)
#     return fact

# factorial(5) 
    #OR
# def factorial(n):
#     if n ==0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5)) 



# Q.4: WAP to convert USD to INR.
# def con(usd):
#     inr = usd * 80
#     print(inr)
#     return inr 
# con(78) 



# Q.5: WAP to find the number is even or odd.
# def num(n):
#     if n%2 == 0:
#         return "EVEN NUMBER"
#     else:
#         return "ODD NUMBER"
# # print(num(6)) 
# n = int(input("Enter a number: ")) 
# print(num(n)) 




# RECURSION: When a function calls itself repeatedly.  
# def show(n):
#     if (n ==0):
#         return
#     print(n)
#     show(n-1)
#     print("end")
# show(5) 

# def fact(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(6)) 

#NOTE : Recursion works as a stack.
#NOTE : Recursion is used to solve problems that can be broken down into smaller subproblems.
#NOTE : Recursion can lead to stack overflow if the recursion depth is too high.
#NOTE : Recursion is not always the best solution for every problem, as it can be less efficient than iterative solutions in some cases.


# PRACTICE QUESTIONS:
# Q.1: WAP T]to find the sum of first n natural numbers using recursion function.
# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n-1)

# n = int(input("Enter a number: "))
# print("Sum of first", n, "natural numbers is:", sum(n)) 



# Q.2: WAP to print all element of a list using recursion.
# list = ["apple", "banana", "cherry", "watermelon", "kiwi", "orange"]
# def element(list, idx = 0):
#     if idx < len(list):
#         print(list[idx])
#         element(list, idx+1)
#     else:
#         return 
# element(list)