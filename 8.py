# coding: utf-8
# Created by bondlee on 2016/6/4

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        result = []
        str = str.strip()
        signal = 0
        if str[0] == "+" or str[0] == "-":
            signal = 1 if str[0] == "-" else 0
            str= str[1:]
        ind = 0
        while ind < len(str) and str[ind].isdigit():
            ind += 1
        str = str[:ind]
        if not str:
            return 0
        val = int(str)
        if signal:
            val = -val

        if val > INT_MAX:
            val = INT_MAX
        if val < INT_MIN:
            val = INT_MIN
        return val


if __name__ == '__main__':
    pass