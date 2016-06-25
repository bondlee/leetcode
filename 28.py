# coding: utf-8
# Created by bondlee on 2016/6/1

class Solution(object):
    # 一种解法，还有更好的是KMP算法
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        pind = 0
        nind = 0
        lp, ln = len(haystack), len(needle)
        while pind < lp and nind < ln:
            while (pind + nind) < lp and haystack[pind + nind] == needle[nind]:
                nind += 1
                if nind == ln:
                    return pind
            nind = 0
            pind += 1
        return -1

    def gen_pi(self, pattern):
        m = len(pattern)
        pi = {}
        pi[0] = -1
        k = -1
        for q in xrange(1, m):
            while k > -1 and pattern[k + 1] != pattern[q]:
                k = pi[k]
            if pattern[k + 1] == pattern[q]:
                k = k + 1
            pi[q] = k
        return pi

    def kmp(self, haystack, needle):
        if not needle:
            return 0
        if not haystack:
            return -1
        pi = self.gen_pi(needle)
        m = len(needle)
        n = len(haystack)
        q = -1
        for i in xrange(n):
            while q > -1 and needle[q + 1] != haystack[i]:
                q = pi[q]
            if needle[q + 1] == haystack[i]:
                q = q + 1
            if q == m - 1:
                return i - q
        return -1

if __name__ == '__main__':
    sol = Solution()
    print sol.kmp("a", "a")
    print sol.strStr("a", "a")

    pass