# coding: utf-8
# Created by bondlee on 2016/5/14

class TreeNode(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


def get_tree(s=None):
    # [1, 2, 3, null, null, 4, null, null, 5]
    # [2,3,3,4,5,5,4,"null","null",8,9,9,8]
    if not s:
        return create_tree([1, 2, 3, "null", "null", 4, "null", "null", 5])
    else:
        return create_tree(s)

def create_tree(s):
    """ 根据字符串建立一棵树

    :param s:
    :return:
    """
    if not s:
        return None
    ind = 0
    root = TreeNode(s[0])
    from collections import  deque
    queue = deque([root])

    sl = len(s)
    while len(queue) and ind < sl:
        node = queue.pop()
        ind += 1
        if ind < sl and s[ind] != "null":
            l = TreeNode(int(s[ind]))
            node.left = l
            queue.appendleft(l)
        ind += 1
        if ind < sl and s[ind] != "null":
            r = TreeNode(int(s[ind]))
            node.right = r
            queue.appendleft(r)

    return root


def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    rlist = []

    def inorder(r):
        if not r:
            return "#"
        if r.left:
            inorder(r.left)
        rlist.append(r.val)
        if r.right:
            inorder(r.right)

    inorder(root)
    return rlist


def inorderTravers(root):
    rlist = []
    stack = []
    p = root
    while p or len(stack):
        if p:
            stack.append(p)
            p = p.left
        else:
            p = stack.pop()
            rlist.append(p.val)
            p = p.right
    return rlist


def preorderTravers(root):
    rlist = []

    def preorder(p):
        if not p:
            return
        rlist.append(p.val)
        preorder(p.left)
        preorder(p.right)

    preorder(root)
    return rlist


def preorderTraversIter(root):
    rlist = []
    stack = []
    p = root
    while p or len(stack):
        if p:
            rlist.append(p.val)
            stack.append(p)
            p = p.left
        else:
            p = stack.pop()
            p = p.right
    return rlist


def postorder(root):
    rlist = []

    def postorder(p):
        if not p:
            return
        postorder(p.left)
        postorder(p.right)
        rlist.append(p.val)

    postorder(root)
    return rlist


def postorderTraversIter(root):
    rlist = []
    stack = []
    p = root
    while p or len(stack):
        if p:
            stack.append(p)
            p.visit = False
            p = p.left
        else:
            p = stack[-1]
            if not p.visit:
                p.visit = True
                p = p.right
            else:
                p = stack.pop()
                rlist.append(p.val)
                p = None
    return rlist


if __name__ == '__main__':
    pass