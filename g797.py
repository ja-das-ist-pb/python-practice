n, m=map(int, input().split())
a=[]*n
a=list(map(int, input().split()))

def xipi(a):
    a1=[0]*int(n/2)
    a2=[0]*int(n/2)
    for i in range(int(n/2)):
        a1[i]=a[i]
        a2[i]=a[i+int(n/2)]
    for i in range(0, n, 2):
        a[i]=a1[int(i/2)]
        a[i+1]=a2[int(i/2)]
    return a

for i in range(m):
    xipi(a)
for i in range(n):
    print(a[i], end=" ")