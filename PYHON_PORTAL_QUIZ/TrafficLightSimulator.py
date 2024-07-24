# Create a traffic light simulator
while True:
    # Ask the user to input the color of the traffic light
    user_input = input("\nEnter the color of the traffic light (red/yellow/green), or type 'quit' to exit: ")
    # Check if the user wants to quit the simulation
    if user_input == 'quit':
        print("Exiting the traffic light simulator.")
        break
    # Check the color of the traffic light and provide appropriate instructions
    elif user_input == 'red':
        print("Stop! It's red. Wait for the green light.")
    elif user_input == 'yellow':
        print("Slow down! It's yellow. Prepare to stop.")
    elif user_input == 'green':
        print("Go! It's green. You can proceed safely.")
    else:
        print("Invalid input. Please enter either 'red', 'yellow', 'green', or 'quit'.")