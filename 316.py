# coding:utf-8

class Solution():
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        alpha = [chr(i) for i in range(97, 97+26)]
        ad = {}
        for i in alpha:
            ad[i] = []
        for i, a in enumerate(s):
            ad[a].append(i)
        for i in alpha:
            ad[i].reverse()

        for i, a in enumerate(s):
            if len(ad[a]) > 1:
                if ord(a) >= ord(s[i+1]):
                    ad[a].pop()
                else:
                    ad[a] = [i]

        al = [(k,v[0]) for k,v in ad.iteritems() if v]
        al.sort(key=lambda x: x[1])
        return "".join([i[0] for i in al])



if __name__ == "__main__":
    sol = Solution()
    print ord("A")
    pass