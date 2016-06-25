# coding: utf-8
# Created by bondlee on 2016/5/14

from tree import  get_tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        rlist = []
        def DFS(r, ls):
            if not r:
                return
            t = ls*10 + r.val
            if not r.left and not r.right:
                rlist.append(t)
                return
            if r.left:
                DFS(r.left, t)
            if r.right:
                DFS(r.right, t)
        DFS(root, 0)
        return sum(rlist)

if __name__ == '__main__':
    node = get_tree()
    sol = Solution()
    print sol.sumNumbers(node)
    pass