# coding: utf-8
# Created by bondlee on 2016/6/11
from collections import defaultdict

def find_root(n, r):
    if r[n] == -1:
        return n
    else:
        tmp = find_root(r[n], r)
        r[n] = tmp
        return tmp


def union():
    a = xrange(1001)
    r = defaultdict(lambda :-1)
    edges = zip(xrange(1000), xrange(1,1001))
    for x, y in edges:
        xr = find_root(x, r)
        yr = find_root(y, r)
        if xr != yr:
            r[y] = xr  # 加入到同一个集合中
    print r

if __name__ == '__main__':
    union()
    pass