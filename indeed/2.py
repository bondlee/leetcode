# coding:utf-8

p = int(raw_input())
seq = raw_input()
seq = seq.split()
seq = map(int, seq)
edge = []
from collections import defaultdict
edic = defaultdict(lambda: 0)
for i,v in enumerate(seq):
    edge.append((i+1, v))
    edic[i+1] = 1

res = 0
for i in xrange(1, p+1):
    if edic[i]:
        start, q = edge[i-1]
        edic[i] = 0
        while q != start:
            pre, q = edge[q-1]
            edic[pre] = 0
        res += 1
print res