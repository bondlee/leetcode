# coding: utf-8
# Created by bondlee on 2016/5/14


from tree import create_tree

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        queue = deque([])
        queue.appendleft(root)
        from collections import defaultdict
        tree_dic = defaultdict(lambda: 0)
        level = 0
        tree_dic[level] = 1
        tree_list = []
        level_list = []
        while len(queue):
            level_count = tree_dic[level]
            ind = 0
            while level_count:
                q = queue.pop()
                level_count -= 1
                level_list.append(q.val)
                if q.left:
                    queue.appendleft(q.left)
                    tree_dic[level + 1] += 1
                if q.right:
                    queue.appendleft(q.right)
                    tree_dic[level + 1] += 1
            tree_list.append(level_list)
            level_list = []
            level += 1

        return tree_list


if __name__ == '__main__':
    pass