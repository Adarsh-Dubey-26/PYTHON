# LOOPS: These are repeated instructions. 
# While loops, for loops, and nested loops are common types.

# WHILE LOOP: It executes a block of code as long as a specified condition is true.
# count = 1
# while count <= 5:
#     print("hello")
#     count += 1
# print(count)
#         #NOTE: here we say iterators and iteration, here count is the iterator and the number of times the loop runs is the iteration.


#PRACTISE QUESTIONS: 
# Q.1: Print numbers froms 1 to 100.
# count = 1
# while count <=100:
#     print(count)
#     count += 1


# Q.2: Print number from 100 to 1.
# i =  100
# while i >= 1:
#     print(i)
#     i -= 1



# Q.3: Print the multiplication table of number n.
# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(n*i) 
#     i += 1  



# Q.4: Print the element of the following list.
# i = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# index = 0
# while index <= len(i) - 1:
#     print(i[index])
#     index += 1




# Q.5: Search for a number in the tuple.
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# num = int(input("Enter the number to be searched: "))
# idx = 0
# while idx <= len(tup):
#     if (tup[idx] == num):
#         print("Number is found at index: ", idx)
#     else:
#         print("Number not found at index: ", idx)
#     idx += 1






# BREAK AND CONTINUE STATEMENTS:
# BREAK: It is used to exit the loop prematurely.
# i = 1
# while i <= 10:
#     print(i)
#     if i == 5:
#         break    # This will exit the loop when i is 5.
#     i += 1
   
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# num = int(input("Enter the number to be searched: "))
# idx = 0
# while idx <= len(tup):
#     if (tup[idx] == num):
#         print("Number is found at index: ", idx)
#         break
#     else:
#         print("Number not found at index: ", idx)
#     idx += 1


# CONTINUE: It is used to skip the current iteration and continue with the next iteration.
# i = 1
# while i <= 10:
#     if i == 5:      
#         i += 1
#         continue    # This will skip the current iteration when i is 5 and continue with the next iteration.
#     print(i)
#     i += 1


# i = 1
# while i <= 100:
#     if (i%2 == 0):
#         i += 1
#         continue
#     print(i) 
#     i += 1


# i = 1
# while i <= 100:
#     if (i%2 != 0):
#         i += 1
#         continue
#     print(i) 
#     i += 1






# FOR LOOP: It is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.

# Q.1: print the elements of the list.
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for i in list:
#     print(i)


# Q.2: Search for a number in the tuple>
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("Print the number to be searched: "))
# for i in tup:
#     if (i == x):
#         print("Number found at index: ", tup.index(i))


# for i in range(10):
#     print(i)

# for n in range (4,9):       #(start, end) start-> included. end-> not included.
#     print(n)


# for i in range (2, 101, 2):  
#     # Here (start, end, step) start-> included. end-> not included. step-> increment by 2.
#     print(i) 


#PRACTISE QUESTIONS:
# Q.1: Print numbers from 1 to 100.
# for i in range(1, 101):
#     print(i)


# Q.2: Print numbers from 100 to 1. 
# for i in range (100, 0, -1):
#     print(i)


# Q.3: Print the multiplication table of number n.
# n = int(input("Enter a number: "))
# for i in range (1, 11):
#     print(n*i)


#NOTE: We have a "pass" statement which do nothing. It is used as a placeholder for future code.
# for i in range (1, 11):
#     pass 


# Q.4: WAP to find the sum of first n number.
# n = int(input("Enter a number: "))
# i = 0
# sum = 0
# # while i < n:
# #     i += 1
# #     sum = sum + i

# for i in range(1, n+1):
#     sum += i 
   
# print("Sum of first", n, "number is: ", sum)  




# Q.5: WAP to find the factorial of n number.
# n = int(input("Enter a number: "))
# fact = 1
# # for i in range (1, n+1):
# #     fact *= i
# while n > 0:
#     fact *= n
#     n -= 1
# print("Factorial of given number is: ", fact)