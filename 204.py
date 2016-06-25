# coding: utf-8
# Created by bondlee on 2016/5/11

class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                # j * i (j<i) 对应的因子在前面的因子探测中都已经探测过了，所以这里不需要再重新赋值
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)
if __name__ == '__main__':
    sol = Solution()
    #print sol.countPrimes(1500000)
    print ~(-1<<1000)
    pass