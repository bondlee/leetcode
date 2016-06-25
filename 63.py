# coding: utf-8
# Created by bondlee on 2016/6/19


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        dp = defaultdict(lambda: defaultdict(lambda: 0))
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0]:
            return 0
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    continue
                if obstacleGrid[i-1][j-1]:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]
if __name__ == '__main__':
    sol = Solution()
    print sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
    pass