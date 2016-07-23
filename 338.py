# coding:utf-8

class Solution():
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        d = {}
        d[0] = 0
        for i in range(0,32):
            d[2**i] = 1
        r = []
        for i in range(0,num+1):
            r.append(sum([d[j&i] for j in d]))
        return r


if __name__ == "__main__":
    sol = Solution()
    print sol.countBits(5)
    pass