import sys
def input(): return sys.stdin.readline().strip()

n, m=map(int, input().split())
a=[['.']*m for _ in range(n)]
s=list(map(int, list(input())))
l=[0, 0]
a[0][0] = '*'  # 標記起點
# 方向: 右、下、左、上
move = [(0,1), (1,0), (0,-1), (-1,0)]
for i in range(len(s)):
    dx, dy = move[i%4]
    for _ in range(s[i]):
        nx, ny = l[0]+dx, l[1]+dy
        if 0<=nx<n and 0<=ny<m:
            l[0], l[1] = nx, ny
            a[l[0]][l[1]] = '*'
        else:
            break
for i in range(n):
    for j in range(m):
        print(a[i][j], end="")
    print()