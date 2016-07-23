# coding:utf-8

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.m = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.s.append(x)
        if self.m is None:
            self.m = x
        elif x < self.m:
            self.m = x

    def pop(self):
        """
        :rtype: void
        """
        self.s.pop()
        if not self.s:
            self.m = None
        else:
            self.m = min(self.s)

    def top(self):
        """
        :rtype: int
        """
        if not self.s:
            return None
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.m


if __name__ == "__main__":
    sol = MinStack()
    print sol.push(1)
    print sol.push(2)
    print sol.push(3)
    print sol.push(4)
    print sol.pop()
    print sol.top()
    print sol.getMin()
    pass