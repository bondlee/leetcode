# coding: utf-8
# Created by bondlee on 2016/7/3

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(cur, ss, r):
            if r == 4 and len(ss) == 0:
                ip = ".".join([str(i) for i in cur])
                if not sdic[ip]:
                    res.append(ip)
                    sdic[ip] = 1
                return
            if r < 4 and ss and len(ss)/(4-r) <=3:
                for i in range(1,4):
                    ts = ss[0:i]
                    if int(ts)<256 and (len(ts) >1 and ts[0] !="0" or len(ts) < 2):
                        dfs(cur + [ts], ss[i:], r+1)

        res = []
        cur = []
        from collections import  defaultdict
        sdic = defaultdict(lambda :0)
        dfs(cur, s, 0)
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.restoreIpAddresses("010010")