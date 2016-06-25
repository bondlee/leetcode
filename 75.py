# coding: utf-8
# Created by bondlee on 2016/6/1

class Solution(object):

    def sortColors(self, nums, k):
        ps = [0] * (k-1)
        for i,v in enumerate(nums):
            nums[i] = k-1
            ind = k - 2
            while ind >=v and ind <= k-2 :
                nums[ps[ind]] = ind
                ps[ind] += 1
                ind -= 1


if __name__ == '__main__':
    sol = Solution()
    k = 10
    nums = range(k)*k
    print nums
    sol.sortColors(nums, k)
    print nums
    pass