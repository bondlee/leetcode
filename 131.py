# coding: utf-8
# Created by bondlee on 2016/7/3

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isP(rs):
            l = 0
            r = len(rs)-1
            while l <= r:
                if rs[l] != rs[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(cur, ss):
            if not ss:
                res.append(cur)
                return
            ind = 0
            while ind < len(ss):
                tmp = ss[0:ind+1]
                if len(tmp) == 1 or isP(tmp):
                    dfs(cur + [tmp], ss[ind+1:])
                ind += 1

        cur = []
        res = []
        dfs(cur, s)
        return res


if __name__ == '__main__':
    sol = Solution()
    print sol.partition("aabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    pass