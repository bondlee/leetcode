# coding: utf-8
# Created by bondlee on 2016/6/4

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or not k:
            return nums
        ln = len(nums)
        k = ln % k
        num_dic = {}
        for i, v in enumerate(nums):
            ind =  (i+k) % ln
            num_dic[ind] = v
        for i in xrange(ln):
            nums[i] = num_dic[i]


if __name__ == '__main__':
    pass