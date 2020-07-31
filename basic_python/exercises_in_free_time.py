
# modules = ["HRM", "Strategic Management",
#            "Project Management", "Lean & Agile Manufacturing"]

# print(modules)
# print(len(modules))
# print(modules[0])

# can also access a range of values
# from first index- up to but not including 3
# print(modules[1:3])
# assuming that we are accessing from 0
# print(modules[:2])

# this adds research methods at the 0 index
# modules[0] = "Research Methods"



# indexing allows you to access/change/delete only a single cell of a list

# # print the list reverse
# modules.reverse()
# print(modules)
#
# # print list in alphabetical or ascending order
# modules.sort()
# print(modules)
#
# # print in descending order
# # pass an argument in sort method
# modules.sort(reverse=True)
# print(modules)
#
# # sorted version of list without having to alter the list itself!
# sorted_courses = sorted(modules)
#
# print(sorted_courses)

# 1) Create program that asks the user to enter their name & age
# print out message addressed to them that tells them in how many years they will turn 100

# to enter name
# name = input("Please enter your name : ")

# asking to enter age

# age = input("Please enter your age : ")
#
# calculated_age = (100 - int(age))
#
# #print message addressed to them that tells them the year they will turn 100
#
# print("Dear {}".format(name) + ", you will turn 100 in {} years".format(calculated_age))



# 2) Ask user for a number. Depending on whether the number is even or odd, print out message

# asking user for a number
# number = int(input("Please enter your number:  "))
# # creating a variable mod where the remainder of the number is found
# mod  = number % 2
# # if there is a remainder then its an off number
# if mod > 0:
#     print("Your number is an odd number")
#
# else:
#     print("Your number is an even number ")
