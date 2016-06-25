# coding: utf-8
# Created by bondlee on 2016/5/12


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        numDic = {}
        pre = "0."
        base = ""
        ind = 0
        while numerator not in numDic:
            numDic[numerator] = 0
            shang, yu = divmod(numerator*10, denominator)
            base += str(shang)
            numerator = yu
            ind += 1
        print numDic[numerator]
        # 整除
        if 0 in numDic:
            return pre + base[0:-1]
        else:
            # 非整除
            return pre + "(" + base + ")"

if __name__ == '__main__':
    sol = Solution()
    print sol.fractionToDecimal(1, 6)
    pass