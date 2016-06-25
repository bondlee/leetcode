# coding: utf-8
# Created by bondlee on 2016/5/15


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        from collections import defaultdict, deque
        queue = deque([])
        queue.appendleft(root)
        level = 0
        level_dic = defaultdict(lambda :0)
        level_dic[level] = 1
        rlist = []
        while len(queue):
            level_list = []
            level_count = level_dic[level]
            while level_count:
                p = queue.pop()
                level_list.append(p.val)
                level_count -= 1

                if p.left:
                    queue.appendleft(p.left)
                    level_dic[level+1] += 1
                if p.right:
                    queue.appendleft(p.right)
                    level_dic[level+1] += 1

            if level % 2 == 0:
                rlist.append(level_list)
            else:
                level_list.reverse()
                rlist.append(level_list)
            level += 1
        return rlist





if __name__ == '__main__':
    pass