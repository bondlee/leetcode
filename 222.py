# coding: utf-8
# Created by bondlee on 2016/5/15

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 返回节点的高度
        def height(r):
            if not r:
                return [0, 0]
            lh =  rh = 1
            p = q = r
            while p.left:
                lh +=1
                p = p.left
            while q.right:
                rh +=1
                q = q.right
            return [lh, rh]

        if not root:
            return 0

        node_count = 0

        node = root
        nl, nr = height(node)
        while node:
            # 根节点计数
            node_count += 1
            [llh, lrh] = height(node.left)
            [rlh, rrh] = height(node.right)
            # 左子树不平衡，向左树
            if llh != lrh:
                node_count += 2**rlh - 1
                node = node.left
            # 右子树不平衡,向右子树搜索
            elif rlh != rrh:
                node_count +=  2**llh - 1
                node = node.right
            else:
                # 两边分别平衡，不用找了
                node_count += 2**llh - 1
                node_count += 2**rlh - 1
                return node_count

if __name__ == '__main__':

    pass