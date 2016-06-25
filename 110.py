# coding: utf-8
# Created by bondlee on 2016/5/14

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1

        if not root:
            return True
        left = depth(root.left)
        right = depth(root.right)

        return abs(left - right) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == '__main__':

    sol = Solution()
    sol.isBalanced()

    pass