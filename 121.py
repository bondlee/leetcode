# coding: utf-8
# Created by bondlee on 2016/6/19

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pre = 0
        cur = 0
        dp = 0
        while cur < len(prices):
            if prices[pre] < prices[cur]:
                dp = max(dp, prices[cur] - prices[pre])
            else:
                pre = cur
            cur += 1
        return dp



if __name__ == '__main__':
    sol = Solution()
    nums = range(4,7)
    nums.extend([5,4,1])
    nums.extend(range(1,10))
    print nums
    print sol.maxProfit(nums)
    pass