# coding: utf-8
# Created by bondlee on 2016/7/3

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(cur, s):
            for i in candidates:
                if not cur or i >= cur[-1]:
                    ss = s+i
                    tmp = cur + [i]
                    if ss == target:
                        res.append(tmp)
                    elif ss < target:
                        dfs(tmp, ss)
        cur = []
        res = []
        candidates = list(set(candidates))
        candidates.sort()
        dfs(cur, 0)
        return res


if __name__ == '__main__':

    sol = Solution()
    print sol.combinationSum([1, 1, 1, 1], 7)

    pass