import matplotlib.pyplot as plt
import math
def ViewScatter(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    # plt.xlim((-5, 120))
    # plt.ylim((-5, 130))
    plt.scatter(x, y, color='y', s=2., alpha=0.5)
    # plt.hold()
    # plt.show()

def ViewConvexhull(convexhull, color, label, linewidth):
    m = min(convexhull, key=lambda x:x[1])
    c = convexhull.copy()
    for i in range(len(c)):
        if c[i] == m:
            mark = i
        else:
            c[i] = (c[i][0] - m[0], c[i][1] - m[1], i)

    del c[mark]
    newc = sorted(c, key=lambda x: (x[0] / math.sqrt(x[0] ** 2 + x[1] ** 2)), reverse=True)
    rankedConvexhull = [m]
    for each in newc:
        rankedConvexhull.append(convexhull[each[2]])
    rankedConvexhull.append(m)
    x = [p[0] for p in rankedConvexhull]
    y = [p[1] for p in rankedConvexhull]
    # plt.xlim((-5, 120))
    # plt.ylim((-5, 130))
    l, = plt.plot(x, y, color=color, label=label, linewidth=linewidth)
    # plt.hold(True)
    # plt.legend((l[0],), (label,), loc=1)
    # plt.hold()
    # plt.show()
    # print(dir(l))
    return l

def Viewallresult(size, datalist, ch, color, label):
    plt.figure()
    plt.title('exam on data size of {}'.format(size))
    plt.xlim((-5, 120))
    plt.ylim((-5, 130))
    ViewScatter(datalist)
    drawturn = [i for i in range(len(ch))]
    linewidths = [3.-i for i in range(len(ch))]
    # drawturn = [2, 0, 1]
    # chlines = [ViewConvexhull(ch[i], color[i], label[i]) for i in range(len(ch))]
    chlines = [ViewConvexhull(ch[drawturn[i]], color[drawturn[i]], label[drawturn[i]], linewidths[i]) for i in range(len(drawturn))]
    newlabel = [label[i] for i in drawturn]
    plt.legend(chlines, newlabel, loc=1)

    mk = ['o', '^', 'x', 's', '>', 'p', '<', 'v', '*']
    for i in range(len(drawturn)):
        x = [p[0] for p in ch[drawturn[i]]]
        y = [p[1] for p in ch[drawturn[i]]]
        plt.scatter(x, y, marker=mk[drawturn[i]], color=color[drawturn[i]], s=linewidths[i]*20+30)


def ViewTimeExpense(algorithmkinds, size, timeonsize, color, label):
    plt.figure()
    plt.title('time expense on different data size')
    lines = []
    for i in range(algorithmkinds):
        l, = plt.plot(size, [t[i] for t in timeonsize], color=color[i])
        plt.scatter(size, [t[i] for t in timeonsize])
        lines.append(l)
        # for j in range(len(size)):
        #     plt.text(size[j]-0.5, timeonsize[j][i], '{}'.format(round(timeonsize[j][i], 2)))

    plt.xlabel('data size')
    plt.ylabel('time expense')
    plt.legend(lines, label, loc=1)

def ViewSingleTimeExpense(algorithmID, size, timeonsize, color, label):
    plt.figure()
    plt.title('{} time expense on different data size'.format(label[algorithmID]))
    l, = plt.plot(size, [t[algorithmID] for t in timeonsize], color=color[algorithmID])
    plt.scatter(size, [t[algorithmID] for t in timeonsize])
    for j in range(len(size)):
        plt.text(size[j]-0.5, timeonsize[j][algorithmID], '{}'.format(round(timeonsize[j][algorithmID], 2)))
    plt.xlabel('data size')
    plt.ylabel('time expense')
