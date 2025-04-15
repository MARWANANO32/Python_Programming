# While loop [based on Conditions]
n = 0
while(n < 5):
    n = n + 1
    print("Marwan")
else:
    print("Go ahead")


# For loop [based on counting through items]

n = 5

for i in range(n):
    print("hello marwan")

# Nested loop [Loop on loop]

for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print("hello")