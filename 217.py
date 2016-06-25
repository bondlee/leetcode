# coding: utf-8
# Created by bondlee on 2016/5/11

class Solution(object):
    # def containsDuplicate(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     return  len(set(nums)) != len(nums)

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsDic = {}
        for i in nums:
            if i not in numsDic:
                numsDic[i] = 0
            else:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.containsDuplicate([1, 2])
    pass