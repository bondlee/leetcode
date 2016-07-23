# coding:utf-8

from collections import defaultdict

class Solution():

    def isValid(self, cur, row, col):
        """ 判断当前状态是否合法

        :param cur:
        :param row:
        :param col:
        :return:
        """
        for i in xrange(row):
            if cur[i][col] == "Q":
                return False
            m = row-i-1
            n = col-i-1
            if m>=0 and n >=0 and cur[m][n] == "Q":
                return False
            p = row-i-1
            q = col+i+1
            if p>=0 and q<len(cur) and cur[p][q] == "Q":
                return False
        return True

    def solve(self, cur, row):
        if row == len(cur):
            print cur
        else:
            for i in xrange(len(cur)):
                if self.isValid(cur, row, i):
                    cur[row][i] = "Q"
                    self.solve(cur, row+1)
                    cur[row][i] = "."

    def nqueue(self, n):
        r = [["."]*n for i in range(n)]
        self.solve(r, 0)




    def solveNQueens(self, n):
        def check(k, j):  # check if the kth queen can be put in column j!
            for i in range(k):
                if board[i]==j or abs(k-i)==abs(board[i]-j):
                    return False
            return True
        def dfs(depth, valuelist):
            if depth==n: res.append(valuelist); return
            for i in range(n):
                if check(depth,i):
                    s='.'*n
                    board[depth] = i
                    dfs(depth+1, valuelist+[s[:i]+'Q'+s[i+1:]])


        board=[-1 for i in range(n)]
        res=[]
        dfs(0,[])
        return res


if __name__ == "__main__":
    sol = Solution()
    print sol.nqueue(4)
    # print sol.solveNQueens(10)
    pass