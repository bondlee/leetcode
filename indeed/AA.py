# coding:utf-8
def can_repalce(ss, tt):
    if len(ss) != len(tt):
        return False
    if ss == tt:
        return True
    sss = set(ss)
    ttt = set(tt)
    if len(sss) - len(ttt) > 1:
        return False
    for i, v in enumerate(ss):
        if v != tt[i]:
            if tt.replace(v, tt[i]) == ss.replace(v, tt[i]):
                return True

    return False

s = raw_input()
t = raw_input()

if can_repalce(s, t):
    print "Possible"
else:
    print "Impossible"