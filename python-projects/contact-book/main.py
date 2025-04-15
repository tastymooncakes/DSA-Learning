import argparse
import os
import json

FILE = "contact.json"

def load_contacts():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)
    
def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def add(name, phone, email):
    contacts = load_contacts()
    found = False
    for c in contacts:
        if c["name"] == name:
            found = True
            break
    if found:
        print("Contact already exists.")
        return
    
    contact = {
        "name" : name,
        "phone" : phone,
        "email" : email
    }
    contacts.append(contact)
    save_contacts(contacts)
    show_all()

def remove(name=None, phone=None, email=None):
    contacts = load_contacts()
    found = False
    if name:
        for c in contacts:
            if c["name"] == name:
                found = True
                contacts.remove(c)
                break
    elif phone:
        for c in contacts:
            if c["phone"] == phone:
                found = True
                contacts.remove(c)
                break
    elif email:
        for c in contacts:
            if c["email"] == email:
                found = True
                contacts.remove(c)
                break
    if not found:
        print("Contact not found.")
        return
    
    save_contacts(contacts)
    show_all()

def update(name):
    contacts =load_contacts()
    found = False
    for c in contacts:
        if c["name"] == name:
            found = True
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email address: ")
            if new_name:
                c["name"] = new_name
            if new_phone:
                c["phone"] = new_phone
            if new_email:
                c["email"] = new_email
            break
    if not found:
        print("Contact not found.")
        return
    save_contacts(contacts)
    show_all()

def show_all():
    contacts = load_contacts()
    if contacts:
        print("Contacts:")
        for c in contacts:
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
    else:
        print("No contacts found.")

def show(name=None, phone=None, email=None):
    found = False
    contacts = load_contacts()
    if name:
        for c in contacts:
            if c["name"] == name:
                found = True
                print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
                break
    elif phone:
        for c in contacts:
            if c["phone"] == phone:
                found = True
                print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
                break
    
    elif email:
        for c in contacts:
            if c["email"] == email:
                found = True
                print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
                break
    if not found:
        print("Contact not found.")
        return

def main():
    parser = argparse.ArgumentParser(description="Contact Book")
    subparser = parser.add_subparsers(dest="operation", required=True)

    add_parser = subparser.add_parser("add", help="Add a contact")
    add_parser.add_argument("name", type=str, help="contact name")
    add_parser.add_argument("phone", type=str, help="contact phone number")
    add_parser.add_argument("email", type=str, help="contact email address")

    remove_parser = subparser.add_parser("remove", help="Remove a contact")
    remove_parser.add_argument("--name", type=str, help="contact name")
    remove_parser.add_argument("--phone", type=str, help="contact phone number")
    remove_parser.add_argument("--email", type=str, help="contact email address")

    show_parser = subparser.add_parser("show", help="Show all contacts")
    show_parser.add_argument("--name", type=str, help="contact name")
    show_parser.add_argument("--phone", type=str, help="contact phone number")
    show_parser.add_argument("--email", type=str, help="contact email address")
    show_parser.add_argument("--all", help="show all contacts", action="store_true")

    update_parser = subparser.add_parser("update", help="Update a contact")
    update_parser.add_argument("--name", type=str, help="contact name", required=True)

    args = parser.parse_args()
    print(args)

    if args.operation == "add":
        add(args.name, args.phone, args.email)
    elif args.operation == "remove":
        remove(args.name, args.phone, args.email)
    elif args.operation == "update":
        update(args.name)
    elif args.operation == "show":
        if args.all:
            show_all()
        else:
            show(args.name, args.phone, args.email)

if __name__ == "__main__":
    main()

