# coding: utf-8
# Created by bondlee on 2016/5/14

from tree import get_tree

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        rlist = []
        def DFS(r, ls, s, ss):
            if not r:
                return
            s += r.val
            if not r.left and not r.right:
                if s == ss:
                    rlist.append(ls + str(r.val))
            ls = ls + str(r.val) + "->"
            if r.left:
                DFS(r.left, ls, s, ss)
            if r.right:
                DFS(r.right, ls, s, ss)

        DFS(root, "", 0, sum)
        if not len(rlist):
            return False
        else:
            return True

if __name__ == '__main__':
    from tree import create_tree
    node = create_tree([-2, "null", -3])
    sol = Solution()
    print sol.hasPathSum(node, -5)
    pass