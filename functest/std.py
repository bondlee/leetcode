# coding: utf-8
# Created by bondlee on 2016/6/6

import sys

def test_stdout():
    fsock = open("info.log", "wb")
    print "open files "
    sys.stdout.write("open file to stdout")
    sys.stdout = fsock
    print "write file"
    sys.stdout.write("write to stdout")
    sys.stdout.write("change file as stdout, write info to stdout")


def test_stderr():
    sys.stdout.write("write msg to stdout")
    sys.stderr.write("write msg to stderr")
    raise ValueError("std error")


def test_stderr_file():

    fsock = open("error.log", "wb")
    sys.stderr = fsock
    sys.stderr.write("write msg to stderr\n")
    print >> sys.stderr, "enetering function"
    raise ValueError("STD ERROR")

def test_stdin():
    fsock = open("input.log", "r")
    sys.stdin = fsock
    a = raw_input()
    print a
    sys.stdin.flush()



if __name__ == '__main__':
    # test_stdout()
    test_stdin()
    try:
        test_stderr()
    except Exception as e:
        print e
    finally:
        test_stderr_file()
    pass