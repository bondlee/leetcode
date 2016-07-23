# coding:utf-8

class Solution():
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zz = 0
        ind = 1
        while 5**ind <=n:
            zz += n/5**ind
            ind +=1
        return zz

if __name__ == "__main__":
    sol = Solution()
    print sol.trailingZeroes(0)
    pass