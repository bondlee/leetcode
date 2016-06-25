# coding: utf-8
# Created by bondlee on 2016/6/9


def main():

    b = [{'a': 1.1, 'b': 1.2}, {'a': 2.1, 'b': 3.2}]
    # for y in b:
    c = map(lambda y: dict(map(lambda x: (x[0], int(x[1])), y.iteritems())), b)
    # map(lambda x: x,b)
    print c





if __name__ == '__main__':
    main()
    pass