import sys
def input(): return sys.stdin.readline()

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
s=set()
for i in range(len(a)):
    for j in range(a[i][0], a[i][1]+1):
        s.add(j)
new=list(s)
new.sort()
backup=0
for i in range(1, len(new)):
    if new[i]==new[i-1]+1:
        backup+=1
print(backup)