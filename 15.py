# coding: utf-8
# Created by bondlee on 2016/5/9

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        nums.sort()
        solList = []
        nlen = len(nums)
        for i in range(nlen-2):
            a = nums[i]
            if i == 0 or (i > 0 and nums[i]!= nums[i-1]):
                left = i + 1
                right = nlen - 1
                while left < right:
                    delta = target - (a + nums[left] + nums[right])
                    if delta == 0:
                        sol = [a, nums[left], nums[right]]
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        solList.append(sol)
                        left += 1
                        right -= 1
                    elif delta < 0:
                        right -= 1
                    else:
                        left += 1
        # strList = [".".join(str(e) for e in sol) for sol in solList]
        # strSet = set(strList)
        #
        # solList = []
        # for i in strSet:
        #     solList.append([int(j) for j in i.split(".")])
        return solList

if __name__ == '__main__':
    sol = Solution()
    for i in sol.threeSum([0, 0, 0, 0]):
        print i
    pass