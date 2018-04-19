import math
import matplotlib.pyplot as plt
from exam1 import DataGenerator, ViewResult

class GranhamScanAlgorithm:
    def __init__(self):
        pass

    def findConvexHull(self, data):  # data is a DataContainer Class
        polardata = data.data.copy()
        m = min(polardata, key=lambda x: x[1])
        for i in range(len(polardata)):
            if polardata[i] == m:
                mark = i
            else:
                polardata[i] = (polardata[i][0] - m[0], polardata[i][1] - m[1], i)

        del polardata[mark]
        #### the polardata above is not really polar coordinates data, but right angle axes data whose origin is the polar point.

        sortedpolardata = sorted(polardata, key=lambda x:(x[0]/math.sqrt(x[0]**2+x[1]**2)), reverse=True) # sorted by cosine value of polar angle of point

        convexhullstack = [(0., 0., mark), sortedpolardata[0], sortedpolardata[1]]

        for i in range(2, len(sortedpolardata)):
            # (x2-x1)y - (y2-y1)x + (y2-y1)x1 - (x2-x1)y1 = 0 line formula, (x2,y2)'s polar angle is larger than (x1,y1)
            # if [(x2-x1)y - (y2-y1)x + (y2-y1)x1 - (x2-x1)y1] * [(x2-x1)0 - (y2-y1)0 + (y2-y1)x1 - (x2-x1)y1] < 0
            # than (x,y) is on the opposite side of line with polar point(0,0)

            judge = ((convexhullstack[-1][0] - convexhullstack[-2][0]) * sortedpolardata[i][1] -
                     (convexhullstack[-1][1] - convexhullstack[-2][1]) * sortedpolardata[i][0] +
                     (convexhullstack[-1][1] - convexhullstack[-2][1]) * convexhullstack[-2][0] -
                     (convexhullstack[-1][0] - convexhullstack[-2][0]) * convexhullstack[-2][1]) * \
                    ((convexhullstack[-1][1] - convexhullstack[-2][1]) * convexhullstack[-2][0] -
                     (convexhullstack[-1][0] - convexhullstack[-2][0]) * convexhullstack[-2][1])

            while(judge < 0):
                convexhullstack.pop()
                judge = ((convexhullstack[-1][0] - convexhullstack[-2][0]) * sortedpolardata[i][1] -
                         (convexhullstack[-1][1] - convexhullstack[-2][1]) * sortedpolardata[i][0] +
                         (convexhullstack[-1][1] - convexhullstack[-2][1]) * convexhullstack[-2][0] -
                         (convexhullstack[-1][0] - convexhullstack[-2][0]) * convexhullstack[-2][1]) * \
                        ((convexhullstack[-1][1] - convexhullstack[-2][1]) * convexhullstack[-2][0] -
                         (convexhullstack[-1][0] - convexhullstack[-2][0]) * convexhullstack[-2][1])

            convexhullstack.append(sortedpolardata[i])

        convexhull = [data.data[p[2]] for p in convexhullstack]

        return convexhull

    def __merge2queen(self, a, b):
        result = []
        ia = 0
        ib = 0
        while(ia < len(a) and ib < len(b)):
            if a[ia][2] > b[ib][2]:
                result.append(a[ia])
                ia += 1
            else:
                result.append(b[ib])
                ib += 1

        if ia<len(a):
            result = result + a[ia:]
        else:
            result = result + b[ib:]
        # print(result)
        return result

    def __dcFindCH(self, data):  # data here is just list of right angle axes data point
        if len(data) <= 3:
            m = min(data, key=lambda x: x[1])
            polardata = []
            for i in range(len(data)):
                if data[i] != m:
                    polardata.append((data[i][0] - m[0], data[i][1] - m[1], i))
            polardata.sort(key=lambda x:(x[0]/math.sqrt(x[0]**2+x[1]**2)), reverse=True)
            chdata = [m]
            for each in polardata:
                chdata.append(data[each[2]])
            # print(chdata)
            return chdata

        else:
            xmin = data[0][0]
            xmax = data[0][0]
            for each in data:
                if each[0] < xmin:
                    xmin = each[0]
                elif each[0] > xmax:
                    xmax = each[0]

            xmid = (xmax + xmin)/2.0

            left = []
            right = []
            for each in data:
                if each[0] <= xmid:
                    left.append(each)
                else:
                    right.append(each)

            chleft = self.__dcFindCH(left)
            chright = self.__dcFindCH(right)

            chcur = self.__mergeCH(chleft, chright)
            return chcur

    def __mergeCH(self, left, right):  ## left and right here is present by right angle axes
        ml = left[0]
        mr = right[0]
        q = {}
        whole = 1
        divide = 0
        if ml[1] <= mr[1]:
            m = ml
            q[divide] = right
            q[whole] = left[1:]
        else:
            m = mr
            q[divide] = left
            q[whole] = right[1:]

        polarwhole = []
        for i in range(len(q[whole])):
            x = q[whole][i][0]-m[0]
            y = q[whole][i][1]-m[1]
            polarwhole.append((x, y, x/math.sqrt(x**2 + y**2), (whole, i)))

        x = q[divide][0][0] - m[0]
        y = q[divide][0][1] - m[1]
        polardivide = [(x, y, x/math.sqrt(x**2 + y**2), (divide, 0))]
        cosmin_anglemax = polardivide[0][2]
        cosmax_anglemin = polardivide[0][2]
        anglemax_mark = 0
        anglemin_mark = 0
        for i in range(1, len(q[divide])):
            x = q[divide][i][0]-m[0]
            y = q[divide][i][1]-m[1]
            polardivide.append((x, y, x/math.sqrt(x**2 + y**2), (divide, i)))
            # print(polardivide[i])
            if polardivide[i][2] <= cosmin_anglemax:
                anglemax_mark = i
                cosmin_anglemax = polardivide[i][2]
            elif polardivide[i][2] > cosmax_anglemin:
                anglemin_mark = i
                cosmax_anglemin = polardivide[i][2]

        # tam = max(polardivide, key=lambda x: x[2])
        # print(tam == polardivide[anglemin_mark])
        # tam = min(polardivide, key=lambda x: x[2])
        # print(tam == polardivide[anglemax_mark])

        length = len(polardivide)
        i = anglemin_mark
        polard1 = []
        while(True):
            polard1.append(polardivide[i])
            i = (i+1)%length
            if i == anglemax_mark:
                break
        # polard1.sort(key=lambda x: x[2], reverse=True)
        # print(polard1)

        i = anglemin_mark
        polard2 = []
        while(i != anglemax_mark):
            i = (i+length-1)%length
            polard2.append(polardivide[i])

        # polard2.sort(key=lambda x: x[2], reverse=True)
        # print(polard2)

        polardata = self.__merge2queen(polard1, polard2)
        sortedpolardata = self.__merge2queen(polardata, polarwhole)
        # sortedpolardata.sort(key=lambda x: x[2], reverse=True)

        convexhullstack = [(0., 0.), sortedpolardata[0], sortedpolardata[1]]

        for i in range(2, len(sortedpolardata)):
            # (x2-x1)y - (y2-y1)x + (y2-y1)x1 - (x2-x1)y1 = 0 line formula, (x2,y2)'s polar angle is larger than (x1,y1)
            # if [(x2-x1)y - (y2-y1)x + (y2-y1)x1 - (x2-x1)y1] * [(x2-x1)0 - (y2-y1)0 + (y2-y1)x1 - (x2-x1)y1] < 0
            # than (x,y) is on the opposite side of line with polar point(0,0)

            judge = ((convexhullstack[-1][0] - convexhullstack[-2][0]) * sortedpolardata[i][1] -
                     (convexhullstack[-1][1] - convexhullstack[-2][1]) * sortedpolardata[i][0] +
                     (convexhullstack[-1][1] - convexhullstack[-2][1]) * convexhullstack[-2][0] -
                     (convexhullstack[-1][0] - convexhullstack[-2][0]) * convexhullstack[-2][1]) * \
                    ((convexhullstack[-1][1] - convexhullstack[-2][1]) * convexhullstack[-2][0] -
                     (convexhullstack[-1][0] - convexhullstack[-2][0]) * convexhullstack[-2][1])

            while (judge < 0):
                convexhullstack.pop()
                judge = ((convexhullstack[-1][0] - convexhullstack[-2][0]) * sortedpolardata[i][1] -
                         (convexhullstack[-1][1] - convexhullstack[-2][1]) * sortedpolardata[i][0] +
                         (convexhullstack[-1][1] - convexhullstack[-2][1]) * convexhullstack[-2][0] -
                         (convexhullstack[-1][0] - convexhullstack[-2][0]) * convexhullstack[-2][1]) * \
                        ((convexhullstack[-1][1] - convexhullstack[-2][1]) * convexhullstack[-2][0] -
                         (convexhullstack[-1][0] - convexhullstack[-2][0]) * convexhullstack[-2][1])

            convexhullstack.append(sortedpolardata[i])

        convexhullstack.pop(0)
        convexhull = [m] + [q[p[3][0]][p[3][1]] for p in convexhullstack]
        return convexhull

    def DivideConquerFindCH(self, data):
        listdata = data.data.copy()
        convexhull = self.__dcFindCH(listdata)

        return convexhull

if __name__ == '__main__':
    gsa = GranhamScanAlgorithm()
    data = DataGenerator.DataContainer((0, 100), (0, 100), 100)
    ch = gsa.findConvexHull(data)
    plt.figure()
    ViewResult.ViewScatter(data.data)
    ViewResult.ViewConvexhull(ch, 'b', 'gsa', 2.0)
    # plt.show()
    plt.figure()
    ch = gsa.DivideConquerFindCH(data)
    ViewResult.ViewScatter(data.data)
    ViewResult.ViewConvexhull(ch, 'g', 'dcgsa', 2.0)
    plt.show()


