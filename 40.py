# coding: utf-8
# Created by bondlee on 2016/7/3

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(cur, ind, s):
            while ind < len(candidates):
                v = candidates[ind]
                ss = s + v
                tmp = cur + [v]
                if ss == target:
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

        candidates.sort()
        from collections import defaultdict
        rdic = defaultdict(lambda :0)
        res = []
        cur = []
        dfs(cur, 0, 0)
        return res




if __name__ == '__main__':
    sol = Solution()
    print sol.combinationSum2([32,33,5,32,12,7,17,33,29,13,18,16,23,28,26,26,12,6,23,19,22,12,9,6,5,34,22,27,11,33,27,30,24,27,27,31,29,32,21,24,32,5,27,21,20,10,12,28,11,31,12,20,30,17,21,30,8,8], 27)
    pass