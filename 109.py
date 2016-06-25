# coding: utf-8
# Created by bondlee on 2016/5/30

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def buildTree(self, s, start, end):
        if start > end:
            return None
        mid = (start + end)/2
        node = TreeNode(s[mid])
        node.left = self.buildTree(s, start, mid-1)
        node.right = self.buildTree(s, mid+1, end)
        return node

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        vs = []
        while head:
            vs.append(head.val)
            head = head.next
        ls = len(vs) - 1
        h = self.buildTree(vs, 0, ls)
        return h

if __name__ == '__main__':
    pass