# coding: utf-8
# Created by bondlee on 2016/5/8

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import  defaultdict
        import heapq
        numdic = defaultdict(lambda : 0)
        for i in nums:
            numdic[i] += 1

        rh = heapq.nlargest(k, numdic.iteritems(), key=lambda x: x[1])
        rh = [x[0] for x in rh]
        return rh

if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))
    pass