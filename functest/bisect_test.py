# coding: utf-8
# Created by bondlee on 2016/6/6

import bisect
from collections import namedtuple
from itertools import  combinations_with_replacement
from collections import Counter

def test(*pa, **pb):
    print pa
    print pb
    b = pa[0]
    b = 4


def test_nametuple():
    Person = namedtuple("Person", ['age', 'sex'])
    b = Person(age=10, sex="male")
    x, y = b
    print x, y
    a = Person(12, "female")
    print a + b

def test_orderdic():
    """

    :return:
    """



def main():

    data = [('red', 5), ('blue', 2), ('yellow', 1), ('black', 10)]
    data.sort(key=lambda x:x[1])
    keys = [r[1] for r in data]
    bisect.insort_left(keys, ("t1", 2))

    d = dict()
    d["1"] = 2
    d["2"] = 3

    c = [1, 2]
    # test(*c, **d)
    test_nametuple()


if __name__ == '__main__':
    main()
    a = combinations_with_replacement('ABC', 2)
    map(Counter, combinations_with_replacement('ABC', 2))




    pass