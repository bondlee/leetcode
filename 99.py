# coding: utf-8
# Created by bondlee on 2016/5/15

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        p = root
        pre = None
        wrong = []
        while p or len(stack):
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                if not pre:
                    pre = p
                if pre.val > p.val:
                    if len(wrong) > 1:
                        wrong[1] = p
                    else:
                        wrong.append(pre)
                        wrong.append(p)
                pre = p
                p = p.right
        if len(wrong) > 1:

            wrong[0].val ^= wrong[1].val
            wrong[1].val ^= wrong[0].val
            wrong[0].val ^= wrong[1].val



if __name__ == '__main__':
    from tree import get_tree, preorderTraversIter
    node = get_tree([3, 1, 2])
    print preorderTraversIter(node)
    sol = Solution()
    sol.recoverTree(node)
    print preorderTraversIter(node)
    pass