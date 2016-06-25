# coding: utf-8
# Created by bondlee on 2016/4/10

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        switcher = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(float(x) / y),
        }
        result = []
        for i, item in enumerate(tokens):
            if item not in switcher:
                result.append(int(item))
            else:
                a = result.pop()
                b = result.pop()
                c = switcher[item](b, a)
                result.append(c)
        return result.pop()

if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"] ))


