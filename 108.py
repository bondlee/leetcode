# coding: utf-8
# Created by bondlee on 2016/5/15

from tree import TreeNode
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        def build(ns):
            ln = len(ns)
            if not ln:
                return
            m = (ln-1)/2
            node = TreeNode(ns[m])
            node.left = build(ns[0:m])
            node.right = build(ns[m+1:])
            return node

        return build(nums)


if __name__ == '__main__':
    sol = Solution()
    node = sol.sortedArrayToBST([1,2,3,4,5,6])
    from tree import preorderTraversIter
    print preorderTraversIter(node)

    pass