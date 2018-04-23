import random
class DataContainer:
    def __init__(self, dataSize):
        self.__dataSize = dataSize
        self.X = set([i for i in range(dataSize)])
        self.F = []
        self.element_frequency = {}

        self.__generate()
        # print(self.F)

    def __generate(self):
        Xtemp = self.X
        while(len(Xtemp) > 0):
            size = min(random.randint(1, 20), len(Xtemp))
            take = set(random.sample(Xtemp, size))
            self.F.append(take)
            Xtemp = Xtemp - take
            for each_element in take:
                self.element_frequency[each_element] = self.element_frequency.get(each_element, 0) + 1

        while(len(self.F) < self.__dataSize):
            size = random.randint(1, 20)
            take = set(random.sample(self.X, size))
            if take not in self.F:
                self.F.append(take)
                for each_element in take:
                    self.element_frequency[each_element] = self.element_frequency.get(each_element, 0) + 1


    def statistics_lp_a_matrix(self):
        a = [[0 for _ in range(len(self.F))] for i in range(len(self.X))]
        for i in range(len(self.F)):
            for each in self.F[i]:
                a[each][i] = 1

        return a


if __name__ == '__main__':
    d = DataContainer(5000)
    print(d.X)
    print(d.F)
    print(d.element_frequency)
    for i in d.statistics_lp_a_matrix()[0]:
        print(i)
