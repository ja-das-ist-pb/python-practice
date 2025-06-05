n=int(input())
a=[]
b=[]
tot=[]

for i in range(n):
    x, y=map(int, input().split())
    a.append(x)
    b.append(y)
    tot.append(x**2+y**2)

position=tot.index(max(tot))
tot[position]=-1
new=tot.index(max(tot))
print(a[new], b[new])