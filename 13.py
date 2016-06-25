# coding: utf-8
# Created by bondlee on 2016/5/14

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romDic = {}
        romDic["I"] = 1
        romDic["V"] = 5
        romDic["X"] = 10
        romDic["L"] = 50
        romDic["C"] = 100
        romDic["D"] = 500
        romDic["M"] = 1000
        r = 0
        pre = romDic[s[0]]
        curInd = 1
        while curInd < len(s):
            cur = romDic[s[curInd]]
            if pre < cur:
                pre = (cur - pre)
                curInd += 1
                continue
            else:
                r += pre
            curInd += 1
            pre = cur

        r += pre
        return r

if __name__ == '__main__':
    sol = Solution()
    print sol.romanToInt("MMXC")
    pass