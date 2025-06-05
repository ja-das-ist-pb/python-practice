m, n=map(int, input().split())
a=[]
for i in range(m):
    a.append([int(x) for x in input().split()])
where=-1
for i in range(m):
    for j in range(n):
        where=-1
        if a[i][j]==1:
            for k in range(n-j-1):
                if a[i][k]==1:
                    where=k
                    break
            if where>0:
                for k in range(j+1, k):
                    a[i][k]=1

for i in range(m):
    for j in a[i]:
        print(j, end=" ")
    print()