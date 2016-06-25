# coding: utf-8
# Created by bondlee on 2016/5/11

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import  defaultdict
        numDic = {}
        for i, v in enumerate(nums):
            if v not in numDic:
                numDic[v] = i
            else:
                if k >= (i - numDic[v]):
                    return True
                numDic[v] = i
        return False


if __name__ == '__main__':
    sol = Solution()
    print sol.containsNearbyDuplicate([], 1)
    pass