# coding:utf-8

class Solution():

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        dp = [0]*len(primes)
        for i in xrange(n-1):
            nums = [ugly[dp[j]]*primes[j] for j in range(len(primes))]
            minp = min(nums)
            for j, v in enumerate(nums):
                if minp == ugly[dp[j]]*primes[j]:
                    dp[j] += 1
            ugly.append(minp)
        return ugly[-1]


if __name__ == "__main__":
    sol = Solution()
    print sol.nthSuperUglyNumber(12, [2, 7, 13, 19])
    pass