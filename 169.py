# coding: utf-8
# Created by bondlee on 2016/5/12

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 特殊解法，必须要主数在该队列中出现次数超过一半才有效
        candidate, count = None, 0
        for i in nums:
            if count == 0:
                candidate, count = i, 1
            elif i == candidate:
                count += 1
            else:
                count -= 1
        return candidate

if __name__ == '__main__':
    sol = Solution()
    print sol.majorityElement([1, 1, 1, 4, 6])
    pass