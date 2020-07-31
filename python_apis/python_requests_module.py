import requests

# What is an API
# Application programming interface

# Why do we use it?
# --> to connect to other programs!

# in python we have a module called requests to interact with web - APIs

# how can we install a python package in PyCharm
# pip install and the name of package
# I inserted (pip install requests)

# put the quotes to turn it into string
# in order to see the data in back and check the response codes
# check HTTP/HTTPS 200 success- 400- 404 page not found

# How I would like to store it
# How I would like to get it
response_bbc = requests.get("https://www.bbc.co.uk/")
#
# # result = 200 is success showing website is live and working
# print(response_bbc)
# # print(response_bbc.status_code)
#
# displaying headers for us
# print(response_bbc.headers)
#
# # what kind of data
# # showing us that its a Case insensitive list
# print(type(response_bbc.headers))
#
# # if I just wanted to know what keys there are
# print(print(response_bbc.keys)
print(response_bbc.content)

# Iteration 1
# receive a response and check if 200 - print success
# elif page not found
# else oooooops something went  wong!

# response_bbc = requests.get("https://www.bbc.co.uk/")
# def check_response_code():
# #for response in str(response_bbc.status_code):
#     if response_bbc.status_code == 200:
#         print("Success!")
#     elif response_bbc.status_code == 404:
#         print("Not found")
#     else:
#         print("Ooooops !! Sorry, something went wrong")

# check_response_code()


 #2nd Iteration
# create a function called check_response_code() including all of the above
# returns the message with status code

# 3rd Iteration
# OOP with 4 pillars