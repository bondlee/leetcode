# coding: utf-8
# Created by bondlee on 2016/5/15


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        r = root
        while r:
            stack.append(r)
            r = r.left
        x = 0
        while stack and x !=k:
            r = stack.pop()
            x += 1
            right = r.right
            while right:
                stack.append(right)
                right = right.left

        return r.val






if __name__ == '__main__':
    pass