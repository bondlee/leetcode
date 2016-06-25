# coding: utf-8
# Created by bondlee on 2016/5/25

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swap(self, a, b):
        t = a.val
        a.val = b.val
        b.val = t
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m == n:
            return head
        stack =[]
        p = head
        m -= 1
        n -= 1
        while n:
            if m <= 0:
                stack.append(p)
            p = p.next
            n -= 1
            m -= 1

        stack.append(p)
        right = len(stack) - 1
        left = 0
        while left <= right:
            self.swap(stack[left], stack[right])
            left += 1
            right -= 1
        return head

if __name__ == '__main__':
    pass