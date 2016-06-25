# coding: utf-8
# Created by bondlee on 2016/5/31

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        right = left = 0
        cur = 0
        while left < len(nums):
            if right < len(nums) and nums[left] == nums[right]:
                right += 1
            else:
                nums[cur] = nums[left]
                tmp = min(right - left, 2)
                while tmp:
                    nums[cur] = nums[left]
                    tmp -= 1
                    cur +=  1
                    left += 1
                left = right
        return cur

if __name__ == '__main__':

    sol = Solution()
    nums = [3, 3, 3, 1, 1, 1]
    l = sol.removeDuplicates(nums)
    print nums[0:l]

    pass