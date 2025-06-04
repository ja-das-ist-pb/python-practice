a=[0]*3
a=list(map(int, input().split()))
max=0
most=1
a.sort()

for i in range(2):
    if (a[i]==a[i+1]):
        most+=1
    else:
        most=1
    if max<most:
        max=most

if max==1:
    print(max, a[2], a[1], a[0])
elif max==2:
    print(max,a[2], a[0])
else:
    print(max, a[0])