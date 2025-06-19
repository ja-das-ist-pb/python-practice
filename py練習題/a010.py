import sys
from math import sqrt

n=int(sys.stdin.readline())
a=[]
if n==1: print(1)
elif n==0: print(0)
else:
    while n>1:
        for i in range(2, int(sqrt(n))+1):
            if n%i==0:
                if i in a:
                    a[a.index(i)][1]+=1
                else:
                    a.append([i, 1])
    for i in range(len(a)-1):
        if a[i][1]==1:
            print(a[i], end=" * ")
        else:
            print(f"{a[i][0]}^{a[i][1]}")
    if a.count(a[len(a)-1][1])==1:
        print(a[len(a)-1][0], end=" * ")
    else:
        print(f"{a[len(a)-1][0]}^{a[len(a)-1][1]}")