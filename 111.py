# coding: utf-8
# Created by bondlee on 2016/5/14

from tree import create_tree

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return 0
        from collections import deque
        queue = deque([])
        queue.appendleft(root)
        from collections import defaultdict
        tree_dic = defaultdict(lambda: 0)
        level = 1
        tree_dic[level] = 1
        while len(queue):
            level_count = tree_dic[level]
            ind = 0
            while level_count:
                q = queue.pop()
                level_count -= 1

                if not q.left and not q.right:
                    return level

                if q.left:
                    queue.appendleft(q.left)
                    tree_dic[level + 1] += 1
                if q.right:
                    queue.appendleft(q.right)
                    tree_dic[level + 1] += 1
            level += 1

        return level

if __name__ == '__main__':
    # [1, 2, 3, null, null, 4, null, null, 5]
    node = create_tree([1, 2, 3, "null", "null", 4, "null", "null", 5])
    sol = Solution()
    print sol.minDepth(node)
    pass