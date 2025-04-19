# Task 1: Calculate Factorial Using a Function 





def factorial(n):
    try:
        num = int(n)
    except ValueError:
        return "Invalid input! Please enter a valid integer."
    if num < 0:
        return "Factorial is not defined for negative numbers."
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result
    
factorial = factorial(0)

print(f"The factorial of 5 is: {factorial}")