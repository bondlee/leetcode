# coding:utf-8

class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2, i3, i5 = [0]*3
        ugly = [1]
        while n > 1:
            l1, l2, l3 = 2*ugly[i2], 3*ugly[i3], 5*ugly[i5]
            minu = min(l1, l2, l3)
            if minu == l1:
                i2 += 1
            if minu == l2:
                i3 += 1
            if minu == l3:
                i5 += 1
            ugly.append(minu)
            n -= 1
        return ugly[-1]


if __name__ == "__main__":
    sol = Solution()
    print sol.nthUglyNumber(10)
    pass