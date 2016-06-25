# coding: utf-8
# Created by bondlee on 2016/5/31

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        slist = []
        ss = 0
        for i,v in enumerate(nums):
            ss += v
            slist.append(ss)
        left = 0
        right = len(nums) - 1
        if ss[-1] < s:
            return 0
        while left <= right:
            sp = ss[right] - ss[left] + nums[left]
            # 小于回退
            if sp < s:
                if nums[left] < nums[right]:
                    left -= 1
                else:
                    right += 1

            if sp >= s:
                if nums[left] < nums[right]:
                    left += 1
                if nums[left] > nums[right]:
                    right -= 1

        return right - left + 1


if __name__ == '__main__':
    pass