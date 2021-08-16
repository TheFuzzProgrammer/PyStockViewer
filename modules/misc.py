__Author__ = "Fuzz"


class Tax:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.active = True

    def is_active(self, status):
        self.active = status

    def change_value(self, value):
        self.value = value


class Discount(Tax):
    def __init__(self, name, value, reason):
        super().__init__(name, value)
        self.name = name
        self.value = (-1) * value
        self.active = True
        self.reason = reason


if __name__ == "__main__":
    print("Tax module by Fuzz")
