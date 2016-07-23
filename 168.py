# coding:utf-8

class Solution():

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        alpha = {}
        for i in xrange(1,26):
            alpha[i] = chr(64+i)
        alpha[0] = "Z"
        s = []
        c = 1
        while n > 0 and c >=0:
            n, c = divmod(n, 26)
            s.append(alpha[c])
            if not c:
                n -= 1
        s.reverse()
        return "".join(s)


if __name__ == "__main__":
    sol = Solution()
    print sol.convertToTitle(2)

    pass