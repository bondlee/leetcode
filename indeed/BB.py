# coding:utf-8

ss = raw_input()
a, b , k = map(int, ss.split())
t = (k*a*b+0.5*a)/float((a+b))
aa = a - (t-int(t/a)*a)
bb = b - (t-int((t-0.5)/b)*b)
if aa > bb:
    print "Aoki"
else:
    print "Takahashi"
