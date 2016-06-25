# coding: utf-8
# Created by bondlee on 2016/5/23

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        hl = len(citations)
        left = 0
        right = hl - 1
        mid = 0
        while left <= right:
            mid = (left + right)/2
            hi = hl - mid
            if citations[mid] == hi:
                return citations[mid]
            if citations[mid] < hi:
                left = mid + 1
            else:
                right = mid - 1
        hi = hl - mid - 1
        return min(hl, hi+1) if citations[mid] > hi else hi


if __name__ == '__main__':
    sol = Solution()
    print sol.hIndex([1, 3, 3, 5, 7, 9])
    pass