contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print(f"Contact for {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print("")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    if not results:
        print("No contact found.")
        return
    print("\nSearch Results:")
    for i, contact in enumerate(results, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print("")

def update_contact():
    search_term = input("Enter name or phone number of contact to update: ")
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            print(f"Updating contact for {contact['name']}")
            contact['name'] = input("Enter new name: ") or contact['name']
            contact['phone'] = input("Enter new phone number: ") or contact['phone']
            contact['email'] = input("Enter new email: ") or contact['email']
            contact['address'] = input("Enter new address: ") or contact['address']
            print(f"Contact for {contact['name']} updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    search_term = input("Enter name or phone number of contact to delete: ")
    for i, contact in enumerate(contacts):
        if search_term in contact['name'] or search_term in contact['phone']:
            confirm = input(f"Are you sure you want to delete contact for {contact['name']}? (yes/no): ")
            if confirm.lower() == 'yes':
                contacts.pop(i)
                print(f"Contact for {contact['name']} deleted successfully!")
            else:
                print("Delete action cancelled.")
            return
    print("Contact not found.")

def main_menu():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

# Run the contact book application
main_menu()
