#when displaying to a user
# try:
#   result = 4 / 0
# except ZeroDivisionError:
#    print("Sorry, Input cannot be divided by zero!")



#when developing a program
# try:
#     risky_operation()
# except Exception as e:
#     print(f"An error occured:{e}")
   


def validate_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older")
    else:
        return True
try:
    validate_age(20)
except ValueError as e:
    print(e)
else:
    print("Meets minimums")
finally:#executes no matter what
    print("I am unstoppable")
  
