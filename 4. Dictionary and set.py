# DICTIONARY : Dictionary are used to store data values in key:value pairs. 
# A dictionary is a collection which is unordered, changeable (mutable) and do not allow duplicates.

# dict = {
#     "name": "Adarsh",
#     "age": 21,
#     "cgpa": 9.8,
#     "isMale": True,
#     "hobbies": ["coding", "reading", "gaming"],
#     "address": "jaipur"
# }
# print(dict) 

# #We can perform various operations on dictionary like we do on lists. 
# dict["name"] = "Adarsh Dubey" 
# dict["address"] = "Ujjain"
# dict["surname"] = "Dubey"
# print(dict) 

# null_dict = {}  
# print(null_dict)

# student = {
#     "name": "Adarsh",
#     "address": {                    #nesting of dictionary
#         "street": "Mansarovar",
#         "city": "Jaipur",
#         "state": "Rajasthan",
#         "country": "India"
#     }
# }
# # print(student) 
# print(student["address"])


# DICTIONARY METHODS:
# dict.keys()        #returns all the keys of the dictionary
# dict.values()      #returns all the values of the dictionary
# dict.items()       #returns all the key-value pairs of the dictionary
# dict.get("name")   #returns the value of the key 
# dict.update({"name": "Adarsh Dubey"})  #updates the value of the key
# dict.pop("isMale")   #removes the key-value pair from the dictionary






# SET: A set is a collection which is unordered, unchangeable (immutable) and unindexed.
# Sets are mutuable but the elements of the set are immutable. 
# Each element is unique (no duplicates).
# We can store data of different types in set like bool, int, float, string, tuple, etc. 
# But we cannot store list, dict, in a set as the are mutable.

# nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(type(nums)) 
# print(len(nums))
# print(nums) 

# set = {1, 2, 2, 2, "hello", "world", "world"}   # Set does not allow duplicates, it ignores them.
# print(set)

# null_set = set()   #empty set, if we use {} it will create empty dictionary.

# SET METHODS:
# set = {1, 2, 3, 4, 5, 6, "hello", "world", 9}
# set.add(10)                    #adds element to the set, we can add any data type, but not list and dict. 
# set.add((23, 45))              #adds tuple to the set.
# # set.add([56, 78])            #throws error as we cannot add list to the set. 
# set.remove(5)                  #removes element from the set, if not present it throws error.
# set.discard(6)                 #removes element from the set, if not present it does not throw error.
# set.pop()                      #removes last element from the set
# set.clear()                    #clears the set
# set.union(set2)           #returns the union of two sets(combines both sets)
# set.intersection(set2)    #returns the intersection of two sets(common elements) 
# print(set) 
 




# PRACTICE QUESTIONS:
# Q.1: Store words meaning in dictionary and print the meaning of the word. 
# dict = {}
# dict["hello"] = "A greeting or expression of goodwill."
# dict["world"] = "The earth or globe, considered as a planet."
# dict["python"] = ["A high-level programming language.", "A large non-venomous snake."] 
# dict["earth"] = "The planet on which we live." 
# print(dict) 
# print(dict["hello"])
# print(dict["python"])



# Q.2: You are given a list of students. Assume one classroom is required for one subject. how many classrooms are needed by all students.
# subjects = {"Hindi", "English", "Maths", "Science", "Social Science", "Computer Science", "English", "Hindi", "Maths", "Hindi", "English", "Maths", "Science", "Social Science", "Computer Science"}
# print(len(subjects))         #As the length of this set is equal to the number of unique subjects, so it will give us the number of classrooms needed. 



# Q.3: WAP to enter marks of 3 subjeccts from the user and store them in a dictionary. Start with an empty dictionary and add one by one. 
# dict = {}
# dict["Operarting System"] = int(input("Enter marks obtained in Operating system: "))
# dict["Computer Network"] = int(input("Enter marks obtained in Computer Network : "))
# dict["Digital Electronics"] = int(input("Enter marks obtained in Digital Electronics: "))
# print(dict) 



# Q.4: Store 9 and 9.0 as separaterte elements in a set. 
# set = {
#     ("float", 9.0),
#     ("int", 9)
#     # ("9", 9.0)
# }
# print(set)