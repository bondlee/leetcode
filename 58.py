# coding: utf-8
# Created by bondlee on 2016/6/4

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        items = s.split()
        return len(items[-1]) if items else 0


if __name__ == '__main__':
    pass