m, n=map(int, input().split())
a=[]
tran=[]
for i in range(m):
    a.append([int(x) for x in input().split()])
input()
for i in range(m):
    tran.append([int(x) for x in input().split()])
for i in range(m):
    for j in range(n):
        if (sum(tran[i])+sum(row[j] for row in tran)-tran[i][j])%2==1:
            if a[i][j]==1:
                a[i][j]=0
            else:
                a[i][j]=1

for i in range(m):
    for j in range(n):
        print(a[i][j], end=" ")
    print()