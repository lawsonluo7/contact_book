import pickle
import typing
import logging

logging.basicConfig(level=logging.error)

class Contact:
    def __init__(self, name: str, *, phone_number: typing.Optional[str] = None, email: typing.Optional[str] = None):
        if not name.strip():
            logging.error("Name cannot be empty. `None` was returned.")
            return
        if not any((phone_number, email)):
            logging.error("At least one contact detail (phone number or email) must be provided. `None` was returned.")
            return

        self.name: str = name
        self.phone_number: typing.Optional[str] = phone_number
        self.email: typing.Optional[str] = email

    def __repr__(self):
        return ', '.join(f'{key}={value}' for key, value in vars(self).items())

class ContactBook:
    def __init__(self, file_obj: typing.Optional[typing.BinaryIO] = None):
        self.contacts: list[Contact] = []
        if file_obj:
            self.contacts = pickle.load(file_obj)

    def save(self, file_obj: typing.BinaryIO) -> None:
        try:
            pickle.dump(self, file_obj)
        except Exception as e:
            logging.error(f"Failed to save: {e}")

    def add(self, contact: Contact) -> None:
        try:
            self.contacts.append(contact)
        except Exception as e:
            logging.error(f"Failed to add contact: {e}")

    def read(self, index: typing.Optional[int] = None) -> Contact | list[Contact]:
        try:
            if index is None:
                return self.contacts
            else:
                return self.contacts[index]
        except IndexError:
            logging.error(f"The index {index} is out of range")
        except Exception as e:
            logging.error(f"Unexpected error during reading: {e}")

    def modify(self, index: int, new: Contact) -> None:
        try:
            self.contacts[index] = new
        except IndexError:
            logging.error(f"The index {index} is out of range")
        except Exception as e:
            logging.error(f"Unexpected error during modifying: {e}")

    def delete(self, index: int) -> None:
        try:
            self.contacts.pop(index)
        except IndexError:
            logging.error(f"The index {index} is out of range")
        except Exception as e:
            logging.error(f"Unexpected error during deleting: {e}")
