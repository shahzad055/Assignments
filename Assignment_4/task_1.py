# Task 1: Read a File and Handle Errors 
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.

file_path = 'sample.txt'
try:
    # Attempt to open the file
    with open(file_path, 'r') as file:
        # Read the file line by line
        for line in file:
            print(line.strip())  # Print each line without extra newline characters
except FileNotFoundError:
    # Handle the case where the file does not exist
    print(f"Error: The file '{file_path}' was not found.")
except IOError:
    # Handle other I/O errors
    print(f"Error: An I/O error occurred while trying to read the file '{file_path}'.")