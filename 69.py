# coding: utf-8
# Created by bondlee on 2016/6/29

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return x
        a = float(1)
        count = 1000
        while count:
            a = (a*a+x)/(2*a)
            count -= 1
        return int(a)


    def binary(self, x):
        """

        :param x:
        :return:
        """
        l = 0
        r = x/2 + 1
        while l <= r:
            mid = (l+r)/2
            sq = mid*mid
            if sq == x:
                return mid
            if sq < x:
                l = mid+1
            else:
                r = mid-1
        return r

if __name__ == '__main__':
    sol =Solution()
    print sol.binary(4)

    pass