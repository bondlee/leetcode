# coding: utf-8
# Created by bondlee on 2016/6/4

class Solution(object):

    def __init__(self):
        self.counts = [1]
        self.ind = 1

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < self.ind:
            return self.counts[n-1]
        while self.ind < n:
            pre_num = str(self.counts[self.ind-1])
            next = []
            pre = 0
            cur = 0
            cur_num = 0
            while cur < len(pre_num):
                if pre_num[pre] == pre_num[cur]:
                    cur += 1
                else:
                    next.extend([cur-pre, pre_num[pre]])
                    cur_num = cur_num * 10 + cur-pre
                    cur_num = cur_num * 10 + int(pre_num[pre])
                    pre = cur
            if pre != cur:
                cur_num = cur_num * 10 + cur - pre
                cur_num = cur_num * 10 + int(pre_num[pre])
            self.counts.append(cur_num)
            self.ind += 1
        return self.counts[n-1]




if __name__ == '__main__':
    pass