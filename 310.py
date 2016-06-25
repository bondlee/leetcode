# coding: utf-8
# Created by bondlee on 2016/6/10

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return range(n)
        from collections import defaultdict, deque
        d, g, dn = defaultdict(lambda :0), defaultdict(set), defaultdict(set)
        for e in edges:
            i, j = e
            g[i].add(j)
            g[j].add(i)

        # 状态和队列
        q = deque([])
        # 选择端点作为起点, 然后做拓扑排序，得到最中间的那个点
        heads = [i for i in g if len(g[i]) == 1]
        s = set(heads)
        for head in heads:
            d[head] = 0
            dn[d[head]].add(head)
            q.appendleft(head)
        while len(q):
            n = q.pop()
            if g[n]:
                i = list(g[n])[0]
                g[n].remove(i)
                g[i].remove(n)
                if i not in s:
                    if i in dn[d[i]]:
                        dn[d[i]].remove(i)
                    d[i] = d[n] + 1
                    dn[d[i]].add(i)
                if len(g[i]) == 1:
                    q.appendleft(i)
                    s.add(i)
        md = max(dn.iterkeys())
        return list(dn[md])

if __name__ == '__main__':
    sol = Solution()
    print sol.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
    pass