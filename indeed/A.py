# coding: utf-8
# Created by bondlee on 2016/6/4

from copy import deepcopy
import itertools

s = raw_input()
ss = list(s)
sdic = {}
sdic[s] = 1
alpha = ["a", "b", "c", "d"]
for i in xrange(len(ss)):
    for t in alpha:
        st = deepcopy(ss)
        st[i] = t
        pwds = itertools.permutations(st, len(st))

        for pwd in pwds:
            pwd = "".join(pwd)
            if pwd not in sdic:
                sdic[pwd] = 1
pwd_list = [pwd for pwd in sdic.iterkeys()]
pwd_list.sort()
for i in pwd_list:
    print i
