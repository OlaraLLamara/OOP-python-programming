# Create a while loop that counts from 0 to 10, and prints even numbers to the screen. Use the skeleton below:
# We will declare a variable for loop counter (x).
# We will check the condition whether loop counter is less than or equal to 10, if condition is true numbers will be printed.
# If condition is false – loop will be terminated

x = 10
i = 1

while i <= x:
    if i % 2 == 0:
        print(i, end=" ")
    i = i + 1

# this works too but does not use the if statement inside the loop
# num = 2

# while num <= 10:
#     print(num)
#     num = num + 2