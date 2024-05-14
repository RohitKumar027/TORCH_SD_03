
import json

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number of the contact: ")
    email = input("Enter the email address of the contact: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("List of contacts:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Function to edit an existing contact
def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter the index of the contact you want to edit: ")) - 1
        if 0 <= index < len(contacts):
            print("Enter new contact details:")
            name = input("Enter the name of the contact: ")
            phone = input("Enter the phone number of the contact: ")
            email = input("Enter the email address of the contact: ")
            contacts[index] = {"name": name, "phone": phone, "email": email}
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")

# Function to save contacts to a JSON file
def save_contacts(contacts):
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)

# Function to load contacts from a JSON file
def load_contacts():
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []
    return contacts

# Main function
def main():
    contacts = load_contacts()  # Load contacts from file

    # Main menu loop
    while True:
        print("\nContact Manager")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Edit a contact")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
