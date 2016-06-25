# coding: utf-8
# Created by bondlee on 2016/5/11

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def sumn(n):
            strn = str(n)
            r = 0
            for i in strn:
                r += int(i) * int(i)
            return r
        nsum = sumn(n)
        states = set([])
        states.add(nsum)
        if nsum == 1:
            return True
        count = 10000
        while nsum != 1 and count > 0:
            nsum = sumn(nsum)
            if nsum == 1:
                return True
            if nsum in states:
                return False
            states.add(nsum)
        return  False

if __name__ == '__main__':
    sol = Solution()
    print sol.isHappy(50)
    pass