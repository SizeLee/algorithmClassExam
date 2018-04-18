import matplotlib.pyplot as plt
import time
from exam1 import DataGenerator, ViewResult, BruteForce, GrahamScan

class ConvexHullExam:
    def __init__(self, dataSize, x_range, y_range):
        self.__dataSize = dataSize
        self.__x_range = x_range
        self.__y_range = y_range
        self.__data = {}
        for eachsize in self.__dataSize:  # generate and save data
            self.__data[eachsize] = (DataGenerator.DataContainer(self.__x_range, self.__y_range, eachsize))
        self.bfa = BruteForce.BruteForceAlgorithm()
        self.gsa = GrahamScan.GranhamScanAlgorithm()

    def __runBruteForce(self, size):
        data = self.__data[size]
        start = time.time()
        ch = self.bfa.findConvexHull(data)
        end = time.time()
        return ch, end-start

    def __runGrahamScan(self, size):
        data = self.__data[size]
        start = time.time()
        ch = self.gsa.findConvexHull(data)
        end = time.time()
        return ch, end-start

    def __runDCGScan(self, size):
        data = self.__data[size]
        start = time.time()
        ch = self.gsa.DivideConquerFindCH(data)
        end = time.time()
        return ch, end-start

    def Analysis(self):
        timeonsize = []
        for eachsize in self.__dataSize:
            chb, timeb = self.__runBruteForce(eachsize)
            chg, timeg = self.__runGrahamScan(eachsize)
            chdcg, timedcg = self.__runDCGScan(eachsize)
            timeonsize.append((timeb, timeg, timedcg))
            ViewResult.Viewallresult(eachsize, self.__data[eachsize].data, (chb, chg, chdcg),
                                     ('r', 'g', 'b'), ('Brute Force', 'GrahamScan', 'Divide-Conquer'))

        for i in range(3):
            ViewResult.ViewSingleTimeExpense(i, self.__dataSize, timeonsize,
                                   ('b', 'g', 'r'), ('Brute Force', 'GrahamScan', 'Divide-Conquer'))

        ViewResult.ViewTimeExpense(3, self.__dataSize, timeonsize,
                                   ('b', 'g', 'r'), ('Brute Force', 'GrahamScan', 'Divide-Conquer'))

        plt.show()

if __name__ == '__main__':
    # datasize = [i*100 for i in range(1, 21)]
    datasize = [i*1000 for i in range(1, 11)]
    e = ConvexHullExam(datasize, (0, 100), (0, 100))
    e.Analysis()

    # ba = BruteForce.BruteForceAlgorithm()
    # gsa = GrahamScan.GranhamScanAlgorithm()
    # data = DataGenerator.DataContainer((0, 100), (0, 100), 130000)
    # sb = time.time()
    # chb = ba.findConvexHull(data)
    # # chb = []
    # eb = time.time()
    # sg = time.time()
    # chg = gsa.findConvexHull(data)
    # eg = time.time()
    # sdcg = time.time()
    # chdcg = gsa.DivideConquerFindCH(data)
    # edcg = time.time()
    # print(len(chb), len(chg), len(chdcg))
    # print(eb - sb, eg - sg, edcg - sdcg)