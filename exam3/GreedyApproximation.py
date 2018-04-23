import time
from exam3 import DataGenerator

class GreedyApproximationAlgorithm:
    def __init__(self):
        pass

    def run(self, data):  # data here is a data container
        alreadyCover = set()
        C = []
        X = data.X
        F = data.F
        while(alreadyCover != X):
            F = sorted(F, key=lambda x: 1.0/(len(x-alreadyCover)+1))  # weight of each subset is set to be 1.0
                                                 # +1 prevent 0 division error when x-alreadyCover is an empty set
            C.append(F[0])
            alreadyCover = alreadyCover.union(F[0])
            F = F[1:]

        return C

if __name__ == '__main__':
    data = DataGenerator.DataContainer(5000)
    gaa = GreedyApproximationAlgorithm()
    s = time.time()
    c = gaa.run(data)
    e = time.time()
    print(c)
    print(len(c))
    print(e - s)
