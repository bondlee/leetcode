# coding: utf-8
# Created by bondlee on 2016/5/24


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = len(s)

        for i in xrange(sl):
            for j in xrange(i+1, sl):
                s = s[i:]

if __name__ == '__main__':
    pass