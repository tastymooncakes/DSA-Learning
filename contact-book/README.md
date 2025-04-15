# Contact Book Program

This is a Python-based Contact Book program that allows users to manage their contacts. Users can add, remove, search, and display contacts.

## Features

- **Add a Contact**: Add a new contact with details like name, phone number, and email.
- **Remove a Contact**: Remove an existing contact by name or other identifiers.
- **Search for a Contact**: Search for a contact by name or other details.
- **Display All Contacts**: View all saved contacts in the contact book.

## Usage

Run the script using Python and follow the prompts or use command-line arguments (if applicable).

### Example Commands

#### Add a Contact
```bash
python main.py add --name "John Doe" --phone "123-456-7890" --email "john@example.com"
```
Output:
```
Contact added: John Doe
```

#### Remove a Contact
```bash
python main.py remove --name "John Doe"
```
Output:
```
Contact removed: John Doe
```

#### Search for a Contact
```bash
python main.py search --name "John Doe"
```
Output:
```
Contact found:
Name: John Doe
Phone: 123-456-7890
Email: john@example.com
```

#### Display All Contacts
```bash
python main.py show
```
Output:
```
Contacts:
- Name: John Doe, Phone: 123-456-7890, Email: john@example.com
- Name: Jane Smith, Phone: 987-654-3210, Email: jane@example.com
```

## Requirements

- Python 3.x

## How It Works

The program uses Python's data structures (e.g., dictionaries or lists) to store contact information. It may also use file handling or databases for persistent storage.

### Key Functions

- **Add Contact**: Adds a new contact to the contact book.
- **Remove Contact**: Deletes a contact by matching the provided details.
- **Search Contact**: Finds and displays a contact based on the search criteria.
- **Show Contacts**: Lists all saved contacts.

This project is a practical demonstration of Python's data handling, file I/O, and command-line argument parsing capabilities.
