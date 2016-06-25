# coding: utf-8
# Created by bondlee on 2016/5/29

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return head
        slow = head.next
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 找到中点, 分裂成两个链表
        pre = None
        cur = slow.next
        slow.next = None
        while cur:
            t = cur.next
            cur.next = pre
            pre = cur
            cur = t
        rhead = pre

        # 合并两个链表
        la = head
        lb = rhead
        while la or lb:
            na = la.next
            nb = lb.next if lb else None
            la.next = lb
            la = na
            if lb:
                lb.next = la
            lb = nb
        return head

if __name__ == '__main__':
    pass