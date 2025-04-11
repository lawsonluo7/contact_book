import pickle

class Contact:
    def __init__(self, name, phone_number, email, age):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.age = age

    def __repr__(self):
        return str((self.name, self.phone_number, self.email, self.age))
        return f"""name: {self.name}
    phone_number: {self.phone_number}
    email: {self.email}
    age: {self.age}"""

class ContactBook:
    def __init__(self):
        self.contacts = self._load1("contacts.bin")

    def _load0(self, filename: str) -> list:
        # list
        loaded = []
        # loop lines in contacts
        with open(filename, "r") as file:
            for contact in file.readlines():
                # seperate tuple(line)
                contact = tuple(contact)
                name = contact[0]
                phone_number = contact[1]
                email = contact[2]
                age = contact[3]
                # list append Contact(seperated values)
                loaded.append(Contact(name, phone_number, email, age))
        # return list
        return loaded

    def _save0(self, filename: str, to_save: list):
        with open(filename, "w") as contact_book:
            for contact in to_save:
                contact_book.write(str(contact)+"\n")

    def _load1(self, filename: str) -> list:
        with open(filename, "rb") as contacts:
            return pickle.load(contacts)

    def save1(self, filename: str, to_save: list):
        with open(filename, "wb") as contacts:
            pickle.dump(to_save, contacts)

    def _create(self) -> Contact:
        return Contact(input("name: "), input("phone number: "), input("email: "), int(input("age: ")))

    def _ask(self, msg, old):
        return input(f"{msg}:\noriginal: {old}\nnew: ") or old

    def _modify(self, contact: Contact) -> Contact:
        print("type something to change attributes\notherwise leave blank")
        return Contact(
            self._ask("name", contact.name),
            self._ask("phone_number", contact.name),
            self._ask("email", contact.name),
            int(self._ask("age", contact.name)),
        )

    def _modify_in_place(self, contact: Contact) -> None:
        contact.name = self._ask("name", contact.name)
        contact.phone_number = self._ask("phone number", contact.phone_number)
        contact.email = self._ask("email", contact.name)
        contact.age = int(self._ask("age", contact.name))

    def add(self) -> None:
        self.contacts.append(self._create())

    def list_all(self) -> None:
        print(self.contacts)

    def update(self, contacts: list, index: int):
        #contacts[index] = modify(contacts[index])
        self._modify_in_place(self.contacts[index])

    def delete(self, index):
        del self.contacts[index]
