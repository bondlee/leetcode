# coding:utf-8

class Solution():



    def re(self):
        def dfs(i):
            if i > 10:
                return
            df[i] = i
            dfs(i+1)
        df = [1]*11
        dfs(0)



if __name__ == "__main__":
    sol = Solution()
    print sol.re()
    pass