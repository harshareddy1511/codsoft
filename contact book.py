import json
import os

# File to save contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from the file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    print("\nAdd New Contact")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    print("\nAll Contacts")
    if not contacts:
        print("No contacts found!")
        return
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

# Search for a contact
def search_contact(contacts):
    print("\nSearch Contacts")
    query = input("Enter name or phone number to search: ").lower()
    results = [c for c in contacts if query in c["name"].lower() or query in c["phone"]]
    
    if not results:
        print("No matching contacts found.")
        return
    
    for idx, contact in enumerate(results, 1):
        print(f"\nContact {idx}:")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")

# Update contact details
def update_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the contact number to update: ")) - 1
        if index < 0 or index >= len(contacts):
            print("Invalid contact number.")
            return
        print("\nUpdating Contact:")
        contact = contacts[index]
        print(f"Current Name: {contact['name']}")
        contact["name"] = input("Enter new name (leave blank to keep current): ") or contact["name"]
        print(f"Current Phone: {contact['phone']}")
        contact["phone"] = input("Enter new phone (leave blank to keep current): ") or contact["phone"]
        print(f"Current Email: {contact['email']}")
        contact["email"] = input("Enter new email (leave blank to keep current): ") or contact["email"]
        print(f"Current Address: {contact['address']}")
        contact["address"] = input("Enter new address (leave blank to keep current): ") or contact["address"]
        save_contacts(contacts)
        print("Contact updated successfully!")
    except ValueError:
        print("Invalid input.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the contact number to delete: ")) - 1
        if index < 0 or index >= len(contacts):
            print("Invalid contact number.")
            return
        contacts.pop(index)
        save_contacts(contacts)
        print("Contact deleted successfully!")
    except ValueError:
        print("Invalid input.")

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
