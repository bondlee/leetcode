# coding: utf-8
# Created by bondlee on 2016/5/9

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        numDic = defaultdict(lambda: 0)
        for i in nums:
            numDic[i] += 1
        nums = sorted(nums)
        sindDic = {}
        sols = defaultdict(lambda: 0)
        nlen = len(nums)
        for i in range(nlen):
            a = nums[i]
            for j in range(i+1, nlen):
                b = nums[j]
                for k in range(j+1, nlen):
                    c = nums[k]
                    d = target - a - b - c
                    if d in numDic and d > c:
                        sol = [a, b , c, d]
                        tmpDic = defaultdict(lambda:0)
                        for p in sol:
                            tmpDic[p] += 1
                        tt = 0
                        for t in tmpDic:
                            if tmpDic[t]>numDic[t]:
                                break
                            tt += tmpDic[t]
                        if tt == 4:
                            sol = sorted(sol)
                            solKey = ".".join([str(s) for s in sol])
                            sols[solKey] += 1
        solList = []
        for i in sols.iterkeys():
            solList.append([int(j) for j in i.split(".")])
        return solList

if __name__ == '__main__':
    sol = Solution()
    for i in sol.fourSum([2,1,0,-1], 2):
        print i
    pass
