# coding: utf-8
# Created by bondlee on 2016/6/29

class Solution(object):

    def bpow(self, x, n):
        if n == 0:
            return 1
        half = n / 2
        pow = self.bpow(x, half)
        if n % 2:
            return pow * pow * x
        else:
            return pow * pow

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1/self.bpow(x, -n)
        else:
            return self.bpow(x, n)




if __name__ == '__main__':
    pass