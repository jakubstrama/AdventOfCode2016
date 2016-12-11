class Bot:

    values = None
    number = None
    values_compared = None

    def __init__(self, num, val):
        self.number = num
        self.values = []
        self.values_compared = []
        if val:
            self.values.append(val)

    def is_ready(self):
        return len(self.values) is 2

    def give_low(self, bot):
        self.log_values_compared()
        min_val = min(self.values)
        self.values.remove(min_val)
        bot.add_value(min_val)

    def give_hi(self, bot):
        self.log_values_compared()
        max_val = max(self.values)
        self.values.remove(max_val)
        bot.add_value(max_val)

    def add_value(self, value):
        self.values.append(value)

    def log_values_compared(self):
        self.values_compared.append((max(self.values), min(self.values)))

    def __str__(self):
        return "{Number %d, values %s, values compared %s}" % (self.number, str(self.values), str(self.values_compared))

    def __repr__(self):
        return self.__str__()
