# how can we use builtin python library

from random import random
# import math #import built in modules
#
# # to generate a random number- mostly used in lottery
# # print(random()
# float_num = 24.5  # float
#
# # round the float number
# # math. shows you all builtin math functions
# # ceil rounds the number
#
# print(math.ceil(float_num))
#
# print(math.floor(float_num))


# create a method that would take 2 arguments
# calculate cm into inches

# num = float(input("Enter the distance in cm "))
# inch = num/2.54
# print("In inches this will be ", inch)

# def conversion(cm):
#     return(cm / 2.54)
# print (conversion(4))


# def multiply_values(number1, number2):
#     return(number1 * number2)
# print(multiply_values(5,5))

# def cm_to_inches(cm):
#     print("cm converted into inches is:")
#     return (cm/2.54)
#
# print(cm_to_inches(9))

def cm_to_inches():
    select = int(input("Select a number you would like to convert: \n"))
    print("{} cm converted into inches is:".format(str(select)))
    return (select / 2.54)

print(cm_to_inches())