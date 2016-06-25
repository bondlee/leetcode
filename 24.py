# coding: utf-8
# Created by bondlee on 2016/5/24

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swap(self, a, b):
        t = b.val
        b.val = a.val
        a.val = t

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        node = pre = head
        curent = head.next
        while pre and curent:
            self.swap(pre, curent)
            pre = curent.next
            if curent.next:
                curent = curent.next.next

        return node

if __name__ == '__main__':
    pass