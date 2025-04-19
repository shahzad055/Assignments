# Task 2: Using the Math Module for Calculations





from calendar import c
import math
# Function to perform calculations using the math module
def calculate_math_operations(number):
    try:
        # Calculate square root
        square_root = math.sqrt(number)
        print(f"The square root of {number} is: {square_root}")
        
        # Calculate natural logarithm
        natural_log = math.log(number)
        print(f"The natural logarithm of {number} is: {natural_log}")
        
        # Calculate sine (in radians)
        sine_value = math.sin(number)
        print(f"The sine of {number} (in radians) is: {sine_value}")
        
        return square_root, natural_log, sine_value
    except ValueError as e:
        return str(e)
    except Exception as e:
        return str(e)

calculate_math_operations(25)
