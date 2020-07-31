# What are loops??
    # FOR loops are used to iterate through Lists, Strings, Dictionaries and Tuples (repeating code for a first number of times)
    # e.g. execute a set of statements, once for each item in a list, tuple, set etc.
    # does not require an indexing variable to set beforehand.

# list_data = [1, 2, 3]
# print(list_data)
# print(list_data[0])
# print(list_data[1])
# print(list_data[2])

# How will for loop benefit in this situation?

# list_data = [1, 2, 3, 4, 5]
# for data in list_data:
#     # same if we were gonna do new_list = list_date [1]
#     print(data)

# LOOPING THROUGH LIST !!

# list_data = [1, 2, 3, 4]
# for data in list_data:
# # for condition will come inside loop
#     if data > 4:
#         print(data)
#         #break # break condition will come inside if block
#     elif data < 0:
#         print("Please enter number above 0")


# LOOPING THROUGH STRING!!
# create a string and loop through the string
# city = "London"
# for letter in city:
#     print(letter)


# city = "London"
# for letter in "London":
#     print(letter)

# print the string in one line
# asking python to take name variable
# & each time it goes through it to add the letter to the one_line variable and then print it

# name = "Ugne Okmanaite"
# one_line = ""
# for letter in name:
#     one_line += letter
# print(one_line)
#
# city = "Vilnius"
# one_line = ""
# for letter in city:
#     one_line+= letter
# print(one_line)


# LOOPING THROUGH DICTIONARY
# student_record = {"name": "Ugne",
#                   "stream": "DevOps",
#                   "completed_lessons": 5,
#                   "completed_lessons_names": ["strings", "Tuples", "variables"]}


# for record in student_record.keys():
#     print(record)
# #
# for record in student_record.values():
#     print(record)

# for record in student_record.keys():
#     if record == "name":
#         print(record)
#     elif record == 5:
#     print(record)

# EXERCISE
# Create dictionary with employee records minimum 5 key value pairs

# employee_records = {"name": "Ugne",
#                     "position": "DevOps Trainee",
#                     "location": "Birmingham",
#                     "salary": 23000,
#                     "skills": ["Agile", "SQL", "Python"]
#                     }

# # using loop iterate through the dictionary

# for record in employee_records:
#     print(record)
# # display the values of and keys of dictionary
# for record in employee_records:
#     print(record,"->", employee_records[record])
# # This used indexing operator [] with the dictionary and its keys to access the values


# WHILE LOOP - What is it?
    # it runs until the condition is true
    # syntax : while variable name with condition then :

# x = 1
#
# while x < 5:
#     print(f"it's working->{x}")
#     # if x == 4:
#     #     break
#     x += 1

# with the break statement we can stop the loop even if the while condition is true
# x = 1
# while x < 6:
#     print(x)
#     if x == 3:
#       break
#     x += 1