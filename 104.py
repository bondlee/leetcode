# coding: utf-8
# Created by bondlee on 2016/5/14

from tree import create_tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(p):
            if not p:
                return 0
            left_depth = depth(p.left)
            right_depth = depth(p.right)
            return max(left_depth, right_depth) + 1
        return depth(root)

if __name__ == '__main__':
    node = create_tree([1, 2, 3, "null", "null", 4, "null", "null", 5])
    sol = Solution()
    print sol.maxDepth(node)