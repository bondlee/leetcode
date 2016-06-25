# coding: utf-8
# Created by bondlee on 2016/5/21


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        from collections import defaultdict, deque
        queue = deque([])
        ps = []
        qs = []
        queue.appendleft(root)
        count = 2
        root.parent = None
        pp = None
        qq = None
        s = []
        while len(queue):
            node = queue.pop()
            # 对象的引用
            if node == p:
                s.append(node)
            elif node == q:
                s.append(node)

            if node.left:
                node.left.parent = node
                queue.appendleft(node.left)
            if node.right:
                node.right.parent = node
                queue.appendleft(node.right)

        pp = s[-2]
        while pp:
            ps.append(pp)
            pp = pp.parent
        qq = s[-1]
        while qq:
            qs.append(qq)
            qq = qq.parent

        pre = 1
        pi = len(ps) - pre
        qi = len(qs) - pre
        while qi>=0 and pi>=0 and ps[pi].val == qs[qi].val:
            pre += 1
            pi = len(ps) - pre
            qi = len(qs) - pre

        return ps[pi+1]

if __name__ == '__main__':
    from tree import  get_tree, TreeNode
    node = get_tree([37,-34,-48,"null",-100,-100,48,"null","null","null","null",-54,"null",-71,-22,"null","null","null",8])
    p = TreeNode(-100)
    q = TreeNode(-100)
    sol = Solution()
    print sol.lowestCommonAncestor(node, p, q).val
    pass