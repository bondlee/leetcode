# coding: utf-8
# Created by bondlee on 2016/6/19


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        from collections import defaultdict
        dp = defaultdict(lambda: defaultdict(lambda: 0))
        dp[1][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j==1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]

if __name__ == '__main__':
    sol = Solution()
    print sol.uniquePaths(3,3)
    pass