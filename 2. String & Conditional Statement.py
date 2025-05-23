#STRING 

# str1 = "This is a String."  #We can use single, double and triple quotes. 

#escape sequence charater: used for formating, e.g: tab space, next line, etc. 
# \n : escape sequence charater for next line. 
# str = "My name is Adarsh. \nMy age is 21."
# print(str)
# \t : escape sequence charater for tab space. 
# str = "My name is Adarsh. \tMy age is 21."
# print(str)

#operation on string:
# concatenation: used to join two string, e,g: "hello"+"world" = "helloworld". 
# str1 = "Adarsh"
# str2 = "Dubey"
# print(str1+str2) 

#Length of string: len(str)
# str = "I am Adarsh Dubey"
# print(len(str))

#Indexing
# str = "ADARSH"
# print(str[1])     #By indexing we can access the data at the particular location but cannot manipulate it. 

#Slicing : Accessing part of a string
#e.g: str[starting index : ending index] ending index not included
# str = "ADARSH DUBEY"
# print(str[1:4])
# print(str[:4])
# print(str[4:])
# print(str[5:8]) 

# str = "APPLE"    #Negative indexing(starts from right to left, here also last index will not be inckuded. )  
# # A   P   P   L   E   
# # -5 -4  -3  -2  -1
# print(str[-5:-2]) 


#String Function
# str = "i am Adarsh Dubey"
# print(str.endswith("ey"))      #returns True if string ends with "ey" 
# print(str.capitalize())        #capitalize 1st character
# print(str.replace("a" , "o"))  #replaces all occurrrrence of old with new
# print(str.find("s"))           #return 1st index of 1st occurrence
# print(str.count("Dubey"))      #counts the occurrence of substring in string


#PRACTISE QUESTION bas on Strings. 
#Q.1: WAP to input user's first name and prnt its length. 
# a = str(input("Enter your name: "))
# print(len(a)) 

#Q.2: WAP to find the occurrence of a particular letter in a string. 
# str = "qwertyuiolkjhgfdsazxcvbnmkjhgfdsaqwertyuiussaaasas"
# print(str.count("s"))












#CONDITIONAL STATEMENT.
# age = 20
# if(age >= 18):
#     print("You can apply")

# light = "green"
# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("look")
# elif(light == "green"):
#     print("go")

#In "if" statement always checks, whereas "elif" statement checks only when if condition is false. 
# num = 5
# if(num > 2):
#     print("greater tha 2")
# if(num > 3):
#     print("greater than 3")

# if(num > 2):
#     print("greater tha 2")
# elif(num > 3):
#     print("greater than 3")



#else: if all above conditions are false we print default value in else condition. 
# light = "pink"
# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("look")
# elif(light == "green"):
#     print("go")
# else:
#     print("lights is broken")

# marks = int(input("Enter marks obtained= "))
# if(marks >= 90):
#     grade = "A" 
# elif(90 > marks >= 80):
#    grade = "B"
# elif(80 > marks >= 70):
#     grade = "C"
# else:
#     grade = "D"

# print("Grade obtained by student is -> ", grade)


#PRACTICE QUESTIONS. 
# Q.1: WAP to check if a number entered by the user is odd or even. 
# x = int(input("Enter a number: "))
# if(x%2 == 0):
#     print("EVEN")
# else:
#     print("ODD") 

# Q.2: WAP to find the greatest of 3 numbers entered by user. 
# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# z = int(input("Enter a number: "))
# if(x > y and x > z):
#     print("X is the greatest number.")
# elif(y>x and y>z):
#     print("Y is the greatest number.")
# else:
#     print("Z is the greatest number.")


# Q.3: WAP to check if a number is a multiple of 7 or not. 
# x = int(input("enter a number = "))
# if(x%7 == 0):
#     print("Multiple of 7")
# else:
#     print("Not a multiple of 7") 