# coding: utf-8
# Created by bondlee on 2016/5/23

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_dic = set(["a", "e", "i", "o", "u", "A", "O", "E", "I", "U"])
        sv = []
        for i, v in enumerate(s):
            if v in vowel_dic:
                sv.append((i, v))
        lv = len(sv)
        ss = list(s)
        for i in range(lv):
            ss[sv[i][0]] = sv[lv-i-1][1]
        return "".join(ss)

if __name__ == '__main__':
    sol = Solution()
    print sol.reverseVowels("hello")
    pass