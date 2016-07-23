# coding:utf-8


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ln = len(prices)
        if ln < 2:
            return 0
        cur = 0
        ne = cur + 1
        profit = 0
        while ne < ln:
            if prices[cur] < prices[ne]:
                profit += prices[ne] - prices[cur]
            cur = ne
            ne += 1
        profit += prices[-1] - prices[cur]
        return profit

if __name__ == "__main__":
    sol = Solution()
    print sol.maxProfit([1, 2, 3])