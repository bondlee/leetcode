# coding: utf-8
# Created by bondlee on 2016/7/3

class Solution(object):



    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def check(cur, r, c):
            for i in range(r):
                # 检查同一列
                if board[i] == c:
                    return False
                # 检查对角线， (r-1， c-1), (r-1, c+1)
                if board[r-i-1] == c-i-1 or board[r-i-1] == c+i+1:
                    return False
            return True

        def dfs(cur, row):
            if row == n:
                res[0] += 1
                return
            for i in range(n):
                if check(cur, row, i):
                    board[row] = i
                    tmp = "."*n
                    tmp = tmp[0:i] + "Q" + tmp[i+1:]
                    dfs(cur + [tmp], row+1)
                    board[row] = -1

        board = [-1]*(n+1)
        res = [0]
        cur = []
        dfs(cur, 0)
        return res[0]

if __name__ == '__main__':
    sol = Solution()
    print sol.solveNQueens(20)
    pass