# What is a Tuple?
    # same as list but IMMUTABLE
    # will not allow data to be changed or deleted

# why Tuple? - to store data that would not need changing e.g. Date of birth, passport number, insurance number etc (primary key concept)

# Syntax of Tuple: we us () to create a Tuple
# user_details_tuple = ("name", "dob", "passport number")

# Convert tuple into a string
# add name into the string at 0 index
# display the list

# we start off with a Tuple
user_details = ("23/04/1996", "Kaunas")
# convert it into a list
user_details_list = list(user_details)
print(user_details_list)
print(type(user_details))
user_details_list.insert(0,"Ugne")
print(user_details_list)
