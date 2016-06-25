# coding: utf-8
# Created by bondlee on 2016/6/19

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        from collections import defaultdict
        dp = defaultdict(lambda: {})
        ps = 0
        for i in xrange(1, m+1):
            ps += grid[i-1][0]
            dp[i][1] = ps
        ps = 0
        for j in xrange(1, n+1):
            ps += grid[0][j-1]
            dp[1][j] = ps

        for i in xrange(2, m+1):
            for j in xrange(2, n+1):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i-1][j-1]

        return dp[m][n]


if __name__ == '__main__':
    sol = Solution()
    print sol.minPathSum([[1,2,3], [2,1,1], [2,1,3]])
    pass