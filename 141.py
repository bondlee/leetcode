# coding: utf-8
# Created by bondlee on 2016/5/25


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        slow = head
        fast = head.next

        while slow and fast:
            if slow == fast:
                return True
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
        return False

if __name__ == '__main__':
    pass