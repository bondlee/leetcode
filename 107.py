# coding: utf-8
# Created by bondlee on 2016/5/14


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from tree import create_tree

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        queue = deque([])
        queue.appendleft(root)
        from collections import defaultdict
        tree_dic = defaultdict(lambda: 0)
        level = 0
        tree_dic[level] = 1
        tree_list = []
        level_list = []
        while len(queue):
            level_count = tree_dic[level]
            ind = 0
            while level_count:
                q = queue.pop()
                level_count -= 1
                level_list.append(q.val)
                if q.left:
                    queue.appendleft(q.left)
                    tree_dic[level + 1] += 1
                if q.right:
                    queue.appendleft(q.right)
                    tree_dic[level + 1] += 1
            tree_list.append(level_list)
            level_list = []
            level += 1

        tree_list.reverse()
        return tree_list

if __name__ == '__main__':
    # [1, 2, 3, null, null, 4, null, null, 5]
    node = create_tree([1, 2, 3, "null", "null", 4, "null", "null", 5])
    sol = Solution()
    print sol.levelOrderBottom(node)
    pass