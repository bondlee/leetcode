# coding: utf-8
# Created by bondlee on 2016/5/25


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def merge(self, h1, h2):
        dummy = ListNode(0)
        c = dummy
        while h1 and h2:
            if h1.val <= h2.val:
                c.next = h1
                h1 = h1.next
            else:
                c.next = h2
                h2 = h2.next
            c = c.next
        c.next = h1 or h2
        return dummy.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        left = head
        right = head
        while right and right.next and right.next.next:
            left = left.next
            right = right.next.next

        right = left.next
        left.next = None
        h1 = self.sortList(head)
        h2 = self.sortList(right)
        return self.merge(h1, h2)

if __name__ == '__main__':
    pass