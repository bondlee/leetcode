# coding: utf-8
# Created by bondlee on 2016/6/4

class Solution(object):

    def sums(self, nums):
        """ n个数相加

        :param nums: str的集合
        :return:
        """
        cl = max([len(num) for num in nums])
        cind = 0
        carry = 0
        rs = []
        while cind < cl:
            tmp = sum([num[cind] if cind < len(num) else 0 for num in nums ]) + carry
            rs.append(tmp%10)
            carry = tmp/10
            cind += 1
        if carry:
            rs.append(carry)
        rs.reverse()
        return rs

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1, l2 = len(num1) - 1, len(num2) - 1
        num1, num2 = map(int, num1), map(int, num2)
        c2 = l2
        ts_list = []
        while c2 >= 0:
            # 局部和
            ts = []
            c1 = l1
            carry = 0
            while c1 >=0 :
                tmp = num1[c1]*num2[c2] + carry
                ts.append(tmp % 10)
                carry = tmp / 10
                c1 -= 1
            if carry:
                ts.append(carry)
            # 不断补0
            tts = [0] * (l2 - c2)
            tts.extend(ts)
            ts_list.append(tts)
            c2 -= 1
        rs = self.sums(ts_list)
        rs = map(str, rs)
        ii = -1
        for i, v in enumerate(rs):
            if v != "0":
                break
            ii = i
        ii += 1
        if ii == len(rs):
            return "0"
        return "".join(rs[ii:])

if __name__ == '__main__':
    sol = Solution()
    print sol.multiply("99999999999999999999999999999999", "0")
    pass