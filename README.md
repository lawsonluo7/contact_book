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
cb = contact_book.ContactBook(file_obj: typing.Optinal[typing.BinaryIO] = None)
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
#### `ContactBook.read(index: typing.Optional[int] = None) -> Contact | list[Contact]`
returns the `Contact` instance at index provided, if index not provided, a list of all `Contact` \
does the job of R in CRUD
#### `ContactBook.modify(index: int, contact: Contact) -> None`
change the `Contact` instance at index provided to the `Contact` instance given \
does the job of U in CRUD
#### `ContactBook.delete(index: int) -> None`
delete the `Contact` at the index provided \
does the job of D in CRUD