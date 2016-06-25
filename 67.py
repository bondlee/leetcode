# coding: utf-8
# Created by bondlee on 2016/6/4

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)
        cur = 0
        ss = []
        while la and lb:
            na, nb = int(a[la-1]),  int(b[lb-1])
            tmp = na + nb + cur
            sn = tmp % 2
            cur = tmp / 2
            ss.append(sn)
            la -= 1
            lb -= 1
        while la:
            na = int(a[la-1])
            tmp = na + cur
            sn = tmp % 2
            cur = tmp / 2
            ss.append(sn)
            la -= 1
        while lb:
            na = int(b[lb - 1])
            tmp = na + cur
            sn = tmp % 2
            cur = tmp / 2
            ss.append(sn)
            lb -= 1
        if cur:
            ss.append(cur)
        ss.reverse()
        return "".join([str(i) for i in ss])

if __name__ == '__main__':
    sol = Solution()
    print sol.addBinary("111111", "11")
    pass