# Contact Book

contacts = {}

def menu():
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Update Contact")
    print("4. Display Contacts")
    print("5. Exit")

# Phone Number Validation
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10 and phone != "0" * 10

# Name Validation
def is_valid_name(name):
    return name and len(name) <= 50

# Add Contact
def add_contact(contacts):
    name = input("Enter name: ")

    if not is_valid_name(name):
        print("Invalid name. It must be non-empty and up to 15 characters.")
        return
    
    phone = input("Enter phone: ")

    if not is_valid_phone(phone):
        print("Invalid phone. It must be exactly 10 digits and not all zeros.")
        return

    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = phone
        print("Contact added successfully.")

# Remove Contact
def remove_contact(contacts):
    name = input("Enter name to remove: ")
    
    if name in contacts:
        del contacts[name]
        print("Contact removed.")
    else:
        print("Contact not found.")

# Update Contact
def update_contact(contacts):
    name = input("Enter name to update: ")
    
    if name in contacts:
        print("1. Update Name")
        print("2. Update Phone Number")
        
        choice = input("Enter choice: ")

        if choice == "1":
            new_name = input("Enter new name: ")

            if not is_valid_name(new_name):
                print("Invalid name. It must be up to 15 characters.")
                return

            if new_name in contacts:
                print("A contact with this name already exists.")
            else:
                contacts[new_name] = contacts[name]
                del contacts[name]
                print("Name updated successfully.")

        elif choice == "2":
            new_phone = input("Enter new phone number: ")

            if not is_valid_phone(new_phone):
                print("Invalid phone number. It must be exactly 10 digits.")
                return

            contacts[name] = new_phone
            print("Phone number updated successfully.")

        else:
            print("Invalid choice.")

    else:
        print("Contact not found.")

# Display Contacts
def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\nSaved Contacts:")
        for name, phone in contacts.items():
            print(name, ":", phone)
# Main Loop
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        remove_contact(contacts)
    elif choice == "3":
        update_contact(contacts)
    elif choice == "4":
        display_contacts(contacts)
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")





        # Display Contacts
# def display_contacts(contacts):
#     if not contacts:
#         print("No contacts found.")
#     else:
#         print("\nSaved Contacts:")
#         for i, (name, phone) in enumerate(contacts.items(), start=1):
#             print(f"{i}. {name} : {phone}")