# coding: utf-8
# Created by bondlee on 2016/5/31


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cur = 0
        for i,v in enumerate(nums):
            if v != val:
                nums[cur] = v
                cur += 1
        return cur


if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,3,3,2,3,3,3]
    l = sol.removeElement(nums, 3)
    print nums[0:l]
    pass