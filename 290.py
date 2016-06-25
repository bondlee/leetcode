# coding: utf-8
# Created by bondlee on 2016/5/10

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        items = str.split()
        i_len = len(items)
        p_len = len(pattern)
        if i_len != p_len:
            return False

        patternDic = {}
        itemDic = {}
        for i in range(i_len):

            if pattern[i] not in patternDic:
                patternDic[pattern[i]] = items[i]
            elif items[i] != patternDic[pattern[i]]:
                return False

            if items[i] not in itemDic:
                itemDic[items[i]] = pattern[i]
            elif pattern[i] != itemDic[items[i]]:
                return False
        return True

    def wordPattern1(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        items = str.split()
        i_len = len(items)
        p_len = len(pattern)
        if i_len != p_len:
            return False

        idic, pdic = {}, {}

        for i,v in enumerate(items):
            if v not in idic:
                idic[v] = pattern[i]
                if pattern[i] in pdic:
                    return False
                pdic[pattern[i]] = v
            elif pattern[i] != idic[v]:
                return False
        return True

    def wordzip(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = pattern
        t = str.split()
        k = ["k" + i for i in pattern]
        return zip(s,t,k)


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordzip("abba", "a a a"))
    pass