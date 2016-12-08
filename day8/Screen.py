import numpy as np
from collections import deque

class Screen:
    width = 0
    tall = 0
    lcd = None

    def __init__(self, tall, width):
        self.width = width
        self.tall = tall
        self.lcd = np.zeros(shape=[tall, width], dtype=int)

    def rect(self, tall, width):
        tall = int(tall)
        width = int(width)

        for i in range(0, tall):
            for j in range(0, width):
                self.lcd[i][j] = 1

    def rotate_column(self, num, by):
        num = int(num)
        by = int(by)

        items = [item[num] for item in self.lcd]
        items = deque(items)
        items.rotate(by)

        for item in self.lcd:
            item[num] = items.popleft()

    def rotate_row(self, num, by):
        num = int(num)
        by = int(by)

        items = deque(self.lcd[num])
        items.rotate(by)
        self.lcd[num] = list(items)

    def count_lit(self):
        return np.sum(self.lcd)

    def print_code(self):
        items = ["".join([self.__decode_pixel(val) for val in row]) for row in self.lcd ]
        with open('code.txt', 'a') as myfile:
            myfile.write("\n".join(items))

    def __decode_pixel(self, num):
        return " " if num == 0 else "#"