# coding:utf-8

class Solution():

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        opdic = {
            "+": lambda x,y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
        }

        opt = {}
        for i in opdic:
            opt[("#", i)] = 1
            opt[("+", i)] = -1
            opt[("-", i)] = -1
            opt[("*", i)] = -1
            opt[("/", i)] = -1

        opt[("*", "+")] = 1
        opt[("/", "-")] = 1
        opt[("*", "-")] = 1
        opt[("/", "+")] = 1

        def cal(ops, ds):
            op = ops.pop()
            r = ds.pop()
            l = ds.pop()
            ds.append(opdic[op](l, r))

        def cmp(opt, ops, op):
            c = ops[-1]
            return opt[(c, op)]

        d = ""
        ops = ["#"]
        ds = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue

            if s[i] in opdic:
                if len(d) > 0:
                    ds.append(int(d))
                    d = ""
                if cmp(opt, ops, s[i]) < 0:
                    ops.append(s[i])
                    i += 1
                    while i < len(s):
                        if s[i] not in opdic and s[i] != " ":
                            d += s[i]
                        elif s[i] in opdic:
                            break
                        i += 1
                    if len(d) > 0:
                        ds.append(int(d))
                        d = ""
                        cal(ops, ds)
                else:
                    ops.append(s[i])
                    i += 1
            else:
                d += s[i]
                i += 1

        while len(ops) > 1:
            cal(ops, ds)
        return ds[-1]
if __name__ == "__main__":
    sol = Solution()
    print sol.calculate("1+2+3")
    pass