from math import gcd
from functools import reduce

n = int(input())
s = set()

for _ in range(n):
    a = list(map(int, input().split()))
    a.sort()
    mgcd = reduce(gcd, a)
    a = [x//mgcd for x in a]
    s.add(tuple(a))
print(len(s))