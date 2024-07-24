def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score < 60:
        return "F"
    else:
        return "Invalid score. Please enter a valid score between 0 and 100."
    
score = int(input("\nEnter your score: "))
grade = calculate_grade(score)
print("Your grade is:", grade)