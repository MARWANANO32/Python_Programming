# Input() and Output() functions
""" Input() to input user data as a string . 
    Print() is the output function for display text for User
"""
# Define a variable name
name = input("What is your name ?")
age = input("How old are you? ")
city = input("what is your city?")

# User print() as output text
print("Hello" + name + age + city + "!")

# For multiple variables
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

n = int(input("How old are you? :"))
print(n)
