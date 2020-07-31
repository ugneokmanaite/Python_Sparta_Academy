import requests

# put the quotes to turn it into string

# 1. How I would like to store it
# 2. How I would like to get it

# response_bbc = requests.get("https://www.bbc.co.uk/")

# print(response_bbc) # shows us the response code
#
# print(response_bbc.status_code)
#
# print(response_bbc.headers) # displaying header
#
# print(type(response_bbc.headers)) # displaying data type

# Checking only the keys which are displayed
# print(response_bbc.headers.keys())

# print(response_bbc.content) # displaying content

# Iteration 1
# receive a response and check if 200 - print success
# elif page not found
# else oooooops something went  wong!

# response_bbc = requests.get("https://www.bbc.co.uk/")

# creating a function

# def check_response_code():
#     for response in str(response_bbc.status_code):
#         if response_bbc.status_code == 200:
#             print("Success!")
#         elif response_bbc.status_code == 404:
#             print("Not found")
#         else:
#             print("Ooooops !! Sorry, something went wrong")
#
# check_response_code()


 #2nd Iteration
# create a function called check_response_code() including all of the above
# returns the message with status code

# def check_response_code():
#     for response in str(response_bbc.status_code):
#         if response_bbc.status_code == 200:
#             print(str(response_bbc.status_code) + ": Success!")
#             #print("Success!")
#         elif response_bbc.status_code == 404:
#             print(str(response_bbc.status_code) + ": Not found...")
#         else:
#             print("Ooooops !! Sorry, something went wrong")
#
# check_response_code()

# 3rd Iteration
