# coding: utf-8
# Created by bondlee on 2016/5/14

from tree import create_tree

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rlist = []
        def inorder(r):
            if not r:
                return "#"
            if r.left:
                inorder(r.left)
            rlist.append(r.val)
            if r.right:
                inorder(r.right)

        inorder(root)
        return rlist

    def inorderTravers(self, root):
        rlist = []
        stack = []
        p = root
        while p or len(stack):
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                rlist.append(p.val)
                p = p.right
        return rlist

    def preorderTravers(self, root):
        rlist = []
        def preorder(p):
            if not p:
                return
            rlist.append(p.val)
            preorder(p.left)
            preorder(p.right)
        preorder(root)
        return rlist

    def preorderTraversIter(self, root):
        rlist = []
        stack = []
        p = root
        while p or len(stack):
            if p:
                rlist.append(p.val)
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                p = p.right
        return rlist

    def postorder(self, root):
        rlist = []

        def postorder(p):
            if not p:
                return
            postorder(p.left)
            postorder(p.right)
            rlist.append(p.val)

        postorder(root)
        return rlist

    def postorderTraversIter(self, root):

        rlist = []
        stack = []
        p = root
        while p or len(stack):
            if p:
                stack.append(p)
                p.visit = False
                p = p.left
            else:
                p = stack[-1]
                if not p.visit:
                    p.visit = True
                    p = p.right
                else:
                    p = stack.pop()
                    rlist.append(p.val)
                    p = None
        return rlist

if __name__ == '__main__':
    node = create_tree([1, 2, 3, "null", "null", 4, "null", "null", 5])
    sol = Solution()
    print sol.inorderTraversal(node)
    print sol.inorderTravers(node)
    print sol.preorderTravers(node)
    print sol.preorderTraversIter(node)
    print sol.postorder(node)
    print sol.postorderTraversIter(node)

    pass