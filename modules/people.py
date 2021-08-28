__author__ = 'Fuzz'


class Person:
    def __init__(self, surname, nm, doc, d_type, phn, mail):
        self.surname = surname
        self.name = nm
        self.document = doc
        self.doc_type = d_type
        self.phone = phn
        self.email = mail

    def change_name(self, new_name):
        self.name = new_name
        return 0

    def change_surname(self, new_surname):
        self.surname = new_surname
        return 0

    def change_phone(self, new_phone):
        self.phone = new_phone
        return 0

    def change_mail(self, new_mail):
        self.email = new_mail
        return 0

    def show(self):
        return ("Name: \n", self.name, self.surname, "\nDocument: \n", self.document,
                "\nContact: \n", self.phone, self.email)


class Client(Person):
    def __init__(self, number, account, surname, nm, d_type, doc, phn, mail):
        super().__init__(surname, nm, doc, d_type, phn, mail)
        self.clientNumber = number
        self.account = account
        self.taxes = []

    def show(self):
        return ("Cliente: \n" + str(self.name) + str(self.surname) +
                "\nContacto: \n" + str(self.phone) + " " + str(self.email) + "\nNumero de cliente: \n" +
                str(self.doc_type) + "\nCuenta: \n" + str(self.account))

    def change_account(self, account):
        self.account = account
        return 0

    def add_tax(self, tax):
        self.taxes.append(tax)


class Employed(Person):
    def __init__(self, key, date_in, surname, nm, doc, d_type, phn, mail):
        super().__init__(surname, nm, doc, d_type, phn, mail)
        self.dateIn = date_in
        self.number = int
        self.accessKey = key
        self.is_admin = False

    def show(self):
        super(Employed, self).show()
        print("Employed date in: \n", self.dateIn)

    def set_as_admin(self):
        self.is_admin = True

    def set_number(self, number):
        self.number = number

    def key_change(self, old_key, new_key):
        if self.accessKey == old_key:
            self.accessKey = new_key
            return 1
        else:
            return 99


if __name__ == "__main__":
    print("Object generator module")
