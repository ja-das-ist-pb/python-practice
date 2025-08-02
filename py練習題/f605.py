import sys
def input(): return sys.stdin.readline().strip()

n, d=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(n)]
t=0
ts=0
for i in range(n):
    if max(a[i])-min(a[i])>=d:
        t+=1
        ts+=sum(a[i])//len(a[i])
print(t, ts)