# coding: utf-8
# Created by bondlee on 2016/6/18

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums: last, now = now, max(last + i, now)
        return now