import sys, math
def input(): return sys.stdin.readline()

n=int(input())
for _ in range(n):
    d, I=map(int, input().split())
    a=[False for _ in range(pow(2, d))]
    for i in range(I):
        ptr=1
        for j in range(d-1):
            if a[ptr]==False:
                a[ptr]=True
                ptr=ptr*2
            else:
                a[ptr]=False
                ptr=ptr*2+1
    print(ptr)