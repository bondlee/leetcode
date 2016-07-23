# coding: utf-8
# Created by bondlee on 2016/7/3

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(cur, ss, k):
            if k == len(nums):
                res.append(cur)
                return
            for i, v in enumerate(ss):
                tmp = cur + [v]
                if not ndic[tuple(tmp)]:
                    ndic[tuple(tmp)] = 1
                    dfs(cur + [v], ss[0:i] + ss[i+1:], k+1)


        from collections import defaultdict
        ndic = defaultdict(lambda :0)
        res = []
        dfs([], nums, 0)
        return res

if __name__ == '__main__':

    sol = Solution()
    print sol.permute([3,3,0,0,2,3,2])
    pass