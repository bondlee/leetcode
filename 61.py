# coding: utf-8
# Created by bondlee on 2016/5/30

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        lh = 0
        cur = head
        while cur:
            lh += 1
            cur = cur.next
        if lh <=1:
            return head
        k = k % lh
        h = head
        tail = head
        while k:
            h = h.next
            k -= 1
        while h.next:
            h = h.next
            tail = tail.next
        h.next = head
        node = tail.next
        tail.next = None
        return node

if __name__ == '__main__':
    pass