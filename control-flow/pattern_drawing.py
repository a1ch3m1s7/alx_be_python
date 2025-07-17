# Prompt the user to input the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the square pattern using a while loop
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after printing a row
    row += 1