# Contact Book

contacts = {}
FILE_NAME = "contacts.txt"

# Load contacts from txt file at startup
# def load_contacts():
#     global contacts 
#     try:
#         with open(FILE_NAME, "r") as file:
#             for line in file:
#                 line = line.strip()
#                 if line:
#                     name, phone = line.split(",")
#                     contacts[name] = phone
#     except FileNotFoundError:
#         contacts = {}

def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    name, phone = line.split(",")
                    contacts[name] = phone
    except FileNotFoundError:
        pass


# Save contacts to txt file
def save_contacts():
    with open(FILE_NAME, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")

def menu():
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Update Contact")
    print("4. Display Contacts")
    print("5. Search Contact")
    print("6. Exit")

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
        print("Invalid name. It must be non-empty and up to 50 characters.")
        return
    
    phone = input("Enter phone: ")

    if not is_valid_phone(phone):
        print("Invalid phone. It must be exactly 10 digits and not all zeros.")
        return

    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = phone
        save_contacts()
        print("Contact added successfully.")

# Remove Contact
def remove_contact(contacts):
    name = input("Enter name to remove: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts()
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
                print("Invalid name. It must be non-empty and up to 50 characters.")
                return

            if new_name in contacts:
                print("A contact with this name already exists.")
            else:
                contacts[new_name] = contacts[name]
                del contacts[name]
                save_contacts()
                print("Name updated successfully.")

        elif choice == "2":
            new_phone = input("Enter new phone number: ")

            if not is_valid_phone(new_phone):
                print("Invalid phone number. It must be exactly 10 digits.")
                return

            contacts[name] = new_phone
            save_contacts()
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
        for i, (name, phone) in enumerate(contacts.items(), start=1):
            print(f"{i}. {name} : {phone}")

# Search Contact
def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Found: {name} : {contacts[name]}")
    else:
        print("Contact not found.")

# Main Loop
load_contacts()

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
        search_contact(contacts)
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")




        


# # import json

# # # Contact Book
# # contacts = {}

# # FILE_NAME = "contacts.json"

# # # Load contacts from file at startup
# # def load_contacts():
# #     global contacts
# #     try:
# #         with open(FILE_NAME, "r") as file:
# #             contacts = json.load(file)
# #     except:
# #         contacts = {}

# # # Save contacts to file
# # def save_contacts():
# #     with open(FILE_NAME, "w") as file:
# #         json.dump(contacts, file)

# # # SEARCH OPTION 
# # # SAVE IT
# # def menu():
# #     print("\n--- Contact Book ---")
# #     print("1. Add Contact")
# #     print("2. Remove Contact")
# #     print("3. Update Contact")
# #     print("4. Display Contacts")
# #     print("5. Search Contact")
# #     print("6. Exit")

# # # Phone Number Validation
# # def is_valid_phone(phone):
# #     return phone.isdigit() and len(phone) == 10 and phone != "0" * 10

# # # Name Validation
# # def is_valid_name(name):
# #     return name and len(name) <= 50

# # # Add Contact
# # def add_contact(contacts):
# #     name = input("Enter name: ")

# #     if not is_valid_name(name):
# #         print("Invalid name. It must be non-empty and up to 15 characters.")
# #         return
    
# #     phone = input("Enter phone: ")

# #     if not is_valid_phone(phone):
# #         print("Invalid phone. It must be exactly 10 digits and not all zeros.")
# #         return

# #     if name in contacts:
# #         print("Contact already exists.")
# #     else:
# #         contacts[name] = phone
# #         save_contacts()
# #         print("Contact added successfully.")

# # # Remove Contact
# # def remove_contact(contacts):
# #     name = input("Enter name to remove: ")
    
# #     if name in contacts:
# #         del contacts[name]
# #         save_contacts()
# #         print("Contact removed.")
# #     else:
# #         print("Contact not found.")

# # # Update Contact
# # def update_contact(contacts):
# #     name = input("Enter name to update: ")
    
# #     if name in contacts:
# #         print("1. Update Name")
# #         print("2. Update Phone Number")
        
# #         choice = input("Enter choice: ")

# #         if choice == "1":
# #             new_name = input("Enter new name: ")

# #             if not is_valid_name(new_name):
# #                 print("Invalid name. It must be up to 15 characters.")
# #                 return

# #             if new_name in contacts:
# #                 print("A contact with this name already exists.")
# #             else:
# #                 contacts[new_name] = contacts[name]
# #                 del contacts[name]
# #                 save_contacts()
# #                 print("Name updated successfully.")

# #         elif choice == "2":
# #             new_phone = input("Enter new phone number: ")

# #             if not is_valid_phone(new_phone):
# #                 print("Invalid phone number. It must be exactly 10 digits.")
# #                 return

# #             contacts[name] = new_phone
# #             save_contacts()
# #             print("Phone number updated successfully.")

# #         else:
# #             print("Invalid choice.")

# #     else:
# #         print("Contact not found.")

# # # Display Contacts
# # def display_contacts(contacts):
# #     if not contacts:
# #         print("No contacts found.")
# #     else:
# #         print("\nSaved Contacts:")
# #         for name, phone in contacts.items():
# #             print(name, ":", phone)

# # # Search Contact
# # def search_contact(contacts):
# #     name = input("Enter name to search: ")
# #     if name in contacts:
# #         print("Found:", name, ":", contacts[name])
# #     else:
# #         print("Contact not found.")

# # # Main Loop

# # load_contacts()

# # while True:
# #     menu()
# #     choice = input("Enter your choice: ")

# #     if choice == "1":
# #         add_contact(contacts)
# #     elif choice == "2":
# #         remove_contact(contacts)
# #     elif choice == "3":
# #         update_contact(contacts)
# #     elif choice == "4":
# #         display_contacts(contacts)
# #     elif choice == "5":
# #         search_contact(contacts)
# #     elif choice == "6":
# #         print("Exiting program.")
# #         break
# #     else:
# #         print("Invalid choice. Please try again.")




# # Contact Book

# contacts = {}

# #SEARCH OPTION 
# #SAVE IT
# def menu():
#     print("\n--- Contact Book ---")
#     print("1. Add Contact")
#     print("2. Remove Contact")
#     print("3. Update Contact")
#     print("4. Display Contacts")
#     print("5. Exit")

# # Phone Number Validation
# def is_valid_phone(phone):
#     return phone.isdigit() and len(phone) == 10 and phone != "0" * 10

# # Name Validation
# def is_valid_name(name):
#     return name and len(name) <= 50

# # Add Contact
# def add_contact(contacts):
#     name = input("Enter name: ")

#     if not is_valid_name(name):
#         print("Invalid name. It must be non-empty and up to 15 characters.")
#         return
    
#     phone = input("Enter phone: ")

#     if not is_valid_phone(phone):
#         print("Invalid phone. It must be exactly 10 digits and not all zeros.")
#         return

#     if name in contacts:
#         print("Contact already exists.")
#     else:
#         contacts[name] = phone
#         print("Contact added successfully.")

# # Remove Contact
# def remove_contact(contacts):
#     name = input("Enter name to remove: ")
    
#     if name in contacts:
#         del contacts[name]
#         print("Contact removed.")
#     else:
#         print("Contact not found.")

# # Update Contact
# def update_contact(contacts):
#     name = input("Enter name to update: ")
    
#     if name in contacts:
#         print("1. Update Name")
#         print("2. Update Phone Number")
        
#         choice = input("Enter choice: ")

#         if choice == "1":
#             new_name = input("Enter new name: ")

#             if not is_valid_name(new_name):
#                 print("Invalid name. It must be up to 15 characters.")
#                 return

#             if new_name in contacts:
#                 print("A contact with this name already exists.")
#             else:
#                 contacts[new_name] = contacts[name]
#                 del contacts[name]
#                 print("Name updated successfully.")

#         elif choice == "2":
#             new_phone = input("Enter new phone number: ")

#             if not is_valid_phone(new_phone):
#                 print("Invalid phone number. It must be exactly 10 digits.")
#                 return

#             contacts[name] = new_phone
#             print("Phone number updated successfully.")

#         else:
#             print("Invalid choice.")

#     else:
#         print("Contact not found.")

# # Display Contacts
# def display_contacts(contacts):
#     if not contacts:
#         print("No contacts found.")
#     else:
#         print("\nSaved Contacts:")
#         for name, phone in contacts.items():
#             print(name, ":", phone)
            
# # Main Loop

# while True:
#     menu()
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_contact(contacts)
#     elif choice == "2":
#         remove_contact(contacts)
#     elif choice == "3":
#         update_contact(contacts)
#     elif choice == "4":
#         display_contacts(contacts)
#     elif choice == "5":
#         print("Exiting program.")
#         break
#     else:
#         print("Invalid choice. Please try again.")





#         # Display Contacts
# # def display_contacts(contacts):
# #     if not contacts:
# #         print("No contacts found.")
# #     else:
# #         print("\nSaved Contacts:")
# #         for i, (name, phone) in enumerate(contacts.items(), start=1):
# #             print(f"{i}. {name} : {phone}")