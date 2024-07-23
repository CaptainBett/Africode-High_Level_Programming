# Python Learning Projects

This repository contains a collection of Python projects that I developed while learning Python at Africode Academy. These projects cover various aspects of Python programming and are intended to showcase my progress and understanding of the language.

## About Africode Academy

[Africode Academy](https://www.africodeacademy.com) is a premier coding school dedicated to empowering individuals with the skills needed to excel in the tech industry. With a focus on practical, hands-on learning, Africode Academy offers courses in various programming languages and technologies, helping students build a strong foundation in software development.

## Sample Projects

### Project 1: Hello World

This is a simple Python script that prints "Hello, World!" to the console.

```python
print("Hello, World!")
```

Project 2: Basic Calculator
A basic calculator that performs addition, subtraction, multiplication, and division.
def add(x, y):
return x + y

def subtract(x, y):
return x - y

def multiply(x, y):
return x \* y

def divide(x, y):
if y == 0:
return "Cannot divide by zero!"
return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice(1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
print(f"{num1} \* {num2} = {multiply(num1, num2)}")
elif choice == '4':
print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
print("Invalid input")

Project 3: Simple Guessing Game
A simple number guessing game where the user has to guess a randomly generated number.
import random

number_to_guess = random.randint(1, 100)
guess = None

while guess != number_to_guess:
guess = int(input("Guess a number between 1 and 100: "))
if guess < number_to_guess:
print("Too low!")
elif guess > number_to_guess:
print("Too high!")
else:
print("Congratulations! You guessed the number.")

Cloning and Using the Source Code
To clone this repository, you'll need to have Git installed on your machine. You can clone the repository using the following command:
git clone https://github.com/CaptainBett/python-learning-projects.git
Once cloned, navigate to the project directory:
cd python-learning-projects
You can run the Python scripts using Python 3:
python3 project1.py
python3 project2.py
python3 project3.py

Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
Please make sure your code adheres to the coding standards and includes appropriate tests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
If you have any questions or suggestions, feel free to reach out to me at [enockbett427@gmail.com].

Happy coding!
