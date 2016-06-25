# coding: utf-8
# Created by bondlee on 2016/5/15


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rlist = []
        if not root:
            return rlist
        from collections import deque,defaultdict
        queue = deque([])
        level_dic = defaultdict(lambda: 0)
        level = 0
        queue.appendleft(root)
        level_dic[level] = 1

        while len(queue):
            lcout = level_dic[level]
            while lcout:
                q = queue.pop()
                lcout -= 1
                if q.left:
                    queue.appendleft(q.left)
                    level_dic[level+1] += 1
                if q.right:
                    queue.appendleft(q.right)
                    level_dic[level+1] += 1
                if not lcout:
                    rlist.append(q.val)
            level += 1

        return rlist


if __name__ == '__main__':
    from tree import  get_tree
    node = get_tree([1, 2, 3])
    sol = Solution()
    print sol.rightSideView(node)
    pass