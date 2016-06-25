# coding: utf-8
# Created by bondlee on 2016/5/11


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        nlen = len(nums)
        for i in xrange(nlen):
            for j in range(i+1, min(i+k+1, nlen)):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.containsNearbyAlmostDuplicate([1, 3, 5, 7, 9], 10000, 1)
    pass