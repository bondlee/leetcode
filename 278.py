# coding:utf-8

def isBadVersion(k):
    if k <2:
        return False
    else:
        return True

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        mid = (l+r)/2
        while l <=r:
            mid = (l+r)/2
            if isBadVersion(mid):
                r = mid-1
                if not isBadVersion(r):
                    return mid
            else:
                l = mid+1
                if isBadVersion(l):
                    return l



if __name__ == "__main__":
    sol = Solution()
    print sol.firstBadVersion(2)
    pass