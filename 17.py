# coding: utf-8
# Created by bondlee on 2016/6/4


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        digits_dic = {
            0: " ",
            1: "*",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        def dfs(cur, r):
            if r == len(digits):
                res.append(cur)
                return
            for i in digits_dic[int(digits[r])]:
                dfs(cur+i, r+1)

        res = []
        dfs("", 0)
        return res


if __name__ == '__main__':
    sol = Solution()
    print sol.letterCombinations("123")
    pass