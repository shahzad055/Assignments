# Task 2: Write and Append Data to a File
 


from math import pi


file_path = 'output.txt'

with open(file_path, 'w') as file:
    # Prompt the user for input
    user_input = input("Enter some text to write to the file: ")
    # Write the user input to the file
    file.write(user_input + '\n')
    # Append additional data to the file
    user_input = input("Enter some additional data to append to the file: ")
    file.write(user_input + "\n")

try:
    with open(file_path, 'r') as file:
        print("Final content of the file:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.") 

