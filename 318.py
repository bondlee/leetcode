# coding:utf-8

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        rt = 0
        from collections import defaultdict
        alpha = defaultdict(list)
        ind = {}
        for i, word in enumerate(words):
            for j in set(word):
                alpha[j].append(i)
            ind[i] = 0
        for i in alpha:
            if len(alpha[i]) > 1:
                for w in alpha[i]:
                    if w in ind:
                        ind.pop(w)
        candidate = [len(words[i]) for i in ind.iterkeys()]
        if len(candidate) < 2:
            return 0
        import heapq
        p, q= heapq.nlargest(2, candidate)
        return p*q

if __name__ == "__main__":
    sol = Solution()
    print sol.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
    pass