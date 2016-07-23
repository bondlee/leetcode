# coding: utf-8
# Created by bondlee on 2016/7/3

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(cur, ind):
            if len(cur) == k:
                res.append(cur)
                return
            while n-ind >= k-len(cur):
                v = nums[ind]
                dfs(cur + [v], ind+1)
                ind += 1

        nums = xrange(1, n+1)
        res = []
        dfs([], 0)
        return res


if __name__ == '__main__':
    sol = Solution()
    print sol.combine(5, 2)
    pass