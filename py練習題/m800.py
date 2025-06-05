m, n, k=map(int, input().split())
a=[]
a.append([0]*(n+2))
c=0
indicate=[]
delta=0

for i in range(m):
    b=[]
    b=list(map(int, input().split()))
    a.append([0]+b+[0])
a.append([0]*(n+2))

for x in range(k):
    for i in range(1, m+1):
        indicate=[[False]*n for _ in range(m)]
        for j in range(1, n+1):
            c=0
            if a[i-1][j]>a[i][j]:
                c+=1
            if a[i+1][j]>a[i][j]:
                c+=1
            if a[i][j-1]>a[i][j]:
                c+=1
            if a[i][j+1]>a[i][j]:
                c+=1
            if c>2:
                indicate[i-1][j-1]=True
    for i in range(m):
        for j in range(n):
            if indicate[i][j]:
                a[i+1][j+1]+=1
                delta+=1
            else:
                a[i+1][j+1]-=1
                delta-=1
print(delta)