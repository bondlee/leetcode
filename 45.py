# coding:utf-8

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)
        if ln < 2:
            return True
        cur = 0
        cc = 0
        while cur < ln - 1:
            # 当前可达范围
            maxp = cur + nums[cur]
            if maxp >= ln-1:
                return cc+1
            np = maxp
            for i in xrange(1, nums[cur] + 1):
                if cur + i >= ln:
                    break
                tmp = cur + i + nums[cur + i]
                if tmp > maxp:
                    maxp = tmp
                    np = cur + i
            if np == cur:
                return -1
            cur = np
            cc += 1
        return cc


if __name__ == "__main__":
    sol = Solution()
    print sol.jump([2,3,1,1, 4])
    pass