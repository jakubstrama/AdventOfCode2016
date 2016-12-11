class Output:

    value = None
    number = None

    def __init__(self, num, val):
        self.number = num
        if val:
            self.value = val

    def add_value(self, value):
        self.value = value

    def __str__(self):
        return "{Number %d, value %s}" % (self.number, str(self.value))

    def __repr__(self):
        return self.__str__()
