# What is a dictionary
    # more dynamic than a list... how? very useful tool within any coding
    # simple concept of KEY VALUE PAIRS

# SYNTAX - we use {} to create a Dictionary
                 # key  :   value
student_record = {"name" : "Ugne",
                  "stream" : "DevOps",
                  "completed_topics" : 5,
                  "completed_lessons_names": ["strings", "Tuples", "variables"]
                  }

# print(student_record)

# to get the type of variable- this will reveal that its a dictionary!
# print(type(student_record))

# will only print values of the dictionary
# print(student_record.values())

# will only print keys of the dictionary
# print(student_record.keys())

# student_record ["completed_lessons_names"] = 3
# new_list = student_record["completed_lessons_names"]
# print(new_list)

# add 2 topics that we have covered, number 1 lists and number 2 Builtin methods
student_record["completed_lessons_names"].append("Lists")
student_record["completed_lessons_names"].append("Built in methods")

print(student_record)

# print(student_record["stream"]) # get the value of the key
# print(student_record["completed_lessons_names"][1]) # get the specific index data
#
# fetch 'variables'
# print(student_record["completed_lessons_names"][2])
#
# # show name
#
# print(student_record["name"])



