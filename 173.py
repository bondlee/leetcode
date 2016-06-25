# coding: utf-8
# Created by bondlee on 2016/5/15


from tree import get_tree
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.p = []
        self.refesh_stack(root)


    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.p:
            return False
        else:
            return True

    def next(self):
        """
        :rtype: int
        """
        cur = self.p.pop()
        self.refesh_stack(cur.right)
        return cur.val

    def refesh_stack(self, node):
        while node:
            self.p.append(node)
            node = node.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


if __name__ == '__main__':
    pass