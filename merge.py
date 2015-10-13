#!/usr/bin/env python3

def mergesort(l):
    if len(l) <= 1:
        return l,0
    else:
        m = len(l)//2
        l1,i1 = mergesort(l[:m])
        l2,i2 = mergesort(l[m:])
        lf,i3 = merge(l1, l2)
        return lf,i1+i2+i3

def merge(l1, l2):
    b = [0] * (len(l1) + len(l2))
    i = 0
    j = 0
    k = 0
    inv = 0
    
    for k in range(len(l1)+len(l2)):
        if i >= len(l1):
            b[k] = l2[j]
            j += 1
        elif j >= len(l2):
            b[k] = l1[i]
            i += 1
        elif l1[i] <= l2[j]:
            b[k] = l1[i]
            i += 1
        else:
            b[k] = l2[j]
            j += 1
            inv += len(l1) - i
    return b,inv

def count_inv(l):
    inv = 0
    for i,x in enumerate(l):
        for y in l[i:]:
            if x > y:
                inv += 1
    return inv

from random import shuffle
l = list(range(10))
shuffle(l)
print(l)
print(count_inv(l))
print(mergesort(l))
