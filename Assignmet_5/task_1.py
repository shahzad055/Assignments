# Task 1: Create a Dictionary of Student Marks



# Create a dictionary of student marks
student_details = {
    'Alice': 85,
    'Bob': 78,
    'Charlie': 92,
    'David': 88,
    'Eve': 95
}

# Prompt the user for a student's name
student_name = input("Enter the student's name: ").strip()
student_name = student_name.capitalize()
if student_name in student_details:
    # Retrieve and display the corresponding marks
    marks = student_details[student_name]
    print(f"{student_name}'s marks: {marks}")
else:
    # Display an appropriate message if the name is not found
    print(f"Error: Student '{student_name}' not found.")


