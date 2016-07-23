# coding: utf-8
# Created by bondlee on 2016/6/19

class Solution(object):

    def nocircle(self, nums):
        """

        :param nums:
        :return:
        """
        if len(nums) < 2:
            return nums[0]
        pp = nums[0]
        p = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            if nums[i] + pp > p:
                tmp = p
                p = nums[i] + pp
                pp = tmp
            else:
                pp = p
        return p

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]

        p = self.nocircle(nums[0:-1])
        q = self.nocircle(nums[1:])
        return max(p,q)


if __name__ == '__main__':
    sol = Solution()
    print sol.rob([1, 2, 2, 1])
    pass