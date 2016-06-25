# coding: utf-8
# Created by bondlee on 2016/5/10

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        sdic = {}
        tdic = {}

        for i, v in enumerate(s):
            if v not in sdic:
                sdic[v] = t[i]
                if t[i] in tdic:
                    return False
                tdic[t[i]] = v
            elif t[i] != sdic[v]:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isIsomorphic("abba", "bbbb"))
    pass