# # Define a tuple called subjects
# subjects = ('Math', 'Science', 'English')
# # Use a loop to ask the user for grades in each subject
# grades = ()
# for subject in subjects:
#     grade = float(input("Enter the grade for {}: ".format(subject)))
#     grades += (grade,)
# # Calculate the average grade
# average_grade = sum(grades) / len(grades)
# print("Average grade:", average_grade)


# Define a tuple called subjects
subjects = ('Math', 'Science', 'English')
# Use a loop to ask the user for grades in each subject
grades = ()
for subject in subjects:
    grade = float(input(f"Enter the grade for {subject}: "))
    grades += (grade,)
# Calculate the average grade
average_grade = sum(grades) / len(grades)
print("Average grade:", average_grade)

