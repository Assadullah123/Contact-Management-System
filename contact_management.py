# contact_management.py

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}"

def main():
    contacts = []

    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            contact = Contact(name, phone)
            contacts.append(contact)
            print("Contact added.")
        elif choice == '2':
            print("\nContact List:")
            for contact in contacts:
                print(contact)
        elif choice == '3':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
