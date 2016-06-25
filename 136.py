# coding: utf-8
# Created by bondlee on 2016/5/7

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        num_dic = defaultdict(lambda: 0)
        for i in nums:
            num_dic[i] += 1
        result = filter(lambda (x, y): y==1, num_dic.iteritems())
        return result[0][0]

    # 异或操作
    def singleNumberor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = reduce(lambda x, y: x^y, nums)



        return result

if __name__ == '__main__':

    sol = Solution()
    print sol.singleNumber([1,2])
    print sol.singleNumberor([1,2])
    pass