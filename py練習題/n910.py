import sys
def input(): return sys.stdin.readline()

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
row=[[] for _ in range(n)]
col=[[] for _ in range(n)]

# row
# for i in range(n):
#     ptr=0
#     for j in range(n):
#         pause=False
#         if a[i][j]==1 and not pause:
#             row[i][ptr]+=1
#         elif a[i][j]==0 and j>1 and a[i][j-2]==1:
#             pause=True
#         elif a[i][j]==1 and pause:
#             row[i][ptr].append(1)

for i in range(n):
    backup=0
    for j in range(n):
        able=False
        if a[i][j]==1 and (j==0 or (j>0 and a[i][j-1]==0)):
            backup+=1
        elif a[i][j]==0:
            row[i].append(backup)
            backup=0

            
for i in range(n):
    print(row[i])