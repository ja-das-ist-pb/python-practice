n=int(input())
id=[""]*n
name=[""]*n#3
dep=[]#1
deg=[]#2
for i in range(n):
    id[i], name[i]=list(map(str, input().split()))
for i in range(n):
    dep.append(list(id[i])[-1])
    deg.append(list(id[i])[0])

