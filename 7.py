# coding: utf-8
# Created by bondlee on 2016/5/13

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xx = abs(x)
        r = 0
        while xx != 0:
            r = r*10 + xx%10
            xx = xx/10
        if x < 0:
            r = -r
        if r > 2**31-1 or r < -2**31:
            r = 0
        return r




if __name__ == '__main__':
    sol = Solution()
    print sol.reverse(1000000003)
    pass