# coding: utf-8
# Created by bondlee on 2016/6/11

import heapq
import random

def main():
    a = [3, 2, 1]
    heapq.heapify(a)
    heapq.heappush(a, 6)
    heapq.heappush(a, 0)
    count = 1
    while a:
        u = heapq.heappop(a)
        if count:
            a[1] = 0.5
            count -= 1
        print u



if __name__ == '__main__':
    main()
    pass