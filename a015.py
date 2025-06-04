m, n=map(int, input().split())
a=[]
for i in range(m):
    b=[]
    b=list(map(int, input().split()))
    a.append(b)

new=[]
for i in range(n):
    c=[]
    for j in range(m):
        c.append(a[j][i])
    new.append(c)

for i in range(n):
    for ja in new:
        print(ja[i], end=" ")
    print()
