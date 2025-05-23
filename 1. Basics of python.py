# #Simplpe PRINT STATEMENT. 
# print("Adarsh Dubey")





# #VARIABLES.     
# name = "Adarsh"   #string will be always in double quotes.    
# age = 21
# height = 172.66

# print(name)
# print("name")   #The difference is of double quotes. 

# print("My name is ", name)
# print("My age is ", age)
# print("My name is ",name , "and my age is ",age)

# #since age=21, by using assignment operator we can assign the the value of this variable to another variable.
# age2 = age
# print(age2) 





# #DATATYPES 
# #(PRIMARY Datatypes- Integer, String, Float, Boolean, None)
# print(type(name))
# print(type(age))
# print(type(height))

# old = False     #Boolean datatype
# a = None        #None datatype
# print(type(old))    
# print(type(a))





# #KEYWORDS : Words reserved in python which we can not use for making variable/identifiers.
# #keywords->   and     as      assert      break       class       continue        def     elif        else        except      finally    
# # False       for     from     global      if      import      in      is      lambda      nonlocal        None        not     or     
# # pass        raise       return      True        try     with    while       yield 
# # Python is a case sensitive programming language.





# #PRINT SUM/SUBTRACT/MULTIPLY/DIVIDE
# a = 2
# b = 4
# sum = a+b
# print(sum)





# # OPERATORS : are symbols that perform a certain operations between operands. 
# # Arithmatic Operators: ( + , - , * , / , ** , % )
# print(a+b)      
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)     #a^b
# print(a%b)      #remainder

# # Relational Operators: ( == , != , > , < , >= , <= )
# print(a == b)
# print(a != b)
# print(a >= b)
# print(a > b)
# print(a <= b)
# print(a < b)

# # Assignment Operators: ( = , += , -= , /= , %= , **= )
# num = 10
# num = num + 10  #10+10
# num += 10       #10+10
# num -= 10       #10-10
# num *= 5        #10*10
# num /= 5        #10/10
# num %= 5        #10%5
# num **= 5       #10^5

# # Logical Operators   : ( not , and , or )
# print(not False)        #not -> opposite
# print(not True)

# val1 = True
# val2 = True
# print("and operator: ", val1 and val2)
# print("or operator: ", val1 or val2) 





# #TYPE CONVERSION
# c = 5
# d = 5.345
# sum = c+d       #Pyhton automatically converts integer into float for giving sum. 

# #TYPE CASTING
# x = "3"
# print(type(x))  #this is string
# x = int(x)
# print(type(x))  #Here we type-casted the string into a integer value. 
# # A string cannot be type-casted into integer/float. Only a number stored as a string can be type-casted or vice versa. 
# y = 5
# print(x+y)





# #INPUTS 
# name = input("Enter your name: ")
# print("WELCOME", name)      #Default datatype STRING. 
# print(type(name))

# val = int(input("enter a value: "))
# print(type(val), val)       #TYPE-CASTED the value into integer value

# val = float(input("enter a value: "))
# print(type(val), val)       #TYPE-CASTED the value into float value


# #example:
# name = input("Enter name: ")
# age = input("Enter age: ")
# marks = input("Enter marks: ")

# print("WELCOME", name)
# print("Age =", age)
# print("Marks =",marks)




#PRACTISE QUESTIONS:
#Q.1: WAP to input two numbers and print their sum. 
# a = int(input("Enter value: "))
# b = int(input("Enter value: "))
# print("sum: ", a+b)

#Q.2: WAP to input side of a square and print its area. 
# a = int(input("Enter side of square: "))
# print("Area of square: ", a*a)

#Q.3: WAP to input two floating points numbers and print their average.
# a = float(input("Enter a value: ")) 
# b = float(input("Enter a value: "))
# print("The average of given two nummbers are: ", (a+b)/2) 

#Q.4: WAP to input two integer number, a and b. Print True if 'a' is greater than or equal to 'b' , if not print False.
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# print(a>=b)