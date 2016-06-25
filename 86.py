# coding: utf-8
# Created by bondlee on 2016/5/29

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return
        ltc = lt = ListNode(None)
        gtec = gte = ListNode(None)
        node = head
        while node:
            if node.val < x:
                ltc.next = node
                ltc = ltc.next
            else:
                gtec.next = node
                gtec = gtec.next
            node = node.next
        ltc.next = None
        gtec.next = None

        if lt.next:
            ltc.next = gte.next
        else:
            lt = gte
        return lt.next

if __name__ == '__main__':
    pass