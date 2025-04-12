import pickle
import typing
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)

class Contact:
    def __init__(self, name: str, *, phone_number: typing.Optional[str] = None, email: typing.Optional[str] = None):
        if not name.strip():
            logger.error("Name cannot be empty. `None` was returned.")
            return
        if not any((phone_number, email)):
            logger.error("At least one contact detail (phone number or email) must be provided. `None` was returned.")
            return

        self.name: str = name
        self.phone_number: typing.Optional[str] = phone_number
        self.email: typing.Optional[str] = email

    def __repr__(self):
        return ', '.join(f'{key}={value}' for key, value in vars(self).items())

    def __dict__(self):
        return {k: v for k, v in vars(self).items() if v}

class ContactBook:
    def __init__(self, file: typing.Optional[str | typing.BinaryIO] = None):
        self.contacts: list[Contact] = []
        if file:
            try:
                if isinstance(file, str):
                    with open(file, 'rb') as f:
                        self.contacts = pickle.load(f).read()
                elif isinstance(file, typing.BinaryIO):
                    self.contacts = pickle.load(file).read()
                else:
                    logger.error(f"Invalid file object type. Expected `str` or `BinaryIO`, but got {type(file).__name__}.")
            except Exception as e:
                logger.error(f"Failed to load contacts: {e}")

    def save(self, file: str | typing.BinaryIO) -> None:
        try:
            if isinstance(file, str):
                with open(file, 'wb') as f:
                    pickle.dump(self, f)
            elif isinstance(file, typing.BinaryIO):
                pickle.dump(self, file)
            else:
                logger.error(f"Invalid file object type. Expected `str` or `BinaryIO`, but got {type(file).__name__}.")
        except Exception as e:
            logger.error(f"Failed to save: {e}")

    def add(self, contact: Contact) -> None:
        try:
            self.contacts.append(contact)
        except Exception as e:
            logger.error(f"Failed to add contact: {e}")

    def read(self, target: typing.Optional[int] = None) -> Contact | list[Contact] | None:
        try:
            if target is None:
                return self.contacts
            elif isinstance(target, int):
                return self.contacts[target]
            else:
                logger.error(f"Invalid target type. Expected `int`, `Contact` or `None`, but got {type(target).__name__}.")
        except IndexError:
            logger.error(f"The index {target} is out of range, returning None")
        except Exception as e:
            logger.error(f"Unexpected error during reading: {e}, returning None")

    def modify(self, target: int | Contact, new: Contact) -> None:
        try:
            if isinstance(target, Contact):
                index = self.contacts.index(target)
            elif isinstance(target, int):
                index = target
            else:
                logger.error(f"Invalid target type. Expected `int` or `Contact`, but got {type(target).__name__}.")
                return
            self.contacts[index] = new
        except ValueError:
            logger.error("The target contact does not exist in the contact book.")
        except IndexError:
            logger.error(f"The index {target} is out of range")
        except Exception as e:
            logger.error(f"Unexpected error during modifying: {e}")

    def delete(self, target: int | Contact) -> None:
        try:
            if isinstance(target, int):
                self.contacts.pop(target)
            elif isinstance(target, Contact):
                self.contacts.remove(target)
            else:
                logger.error(f"Invalid target type. Expected `int` or `Contact`, but got {type(target).__name__}.")
                return
        except ValueError:
            logger.error("The target contact does not exist in the contact book.")
        except IndexError:
            logger.error(f"The index {target} is out of range")
        except Exception as e:
            logger.error(f"Unexpected error during deleting: {e}")

def main():
    # Create a new ContactBook instance
    cb = ContactBook()

    # Add a new contact
    contact1 = Contact(name="John Doe", phone_number="123-456-7890", email="johndoe@example.com")
    cb.add(contact1)

    # Add another contact
    contact2 = Contact(name="Jane Smith", phone_number="987-654-3210", email="janesmith@example.com")
    cb.add(contact2)

    # Read all contacts
    all_contacts = cb.read()
    print("All Contacts:", all_contacts)

    # Search for a contact by index
    contact_at_index_0 = cb.read(0)
    print("Contact at index 0:", contact_at_index_0)

    # Check for a contact
    print(contact2 in cb.read())

    # Modify a contact
    updated_contact = Contact(name="John Doe", phone_number="111-222-3333", email="john.doe@newdomain.com")
    cb.modify(0, updated_contact)

    # Delete a contact
    cb.delete(1)

    # Save to file, could use file name but I want to show the object functionality
    with open("contacts.bin", 'wb') as f:
        cb.save(f)
    # Load from file, could use file object but I want to show file name functionality
    cb = ContactBook("contacts.bin")

    print("Loaded Contacts:", cb.read())

if __name__ == "__main__":
    main()