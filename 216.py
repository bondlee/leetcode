# coding: utf-8
# Created by bondlee on 2016/7/3

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = range(1,10)
        target = n

        def dfs(cur, ind, s):
            while ind < len(candidates):
                v = candidates[ind]
                ss = s + v
                tmp = cur + [v]
                if ss == target and len(tmp) == k:
                    if not rdic[tuple(tmp)]:
                        res.append(tmp)
                        rdic[tuple(tmp)] = 1
                if ss < target:
                    ind += 1
                    dfs(tmp, ind, ss)
                    ind -= 1
                else:
                    break
                ind +=1

        from collections import defaultdict
        rdic = defaultdict(lambda :0)
        res = []
        cur = []
        dfs(cur, 0, 0)
        return res


if __name__ == '__main__':
    sol = Solution()
    print sol.combinationSum3(3, 10)
    pass