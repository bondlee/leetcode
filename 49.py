# coding: utf-8
# Created by bondlee on 2016/5/12

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import  defaultdict
        import bisect
        strsDic = defaultdict(lambda : [])
        for i in strs:
            b = sorted(i)
            bisect.insort_left(strsDic[str(b)], i)
        return strsDic.values()

    def performance(self, strs):
        import bisect

        def getStrSig(s):
            """
            get the signature of str s
            """
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                      101]
            ord_a = ord('a')
            hash = 1
            for c in s: hash *= primes[ord(c) - ord_a]
            return hash

        worddict = {}
        for s in strs:
            sig = getStrSig(s)  # Here use:  sig = ''.join(sorted(s))  still beats 93.9%
            if sig not in worddict:
                worddict[sig] = [s]
            else:
                bisect.insort_left(worddict[sig], s)  # insert the anagram with correct order
        return worddict.values()

if __name__ == '__main__':
    sol = Solution()
    print sol.groupAnagrams(["mes","ems"])

    import bisect
    a = []
    bisect.insort_left(a, 2)
    bisect.insort_left(a, 2,)
    bisect.insort_left(a, -1,)
    print a


    pass