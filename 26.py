# coding: utf-8
# Created by bondlee on 2016/5/31


class Solution(object):

    def remove(self, nums):
        if not nums:
            return

        ls = len(nums)
        if ls < 2:
            return ls
        begin = pre = 0
        cur = 1
        while cur < ls:
            if nums[pre] != nums[cur]:
                nums[begin] = nums[pre]
                begin += 1
            pre += 1
            cur += 1

        begin += 1
        nums[begin] = nums[pre]
        return begin

if __name__ == '__main__':
    pass