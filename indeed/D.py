# coding: utf-8
# Created by bondlee on 2016/6/4

def min_cost(matrix, m, n):





s = raw_input()
H, W = map(int, s.split())
lines = []
for i in xrange(H):
    lines.append(raw_input())
lines = map(lambda x : map(int, x),lines)
