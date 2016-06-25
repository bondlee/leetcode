# coding: utf-8
# Created by bondlee on 2016/6/21

def gen_pi(pattern):
    m = len(pattern)
    pi = {}
    pi[0] = -1
    k = -1
    for q in xrange(1, m):
        while k > -1 and pattern[k+1] != pattern[q]:
            k = pi[k]
        if pattern[k+1] == pattern[q]:
            k = k + 1
        pi[q] = k
    return pi

def kmp(T, P):
    pi = gen_pi(P)
    m = len(P)
    n = len(T)
    q = -1
    for i in xrange(n):
        while q > -1 and P[q+1] != T[i]:
            q = pi[q]
        if P[q+1] == T[i]:
            q = q+1
        if q == m-1:
            return T[i-q: i+1]
    return False


if __name__ == '__main__':
    # gen_pi("ababababca")
    # print gen_pi("ababababca")
    print kmp("fsdafffffffffasfadfsdafasd", "dfsd")
    pass