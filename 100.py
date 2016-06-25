# coding: utf-8
# Created by bondlee on 2016/5/14

from tree import  create_tree

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def isame(p, q):

            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            l = isame(p.left, q.left)
            r = isame(p.right, q.right)
            return l and r

        return isame(p, q)
if __name__ == '__main__':

    sol = Solution()
    p = create_tree([1, 1])
    q = create_tree([1, 1])

    print sol.isSameTree(p, q)

    pass