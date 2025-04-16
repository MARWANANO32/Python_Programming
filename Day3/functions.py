#function is a block of statement and return specific task
"""Types:
- Built-in library function "Standard"
- User-defined function
"""

def Name_function():
    print("MARWAN MOSTAFA ELGENDY")

#call the function to do task
Name_function()

#Python Function with Parameters

def add(num1: int, num2: int) -> int:
    
    num3 = num1 + num2

    return num3

num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second Number: "))

ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")


# This program is to show number (odd or even)
number = int(input("Enter the Number: "))

def function(number):
    if (number % 2 == 0):
        print("The Number is Even")
    else:
        print("The Number is Odd")

function(number)