# coding: utf-8
# Created by bondlee on 2016/6/10

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums:
            return 0
        num_list = [str(num) for num in nums ]
        num_list = sorted(num_list, cmp=lambda x,y: int(x)-int(y) if len(x)== len(y) else 1 if (int(x+y)-int(y+x))>0
                          else -1,
                          reverse=True)
        rs = "".join(num_list)
        ind = 0
        while ind < len(rs) and rs[ind] == "0":
            ind += 1
        if ind < len(rs):
            return rs[ind:]
        else:
            return "0"



if __name__ == '__main__':
    sol = Solution()
    print sol.largestNumber([123, 12312311])
    pass