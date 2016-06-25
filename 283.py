# coding: utf-8
# Created by bondlee on 2016/6/1


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        nonp = 0
        for i, v in enumerate(nums):
            if v:
                nums[nonp] = v
                nonp += 1
        while nonp < len(nums):
            nums[nonp] = 0
            nonp += 1
        return nums

if __name__ == '__main__':
    pass