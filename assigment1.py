#task1

# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division safely
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Display results
print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

#task2 

# Take input from user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenate full name
full_name = first_name + " " + last_name

# Display greeting
print("\nHello,", full_name + "! Welcome!")
