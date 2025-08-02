from sys import stdin
import math

for i in stdin:
    a, b=map(int, i.split())
    t=0
    for i in range(a, b+1):
        if math.sqrt(i)==int(math.sqrt(i)):
            t+=1
    print(t)