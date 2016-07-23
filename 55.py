# coding:utf-8

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ln = len(nums)
        if ln < 2:
            return True
        cur = 0
        while cur < ln-1:
            # 当前可达范围
            maxp = cur + nums[cur]
            np = maxp

            for i in xrange(1, nums[cur]+1):
                if cur + i >= ln:
                    break
                tmp = cur+i + nums[cur+i]
                if tmp > maxp:
                    maxp = tmp
                    np = cur + i
            if np == cur:
                return False
            cur = np
        return True

if __name__ == "__main__":
    sol = Solution()
    print sol.canJump([5,9,3,2,1,0,2,3,3,1,0,0])
