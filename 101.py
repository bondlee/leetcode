# coding: utf-8
# Created by bondlee on 2016/5/14

from tree import create_tree, get_tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        from collections import deque
        queue = deque([])
        root.num = 0
        queue.appendleft(root)
        from collections import  defaultdict
        tree_dic = defaultdict(lambda :0)

        # 层计数
        level = 0
        # 每层的节点数
        tree_dic[level] = 1

        while len(queue):
            level_count = tree_dic[level]
            ind = 0
            val_dic = defaultdict(lambda : 0)
            while level_count:
                q = queue.pop()
                level_count -= 1
                # 每个节点编号
                val_dic[q.num] = q.val
                if q.left:
                    queue.appendleft(q.left)
                    tree_dic[level+1] += 1
                    q.left.num = q.num*2
                if q.right:
                    queue.appendleft(q.right)
                    tree_dic[level + 1] += 1
                    q.right.num = q.num*2+1

            for i in val_dic:
                if val_dic[i] != val_dic[2**(level)-1-i]:
                    return False
            level += 1
            # 检查该层是否符合要求
        return True

if __name__ == '__main__':

    node = get_tree([2,3,3,4,5,5,4,"null","null",8,9,9,8])
    sol = Solution()
    print sol.isSymmetric(node)
    pass