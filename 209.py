# coding: utf-8
# Created by bondlee on 2016/5/31

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        from collections import defaultdict
        slist = defaultdict(lambda :0)
        ss = 0
        for i,v in enumerate(nums):
            ss += v
            slist[i] = ss
        left = 0
        right = 0
        if slist[len(nums)-1] < s:
            return 0
        ml = 10000
        while left <= right and right < len(nums):
            sp = slist[right] - slist[left] + nums[left]
            l = right - left + 1
            if sp < s:
                right += 1
            else:
                if l < ml:
                    ml = l
                left += 1
        return ml


if __name__ == '__main__':
    sol = Solution()
    print sol.minSubArrayLen(7, [2,3,1,2,4,3])
    pass