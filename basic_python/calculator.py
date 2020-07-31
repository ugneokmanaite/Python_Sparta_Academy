class Calculator:
# class created

# basic functions of calculator added
# self is used for function to all itself
    def add(self):
        print(a + b)
    def sub(self):
        print(a - b)
    def multiply(self):
        print(a * b)
    def divide(self):
        print(a / b)
    def remainder(self):
        print (a % b)
# to ask user for inputs
a = int(input("enter first number"))
b = int(input("enter second number"))
# object created
obj = Calculator()

# choices for user

choice = 1
while choice != 0:
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. REMAINDER")
    choice= int(input("Enter your choice: "))

    if choice == 1:
        print(obj.add())
    elif choice == 2:
        print(obj.sub())
    elif choice == 3:
        print(obj.multiply())
    elif choice == 4:
        print(obj.divide())
    elif choice == 5:
        print(obj.divide())
    else:
        print("Error")