import sys

line=sys.stdin.readlines()
n, m=map(int, line[0].split())
do=[[x, 0] for x in range(n)]

for i in range(1, m+1):
    a, b=map(int, line[i].split())
    do[a][1]+=b

do.sort(key=lambda x: (-x[1], x[0]))
for a,b in do:
    print(a, b)