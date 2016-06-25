# coding: utf-8
# Created by bondlee on 2016/6/4


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        items1 = version1.split(".")
        items2 = version2.split(".")
        ind = 0
        while ind < len(items1) and ind < len(items2):
            i1 = int(items1[ind])
            i2 = int(items2[ind])
            ind += 1
            if i1 > i2:
                return 1
            if i1 < i2:
                return -1
        while ind < len(items1):
            i1 = int(items1[ind])
            if i1 > 0:
                return 1
            ind += 1
        while ind < len(items2):
            i2 = int(items2[ind])
            if i2 > 0:
                return -1
            ind += 1
        return 0

if __name__ == '__main__':
    pass