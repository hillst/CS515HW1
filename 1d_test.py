from math import ceil

def mem_f(x):
    def helper(x, d):
        xi = int(x)
        if not xi in d:
            idx = int(x * 2.0 / 3.0)
            d[xi] = 3.0 * d[idx]
        return d[x]
    d = {0: 0.0, 1: 0.0, 2: 1.0}
    for x in range(3, x+1):
        helper(x, d)
    return d[x]

for x in range(50):
    print x, ':', mem_f(x)
