# If and esle Conditional Statement

age = int(input("Enter you Age: "))

if age >= 18:
    print("Eligible to vote")

else:
    print("Not Eligible")


# Nested If & else -> mean that one of them have another condition

age = 70
is_member = True
if age >= 60:
    if is_member:
        print("30% senior disscount")
    else:
        print("20% senior disscount")
else:
    print("print no eligible for disscount")


# # Match-case loop
# number = 1

# match number:
#     case 1:
#         print("one")
#     case 2 | 3:
#         print("Two or Three")
#     case 4:
#         print("Four")
#     case _:
#         print("other number")