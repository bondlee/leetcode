# coding: utf-8
# Created by bondlee on 2016/7/3

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        def dfs(cur, ss, k):
            if not ss:
                res[0] = "".join([str(i) for i in cur])
                return
            q, m = divmod(k-1, math.factorial(len(ss)-1))
            dfs(cur + [ss[q]], ss[0:q] + ss[q+1:], m+1)

        nums = range(1, n+1)
        cur = []
        res = [0]
        dfs(cur, nums, k)
        return res[0]



if __name__ == '__main__':
    sol = Solution()
    print sol.getPermutation(10, 2)
    pass