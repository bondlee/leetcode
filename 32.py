# coding: utf-8
# Created by bondlee on 2016/4/11

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        pn = 0
        max_pn = 0
        stack.append((-1,"#"))

        for i, item in enumerate(s):
            if item == "(":
                stack.append((i,item))
            elif len(stack) > 0 and stack[-1][1] == "(":
                stack.pop()
            else:
                stack.append((i,item))
        stack.append((len(s), "#"))
        upper = 0
        for i in range(len(stack) - 1):
            upper = stack[len(stack) - i - 1][0]
            lower = stack[len(stack) - i - 2][0]
            pn = upper - lower -1
            if pn > max_pn:
                max_pn = pn
            upper = lower
        return max_pn

if __name__ == '__main__':
    s = Solution()
    print s.longestValidParentheses(")(")
