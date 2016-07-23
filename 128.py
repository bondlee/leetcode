# coding: utf-8
# Created by bondlee on 2016/5/8

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findRoot(x, rdic):

            # 根节点的父节点是自己
            if rdic[x] not in rdic:
                return rdic[x]+1

            ox = x # 保留原始的x值
            while x in rdic:
                x = rdic[x]
            r = x # 找到父节点

            # 路径压缩
            while ox in rdic:
                n = rdic[ox]
                rdic[ox] = r
                ox = n
            return r+1

        rootDic = {}
        nums = set(nums)
        nums = list(nums)
        for i in nums:
            rootDic[i] = i-1
        from collections import  defaultdict
        sumDic = defaultdict(lambda: 0)
        for i in nums:
            sumDic[findRoot(i, rootDic)] += 1
        return max(sumDic.itervalues())


if __name__ == '__main__':
    sol = Solution()
    print sol.longestConsecutive([100, 4, 200, 1, 3, 2, 5, 101, 102, 98, 99, 97, 100])
    pass