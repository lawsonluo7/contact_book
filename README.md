# Contact Book

A simple Python-based contact book module to manage and organize your contacts efficiently.\
Made for backend use, does not have any UI. \
Please tell me if there are any bugs.

## Features

- Add new contacts with name, phone number and email. (All of which are stored as strings, phone number and email are optional)
- Edit or delete existing contacts by index.
- Search for contacts by name or other details.
- Save and load contacts from a file for persistence.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/lawsonluo7/contact_book.git
    ```
2. Import and use (see Usage below)
## Usage
### Contructors
#### `ContactBook` Contructor
```
import contact_book
cb = contact_book.ContactBook(file_obj: typing.Optinal[typing.BinaryIO])
```
contructor loads ContactBook object from file provided, new empty instance if file is not provided
##### `Contact` Contructor
```
import contact_book
c = contact_book.Contact(name, phone_number, email)
```
Returns `None` when invalid, which happens when:
- `name` is empty
- no contact info is provided
### Methods Include:
#### `ContactBook.save(file_obj: typing.BinaryIO) -> None`
takes a already opened binary file, and writes the instance's data in
#### `ContactBook.add(contact: Contact) -> None`
append to the current list of contacts \
does the job of C in CRUD
#### `ContactBook.read(target: typing.Optional[int | Contact]) -> bool | Contact | list[Contact]) -> Contact | list[Contact]`
returns the `Contact` instance at index provided, if index not provided, a list of all `Contact` \
when given `Contact` object, returns `bool` that represents whether\
does the job of R in CRUD
#### `ContactBook.modify(target: typing.Optional[int | Contact]) -> bool | Contact | list[Contact]) -> None`
change the `Contact` instance at index provided to the `Contact` instance given \
does the job of U in CRUD
#### `ContactBook.delete(target: int | Contact) -> None`
delete the `Contact` at the index provided \
does the job of D in CRUD
### Example
```python
import contact_book

# Create a new ContactBook instance
cb = contact_book.ContactBook()

# Add a new contact
contact1 = contact_book.Contact(name="John Doe", phone_number="123-456-7890", email="johndoe@example.com")
cb.add(contact1)

# Add another contact
contact2 = contact_book.Contact(name="Jane Smith", phone_number="987-654-3210", email="janesmith@example.com")
cb.add(contact2)

# Read all contacts
all_contacts = cb.read()
print("All Contacts:", all_contacts)

# Search for a contact by index
contact_at_index_0 = cb.read(0)
print("Contact at index 0:", contact_at_index_0)

# Modify a contact
updated_contact = contact_book.Contact(name="John Doe", phone_number="111-222-3333", email="john.doe@newdomain.com")
cb.modify(0, updated_contact)

# Delete a contact
cb.delete(1)

# Save to file, could use file name but I want to show the object functionality
with open("contacts.bin", "wb") as file:
    cb.save(file)
    print("saved")

# Load from file, could also use file object but I want to show file name functionality
cb = contact_book.ContactBook("contacts.bin")

print("Loaded Contacts:", cb.read())
```