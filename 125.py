# coding: utf-8
# Created by bondlee on 2016/6/1

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        head, tail = 0, len(s) - 1
        while head < tail:
            if not s[head].isalnum():
                head += 1
            elif not s[tail].isalnum():
                tail -= 1
            else:
                if s[head] == s[tail]:
                    head += 1
                    tail -= 1
                else:
                    return False
        return True



if __name__ == '__main__':
    pass