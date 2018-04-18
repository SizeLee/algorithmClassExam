import random

class DataContainer:
    def __init__(self, x_range, y_range, size):  # x_range and y_range is both tuple
        self.__x_range = x_range
        self.__y_range = y_range
        self.__size = size
        self.data = []
        self.__generatedata()

    def __generatedata(self):
        self.data = [(random.uniform(*self.__x_range), random.uniform(*self.__y_range)) for _ in range(self.__size)]


if __name__ == '__main__':  # test script
    d = DataContainer((0, 100), (0, 100), 10)
    print(d.data)