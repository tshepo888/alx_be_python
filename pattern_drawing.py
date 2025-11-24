# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

# Use a while loop to handle the rows
while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")  # Print asterisks side by side
    print()  # Move to the next line after each row
    row += 1  # Increment row counter
