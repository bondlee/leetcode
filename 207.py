# coding: utf-8
# Created by bondlee on 2016/6/10

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        from collections import defaultdict, deque
        degree = defaultdict(lambda :0)
        graph = defaultdict(list)
        for pair in prerequisites:
            cur, pre = pair
            # 入度+1
            degree[cur] += 1
            graph[pre].append(cur)

        q = deque([])
        for i in xrange(numCourses):
            if not degree[i]:
                q.appendleft(i)
        nc = 0
        while len(q):
            n = q.pop()
            nc += 1
            ns = graph[n]
            for i in ns:
                degree[i] -= 1
                if not degree[i]:
                    q.appendleft(i)
        return nc == numCourses


if __name__ == '__main__':

    sol = Solution()
    print sol.canFinish(2, [[1,0]])
    pass