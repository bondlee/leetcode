# coding: utf-8
# Created by bondlee on 2016/5/15

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from tree import get_tree
from tree import TreeNode

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        rlist = []

        def preorder(r):
            if not r:
                return
            rlist.append(r)
            if r.left:
                preorder(r.left)
            if r.right:
                preorder(r.right)

        preorder(root)
        rl = len(rlist)
        # ind = 0
        # while ind  < rl-1:
        for i in xrange(rl-1):
            rlist[i].left = None
            rlist[i].right = rlist[i+1]


if __name__ == '__main__':

    node = get_tree()
    sol = Solution()
    r = sol.flatten(node)
    from tree import inorderTravers
    print inorderTravers(r)
    pass