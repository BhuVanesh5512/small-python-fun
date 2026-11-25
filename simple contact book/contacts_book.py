import json
FILENAME = "contacts.json"
def load_contacts():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
def save_contacts(contacts):
    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent=4)
def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    contacts[name] = phone
    print("Contact added.")

def view_contacts(contacts):
    for name, phone in contacts.items():
        print(f"{name} : {phone}")

def search_contact(contacts):
    name = input("Enter name: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")
def main():
    contacts = load_contacts()
    while True:
        print("\n1. Add  2. View  3. Search  4. Delete  5. Exit")
        choice = input("Choose: ")

        if choice == "1": add_contact(contacts)
        elif choice == "2": view_contacts(contacts)
        elif choice == "3": search_contact(contacts)
        elif choice == "4": delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
