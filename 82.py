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
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        cur = head
        while cur and cur.next:
            # 发现开始重复的节点
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                # 删除这些重复的节点
                pre.next = cur
            else:
                pre = pre.next
                cur = cur.next
        return dummy.next

if __name__ == '__main__':
    pass