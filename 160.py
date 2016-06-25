# coding: utf-8
# Created by bondlee on 2016/5/24

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def length(self, node):
        ln = 0
        p = node
        while p:
            ln += 1
            p = p.next
        return ln

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa = headA
        pb = headB

        while pa and pb:
            pa = pa.next
            pb = pb.next

        # pa到尽头了
        if not pa:
            pa = headB
            while pb:
                pa = pa.next
                pb = pb.next
            pb = headA
            while pa != pb:
                pa = pa.next
                pb = pb.next
        else:
            pb = headA
            while pa:
                pa = pa.next
                pb = pb.next
            pa = headB
            while pa != pb:
                pa = pa.next
                pb = pb.next
        return pa
if __name__ == '__main__':
    pass