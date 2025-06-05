n=int(input())
nine=[[0 for j in range(5)] for i in range(5)]
for i in range(1,4):
    for j in range(1, 4):
        nine[i][j]=(i-1)*3+j
for _ in range(n):
    side=int(input())
    notnear=list(map(int, input().split()))
p=[]
imp=[]
for i in range(1, 4):
    for j in range(1,4):
        if nine[i][j]==side:
            p.append(nine[i][j-1])
            p.append(nine[i][j+1])
            p.append(nine[i-1][j])
            p.append(nine[i+1][j])
        if nine[i][j] in notnear:
            imp.append(nine[i][j-1])
            imp.append(nine[i][j+1])
            imp.append(nine[i-1][j])
            imp.append(nine[i+1][j])
for a in p:
    if a==0:
        p.pop(a)
    elif p.count(a)>1:
        for i in range(p.count(a)-1):
            p.pop(a)
            