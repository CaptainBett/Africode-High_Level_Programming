# Define an empty dictionary called contacts
contacts = {}

# Use a loop to ask the user for contact details
while True:
    name = input("Enter the name of the contact (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    email = input("Enter the email address: ")
    phone = input("Enter the phone number: ")
    contacts[name] = {'email': email, 'phone': phone}

# Print out the complete list of contacts with details
print("Contacts:")
for name, details in contacts.items():
    print("Name:", name)
    print("Email:", details['email'])
    print("Phone:", details['phone'])