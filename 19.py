# coding: utf-8
# Created by bondlee on 2016/5/25


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 使用快慢指针，快指针比慢指针快n个节点，然后两个指针同步下移
        # 当快指针到达末尾时，慢指针指的点恰好是需要删除的点
        slow = head
        ps = None
        fast = head
        while n:
            fast = fast.next
            n -= 1
        while fast:
            ps = slow
            slow = slow.next
            fast = fast.next
        if ps:
            ps.next = slow.next
        else:
            return head.next

        return head


if __name__ == '__main__':
    pass