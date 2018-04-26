from exam3 import DataGenerator, GreedyApproximation, LinearProgrammingApproximation
import time
import matplotlib.pyplot as plt
class SetCoverExam:
    def __init__(self, datasize):
        self.__datasize = datasize
        self.data = {}
        for eachsize in self.__datasize:
            self.data[eachsize] = (DataGenerator.DataContainer(eachsize))

        self.gaa = GreedyApproximation.GreedyApproximationAlgorithm()
        self.lpaa = LinearProgrammingApproximation.LinearProgrammingApproximationAlgorithm()

    def analysis(self):
        t = {}
        c = {}
        for eachsize in self.__datasize:
            s = time.time()
            c0 = self.gaa.run(self.data[eachsize])
            e = time.time()
            t0 = e - s

            s = time.time()
            c1 = self.lpaa.runRound(self.data[eachsize])
            e = time.time()
            t1 = e - s

            s = time.time()
            c2 = self.lpaa.runRandomRound(self.data[eachsize])
            e = time.time()
            t2 = e - s

            t[eachsize] = (t0, t1, t2)
            c[eachsize] = (c0, c1, c2)

        name = ['Greedy Approximation Algorithm', 'LP-Round', 'LP-RandomRound']
        for i in range(3):
            self.__printTimeExpenseAndSolution(name[i], i, t, c)

        plt.figure()
        plt.title('time expense on different data size')
        lines = []
        color = ['r', 'g', 'b']
        for i in range(3):
            l, = plt.plot(self.__datasize, [t[datasize][i] for datasize in self.__datasize], color=color[i])
            plt.scatter(self.__datasize, [t[datasize][i] for datasize in self.__datasize], color=color[i])
            lines.append(l)
            for j in range(len(self.__datasize)):
                plt.text(self.__datasize[j]-0.5, t[self.__datasize[j]][i], '{}'.format(round(t[self.__datasize[j]][i], 3)))

        plt.xlabel('data size')
        plt.ylabel('time expense')
        plt.legend(lines, name, loc=2)

        plt.figure()
        plt.title('solution size on different data size')
        lines = []
        color = ['r', 'g', 'b']
        for i in range(3):
            l, = plt.plot(self.__datasize, [len(c[datasize][i]) for datasize in self.__datasize], color=color[i])
            plt.scatter(self.__datasize, [len(c[datasize][i]) for datasize in self.__datasize], color=color[i])
            lines.append(l)
            for j in range(len(self.__datasize)):
                plt.text(self.__datasize[j] - 0.5, len(c[self.__datasize[j]][i]),
                         '{}'.format(len(c[self.__datasize[j]][i])))

        plt.xlabel('data size')
        plt.ylabel('size of solution c')
        plt.legend(lines, name, loc=2)

        plt.show()


    def __printTimeExpenseAndSolution(self, name, index, ti, c):
        print('Time expense of {} and its solution:\n'.format(name))
        for eachsize in self.__datasize:
            print('\tTime on data size of {}: {}s'.format(eachsize, ti[eachsize][index]))
            print('\tSolution of data size {} is:\n \t{}'.format(eachsize, c[eachsize][index]))
            u = set()
            for each in c[eachsize][index]:
                u = u.union(each)
            u = list(u)
            u.sort()
            print('\tSolution covers element:\n \t{}'.format(u))
            print('\tcovers {} elements'.format(len(u)))
            print('\tcost of solution is: {}\n'.format(len(c[eachsize][index])))

        print()



if __name__ == '__main__':
    datasize = [100, 1000, 5000]
    # datasize = [100, 200, 300, 400]
    e = SetCoverExam(datasize)
    e.analysis()

