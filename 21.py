# coding: utf-8
# Created by bondlee on 2016/5/25

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):


    def mergeTwoLists1(self, l1, l2):
        h1 = l1
        h2 = l2
        # 使用头结点，减少了15行判断是否是头结点的代码
        cur = head = ListNode(0)
        while h1 and h2:
            if h1.val <= h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next
        # 剩下差值，直接链接下去
        cur.next = h2 if not h1 else h1
        return head.next

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h1 = l1
        h2 = l2
        if not h1 and not h2:
            return
        cur = head = None
        if not h1:
            cur = head = h2
            h2 = h2.next
        elif not h2:
            cur = head = h1
            h1 = h1.next
        else:
            if h1.val <= h2.val:
                cur = head = h1
                h1 = h1.next

        while h1 and h2:
            if h1.val <= h2.val:
                if not head:
                    cur = head = h1
                    h1 = h1.next
                else:
                    cur.next = h1
                    h1 = h1.next
                    cur = cur.next
            else:
                if not head:
                    cur = head = h2
                    h2 = h2.next
                else:
                    cur.next = h2
                    h2 = h2.next
                    cur = cur.next
        delta = None
        if not h1:
            delta = h2
        if not h2:
            delta = h1
        while delta:
            if not head:
                cur = head = delta
                delta = delta.next
            else:
                cur.next = delta
                delta = delta.next
                cur = cur.next
        return head


if __name__ == '__main__':
    pass