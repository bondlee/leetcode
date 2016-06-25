# coding: utf-8
# Created by bondlee on 2016/5/14

from tree import  get_tree, preorderTraversIter

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def invert(r):
            if not r:
                return []
            left = right = None
            if r.left:
                left = invert(r.left)
            if r.right:
                right = invert(r.right)
            r.right = left
            r.left = right
            return r

        rt = invert(root)
        return rt

if __name__ == '__main__':
    sol = Solution()
    node = get_tree()
    rt = sol.invertTree(node)
    print preorderTraversIter(rt)

    pass