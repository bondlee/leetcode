# coding: utf-8
# Created by bondlee on 2016/5/15

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(cur, ss, k):
            if k == len(nums):
                res.append(cur)
            for i, v in enumerate(ss):
                dfs(cur + [v], ss[0:i] + ss[i+1:], k+1)
        ndic = {}
        for i in nums:
            ndic[i] = 1
        res = []
        dfs([], nums, 0)
        return res



if __name__ == '__main__':
    pass