# coding: utf-8
# Created by bondlee on 2016/5/25

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = head
        cur = head.next
        while cur:
            if pre.val == cur.val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return head


if __name__ == '__main__':
    pass