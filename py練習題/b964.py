n=int(input())
a=[0]*n
a=list(map(int, input().split()))
a.sort()
print(" ".join(map(str, a)))

maxl=0
lowm=101

lyn=True
hyn=True

for i in range (n):
    if a[0]>=60:
        lyn=False
        break
    if a[i]<60:
        maxl=a[i]
if lyn==False:
    print("best case")
else:
    print(maxl)

for i in range(n):
    if a[n-1]<60:
        hyn=False
        break
    if a[i]>=60:
        lowm=a[i]
        break
if hyn==False:
    print("worst case")
else:
    print(lowm)
