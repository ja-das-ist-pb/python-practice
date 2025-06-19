import sys

m, n, k=map(int, sys.stdin.readline())
s=[]
spin=[]
repeat=[]
tot=0
for i in range(m):
    ss=sys.stdin.readline()
    s.append(ss)
for i in range(k):
    alist=list(map(int, sys.stdin.readline().split()))
    spin.append(alist)

for i in range(k):
    for j in range(m):
        if spin[i][j]<0:
            s[j]=s[j][::]