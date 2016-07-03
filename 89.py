# coding: utf-8
# Created by bondlee on 2016/7/3

from collections import defaultdict

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def dfs(cur, rc):
            if rc == n:
                res = cur
                return True
            for i in range(n):
                tmp = cur[-1]
                tmp[i] = tmp&
                if not board[tuple(tmp)]:
                    board[tuple(tmp)] = 1
                    if not dfs(cur + [list(tmp)], rc+1):
                        board[tuple(tmp)] = 0
                    else:
                        break
            return False

        res = []
        rc = 0
        cur = [0]
        board = defaultdict(lambda: 0)
        dfs(cur, 0)
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.grayCode(2)
    pass