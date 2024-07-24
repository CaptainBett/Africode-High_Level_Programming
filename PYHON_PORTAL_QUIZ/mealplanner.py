# Define a function to suggest meals based on the day of the week
def plan_meal(day):
    """Returns a suggested meal for the given day."""
    # Check the day of the week and return a suggested meal accordingly
    if day.lower() == 'monday':
        return "Pasta"
    elif day.lower() == 'tuesday':
        return "Tacos"
    elif day.lower() == 'wednesday':
        return "Chicken stir-fry"
    elif day.lower() == 'thursday':
        return "Salad"
    elif day.lower() == 'friday':
        return "Pizza"
    elif day.lower() == 'saturday':
        return "Burgers"
    elif day.lower() == 'sunday':
        return "Grilled fish"
    else:
        return "Invalid input. Please enter a valid day of the week."
# Ask the user for a day of the week
day_of_week = input("Enter a day of the week to get a suggested meal: ")
# Get the suggested meal for the given day and print it
suggested_meal = plan_meal(day_of_week)
print("Suggested meal for", day_of_week + ":", suggested_meal)