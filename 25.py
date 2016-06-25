# coding: utf-8
# Created by bondlee on 2016/5/30


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverse(self, h, t):
        cur = h
        pre = None
        while pre != t:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return [pre, h]

    def part(self, head, k):
        slow = head
        fast = head
        k -= 1
        while k and fast:
            fast = fast.next
            k -= 1
        return [slow, fast]

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        slow, fast = self.part(head, k)
        dummpy = ListNode(1)
        node = dummpy
        while fast:
            tmp = fast.next
            h, t= self.reverse(slow, fast)
            node.next = h
            node = t
            slow, fast = self.part(tmp, k)
        node.next = slow
        return dummpy.next

if __name__ == '__main__':
    pass