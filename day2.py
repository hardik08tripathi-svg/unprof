import json
import os

FILE_NAME = "contacts.json"

# Load contacts from JSON file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts to JSON file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!\n")

# Display all contacts
def display_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.\n")
        return

    print("\n----- Contact List -----")
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Name    :", contact["Name"])
        print("Phone   :", contact["Phone"])
        print("Email   :", contact["Email"])
        print("Address :", contact["Address"])

# Search contact
def search_contact(contacts):
    keyword = input("\nEnter name, phone, email, or address to search: ").lower()

    found = False

    for contact in contacts:
        if (keyword in contact["Name"].lower() or
            keyword in contact["Phone"].lower() or
            keyword in contact["Email"].lower() or
            keyword in contact["Address"].lower()):

            print("\nContact Found")
            print("Name    :", contact["Name"])
            print("Phone   :", contact["Phone"])
            print("Email   :", contact["Email"])
            print("Address :", contact["Address"])
            found = True

    if not found:
        print("No matching contact found.")

# Main Program
def main():
    contacts = load_contacts()

    while True:
        print("\n===== Contact Management System =====")
        print("1. Add New Contact")
        print("2. Display All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            display_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            print("Contacts saved successfully.")
            print("Thank you!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
