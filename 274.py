# coding: utf-8
# Created by bondlee on 2016/5/8

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        citations = sorted(citations, key=lambda x: x, reverse=True)
        clen = len(citations)
        hindex = 0
        for i in range(clen):
            if citations[i] >= (i+1):
                hindex = i+1
            else:
                break
        return hindex

    def hIndex1(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        clen = len(citations)
        cnt = [0 for i in range(clen+1)]

        for i in citations:
            cnt[min(i,clen)] += 1
        hindex = 0
        for i,v in enumerate(cnt):
            ind = clen - i
            if ind >= hindex:
                hindex += cnt[ind]
                hindex = min(hindex, ind)
            else:
                break
        return hindex


if __name__ == '__main__':
    sol = Solution()
    print sol.hIndex1([1])