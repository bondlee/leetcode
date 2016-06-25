# coding: utf-8
# Created by bondlee on 2016/5/25

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        import sys
        sh = ListNode(-sys.maxint-1)
        while head:
            # 从头开始查找
            cur = sh
            pre = None
            while cur and head.val >= cur.val:
                pre = cur
                cur = cur.next

            # 找到插入位置，pre和cur之间，插入有序链表
            pre.next = head
            # 临时保存head下一个节点的位置
            tmp = head.next
            head.next = cur
            head = tmp

        return sh.next

if __name__ == '__main__':
    pass