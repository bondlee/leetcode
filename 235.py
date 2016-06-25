# coding: utf-8
# Created by bondlee on 2016/5/21


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent = {root:None}
        s = []
        s.append(root)
        while len(s) and (p not in parent or q not in parent):
            node = s.pop()
            if node.left:
                parent[node.left] = node
                s.append(node.left)
            if node.right:
                parent[node.right] = node
                s.append(node.right)
        ancestor = []
        while p:
            ancestor.append(p)
            p = parent[p]

        while q not in ancestor:
            q = parent[q]
        return q
if __name__ == '__main__':
    pass