# coding: utf-8
# Created by bondlee on 2016/5/24

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return
        h = cur = head
        pre = None

        # 找到删除位置
        while cur:
            if cur.val == val:
                # 刪除的元素在队首
                if not pre:
                    h = h.next
                    cur = cur.next
                else:
                    pre.next = cur.next
                    cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return h

if __name__ == '__main__':
    pass