# coding: utf-8
# Created by bondlee on 2016/5/24


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def oddEvenList(self, head):

        ohead = odd = ListNode(1)
        ehead = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if head.next else None
        odd.next = ehead.next
        return ohead.next

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # 奇数的操作节点
        op = oh =  ListNode(0)
        oc = head
        # 偶数的操作节点
        ep = eh = ListNode(0)
        ec = head.next

        while oc and ec:
            # 偶数链表和奇数链表分别连接
            op.next = oc
            ep.next = ec

            # pre节点再向下移动
            op = oc
            ep = ec

            # cur节点向后移动
            # 奇数指针向后移
            oc = ec.next
            if oc:
                ec = oc.next
            else:
                # 节点个数为偶数
                ec = None

        # 完成奇数链表的连接
        if  oc:
            op.next = oc
            op = oc
            oc = oc.next

        # 奇数链表最后一个节点连接到偶数链表的第一个节点
        op.next = eh.next
        # 偶数链表的最后一个节点指向空
        ep.next = oc

        # 返回奇数节点的最后一个节点
        return oh.next

if __name__ == '__main__':
    pass