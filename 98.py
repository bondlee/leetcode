# coding: utf-8
# Created by bondlee on 2016/5/15

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        p = root
        pre = None
        while p or len(stack):
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                if pre is not None and pre >= p.val:
                    return False
                pre = p.val
                p = p.right
        return True

if __name__ == '__main__':
    from tree import  get_tree
    node = get_tree([0, "null" ,-1])
    sol = Solution()
    print sol.isValidBST(node)

    pass