import json
import os
import logging

# Log Configuration
logging.basicConfig(
    filename="contact_manager.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

FILE_NAME = "contacts.json"

# ---------------- Load Contacts ----------------
def load_contacts():
    try:
        if not os.path.exists(FILE_NAME):
            logging.warning("contacts.json not found. Creating a new contact list.")
            return []

        with open(FILE_NAME, "r") as file:
            contacts = json.load(file)
            logging.info("Contacts loaded successfully.")
            return contacts

    except json.JSONDecodeError:
        print("Error: JSON file is corrupted.")
        logging.error("Corrupted JSON file.")
        return []

    except Exception as e:
        print("Unexpected error while loading contacts.")
        logging.error(f"Load Error: {e}")
        return []

# ---------------- Save Contacts ----------------
def save_contacts(contacts):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(contacts, file, indent=4)

        logging.info("Contacts saved successfully.")

    except Exception as e:
        print("Error saving contacts.")
        logging.error(f"Save Error: {e}")

# ---------------- Add Contact ----------------
def add_contact(contacts):
    try:
        print("\n----- Add New Contact -----")

        name = input("Enter Name: ").strip()
        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email: ").strip()
        address = input("Enter Address: ").strip()

        if not name or not phone:
            raise ValueError("Name and Phone Number cannot be empty.")

        contact = {
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        contacts.append(contact)
        save_contacts(contacts)

        print("Contact added successfully.")
        logging.info(f"Contact Added: {name}")

    except ValueError as e:
        print("Invalid Input:", e)
        logging.warning(e)

    except Exception as e:
        print("Unable to add contact.")
        logging.error(f"Add Contact Error: {e}")

# ---------------- Display Contacts ----------------
def display_contacts(contacts):
    try:
        if len(contacts) == 0:
            print("\nNo contacts available.")
            return

        print("\n========== Contact List ==========")

        for i, contact in enumerate(contacts, start=1):
            print(f"\nContact {i}")
            print("Name    :", contact["Name"])
            print("Phone   :", contact["Phone"])
            print("Email   :", contact["Email"])
            print("Address :", contact["Address"])

    except Exception as e:
        print("Error displaying contacts.")
        logging.error(f"Display Error: {e}")

# ---------------- Search Contact ----------------
def search_contact(contacts):
    try:
        keyword = input("\nEnter Name, Phone, Email, or Address: ").lower()

        found = False

        for contact in contacts:
            if (keyword in contact["Name"].lower() or
                keyword in contact["Phone"].lower() or
                keyword in contact["Email"].lower() or
                keyword in contact["Address"].lower()):

                print("\n----- Contact Found -----")
                print("Name    :", contact["Name"])
                print("Phone   :", contact["Phone"])
                print("Email   :", contact["Email"])
                print("Address :", contact["Address"])
                found = True

        if not found:
            print("No matching contact found.")
            logging.warning(f"Search failed for: {keyword}")

    except Exception as e:
        print("Error searching contacts.")
        logging.error(f"Search Error: {e}")

# ---------------- Main Menu ----------------
def main():
    contacts = load_contacts()

    while True:
        print("\n====== Contact Management System ======")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Exit")

        try:
            choice = input("Enter your choice: ")

            if choice == "1":
                add_contact(contacts)

            elif choice == "2":
                display_contacts(contacts)

            elif choice == "3":
                search_contact(contacts)

            elif choice == "4":
                save_contacts(contacts)
                print("Contacts saved successfully.")
                print("Thank you!")
                logging.info("Application closed.")
                break

            else:
                raise ValueError("Please enter a valid option (1-4).")

        except ValueError as e:
            print("Error:", e)
            logging.warning(e)

        except Exception as e:
            print("Unexpected error occurred.")
            logging.error(f"Main Menu Error: {e}")

# ---------------- Program Starts ----------------
if __name__ == "__main__":
    main()
