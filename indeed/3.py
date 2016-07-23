# coding:utf-8

def dfs(s, r):
    if s==36:
        for i in xrange(6):
            if prow[i] !=3 or pcol[i] !=3:
                return
        print r
        r[0] += 1
        return
    if prow[s/6] > 3 and pcol[s%6] > 3:
        return
    if not table[s/6][s%6] and prow[s/6] < 3 and pcol[s%6] < 3:
        prow[s/6] += 1
        pcol[s%6] += 1
        table[s/6][s%6] = 1
        dfs(s+1, r)
        prow[s/6] -= 1
        pcol[s%6] -= 1
        table[s/6][s%6] = 0
    else:
        dfs(s+1, r)

ts = []
for i in range(6):
   s = raw_input()
   ts.append(s)

from collections import defaultdict
prow = defaultdict(lambda :0)
pcol = defaultdict(lambda :0)
table = defaultdict(lambda :defaultdict(lambda :0))

for i, s in enumerate(ts):
    for j, v in enumerate(s):
        if v == "o":
            prow[j] +=1
            pcol[i] += 1
            table[i][j] = 1

result = [0]
flag = True
for i in xrange(6):
    if prow[i] > 3 or pcol[i] > 3:
        print 0
        flag = False
        break

if flag:
    dfs(0, result)
    print result[0]