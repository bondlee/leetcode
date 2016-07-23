# coding:utf-8

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dpp = nums[0]
        dpmax = dpp
        ln = len(nums)
        for i in range(1, ln):
            dpc = nums[i] + dpp if dpp > 0 else nums[i]
            if dpc > dpmax:
                dpmax = dpc
            dpp =dpc
        return dpmax





        return ss[dpr]-ss[dpl]+nums[dpl]



if __name__ == "__main__":
    sol = Solution()
    print sol
    pass