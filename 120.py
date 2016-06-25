# coding: utf-8
# Created by bondlee on 2016/6/19

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        from collections import  defaultdict
        dp = defaultdict(lambda :{})
        dp[0][0] = triangle[0][0]
        ind = 0
        for i, items in enumerate(triangle):
            if not i:
                continue
            for j, v in enumerate(items):
                if j-1 not in dp[i-1]:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j not in dp[i-1]:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            ind += 1
        return min([dp[ind][i] for i in dp[ind]])

if __name__ == '__main__':
    sol = Solution()
    print sol.minimumTotal([[2],[2,4],[6,5,1],[4,1,8,3]])
    pass