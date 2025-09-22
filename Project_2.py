# Simple Calculator Program
# This program provides basic arithmetic operations, average, and percentage calculation
# based on user selection from a menu.

def addition(a, b):
    """
    Adds two numbers.
    
    Args:
    a (float): First number.
    b (float): Second number.
    
    Returns:
    float: Sum of a and b.
    """
    return a + b

def subtraction(a, b):
    """
    Subtracts the second number from the first.
    
    Args:
    a (float): First number.
    b (float): Second number.
    
    Returns:
    float: Difference of a - b.
    """
    return a - b

def multiplication(a, b):
    """
    Multiplies two numbers.
    
    Args:
    a (float): First number.
    b (float): Second number.
    
    Returns:
    float: Product of a and b.
    """
    return a * b

def division(a, b):
    """
    Divides the first number by the second.
    
    Args:
    a (float): Numerator.
    b (float): Denominator.
    
    Returns:
    float or str: Quotient if b != 0, else error message.
    """
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def average(a, b):
    """
    Calculates the average of two numbers.
    
    Args:
    a (float): First number.
    b (float): Second number.
    
    Returns:
    float: Average of a and b.
    """
    return (a + b) / 2

def percentage(a, b, c, d, e):
    """
    Calculates the percentage for five numbers assuming total marks out of 500.
    
    Args:
    a, b, c, d, e (float): Five input numbers (e.g., marks).
    
    Returns:
    float: Percentage score rounded to 2 decimal places.
    """
    total = a + b + c + d + e  # Sum of the five inputs
    percent = (total / 500) * 100  # Percentage out of 500
    return round(percent, 2)  # Round to 2 decimal places

# Display the menu options with full operation names
print("Please Select an operator:\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n"
      "5. Average\n"
      "6. Percentage (out of 500)")

# Get user selection
select = int(input("Please Enter a number between 1 to 6: "))

# Process based on selection
if select == 1:
    # Addition operation
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", addition(a, b))

elif select == 2:
    # Subtraction operation
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", subtraction(a, b))

elif select == 3:
    # Multiplication operation
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", multiplication(a, b))

elif select == 4:
    # Division operation
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", division(a, b))

elif select == 5:
    # Average operation
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", average(a, b))

elif select == 6:
    # Percentage operation (requires five inputs)
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    d = float(input("Enter fourth number: "))
    e = float(input("Enter fifth number: "))
    result = percentage(a, b, c, d, e)
    print(f"Result: {result:.2f}%")  # Formatted output with 2 decimal places and % sign

else:
    # Handle invalid selection
    print("Invalid input! Please enter a number between 1 and 6.")