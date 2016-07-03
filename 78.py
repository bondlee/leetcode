# coding: utf-8
# Created by bondlee on 2016/7/3

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(cur, ns):
            if not cur or not sdic[tuple(cur)]:
                res.append(cur)
                if cur:
                    sdic[tuple(cur)] = 1

            ind = 0
            while ind < len(ns):
                v = ns[ind]
                tmp = cur + [v]
                if not sdic[tuple(tmp)]:
                    dfs(tmp, ns[ind+1:])
                ind += 1

        res = []
        cur = []
        from collections import defaultdict
        sdic = defaultdict(lambda :0)
        nums.sort()
        dfs(cur, nums)
        return res



if __name__ == '__main__':
    sol = Solution()
    print sol.subsets([1, 2, 2, 2,3, 3,3, 2, 2, 2, 2 , 2])
    pass