## Variables

- Containers for storing data values
- A variable is created when you assign a value to it
- Must start with letter or _ character
- Can only contain `A-Z, 0-9 and _`
- Are case sensitive!
- Print statement is often used to output variables
- To combine both text & variable python uses `+ `
- Global variables are created outside of the function

`strings`= used for simple txt (str)- using ""

`intergers`= whole numbers (int)

`float `= decimal numbers flat

`boolean` = true/ false



```python
x = "awesome"

def myfunc():
    print("Python is" + x)

myfunc()
```

`x = 10 ` INT variable

`y = 11.5` FLOAT variable

`name = "Hello"` STRING variable

overwriting a variable

```python
name = "emma"
print(name)
name = "james"
print(name)
```
creating a variable called first & last name
````python
first = input("Please insert your first name")
last = input("Please insert your last name")
print = (first + " " + last)
````

## Tuples

- Collection which is ordered and unchangeable 
- Same as list but **immutable** 
- Written using `(  )`
- Data cannot be changed or deleted
- _Why use tuples?_ to store data that would not need changing! E.g. data of birth

syntax

```python
user_details_tuple = ("name", "dob", "passport number")
```

Accessing Tuple Items:
 ```python
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
# works the same for negative indexing
```
Range of Indexing:
```python
# Return 3rd, 4th, and 5th item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

```

Changing Tuple Values:
- They are immutable!
- However, you can convert it into a list, and then convert the list back into Tuple

```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print (x)
```
```python
user_details = ("23/04/1996", "Kaunas")
user_details_list = list(user_details)
print(user_details_list)
user_details_list.insert(0, "Ugne")
print(user_details_list)
```

## Lists
- In python lists are same as arrays
- Both serve the same purpose of storing data

Why lists?
1. Help manage data
2. Help access data in order
3. Gives us the option to add and remove data 
4. Created using `[] `brackets

creating a list
```python
cities = ["Tokyo", "Paris", "Prague", "Munich"]

print(cities)
```
`print(len(cities))` - number of citiies

`print(cities[-1])` - accesing Munich

changing list

```python
cities [3] = "Amsterdam"
# this will change Munich to Amsterdam
```
adding to list
```python
cities.append("Vilnius")
```
adding via index

```python
cities.insert(0, "London")
```

removing from list
```python
cities.remove("Vilnius")

```
deleting last index
```python
cities.pop()
```

storing mixed data types in lists
```python
mix_type_string = [[1, 2, 3], ["one", "two", "three"]]

string_list = ["one", "two," "three"]

print(mix_type_string + string_list)
```

## Dictionaries

- More dynamic than a list
- Concept of key: value pairs
- we use {} to create dictionary

```python
student_record = {"name" : "Ugne",
                  "stream" : "DevOps",
                  "completed_topics" : 5,
                  "completed_lessons_names": ["strings", "Tuples", "variables"]
                  }

print(student_record)
```
to only print values of the dictionary
```python
print(student_record.values())
```
to only print keys of the dictionary
```python
print(student_record.keys())
```

using dictionaries to create lists
```python
student_record ["completed_lessons_names"] = 3
new_list = student_record["completed_lessons_names"]
print(new_list)
```
to add value to a dictionary
```python
student_record["completed_lessons_names"].append("Lists")
```
getting value of a record
```python
print(student_record["stream"])
```

getting specific index key
```python
print(student_record["completed_lessons_names"][1])
```

## Loops

- `FOR` loops are used to iterate through Lists, Strings, Dictionaries and Tuples (repeating code for a first number of times)
- e.g.execute a set of statements, once for each item in a list, tuple, set etc.
- does not require an indexing variable to set beforehand
```python
list_data = [1, 2, 3, 4, 5]

for data in list_data:
    print(data)
```
looping through a list
```python
list_data = [1, 2, 3, 4, 5]
for data in list_data:
    if data > 4:
        print(data)
```

looping through strings
```python
city = "london"
for letter in city:
    print(letter)

# or can use

city = "London"
for letter in "London":
    print(letter)
```
## Looping through dictionary

```python
student_record = {"name": "Ugne",
                  "stream": "DevOps",
                  "completed_lessons": 5,
                  "completed_lessons_names": ["strings", "Tuples", "variables"]}
```
```python
for record in student_record.keys():
    print(record)
```
```python
for record in student_record.values():
#     print(record)
```
```python
for record in student_record.keys():
    if record == "name":
        print(record)
    elif record == 5:
    print(record)
```

