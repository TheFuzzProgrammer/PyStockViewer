__author__ = "Fuzz"


class Product:
    def __init__(self, code, name, price, stock):
        self.codeProduct = code
        self.name = name
        self.price = price
        self.stock = stock
        self.expires = False
        self.expireDate = None
        self.isToxic = False
        self.isFood = False
        self.isDiet = False

    def set_price(self, price):
        if type(price) is float:
            self.price = price
        else:
            pass

    def show(self):
        return [self.codeProduct, self.name, self.price, self.stock, self.isToxic, self.isFood]

    def set_expiration(self, expires, date):
        if (not self.expires) and expires:
            if type(date) is str:
                self.expireDate = date
                self.expires = True

        elif self.expires and (not expires):
            if type(date) is str:
                self.expireDate = None
                self.expires = False

        elif self.expires and expires:
            if type(date) is str:
                self.expireDate = date

        else:
            pass

    def set_toxicity(self, code):
        if code == 1:
            self.isToxic = True
        elif code == 0:
            self.isToxic = False
        else:
            pass

    def is_food(self, code):
        if code == 1:
            self.isFood = True
        elif code == 0:
            self.isFood = False
        else:
            pass

    def is_diet(self, code):
        if self.isFood and (code == 1):
            self.isDiet = True
        elif self.isFood and (code == 0):
            self.isDiet = False
        else:
            pass


class Liquid(Product):
    def __init__(self, volume, code, name, price, stock):
        super().__init__(code, name, price, stock)
        self.volume = volume
        self.formula = ""

    def set_formula(self, formula):
        self.formula = formula

    def set_volume(self, volume):
        self.volume = volume


class Solid(Product):
    def __init__(self, weight, quantity, code, name, price, stock):
        super().__init__(code, name, price, stock)
        self.quantity = quantity
        self.weight = weight

    def set_weight(self, weight):
        self.weight = weight

    def set_quantity(self, quantity):
        self.quantity = quantity


if __name__ == "__main__":
    print("Object generator module")
