# coding: utf-8
# Created by bondlee on 2016/6/4

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        pair_dic = {
             0 : "1",
            "{": "}",
            "[": "]",
            "(": ")"
        }
        for ind, cur in enumerate(s):
            if cur in pair_dic:
                stack.append(cur)
            else:
                p = stack[-1] if len(stack) else 0
                if pair_dic[p] == cur:
                    stack.pop()
                else:
                    return False
        if len(stack):
            return False
        return True
if __name__ == '__main__':
    pass