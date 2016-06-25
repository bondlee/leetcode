# coding: utf-8
# Created by bondlee on 2016/5/15


class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root:
            from collections import deque, defaultdict
            queue = deque([])
            queue.appendleft(root)
            level_dic = defaultdict(lambda : 0)
            level = 0
            level_dic[level] = 1
            while len(queue):
                level_count = level_dic[level]
                pre = None
                while level_count:
                    q = queue.pop()
                    level_count -= 1
                    if not pre:
                        pre = q
                    else:
                        pre.next = q
                        pre = q
                    if q.left:
                        queue.appendleft(q.left)
                        level_dic[level+1] += 1
                    if q.right:
                        queue.appendleft(q.right)
                        level_dic[level+1] += 1
                level += 1


if __name__ == '__main__':
    pass