# coding: utf-8
# Created by bondlee on 2016/5/23

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        s1 = defaultdict(lambda :0)
        for i in nums1:
            s1[i] += 1
        ss = []
        a = "123"
        for i in nums2:
            if s1[i]:
                ss.append(i)
                s1[i] -= 1
        return ss



if __name__ == '__main__':
    pass