# coding: utf-8
# Created by bondlee on 2016/6/4

s = raw_input()
m = int(raw_input())
# 位置映射
pdic = {}
ls = len(s)

for i, v in enumerate(s):
    pdic[i+1] = v

for j in xrange(m):
    step = pdic[1]
    ind = 1
    while ind < int(step):
        pdic[ind] = pdic[ind+1]
        ind += 1
    pdic[ind] = step

print "".join([pdic[i]for i in xrange(1, ls+1)])


if __name__ == '__main__':
    pass