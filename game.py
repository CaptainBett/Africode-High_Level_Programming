
import random
secret_number = random.randint(1,10)
guess_count = 0

while guess_count < 3:
    try:
        guess = int(input("Guess a number (1-10): ")) 
    except ValueError:
        print("Please enter a valid integer.")
        continue

    guess_count += 1

    if guess == secret_number:
        print("Congratulations, you guessed it!")
        break
    else:
        print("Try again")

if guess_count == 2:
    print(f"Sorry, you ran out of guesses.The number was {secret_number}")



# import random

# secret_number = random.randint(1, 10)
# guess_count = 0
# max_guesses = 3

# while guess_count < max_guesses:
#     try:
#         guess = int(input("Guess a number (1-10): "))
#     except ValueError:
#         print("Please enter a valid integer.")
#         continue

#     guess_count += 1

#     if guess == secret_number:
#         print("Congratulations, you guessed it!")
#         break
#     else:
#         print("Try again")

# if guess_count == max_guesses:
#     print(f"Sorry, you ran out of guesses. The number was {secret_number}")























