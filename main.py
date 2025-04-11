import pickle
import typing

class Contact:
    def __init__(self, name: str, *, phone_number: typing.Optional[str] = None, email: typing.Optional[str] = None):
        self.name: str = name
        self.phone_number: typing.Optional[str] = phone_number
        self.email: typing.Optional[str] = email

    def __repr__(self):
        return ', '.join(f'{key}={value}' for key, value in vars(self).items())

class ContactBook:
    def __init__(self, file_obj: typing.Optional[typing.BinaryIO] = None):  # pickle load ContactBook obj from file, new empty instance if file is None
        self.contacts: list[Contact] = []
        if file_obj:
            self.contacts = pickle.load(file_obj)

    def save(self, file_obj: typing.BinaryIO) -> None:  # pickle dump self to file
        pickle.dump(self, file_obj)

    def add(self, contact: Contact) -> None:  # C
        self.contacts.append(contact)

    def read(self, index: typing.Optional[int] = None) -> Contact | list[Contact]:  # R, if index is None, return all contacts as list
        if index is None:
            return self.contacts
        else:
            return self.contacts[index]

    def modify(self, index: int, contact: Contact) -> None:  # U
        self.contacts[index] = contact

    def delete(self, index: int) -> None:  # D
        self.contacts.pop(index)
