""" what is a function?
- Block of organized, reusable code that is used to perform a single, related action.

Why should we use function?
- Reuse the code and keep it DRY


# syntax: - def name of the function with parenthesis () and colon :
"""
# def greeting():
#     #pass # used to skip the function - do nothing until I have a new set of instructions
#     return "Hello world"

"""
Calling a function by printing it!
"""
# print(greeting())

# def test():
#     pass # it will skip the methods and there will be no outcome
# print(test())

"""
methods with Parameters / Arguments
"""

# def add_values(number1, number2):
#     return number1 + number2 # we can return anything - string -int with + operator
# print(add_values(6,9)) # you need to add both arguments number 1 and number 2

"""
We have created a function that adds any 2 given values
# function should only do 1 job! functions should always be basic

# exercise
- create a function with 2 args to return a subtraction of the 2 values given

"""
#def subtract_values(number1, number2):
#     return (number1-number2)
# print(subtract_values(25,15))


# # create a function with 2 args to return division of the 2 values given
# def divide_values(number1, number2):
#     return(number1 / number2)
# print(divide_values(25,5))


# # create a function with 2 args to return a remainder of the 2 values given
# def remainder_values(number1, number2):
#     return(number1 % number2)
# print(remainder_values(25,6))


# # create a function with 2 args to return a multiplication of 2 values given
# def multiply_values(number1, number2):
#     return(number1 * number2)
# print(multiply_values(5,5))

# Now asking for the user input!

# create a function with multiple arguments
# def multiply_args(*args):
#
#     for args in args:
#         print(args)
#     return args
#
# print(multiply_args(1, 2, 3, 4, 5))

# print is not direct part of method

def subtraction2():
    x = int(input("Enter first number\n"))
    y = int(input("Enter second number\n"))
    return x - y
print(subtraction2())
