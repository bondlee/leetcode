# coding: utf-8
# Created by bondlee on 2016/6/15


from collections import defaultdict
from copy import deepcopy

class Node(object):

    def __init__(self, x):
        self.x = x
        self.nodes = []


def find_min(g, nums):

    ind = -1
    m = 10000
    for i, v in enumerate(g):
        if nums[v] != -1 and nums[v] < m:
            m = nums[v]
            ind = v
    return ind

def print_path(dis, pi):
    """

    :param dis:
    :param pi:
    :return:
    """
    for k, v in dis.iteritems():
        pa = []
        end = k
        while end != -1:
            pa.append(end)
            end = pi[end]
        pa.reverse()
        # print k, v, pa
        print k, v

def dijkstra(graph, s):
    """

    :param graph:
    :return:
    """
    G = [i for i in graph.iterkeys()]
    Q, d, pi = [], defaultdict(lambda: -1), defaultdict(lambda : -1)
    d[s] = 0

    while G:
        u = find_min(G, d)
        # 删除第一个出现的元素
        G.remove(u)
        for v, w in graph[u]:
            if d[v] == -1 or d[v] > d[u] + w:
                d[v] = d[u] + w
                pi[v] = u

    print_path(d, pi)

def floyd(graph):
    """ floyd算法

    :param graph:
    :return:
    """
    D = deepcopy(graph)
    keys = [i for i in graph.iterkeys()]
    n = len(keys)
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                dij = D[keys[i]][keys[j]]
                dik = D[keys[i]][keys[k]]
                dkj = D[keys[k]][keys[j]]
                if dik > 0 and dkj > 0:
                    if dij == -1 or dij > (dik + dkj):
                        dij = dik + dkj
                D[keys[i]][keys[j]] = dij
    print D


def kruthkal():
    """ 图的最小生成树算法，需要使用到并查集

    :return:
    """
    pass



def main():
    graph = {
        "s": [("t", 10), ("y", 5)],
        "t": [("x", 1), ("y", 2)],
        "x": [("z", 4)],
        "y": [("t", 3), ("z", 2), ("x", 9)],
        "z": [("s", 7), ("x", 6)]
    }

    graph_matix = defaultdict(lambda: defaultdict(lambda: -1))
    for s, v in graph.iteritems():
        for i in xrange(len(v)):
            e, w = v[i]
            graph_matix[s][e] = w
        graph_matix[s][s] = 0
    dijkstra(graph, "s")
    floyd(graph_matix)

if __name__ == '__main__':
    main()
