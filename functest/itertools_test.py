# coding: utf-8
# Created by bondlee on 2016/6/6

from itertools import count, cycle, repeat, dropwhile, product

def main():


    a = repeat(10, 10)
    c = cycle("ABCD")
    print [i for i in dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])]

    print [i for i in product([1, 2, 3], [4, 5, 6])]

if __name__ == '__main__':
    main()
    pass