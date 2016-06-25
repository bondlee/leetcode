# coding: utf-8
# Created by bondlee on 2016/5/8

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if len(secret) != len(guess):
            raise  ValueError
        from collections import  defaultdict
        sdic = defaultdict(lambda: 0)
        gdic = defaultdict(lambda: 0)

        acount = 0
        for i in range(len(secret)):
            sdic[secret[i]] += 1
            gdic[guess[i]] += 1
            if secret[i] == guess[i]:
                acount += 1
        tcount = 0
        for i in sdic:
            tcount += min(sdic[i], gdic[i])

        return "%dA%dB" % (acount, tcount-acount)

if __name__ == '__main__':
    s = Solution()
    print(s.getHint("1807", "7810"))