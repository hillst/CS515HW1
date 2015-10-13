#!/usr/bin/env python3

from math import ceil,floor

def fn(num):
    v1 = 2.0 * ceil(n * 2.0 / 3.0) - floor(n / 3.0)
    v2 = n
    b = (v1 >= v2)
    return (b, v1, v2)

for n in range(1000):
    b, x, y = fn(n)
    if not b:
        print('---')
        print(b)
        print(x)
        print(y)
