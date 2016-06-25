# coding: utf-8
# Created by bondlee on 2016/6/4


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return  ""
        ind = 0
        ml = min([len(s) for s in strs])
        while ind < ml:
            ss = set([s[ind] for s in strs])
            if len(ss) < 2:
                ind += 1
            else:
                break
        return strs[0][0:ind]

if __name__ == '__main__':
    sol = Solution()
    print sol.longestCommonPrefix(["a"])
    pass