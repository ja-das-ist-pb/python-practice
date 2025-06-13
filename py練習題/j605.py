import sys

n=int(sys.stdin.readline())
a=[]
for _ in range(n):
    x, y=map(int, input().split())
    a.append([x,y])
maxt=max(a, key=lambda x: x[1])[0]

tot=max(a, key=lambda x: x[1])[1]-n-sum(x[1] == -1 for x in a)
if tot<0: tot=0
print(tot, maxt)
