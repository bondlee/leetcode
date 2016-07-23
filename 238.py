# coding:utf-8

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        p = [1] * len(nums)
        for i, v in enumerate(nums):
            p[i] *= product
            product *= v
        ind = len(nums) - 1
        product = 1
        while ind >= 0:
            p[ind] *= product
            product *= nums[ind]
            ind -= 1
        return p

if __name__ == "__main__":
    sol = Solution()
    print sol.productExceptSelf([2, 3, 4, 5])
    pass