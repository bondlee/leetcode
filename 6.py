# coding: utf-8
# Created by bondlee on 2016/5/13

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <=1:
            return s
        from collections import defaultdict
        rowsDic = defaultdict(list)
        for i,v in enumerate(s):
            y = i % (2*numRows-2)
            if y < numRows:
                rowsDic[y].append(v)
            else:
                rowsDic[2*numRows-2-y].append(v)
        r = ""
        for i in rowsDic:
            r += "".join(rowsDic[i])
        return r

if __name__ == '__main__':
    sol = Solution()
    print sol.convert("A", 1)
    pass