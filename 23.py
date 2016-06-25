# coding: utf-8
# Created by bondlee on 2016/5/24


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return
        head = node = ListNode(0)
        from heapq import heapify, heappush, heappop

        heap = [(i.val, i) for i in lists if i]
        heapify(heap)

        while heap:
            val, n = heappop(heap)
            node.next = n
            node = node.next
            if n.next:
                heappush(heap, (n.next.val, n.next))
        return head.next

if __name__ == '__main__':
    sol = Solution()


    from heapq import heapify, heappush, heappop
    import random
    heap = []
    heapify(heap)
    for i in range(10):
        node = ListNode(random.randint(i, 100))
        heappush(heap, (node.val, node))
    while heap:
        n = heappop(heap)
        print n[0]

    pass