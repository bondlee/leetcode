# coding: utf-8
# Created by bondlee on 2016/5/14

from tree import get_tree
from copy import deepcopy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        from copy import deepcopy
        path_list = []
        def DFS(r, paths):
            if not root:
                return
            paths.append(r.val)
            if r.left:
                tmp_path = deepcopy(paths)
                DFS(r.left, tmp_path)
            if r.right:
                tmp_path = deepcopy(paths)
                DFS(r.right, tmp_path)
            if not r.left and not r.right:
                tmp_path = deepcopy(paths)
                path_list.append([str(i) for i in tmp_path])
        path_array = []
        DFS(root, path_array)
        return ["->".join(i) for i in path_list]

    def binaryTreePaths_tiny(self, root):
        path_list = []
        def DFS(r, ls):
            if not root:
                return

            if not r.left and not r.right:
                path_list.append(ls + str(r.val))
                return

            ls = ls + (str(r.val) + "->")
            if r.left:
                DFS(r.left, ls)
            if r.right:
                DFS(r.right, ls)

        DFS(root, "")
        return path_list

if __name__ == '__main__':
    sol = Solution()
    node = get_tree()
    print sol.binaryTreePaths(node)
    print sol.binaryTreePaths_tiny(node)
    pass