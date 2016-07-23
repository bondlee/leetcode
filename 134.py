# coding:utf-8

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        ln = len(gas)
        delta = map(lambda x,y: x-y, gas, cost)
        if sum(delta) < 0:
            return -1
        ind = 0
        while ind < ln:
            if delta[ind] < 0:
                ind += 1
                continue
            cur = ind
            s = delta[ind]
            while (cur+1) % ln != ind:
                cur = (cur+1) % ln
                s += delta[cur]
                # 中途没油无法继续
                if s < 0:
                    # 因为ind以前的都是无法继续的，此时循环如果越过ind则不可能是正常路劲
                    if cur < ind:
                        return -1
                    break
            if s >= 0:
                return ind
            ind = cur + 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    print sol.canCompleteCircuit([2, 4], [3, 4])
