def bfs(n, m, a):
    queue=[]
    walked=[[False]*m for i in range(n)]
    s=None
    e=None
    direction=[(1, 0), (-1, 0), (0, 1), (-1, 0)]
    char="QWERTYUIOPASDFGHJKLZXCVBNM"
    tran=[]
    tranpos={}
    tran.append([a[i] for i in range(n) if a[i] in char])
    tran.pop([tran[i] for i in tran if tran.count(tran[i])<2])
    for i in range(n):
        for j in range(m):
            if 'A'<=a[i][j]<='Z':
                if a[i][j] not in tranpos:
                    tranpos[a[i][j]]=[]
                    tranpos[a[i][j]].append((j, i))

    for i in range(n):
        for j in range(m):
            if a[i][j]=="S": s=(j, i)
            if a[i][j]=="E": e=(j, i)
    queue.append(s+(0,))
    walked[s[1]][s[0]]=True

    while queue:
        x, y, step=queue.pop(0)
        
        if x==e[0] and y==e[1]:
            return step
        
        for dx, dy in direction:
            nx=x+dx
            ny=y+dy
            if (nx, ny) in tranpos: nx 
            
            if not walked[ny][nx] and 0<=ny<n and 0<=nx<m:
                 
        

n, m=map(int, input().split())
a=[list(input()) for i in range(n)]
print(bfs(n, m, a))