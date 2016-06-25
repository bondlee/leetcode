# coding: utf-8
# Created by bondlee on 2016/6/10


class Solution(object):

    def dfs(self, s, b, g, v):
        i, j = s
        adj = []
        if j-1 >=0:
            adj.append((i, j-1))
        if j+1 <=b[1]:
            adj.append((i, j+1))
        if i-1 >=0:
            adj.append((i-1, j))
        if i+1 <= b[0]:
            adj.append((i+1, j))
        val_list = []
        for p,q in adj:
            if g[p][q] == "1" and not v[p][q]:
                val_list.append((p,q))
        return val_list

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        from collections import defaultdict
        visited = defaultdict(lambda : defaultdict(lambda : 0))
        root = defaultdict(lambda : defaultdict(lambda : -1))
        n, p = len(grid)-1, len(grid[0])-1
        ind = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                # 如果大陆
                if grid[i][j] == "1" and not visited[i][j]:
                    root[i][j] = ind
                    stack = [(i,j)]
                    while len(stack):
                        x,y = stack.pop()
                        visited[x][y] = 1
                        root[x][y] = ind
                        stack.extend(self.dfs((x,y), (n,p), grid, visited))
                    ind += 1
        return ind

if __name__ == '__main__':
    sol = Solution()
    print sol.numIslands(["11000","11000","00100","00011"])
    pass