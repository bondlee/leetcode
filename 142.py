# coding: utf-8
# Created by bondlee on 2016/5/25


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return
        slow = head.next
        fast = head.next.next

        while slow != fast:
            if not slow or not fast:
                return
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow





if __name__ == '__main__':
    pass