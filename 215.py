# coding: utf-8
# Created by bondlee on 2016/5/23

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        ss = heapq.nlargest(k,nums)
        return ss[-1]

    def findKthLargest(self, nums, k):
        # 快速选择排序，利用快排的思想
        from random import randint
        pivot = nums[randint(0, len(nums)-1)]
        left = []
        equal = []
        right = []
        for i in nums:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                right.append(i)
        if k <= len(right):
            return self.findKthLargest(right, k)
        elif k <= (len(right) + len(equal)):
            return equal[0]
        else:
            return self.findKthLargest(left, k - len(right) - len(equal))


if __name__ == '__main__':
    sol = Solution()
    print sol.findKthLargest([2,1], 1)



    pass