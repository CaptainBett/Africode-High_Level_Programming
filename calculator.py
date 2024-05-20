import choices
import print_statements

while True:
    operation = input("Operation:").lower()

    if operation in choices.choice1:
        num1 = int(input("Enter your first number:"))
        num2 = int(input("Enter your second number:"))
        print("The sum is:" + str(num1 + num2))
    
    elif operation in choices.choice2:
        num1 = int(input("Enter your first number:"))
        num2 = int(input("Enter your second number:"))
        print("The difference is:" + str(num1 - num2))

    elif operation in choices.choice3:
        num1 = int(input("Enter your first number:"))
        num2 = int(input("Enter your second number:"))
        print("The product is:" + str(num1 * num2))

    elif operation in choices.choice4:
        num1 = int(input("Enter your first number:"))
        num2 = int(input("Enter your second number:"))
        print("The solution is:" + str(num1 / num2))

    else:
        print("Invalid input!")

    try_again = input("Do you want to perform another operation? (Yes/No)").lower()

    if try_again != "yes":
            break
       
print("Goodbye!")


















