m, n=map(int, input().split())
score=[]
for i in range(m):
    score.append([int(x) for x in input().split()])

go=[]
back=[]

for i in range(m):
    gosum=0
    backsum=0
    for j in range(1, n):
        if score[i][j]>=score[i][j-1]:
            gosum+=score[i][j]-score[i][j-1]
        else:
            backsum+=score[i][j-1]-score[i][j]
    go.append(gosum)
    back.append(backsum)

print(go.index(max(go))+1)
print(back.index(max(back))+1)