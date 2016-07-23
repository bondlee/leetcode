# coding:utf-8
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        p = [1]
        q = []
        ind = 1
        while ind < numRows:
            q = [1]*(ind+1)
            for i in xrange(ind+1):
                pre = 0
                if i-1 >= 0:
                    pre = p[i-1]
                if i >= ind:
                    cur = 0
                else:
                    cur = p[i]
                q[i]=(pre + cur)
            ind += 1
            p = q
        return q
if __name__ == "__main__":
    sol = Solution()
    print sol.generate(5)
    pass