# coding:utf-8

class Solution():
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not num:
            return True
        ind = 1
        d = 0
        while d*d <= num:
            k = 1
            while (d+k)*(d+k) < num:
                k *=2
            if (d+k)*(d+k) == num:
                return True
            d += k/2 if k>1 else 1
        return False



if __name__ == "__main__":
    sol = Solution()
    print sol.isPerfectSquare(16)
    pass