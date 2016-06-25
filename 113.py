# coding: utf-8
# Created by bondlee on 2016/5/15


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        rlist = []
        def DFS(r, ls, ss, target):
            if not r:
                return
            ss += r.val
            if not r.left and not r.right:
                if ss == target:
                    ls = ls + str(r.val)
                    rlist.append(ls)
            ls = ls + str(r.val) + ","
            if r.left:
                DFS(r.left, ls, ss, target)
            if r.right:
                DFS(r.right, ls, ss, target)

        DFS(root, "", 0, sum)
        rrlist = []
        for i in rlist:
            rrlist.append([int(j) for j in  i.split(",")])

        return rrlist

if __name__ == '__main__':

    pass