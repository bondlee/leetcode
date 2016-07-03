# coding: utf-8
# Created by bondlee on 2016/7/3

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(r, i, j):
            if res[0]:
                return
            if r == len(word):
                res[0] = 1
                return
            if r < len(word):
                pos = [(i, j+1), (i,j-1), (i+1, j), (i-1, j)]
                for p in pos:
                    ii, jj = p
                    if not check[ii][jj] and board[ii][jj] == word[r]:
                        check[ii][jj] = 1
                        dfs(r+1, ii, jj)
                        check[ii][jj] = 0

        from collections import defaultdict
        check = defaultdict(lambda :defaultdict(lambda :1))
        slist = []

        res = [0]
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                check[i][j] = 0
                if v == word[0]:
                    slist.append((i,j))
        for s in slist:
            if not res[0]:
                i, j = s
                check[i][j] = 1
                dfs(1, *s)
                check[i][j] = 0
            else:
                break
        return res[0] == 1



if __name__ == '__main__':
    sol = Solution()
    print sol.exist([
  ['a','a'],
], "aaa")
    pass