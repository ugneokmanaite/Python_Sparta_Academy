# What is control flow
    # Conditional statements and loops
    # if, elif, else, for loop, while loop

# The control flow of a Python program is regulated by conditional statements, loops, and function calls. ... Raising and handling exceptions also affects control flow;

# weather = "sunny"
# conditional_weather = "rainy" # condition is almost like a boolean value
# conditional block of code
# if weather == "sunny" and conditional_weather == "rainy": # both conditions must be true
 #   print("lets go to the beach !!!")
# else:
   # print ("sorry better luck next time")

# using OR operator 0- if first condition is met then this will be run!
# if weather == "snow" or conditional_weather == "rainy": # both conditions must be true
#    print("lets go to the beach !!!")
# else:
#    print("sorry better luck next time")

# age = 18
#
# if age >= 18:
#     print("enjoy your film")
# else:
#     print("sorry your age does not meet the minimum requirement for viewing")

# EXERCISE

# write 12a, PG,U, 18, 15

# writing a program to check these conditions by getting user input

# if age  <= 17 can't watch 18 rated mov
# if age 12 or less can't watch any movie rated above the age of 12

# display messages accordingly

age = int(input("Please enter your age to check if you have any viewing restrictions"))

if age == 18:
    print("Your age allows you to access all of our movies! Enjoy. ")
elif 15 <= age < 18:
     print("Your age restricts you from viewing '18 rated' movies only. Please choose a movie rated up to 15 only!")
elif 11 < age < 15:
     print("Your age restricts you from viewing '18' and '15' rated movies. Please choose a movie rated up to 12 only!")
elif 7 < age < 12:
     print("Your age restricts you from viewing '18', '15' and '12' rated movies. Please choose PG or U rated movie only!")
else:
    print("Your age restricts you from viewing all films unless rated U")


