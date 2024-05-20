print("Select an operation you would like to perform from the list below:")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")

operation = input("Operation:")

if operation == "1":
    num1 = int(input("Enter your first number:"))
    num2 = int(input("Enter your second number:"))
    print("The solution is:" + str(num1 + num2))
  
elif operation == "2":
       num1 = int(input("Enter your first number:"))
       num2 = int(input("Enter your second number:"))
       print("The solution is:" + str(num1 - num2))

elif operation == "3":
       num1 = int(input("Enter your first number:"))
       num2 = int(input("Enter your second number:"))
       print("The solution is:" + str(num1 * num2))

elif operation == "4":
       num1 = int(input("Enter your first number:"))
       num2 = int(input("Enter your second number:"))
       print("The solution is:" + str(num1 / num2))

else:
    print("Invalid input!")
















