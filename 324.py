# coding: utf-8
# Created by bondlee on 2016/6/10

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        print nums
        print nums[1::2]
        return nums[::2]



if __name__ == '__main__':
    sol = Solution()
    print sol.wiggleSort([1, 5, 1, 1, 6, 4])
    pass