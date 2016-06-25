# coding: utf-8
# Created by bondlee on 2016/5/10

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import defaultdict
        sdic = defaultdict(lambda : 0)
        tdic = defaultdict(lambda : 0)
        if len(s) != len(t):
            return False
        for i, v in enumerate(s):
            sdic[v] += 1
            tdic[t[i]] += 1

        ss = set(sdic.iteritems())
        ts = set(tdic.iteritems())
        if ss != ts :
            return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.isAnagram("anagram", "nagaram")
    pass