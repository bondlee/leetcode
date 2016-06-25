# coding: utf-8
# Created by bondlee on 2016/5/24


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def swap(self, x, y):
        t = x.val
        x.val = y.val
        y.val = t
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = []
        h = p = head
        while p:
            node.append(p)
            p = p.next
        ln = len(node)
        for i in range(ln/2):
            self.swap(node[i], node[ln-i-1])
        return h

if __name__ == '__main__':
    pass