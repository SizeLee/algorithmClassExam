from pulp import *
from exam3 import DataGenerator
import time
import random

class LinearProgrammingApproximationAlgorithm:
    def __init__(self):
        pass

    def runRound(self, data):
        prob = LpProblem("setCover", LpMinimize)
        a = data.statistics_lp_a_matrix()
        n = list(range(len(data.F)))
        xs = LpVariable.matrix('x', (n, ), 0, 1)
        w = [1 for _ in range(len(data.F))]
        prob += lpDot(w, xs)
        for i in range(len(data.X)):
            express = 0
            for j in n:
                if a[i][j] == 1:
                    express += xs[j]
            prob += express >= 1
            # prob += lpDot(a[i], xs) >= 1

        prob.solve()
        # for i in n:
        #     print(xs[i], "=", xs[i].value())
        maxf = max(data.element_frequency.values())
        C = []
        for i in n:
            if xs[i].value() >= (1.0/maxf):
                C.append(data.F[i])

        return C

    def runRandomRound(self, data):
        prob = LpProblem("setCover", LpMinimize)
        a = data.statistics_lp_a_matrix()
        n = list(range(len(data.F)))
        xs = LpVariable.matrix('x', (n,), 0, 1)
        w = [1 for _ in range(len(data.F))]
        prob += lpDot(w, xs)
        for i in range(len(data.X)):
            express = 0
            for j in n:
                if a[i][j] == 1:
                    express += xs[j]
            prob += express >= 1
            # prob += lpDot(a[i], xs) >= 1

        prob.solve()
        C = []
        for i in n:
            if xs[i].value() > random.uniform(0, 1):
                C.append(data.F[i])

        return C

if __name__ == '__main__':
    data = DataGenerator.DataContainer(500)
    lpaa = LinearProgrammingApproximationAlgorithm()
    s = time.time()
    C = lpaa.runRound(data)
    e = time.time()
    print(e - s)
    print(C)
    print(len(C))
    s = time.time()
    C = lpaa.runRandomRound(data)
    e = time.time()
    print(e - s)
    print(C)
    print(len(C))

