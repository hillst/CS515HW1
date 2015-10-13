from math import ceil,log,pow

def rec(x):
    exp = (1.0 - log(x, 2)) / (1 - log(3, 2))
    exp = ceil(exp)
    return pow(3, exp)

def mem_f(m):
    def helper(x, d):
        xi = int(x)
        if not xi in d:
            idx = int(ceil(x * 2.0 / 3.0))
            d[xi] = 3.0 * d[idx]
        return d[xi]
    d = {0: 0.0, 1: 0.0, 2: 1.0}
    for y in range(3, m+1):
        helper(y, d)
    return d[m]

for x in range(1,40):
    print x, ':', mem_f(x), '=', rec(x)
