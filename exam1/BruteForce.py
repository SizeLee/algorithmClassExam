import math
import matplotlib.pyplot as plt
from exam1 import DataGenerator, ViewResult
class BruteForceAlgorithm:
    def __init__(self):
        pass

    def isConvex(self, a, b, c, d):  # a,b,c,d is tuple of points (x,y)
        d = [a, b, c, d]
        m = min(d, key=lambda x: x[1])
        # print(d)
        for i in range(len(d)):
            if d[i] == m:
                mark = i
            else:
                d[i] = (d[i][0] - m[0], d[i][1] - m[1], i)

        del d[mark]
        # print(d,m)
        newd = sorted(d, key=lambda x:(x[0]/math.sqrt(x[0]**2+x[1]**2)), reverse=True)  # sorted by cosine value of polar angle of point
        # print(newd)

        # (x2-x1)y - (y2-y1)x + (y2-y1)x1 - (x2-x1)y1 = 0 line formula, (x2,y2)'s polar angle is larger than (x1,y1)
        # if [(x2-x1)y - (y2-y1)x + (y2-y1)x1 - (x2-x1)y1] * [(x2-x1)0 - (y2-y1)0 + (y2-y1)x1 - (x2-x1)y1] < 0
        # than (x,y) is on the opposite side of line with polar point(0,0)
        judge = ((newd[1][0] - newd[0][0]) * newd[2][1] -
                 (newd[1][1] - newd[0][1]) * newd[2][0] +
                 (newd[1][1] - newd[0][1]) * newd[0][0] -
                 (newd[1][0] - newd[0][0]) * newd[0][1]) * \
                ((newd[1][1] - newd[0][1]) * newd[0][0] -
                 (newd[1][0] - newd[0][0]) * newd[0][1])

        if judge < 0:
            return False, newd[1][2]  # return the index
        else:
            return True, None


    def findConvexHull(self, data):  # data is a DataContainer Class
        convexhull = data.data.copy()

        ###preprocess fix a point
        miny = 0
        for i in range(len(convexhull)):
            if convexhull[i][1] < convexhull[miny][1]:
                miny = i
        m = convexhull[miny]
        del convexhull[miny]
        convexhull.insert(0, m)

        ####### going through all possible combine version ### take too long time
        # mark = []
        # while(a<len(convexhull)):
        #     b = a+1
        #     while(b<len(convexhull)):
        #         c = b+1
        #         while(c<len(convexhull)):
        #             d = c+1
        #             while(d<len(convexhull)):
        #                 test = self.isConvex(convexhull[a], convexhull[b], convexhull[c], convexhull[d])
        #                 # print(test)
        #                 if test[0] == False:
        #                     if test[1] == 0:
        #                         mark.append(a)
        #                     elif test[1] == 1:
        #                         mark.append(b)
        #                     elif test[1] == 2:
        #                         mark.append(c)
        #                     elif test[1] == 3:
        #                         mark.append(d)
        #                 d += 1
        #             c += 1
        #         b += 1
        #     a += 1
        #
        # for i in mark:
        #     convexhull[i] = None
        # result = []
        # for each in convexhull:
        #     if each is not None:
        #         result.append(each)
        # convexhull = result

        ###### pruning impossible point during going through combines version
        a = 0
        while(a<len(convexhull)):
            b = a+1
            while(b<len(convexhull)):
                c = b+1
                while(c<len(convexhull)):
                    d = c+1
                    while(d<len(convexhull)):
                        test = self.isConvex(convexhull[a], convexhull[b], convexhull[c], convexhull[d])
                        # print(test)
                        if test[0] == False:
                            if test[1] == 3:
                                del convexhull[d]
                                test = (True, None)
                            else:
                                break
                        else:
                            d += 1

                    if test[0] == False:
                        if test[1] == 2:
                            del convexhull[c]
                            test = (True, None)
                        else:
                            break
                    else:
                        c += 1

                if test[0] == False:
                    if test[1] == 1:
                        del convexhull[b]
                        test = (True, None)
                    else:
                        break
                else:
                    b += 1

            if test[0] == False:
                if test[1] == 0:
                    del convexhull[a]
                    test = (True, None)
                else:
                    break
            else:
                a += 1

        return convexhull


if __name__ == '__main__':
    ba = BruteForceAlgorithm()
    data = DataGenerator.DataContainer((0,100), (0,100), 100000)
    # print(ba.isConvex(*data.data[:4]))
    # print(data.data[:4])
    # # print(ba.isConvex((15.566770588283951, 84.39767898518036), (68.30726784322363, 14.656186034429176), (12.006115612729761, 14.025167902560021), (23.885448595576342, 10.711343925329563)))
    # plt.plot([p[0] for p in data.data[:4]], [p[1] for p in data.data[:4]])
    # plt.show()

    ch = ba.findConvexHull(data)
    ViewResult.ViewScatter(data.data)
    ViewResult.ViewConvexhull(ch)
    plt.show()