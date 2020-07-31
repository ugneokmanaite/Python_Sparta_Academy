# What are sets - sets are similar to lists
# What is the difference? - sets are unordered

# Syntax:- we use {} brackets

# # Let's create a set
#
# car_parts = {"wheels","windows","doors"}
# print(car_parts)
#
# # what can we do with sets
# # add an item to set
# car_parts.add("seats")
# # deleting item
# car_parts.remove("windows")
#
# print(car_parts)

# FROZEN SET
# Once you defined them you cannot change them!
# Syntax - () store them in a variable

counting = frozenset([1, 2, 3, 4])
# counting.remove(1)--> this would not work!!
print(counting)
# print(type(counting))
