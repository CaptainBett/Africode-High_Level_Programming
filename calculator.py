import choices
import print_statements

operation = input("Operation:")

if operation in choices.choice1:
    num1 = int(input("Enter your first number:"))
    num2 = int(input("Enter your second number:"))
    print("The solution is:" + str(num1 + num2))
  
elif operation in choices.choice2:
       num1 = int(input("Enter your first number:"))
       num2 = int(input("Enter your second number:"))
       print("The solution is:" + str(num1 - num2))

elif operation in choices.choice3:
       num1 = int(input("Enter your first number:"))
       num2 = int(input("Enter your second number:"))
       print("The solution is:" + str(num1 * num2))

elif operation in choices.choice4:
       num1 = int(input("Enter your first number:"))
       num2 = int(input("Enter your second number:"))
       print("The solution is:" + str(num1 / num2))

else:
    print("Invalid input!")
















