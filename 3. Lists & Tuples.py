#LISTS : A build-in datatype that stores set of values, It can store elements of different types (int, float, string, etc). 
# marks = [23, 34, 45, 56, 67, 78, 89, 90]
# print(type(marks))
# print(len(marks))
# print(marks)
# print(marks[0])
# print(marks[4]) 

#In python LIST we can store data of different types. 
# students = ["Adarsh", 98, "Male", 21, "Jaipur"]
# print(student) 

#string-> Immutable: means not changable
#Lists-> mutable: means changable 
#In strings we can access the data but cannot change it, whereas in lists in python allows us to acess the data as well as change also. 
#example:- 
# str = "HELLO"
# print(str[0])
# str[0] = "Y"    #this is not possible in string datatype, as it is immutable. 

# students = ["Adarsh", 98, "Male", 21, "Jaipur"]
# print(students)   
# print(students[0])
# students[0] = "Adarsh Dubey"
# print(students)   #Since lists are mutable, we can change its data. 


#List Slicing: cutting out the part of the list. 
#syntax-> list_name[starting_idx : ending_idx]   ending index is not included. 
# marks = [23, 34, 45, 56, 67, 78, 89]
# print(marks[2:4])
# print(marks[2:])
# print(marks[:4])
# print(marks[-3:-1]) 


#List Methods:- 
# list = [4, 8, 2, 5, 0, 7, 9, 1]
# print(list) 
# list.append(6)      #adds element at the end
# print(list) 
# list.sort()         #sorts in ascending order, we can also sort strings. 
# print(list) 
# list.sort(reverse = True)   #sorts in decending order
# print(list) 
# list.reverse()       #reverse list, make change in original list. 
# print(list) 
# list.insert(2, 3)   #insert element at index (idx, el)
# print(list) 
# list.remove(8)      #removes first occurrence of element, make change in original list. 
# print(list)
# list.pop(3)         #removes element at index 3, make change in original list. 
# print(list) 











# TUPLES:- A build-in datatype that lets us create immutable sequence of values, immutable means not changable.

# Basic difference between list and tuple is that list is mutable and tuple is immutable.
# and list is created using [] brackets and tuple is created using () brackets.
# tuple = (4, 8, 2, 5, 0, 7, 9, 1)    #we can print empty tuple as well.
# print(tuple)
# print(type(tuple))
# print(len(tuple))
# print(tuple[0])
# tuple[0] = 5   #this is not possible in tuple datatype, as it is immutable.

# tup =  (1,)     #this is a tuple with single element, we need to put comma after the element to make it a tuple.
# print(type(tup))
# tuple =  (1)     #this is not a tuple, this is a set.
# print(type(tuple)) 

# Tuple Methods:-
# tuple = (2, 3, 7, 5, 0, 7, 9, 1, 7, 8, 7, 6, 4, 3, 2)

# tuple.index(7)   #returns the index of first occurrence of element.
# print(tuple.index(7))

# tuple.count(7)   #returns the count of element in tuple.
# print(tuple.count(7)) 



#PRACTISE QUESTIONS:- 
# Q.1: WAP to ask the user to enter name of their 3 favorite movies and store them in a list.
# movies = []
# movie1 = input("Enter your 1st favorite movie: ")
# movie2 = input("Enter your 2st favorite movie: ")
# movie3 = input("Enter your 3st favorite movie: ")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)

# movies.append(input("Enter your 1st favorite movie: "))
# movies.append(input("Enter your 2st favorite movie: "))
# movies.append(input("Enter your 3st favorite movie: "))
# print(movies)



# Q.2: WAP to check is a list contains a palindro1me of elements.
# list = [1, 2, 3, 2, 1]
# copy_list = list.copy()  #copy the original list
# copy_list.reverse()
# if copy_list == list:
#     print("The given list is palindrome.") 
# else:
#     print("The given list is not palindrome.") 




# Q.3: WAP to count the number of students with the grade "A" in the following tuple.
# grades = ("A", "B", "C", "A", "D", "A", "B", "C", "A", "E", "A", "B", "C", "D", "E", "A", "B", "C", "D", "E")

# grades.count("A") 
# print("The number of students with grade A is: ", grades.count("A")) 
# grades.count("B") 
# print("The number of students with grade A is: ", grades.count("B")) 
# grades.count("C") 
# print("The number of students with grade A is: ", grades.count("C")) 
# grades.count("D") 
# print("The number of students with grade A is: ", grades.count("D")) 
# grades.count("E") 
# print("The number of students with grade A is: ", grades.count("E")) 


# Q.4: WAP to store values in a list and sort them from "A" to "D". 
# list = ["D", "A", "C", "B"]
# list.sort()
# print(list)