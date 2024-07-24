# Define an empty list called shopping_list
shopping_list = []

# Use a loop to continuously ask the user to input items
while True:
    item = input("Enter an item to add to the shopping list (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    shopping_list.append(item)

# Print out the complete shopping list
print("Your shopping list:")
for item in shopping_list:
    print("- " + item)