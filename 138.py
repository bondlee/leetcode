# coding: utf-8
# Created by bondlee on 2016/5/30

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        chead = pre = RandomListNode(None)
        copy_dict = {}
        cur = head

        while cur:
            node = RandomListNode(cur.label)
            copy_dict[cur] = node
            pre.next = copy_dict[cur]
            pre = pre.next
            cur = cur.next
        cur = head
        ccur = chead.next
        while cur:
            ccur.random = copy_dict[cur.random] if cur.random else None
            cur = cur.next
            ccur = ccur.next
        return chead.next

if __name__ == '__main__':
    pass