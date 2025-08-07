import sys
def input():return sys.stdin.readline()

def rotate(a):
    global n, m
    ra=[[] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            ra[m-j-1].append(a[i][j])
    n, m=m, n
    return ra

def flip(a):
    fa=[]
    for i in reversed(range(n)):
        fa.append(a[i])
    return fa

n, m, k=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(n)]
c=list(map(int, input().split()))
# 0 = rotate    1 = flip

for i in reversed(range(len(c))):
    if c[i]==0:
        a=rotate(a)
    else:
        a=flip(a)

print(n, m)

for row in a:
    print(" ".join(map(str, row)))